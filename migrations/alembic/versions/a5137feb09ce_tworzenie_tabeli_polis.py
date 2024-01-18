"""Tworzenie tabeli polis

Revision ID: a5137feb09ce
Revises: 698c2b5a9a64
Create Date: 2024-01-15 22:58:38.454948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5137feb09ce'
down_revision: Union[str, None] = '698c2b5a9a64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'insurances',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('legal_identifier', sa.String(20), nullable=False, unique=True),
        sa.Column('start_date', sa.Date, nullable=False),
        sa.Column('end_date', sa.Date, nullable=False),
        sa.Column('car_id', sa.Integer, sa.ForeignKey('cars.id', ondelete='cascade'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('insurances')

