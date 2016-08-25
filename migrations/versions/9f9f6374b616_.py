"""empty message

Revision ID: 9f9f6374b616
Revises: None
Create Date: 2016-08-25 22:48:06.893609

"""

# revision identifiers, used by Alembic.
revision = '9f9f6374b616'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('providers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('tenant_name', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('api_version', sa.String(length=64), nullable=True),
    sa.Column('password', sa.Text(length=256), nullable=True),
    sa.Column('url', sa.Text(length=512), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('enabled', sa.Boolean(), default=True, nullable=False),
    sa.Column('validated', sa.Boolean(), default=False, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_providers_api_version'), 'providers', ['api_version'], unique=False)
    op.create_index(op.f('ix_providers_name'), 'providers', ['name'], unique=True)
    op.create_index(op.f('ix_providers_provider'), 'providers', ['provider'], unique=False)
    op.create_index(op.f('ix_providers_tenant_name'), 'providers', ['tenant_name'], unique=False)
    op.create_index(op.f('ix_providers_username'), 'providers', ['username'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('suspended', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_avatar'), 'users', ['avatar'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_full_name'), 'users', ['full_name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_full_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_avatar'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_providers_username'), table_name='providers')
    op.drop_index(op.f('ix_providers_tenant_name'), table_name='providers')
    op.drop_index(op.f('ix_providers_provider'), table_name='providers')
    op.drop_index(op.f('ix_providers_name'), table_name='providers')
    op.drop_index(op.f('ix_providers_api_version'), table_name='providers')
    op.drop_table('providers')
    ### end Alembic commands ###