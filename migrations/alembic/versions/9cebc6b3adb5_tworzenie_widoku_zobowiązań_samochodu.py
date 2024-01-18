"""Tworzenie widoku zobowiązań samochodu

Revision ID: 9cebc6b3adb5
Revises: a5137feb09ce
Create Date: 2024-01-15 23:01:13.417897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cebc6b3adb5'
down_revision: Union[str, None] = 'a5137feb09ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE VIEW cars_obligations
            AS 
            SELECT 
                c.id,
                c.registration,
                case 
                    when i.id is not null then 'Valid'
                    else 'Invalid'
                end as insurance,
                case 
                    when m.id is not null then 'Valid'
                    else 'Invalid'
                end as mot
            from db_1.cars c 
                left join db_1.mots m on c.id = m.car_id 
                left join db_1.insurances i on c.id = i.car_id;
        """
    )


def downgrade() -> None:
    op.execute('DROP VIEW cars_obligations')
