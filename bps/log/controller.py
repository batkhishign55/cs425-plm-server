from .model import log

#class
class logController:
    def __init__(self):
        self.model = log()

    def get(self):
        data = self.model.get()
        if not data:
            return {'status': False, 'data': data, 'message': 'Data is not found'}
        return {'status': True, 'data': data, 'message': ''}

    def getSinglelog(self, log_id):
        data = self.model.getSinglelog(log_id)
        if not data:
            return {'status': False, 'data': data, 'message': 'Data is not found'}
        return {'status': True, 'data': data, 'message': ''}
