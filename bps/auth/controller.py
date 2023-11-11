from flask import abort, request, session
from .model import Auth


class AuthController:
    def __init__(self):
        self.model = Auth()

    def login(self):
        data = self.model.getUser(request.json['username'])
        if (not data):
            return {'message': "user not found!"}, 404

        session['email'] = request.json['username']
        return {'data': data}

    def logout(self):
        session.pop('email')
        return {'message': "success"}
