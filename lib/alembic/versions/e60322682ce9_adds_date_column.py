"""adds date column

Revision ID: e60322682ce9
Revises: 9756042ca240
Create Date: 2023-08-11 13:41:06.958790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e60322682ce9'
down_revision = '9756042ca240'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expenses', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('expenses', 'date')
    # ### end Alembic commands ###
