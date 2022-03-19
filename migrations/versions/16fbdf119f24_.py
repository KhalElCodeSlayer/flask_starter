"""empty message

Revision ID: 16fbdf119f24
Revises: 
Create Date: 2022-03-17 03:45:27.681258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16fbdf119f24'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('property_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('property_title', sa.String(length=255), nullable=True),
    sa.Column('property_description', sa.String(length=1080), nullable=True),
    sa.Column('property_rooms', sa.String(length=255), nullable=True),
    sa.Column('property_bathroom', sa.String(length=255), nullable=True),
    sa.Column('property_price', sa.String(length=255), nullable=True),
    sa.Column('property_type', sa.String(length=20), nullable=True),
    sa.Column('property_location', sa.String(length=255), nullable=True),
    sa.Column('property_photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('property_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###
