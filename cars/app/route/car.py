from flask_restful import Resource, reqparse
from flask import Response, make_response, request
from app.db.model import CarModel
from sqlalchemy.exc import IntegrityError
from app.db.configuration import sa

import logging

logging.basicConfig(level=logging.DEBUG)

# TODO Wprowadzić walidację

class AllCarsResource(Resource):
    def get(self) -> Response:
        cars = CarModel.get_all()
        response = make_response({'all_cars': cars})
        response.headers['Content-Type'] = 'application/json'
        response.status = 200
        return response

class CarResource(Resource):

    def get(self, car_id):
        car = CarModel.get_by_id(car_id)
        if car:
            return car.as_dict(), 200
        return {"message": "Car does not exist"}, 404

    def delete(self, car_id):
        car_to_delete = CarModel.get_by_id(car_id)
        if car_to_delete:
            car_to_delete.delete()
            return {"message": "Car has been deleted"}, 200
        return {"message": "Car not found"}, 404

    def patch(self, car_id):
        data = request.get_json()
        car = CarModel.get_by_id(car_id)
        if car:
            car.update(data)
            return car.as_dict(), 200
        return {"message": "Car does not exist"}


class CarResourceAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('registration', type=str, required=True, help='Registration of the car is required')
    parser.add_argument('vin', type=str, required=True, help='Vin of the car is required')
    parser.add_argument('make', type=str, required=True, help='Make of the car is required')
    parser.add_argument('model', type=str, required=True, help='Model of the car is required')
    parser.add_argument('first_registration_date', type=str, required=True,
                        help='First Registration Date of the car is required')
    parser.add_argument('production_year', type=str, required=True, help='Production year of the car is required')
    parser.add_argument('mileage', type=str, required=True, help='Mileage of the car is required')
    parser.add_argument('fuel_consumption', type=str, required=True, help='Fuel consumption of the car is required')
    parser.add_argument('fuel_type_id', type=int, required=True, help='Fuel type id of the car is required')
    parser.add_argument('vehicle_status_id', type=int, required=True, help='Vehicle status id of the car is required')

    def post(self):
        # to daję poza try, bo ładnie zwraca 400, jeżeli nie ma argumentu
        data = self.parser.parse_args()
        try:
            car = CarModel(**data)
            car.save()
            return car.id, 201
        except IntegrityError as e:
            sa.session.rollback()
            return {"message": e.orig.args[1]}