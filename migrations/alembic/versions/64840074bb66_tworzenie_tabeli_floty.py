"""Tworzenie tabeli floty

Revision ID: 64840074bb66
Revises: d130ab7099f8
Create Date: 2024-01-15 22:34:05.058580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64840074bb66'
down_revision: Union[str, None] = 'd130ab7099f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'fleets',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100), nullable=False, unique=True),
        sa.Column('creation_date', sa.Date, nullable=False),
        sa.Column('description', sa.String(500), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('fleets')
