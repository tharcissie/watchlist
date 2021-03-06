"""pass field

Revision ID: dbe99de96e32
Revises: acdb8cb4f186
Create Date: 2020-11-26 16:16:59.571943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbe99de96e32'
down_revision = 'acdb8cb4f186'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
