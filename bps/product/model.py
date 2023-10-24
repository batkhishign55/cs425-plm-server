import json
import pathlib

class Product:
    def __init__(self):
        self.collections=json.load(self.openDb())
        
    def openDb(self):
        return open(pathlib.Path().cwd()/'db.json')
    
    def get(self):
        return self.collections.get('products',[])

    def getSingleProduct(self, id):
        products=self.collections.get('products')
        for product in products:
            if str(product.get('id'))==id: 
                return product
        return {}
