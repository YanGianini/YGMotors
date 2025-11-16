"""create vehicles table

Revision ID: 6cee7e8eafc8
Revises: 
Create Date: 2025-11-16 00:58:04.892079

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cee7e8eafc8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('brand', sa.String(length=100), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('vehicles')
