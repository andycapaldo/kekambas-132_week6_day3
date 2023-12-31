"""Create AddressBook Table

Revision ID: 81b1b448dedd
Revises: 
Create Date: 2023-10-25 16:20:15.330876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81b1b448dedd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address_book')
    # ### end Alembic commands ###
