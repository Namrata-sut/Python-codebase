"""renamaed table question

Revision ID: 75d2d9b3112f
Revises: 
Create Date: 2025-02-10 16:02:29.155217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '75d2d9b3112f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('options', sa.JSON(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('level', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Questions')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Questions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('options', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.Column('answer', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('level', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Questions_pkey')
    )
    op.drop_table('questions_table')
    # ### end Alembic commands ###
