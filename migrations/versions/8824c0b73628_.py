"""empty message

Revision ID: 8824c0b73628
Revises: None
Create Date: 2016-12-20 08:40:05.347805

"""

# revision identifiers, used by Alembic.
revision = '8824c0b73628'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('memory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('memory', sa.Integer(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('memory')
    ### end Alembic commands ###