"""Tworzenie tabeli samochodów we flocie

Revision ID: ab14c398fc47
Revises: 64840074bb66
Create Date: 2024-01-15 22:39:06.327835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab14c398fc47'
down_revision: Union[str, None] = '64840074bb66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'fleet_vehicles',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('car_id', sa.Integer, sa.ForeignKey('cars.id', ondelete='cascade', onupdate='cascade'), nullable=False, unique=True),
        sa.Column('fleet_id', sa.Integer, sa.ForeignKey('fleets.id', ondelete='cascade', onupdate='cascade'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('fleet_vehicles')

