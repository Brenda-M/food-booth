"""empty message

Revision ID: 725013ac496e
Revises: 464950a92805
Create Date: 2020-05-14 19:44:42.056625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725013ac496e'
down_revision = '464950a92805'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###