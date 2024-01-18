"""Tworzenie tabeli uzytkownikow

Revision ID: 39d429859d82
Revises: 3f19f99e1717
Create Date: 2024-01-16 21:41:22.856088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from werkzeug.security import generate_password_hash


# revision identifiers, used by Alembic.
revision: str = '39d429859d82'
down_revision: Union[str, None] = '183451d90b79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(255), unique=True),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('role', sa.String(10), nullable=False, default='USER'),
        sa.Column('active', sa.Boolean, default=False, nullable=False)
    )

    op.execute(
        f"INSERT INTO users (username, password, email, role, active) VALUES ('root', '{generate_password_hash('root')}', 'ROOT@GMAIL.COM','ADMIN' ,1)")


def downgrade() -> None:
    op.drop_table('users')
