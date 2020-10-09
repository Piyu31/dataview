from flask import Flask, render_template, redirect, request
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

connection=MongoClient("mongodb+srv://priyanka:piyu31@cluster0.mdba4.mongodb.net/Users?retryWrites=true&w=majority")
db = connection["Users"]
colletions=db["Details"]

@app.route('/')
def index():
	return render_template('index.html')

 #update  single record using mongodb Id
colletions.update_one(
   {'_id': ObjectId("5f6d8fe8d06010e25dbf4219")},   # Query parameter
  {'$set': {"name": "priya"}})

#update  single record using user created Id
colletions.update_one(
   {'password':"rama123"},   # Query parameter
  {'$set': {"name": "roshan"}})


 #update  multiple record using mongodb Id
# ids = [8,4,6]
# colletions.update(
#    { '_id': {'$in': ids } },
#    { '$set': { 'visibility' : 'yes' } },{ 'upsert':'false' ,'multi':'true'}
# )

#removing  single item using user created Id 
colletions.delete_one({"name": 'dash'})
#removing  all  --  colletions.remove({});

colletions.delete_one(
   {'_id': ObjectId("5f80f12eaa737396ad2d1936")})   # Query parameter
  


#removing  single field from collection using user created Id 
colletions.update({"_id": 5}, {'$unset':{'name':1}});
        
if __name__ == "__main__":
    app.run(debug=True)