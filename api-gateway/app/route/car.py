from flask import Blueprint, make_response
from app.security.configuration import token_required
import httpx
import logging

cars_blueprint = Blueprint('cars_blueprint', __name__, url_prefix='/cars')

# NOTE tu wszystko jest ok, lepiej robić blueprinty w api gateway
# @token_required(roles=['ADMIN'])
@cars_blueprint.route('/all')
def get_all():
    res = httpx.get('http://cars-service:8001/cars/all') # NOTE serwisy komunikują się po swoich nazwach kontenerów, a nie localhost
    logging.info(res.json())
    return res.json(), 200
