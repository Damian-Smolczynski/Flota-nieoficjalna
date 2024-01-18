"""Zasilenie tabel

Revision ID: 183451d90b79
Revises: 9cebc6b3adb5
Create Date: 2024-01-15 23:16:36.028134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '183451d90b79'
down_revision: Union[str, None] = '9cebc6b3adb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO db_1.fuel_type(name, efficiency) values 
        ('petrol', 0.89),
        ('diesel', 0.95),
        ('electric', 0.7)
        """
    )

    op.execute(
        """
        INSERT INTO db_1.vehicle_status(name, description) values 
        ('ready', 'Ready to use'),
        ('repair', 'Waiting for repairs to be done'),
        ('not_legal', 'Waiting for mot or insurance')
        """
    )

    op.execute(
        """
        INSERT INTO db_1.cars(
            registration,
            vin,
            make,
            model,
            first_registration_date,
            production_year,
            mileage,
            fuel_consumption,
            fuel_type_id,
            vehicle_status_id
            ) values (
                'WA38900',
                'VF3MJEHZRJS446751',
                'Peugeot',
                '308',
                '2017-08-21',
                2017,
                150000,
                5.6,
                1,
                1
            ),
            (
                'WZ38900',
                'GF3MJE5ZRJS416751',
                'Ford',
                'Focus',
                '2021-08-21',
                2020,
                15000,
                7.9,
                1,
                1
            )
        """
    )

    op.execute(
        """
        INSERT INTO db_1.mots(legal_identifier, start_date, end_date, car_id) 
        values (
            'ZB-2022-11-k',
            '2022-11-11',
            '2023-11-11',
            1
        ) 
        """
    )

    op.execute(
        """
        INSERT INTO db_1.insurances(legal_identifier, start_date, end_date, car_id) 
        values (
            'PZU-2022-11-k',
            '2022-11-11',
            '2023-11-11',
            2
        ) 
        """
    )

    op.execute(
        """
        INSERT INTO db_1.fleets(name, creation_date, description) values 
        ('Orlen', '2024-01-15', 'Flota samochodów pracowników szczebla menadżerskiego')
        """
    )

    op.execute(
        """
        INSERT INTO db_1.fleet_vehicles(car_id, fleet_id) values
        (1, 1),
        (2, 1)
        """
    )



def downgrade() -> None:
    op.execute(
        """
        DELETE FROM db_1.fleet_vehicles;
        DELETE FROM db_1.fleets;
        """
    )

    op.execute(
        """
        DELETE FROM db_1.cars
        """
    )

    op.execute(
        """
            DELETE FROM db_1.mots
            """
    )

    op.execute(
        """
        DELETE FROM db_1.insurances
        """
    )

    op.execute(
        """
        DELETE FROM db_1.fuel_type
        """
    )

    op.execute(
        """
        DELETE FROM db_1.vehicle_status
        """
    )


