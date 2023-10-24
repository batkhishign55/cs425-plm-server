from .model import Product

class ProductController:
    def __init__(self):
        self.model=Product()

    def get(self):
        data=self.model.get()
        if not data:
            return {'status':False, 'data':data, 'message':'Data is not found'}
        return {'status':True, 'data':data, 'message':''} 

    
    def getSingleProduct(self, id):
        data=self.model.getSingleProduct(id)
        if not data:
            return {'status':False, 'data':[data], 'message':'Data is not found'}
        return {'status':True, 'data':[data], 'message':''} 