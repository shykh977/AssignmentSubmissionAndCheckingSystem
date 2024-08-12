from flask import Flask, request, jsonify
class Middleware:
    
    


    def authenticate_request(self):

        API_KEY = '3C5D2DEC-4EE1-4D43-8937-07DF9EA37EC9'

    # Get the API key from the request headers
        api_key = request.headers.get('TrackApi')

        


    # Check if the API key is valid
        if api_key != API_KEY:  

            return jsonify({'message': 'Invalid API key'}), 401


        # Return an unauthorized response if the API key is invalid
        
