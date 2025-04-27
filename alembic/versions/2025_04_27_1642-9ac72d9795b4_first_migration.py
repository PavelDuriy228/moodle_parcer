"""first migration

Revision ID: 9ac72d9795b4
Revises:
Create Date: 2025-04-27 16:42:41.741229

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9ac72d9795b4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    
    op.create_table(
        "answers",
        sa.Column("hash_ans", sa.String(), nullable=False),
        sa.Column("cor_ans", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    
    op.drop_table("answers")
    
