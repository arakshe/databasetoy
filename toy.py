from flask import Blueprint, request, jsonify, make_response
import json
from src import db


toy = Blueprint('toy', __name__)

# Get all customers from the DB
@toy.route('/toy', methods=['GET'])
def get_toy():
    cursor = db.get_db().cursor()
    cursor.execute('select * from toy')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@toy.route('/toy/<toyID>', methods=['GET'])
def get_customer(toyID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from toy where toy_id = {0}'.format(toyID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
