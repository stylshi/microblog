"""followers

Revision ID: 899594498116
Revises: bfc05c79d63b
Create Date: 2021-03-02 11:22:36.615938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '899594498116'
down_revision = 'bfc05c79d63b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
