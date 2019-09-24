"""third commit

Revision ID: 459ab01fece1
Revises: 2312012522ea
Create Date: 2019-09-23 11:20:41.867319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '459ab01fece1'
down_revision = '2312012522ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('category', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
