"""Tworzenie tabeli samochodów

Revision ID: d130ab7099f8
Revises: 
Create Date: 2024-01-15 22:13:43.858914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd130ab7099f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'fuel_type',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(10), nullable=False, unique=True),
        sa.Column('efficiency', sa.Double, nullable=False)
    )
    op.create_table(
        'vehicle_status',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(20), nullable=False, unique=True),
        sa.Column('description', sa.String(500), nullable=False, unique=True)
    )

    op.create_table(
        'cars',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('registration', sa.String(10), nullable=False, unique=True),
        sa.Column('vin', sa.String(17), nullable=False, unique=True),
        sa.Column('make', sa.String(100), nullable=False),
        sa.Column('model', sa.String(100), nullable=False),
        sa.Column('first_registration_date', sa.Date, nullable=False),
        sa.Column('production_year', sa.Integer, nullable=False),
        sa.Column('mileage', sa.Integer, nullable=False, default=0),
        sa.Column('fuel_consumption', sa.Double, nullable=False),
        sa.Column('fuel_type_id', sa.Integer, sa.ForeignKey('fuel_type.id')),
        sa.Column('vehicle_status_id', sa.Integer, sa.ForeignKey('vehicle_status.id'))


    )


def downgrade() -> None:
    op.drop_table('cars')
    op.drop_table('vehicle_status')
    op.drop_table('fuel_type')

