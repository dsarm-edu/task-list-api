"""adds to_dict and from_dict to Goal model

Revision ID: ff647d56c2e6
Revises: 9dba2e6356e9
Create Date: 2023-05-10 20:15:37.499598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff647d56c2e6'
down_revision = '9dba2e6356e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
