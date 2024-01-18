from app.db.configuration import sa

class FuelTypeModel(sa.Model):
    __tablename__ = "fuel_type"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(10), unique=True)
    efficiency = sa.Column(sa.Double, nullable=False)

class VehicleStatusModel(sa.Model):
    __tablename__ = "vehicle_status"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(20), unique=True)
    description = sa.Column(sa.String(500), nullable=False, unique=True)


class CarModel(sa.Model):
    __tablename__ = 'cars'
    id = sa.Column(sa.Integer, primary_key=True)
    registration = sa.Column(sa.String(10), nullable=False)
    vin = sa.Column(sa.String(14), nullable=False)
    make = sa.Column(sa.String(100), nullable=False)
    model = sa.Column(sa.String(100), nullable=False)
    first_registration_date = sa.Column(sa.Date, nullable=False)
    production_year = sa.Column(sa.Integer, nullable=False)
    mileage = sa.Column(sa.Integer, nullable=False)
    fuel_consumption = sa.Column(sa.Double, nullable=False)
    fuel_type_id = sa.Column(sa.Integer, sa.ForeignKey('fuel_type.id'), nullable=False)
    vehicle_status_id = sa.Column(sa.Integer, sa.ForeignKey('vehicle_status.id'), nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'registration': self.registration,
            'vin': self.vin,
            'make': self.make,
            'model': self.model,
            'first_registration_date': self.first_registration_date.isoformat(),
            'production_year': self.production_year,
            'mileage': self.mileage,
            'fuel_type_id': self.fuel_type_id,
            'vehicle_status_id': self.vehicle_status_id
        }

    def save(self):
        sa.session.add(self)
        sa.session.commit()

    def delete(self):
        sa.session.delete(self)
        sa.session.commit()

    def update(self, data):
        self.registration = data.get('registration', self.registration)
        self.vin = data.get('vin', self.vin)
        self.make = data.get('make', self.make)
        self.model = data.get('model', self.model)
        self.first_registration_date = data.get('first_registration_date', self.first_registration_date)
        self.production_year = data.get('production_year', self.production_year)
        self.mileage = data.get('mileage', self.mileage)
        self.fuel_type_id = data.get('fuel_type_id', self.fuel_type_id)
        self.vehicle_status_id = data.get('vehicle_status_id', self.vehicle_status_id)

        sa.session.add(self)
        sa.session.commit()

    @classmethod
    def get_by_id(cls, car_id: int) -> 'CarModel':
        return cls.query.get(car_id)

    @classmethod
    def get_all(cls) -> list['CarModel']:
        return [car.as_dict() for car in cls.query.all()]