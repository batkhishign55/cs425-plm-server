import json
import pathlib

class User:
    def __init__(self):
        self.collections=json.load(self.openDb())
        
    def openDb(self):
        return open(pathlib.Path().cwd()/'db.json')
    
    def getUser(self):
        users=self.collections.get('users')
        return users[0]