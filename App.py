#import Library 
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#Import library flask sqlalchemy
from flask_sqlalchemy import SQLAlchemy 
import os

#inisiasi object flask
app = Flask(__name__)

#inisiasi object flask_restful
api = Api(app)

#inisiasi object flask_cors
CORS(app)


#inisiasi variable kosong bertipe  dictionary
product = {} #variable global, dictionary = json

# #Membuat class Resource(Resource)
class ApiResource(Resource):
    #metode get dan post
    def get(self):
    #    response = 
            
    #         "status" : "Data berhasil dimasukan"
    #     
        return product
    
    def post(self):
        id = request.form["id"]
        d_name = request.form["name"]
        d_price = request.form["price"]
        d_quantity = request.form["quantity"]
        product["id"] = id
        product["name"] = d_name
        product["price"] = d_price
        product["quantity"] = d_quantity
        response ={
            "code" : 1,
             "status" : "Data berhasil dimasukan"
        }
        return response
    

#setup resourcenya
api.add_resource(ApiResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)


