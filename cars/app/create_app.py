from flask import Flask
from flask_restful import Api

from app.cors.configuration import CORS_CONFIG
from app.db.configuration import sa
from app.env_variables import SQLALCHEMY_DATABASE_URI
from app.route.car import AllCarsResource, CarResource
from flask_cors import CORS


app = Flask(__name__)

def main():
    with app.app_context():

        # KONFIGURACJA BAZY
        app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        sa.init_app(app)

        # KONFIGURACJA API
        api = Api(app)
        api.add_resource(AllCarsResource, '/cars/all')
        api.add_resource(CarResource, '/car/<int:car_id>')

        # ----------------------------------------------------------------------
        # CORS CONFIGURATION
        # ----------------------------------------------------------------------
        CORS(app, resources={
            '/*': CORS_CONFIG
        })

        @app.route('/')
        def index():
            # Sprawdzenie czy działają mi poprawnie modele
            # sa.session.add(FuelTypeModel(name='Fuel', efficiency=2.0))
            # sa.session.commit()
            # sa.session.add(VehicleStatusModel(name='working', description='working'))
            # sa.session.commit()
            return 'Index'

    return app