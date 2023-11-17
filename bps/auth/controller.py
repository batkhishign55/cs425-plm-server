from flask import request, session
from .model import Auth


class AuthController:
    def __init__(self):
        self.model = Auth()

    def adminLogin(self):
        data = self.model.getEmployee(request.json['username'])
        if (not data):
            return {'message': "admin user not found!"}, 404
        
        print(data[6])
        if data[6] != request.json['password']:
            return {'message': "admin password incorrect!"}, 401

        session['object'] = {"username": request.json['username'], "type": "admin", "emp_id": str(data[0])}
        return {'data': data}

    def logout(self):
        session.pop('object')
        return {'message': "success"}

    def userLogin(self):
        data = self.model.getUser(request.json['username'])
        if (not data):
            return {'message': "user not found!"}, 404
        
        print(data)
        if data[7] != request.json['password']:
            return {'message': "user password incorrect!"}, 401

        session['object'] = {"username": request.json['username'], "type": "user", "user_id":str(data[0])}
        return {'data': data}
