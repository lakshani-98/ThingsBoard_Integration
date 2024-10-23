from flask import Flask, jsonify, abort, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'a7e7d11a1e7e4f8294d357e45a88f39baf4b55e8b19e1d23e1b1c82945a69c8d'
jwt = JWTManager(app)

# Dictionary Mapping sensor ID to Thingsboard dashboard link
sensor_dashboard_links = {
    'sensor1': 'sensor_1_link',
    'sensor2': 'sensor_2_link',
    'sensor3': 'sensor_3_link',
    'M65-30-20-10-10-F72-F-020' : 'M65-30-20-10-10-F72-F-020_link',
    'M64_BH2S01P01_C_010' : 'M64_BH2S01P01_C_010_link'
}

# Dictionary with sensor ID to customer mappings
sensor_customer_mapping = {
    'sensor1': {'customer1', 'customer2'}, 
    'sensor2': {'customer2'},              
    'sensor3': {'customer1'},              
    'M65-30-20-10-10-F72-F-020': {'customer3'},  
    'M64_BH2S01P01_C_010': {'customer2'}    
}

@app.route('/token', methods=['POST'])
def generate_token():
    # Dummy authentication (replace with your own logic)
    customer_id = request.json.get('customer_id', None)
    if customer_id in ['customer1', 'customer2', 'customer3']:
        access_token = create_access_token(identity={'customer_id': customer_id})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid customer ID"}), 401
    

@app.route('/dashboard/<sensor_id>', methods=['GET'])
@jwt_required()
def get_dashboard_link(sensor_id):
    current_user = get_jwt_identity()
    customer_id = current_user.get('customer_id')
    
    # Check if the sensor ID is mapped to the customer
    if customer_id in sensor_customer_mapping.get(sensor_id, []):
        dashboard_link = sensor_dashboard_links.get(sensor_id)
        if dashboard_link:
            return jsonify({'link': dashboard_link})
        else:
            abort(404, description="Dashboard link not found for the given sensor.")
    else:
        abort(403, description="Access forbidden: Unauthorized customer.")

if __name__ == '__main__':
    app.run(port=3000)





# from flask import Flask, jsonify, abort, request
# from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


# app = Flask(__name__)


# # Dictionary with sensor ID to dashboard link mappings
# sensor_dashboard_links = {
#     'sensor1': '',
#     'sensor2': '',
#     'sensor3': '',
#     'M65-30-20-10-10-F72-F-020' : '',
#     'M64_BH2S01P01_C_010' : ''
# }


# @app.route('/dashboard/<sensor_id>', methods=['GET'])
# def get_dashboard_link(sensor_id):
#     dashboard_link = sensor_dashboard_links.get(sensor_id)
#     if dashboard_link:
#         return jsonify({'link': dashboard_link})
#     else:
#         abort(404, description="Dashboard link not found for the given sensor.")


# if __name__ == '__main__':
#     app.run(port=3000)