from flask import request, session
from .model import Auth


class AuthController:
    def __init__(self):
        self.model = Auth()

    def adminLogin(self):
        data = self.model.getEmployee(request.json['username'])
        if (not data):
            return {'message': "admin user not found!"}, 404

        session['object'] = {"username": request.json['username'], "type": "admin"}
        return {'data': data}

    def logout(self):
        session.pop('object')
        return {'message': "success"}

    def userLogin(self):
        data = self.model.getUser(request.json['username'])
        if (not data):
            return {'message': "user not found!"}, 404

        session['object'] = {"username": request.json['username'], "type": "user"}
        return {'data': data}
