from flask import Blueprint, make_response, Response, request, jsonify
from app.security.configuration import token_required
import httpx
import logging

cars_blueprint = Blueprint('cars_blueprint', __name__, url_prefix='/cars')
# TODO zrobić kilka 'example' w postmanie
# NOTE tu wszystko jest ok, lepiej robić blueprinty w api gateway
# @token_required(roles=['ADMIN'])
@cars_blueprint.route('/all')
def get_all() -> Response:
    res = httpx.get('http://cars-service:8001/cars/all') # NOTE serwisy komunikują się po swoich nazwach kontenerów, a nie localhost
    logging.info(res.json())
    return res.json(), res.status_code

@cars_blueprint.route('/<int:car_id>', methods=['GET'])
def get_one_by_id(car_id) -> Response:
    res = httpx.get(f'http://cars-service:8001/car/{car_id}')
    logging.info(res.json())
    return res.json(), res.status_code


@cars_blueprint.route('/', methods=["POST"])
def create_car() -> Response:
    data = request.get_json()
    res = httpx.post('http://cars-service:8001/car', json=data)
    if type(res.json()) == int:
        return jsonify(res.json())
    return res.json(), 400


@cars_blueprint.route('/<int:car_id>', methods=['DELETE'])
def delete_car(car_id) -> Response:
    res = httpx.delete(f'http://cars-service:8001/car/{car_id}')
    # TODO Czy tutaj zmieniać np message, czy mogę to przenosić bezpośrednio z responsa
    return res.json(), res.status_code
