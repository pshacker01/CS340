from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self):
        USER = 'aacuser'
        PASS = 'aacpassword123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33259
        DB = 'AAC'
        COL = 'animals'
        
        # Connect to MongoDB with authentication
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]
        
        
    # Create
    def create(self, data):
        if data is not None and isinstance(data, dict):
            result = self.collection.insert_one(data)
            return result.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty or invalid.")
        
    # READ    
    def read(self, query):
        if query is not None and isinstance(query, dict):
            cursor = self.collection.find(query)
            return list(cursor)
        else:
            raise Exception("Query must be a dictionary.")
            
            
    # Update
    def update(self, query, new_values):
        if query and new_values and isinstance(query, dict) and isinstance(new_values, dict):
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        else:
            raise Exception("Both query and new_values must be dictionaries.")
            
            
    # Delete
    def delete(self, query):
        if query is not None and isinstance(query, dict):
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Query must be a dictionary.")