"""Add user

Revision ID: 9f832c9f4c6
Revises: 4d255e72ec0e
Create Date: 2014-03-14 10:06:10.357541

"""

# revision identifiers, used by Alembic.
revision = '9f832c9f4c6'
down_revision = '4d255e72ec0e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=False),
    sa.Column('fb_id', sa.Unicode(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###
