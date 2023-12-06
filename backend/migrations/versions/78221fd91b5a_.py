"""empty message

Revision ID: 78221fd91b5a
Revises: 898a0c6cdc39
Create Date: 2023-12-05 16:10:29.668666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78221fd91b5a'
down_revision = '898a0c6cdc39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=128), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###