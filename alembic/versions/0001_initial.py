"""initial migration

Revision ID: 0001_initial
Revises:
Create Date: 2023-01-01 00:00:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'persons',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False)
    )

def downgrade():
    op.drop_table('persons')
