"""Mudando de sistema de pedidos para de registro

Revision ID: 1b3fa53a04d1
Revises: 3f1384c22963
Create Date: 2024-01-05 16:51:24.268283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b3fa53a04d1'
down_revision = '3f1384c22963'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('representative')
    op.drop_table('representative_client_association')
    op.drop_table('employee')
    op.drop_table('user_empresa')
    op.drop_table('admin')
    op.drop_table('empresa')
    op.drop_table('order')
    op.drop_table('client')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))
        batch_op.drop_column('role')
        batch_op.drop_column('contact_email')
        batch_op.drop_column('contact_phone')
        batch_op.drop_column('address')
        batch_op.drop_column('cpf')
        batch_op.drop_column('city')
        batch_op.drop_column('is_person')
        batch_op.drop_column('state')
        batch_op.drop_column('state_registration')
        batch_op.drop_column('postal_code')
        batch_op.drop_column('cnpj')
        batch_op.drop_column('is_complete')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_complete', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('cnpj', sa.VARCHAR(length=18), nullable=True))
        batch_op.add_column(sa.Column('postal_code', sa.VARCHAR(length=9), nullable=True))
        batch_op.add_column(sa.Column('state_registration', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('state', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('is_person', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('city', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('cpf', sa.VARCHAR(length=14), nullable=True))
        batch_op.add_column(sa.Column('address', sa.VARCHAR(length=200), nullable=True))
        batch_op.add_column(sa.Column('contact_phone', sa.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('contact_email', sa.VARCHAR(length=120), nullable=True))
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=50), nullable=True))
        batch_op.drop_column('is_admin')

    op.create_table('client',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=50), nullable=False),
    sa.Column('client_id', sa.INTEGER(), nullable=True),
    sa.Column('employee_id', sa.INTEGER(), nullable=True),
    sa.Column('status_info', sa.VARCHAR(length=200), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('empresa',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_empresa',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('empresa_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['empresa_id'], ['empresa.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'empresa_id')
    )
    op.create_table('employee',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('representative_client_association',
    sa.Column('representative_id', sa.INTEGER(), nullable=True),
    sa.Column('client_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['representative_id'], ['representative.id'], )
    )
    op.create_table('representative',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###