from functools import wraps
from flask import Flask ,request,jsonify
import jwt

from Models.LoginUsers import Users


app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

def token_required(f):
    def decorated():
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['UserName']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(current_user)

    return decorated