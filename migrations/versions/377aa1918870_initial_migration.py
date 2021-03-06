"""Initial Migration

Revision ID: 377aa1918870
Revises: 42390db6d84a
Create Date: 2022-05-04 23:11:59.079264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '377aa1918870'
down_revision = '42390db6d84a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
