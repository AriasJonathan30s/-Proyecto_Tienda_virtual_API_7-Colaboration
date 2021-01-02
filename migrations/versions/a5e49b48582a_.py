"""empty message

Revision ID: a5e49b48582a
Revises: ce5496a63b18
Create Date: 2021-01-01 22:38:33.747878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5e49b48582a'
down_revision = 'ce5496a63b18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('botanas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('costo', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enlatados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('costo', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('licores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('costo', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('refrescos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('costo', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refrescos')
    op.drop_table('licores')
    op.drop_table('enlatados')
    op.drop_table('botanas')
    # ### end Alembic commands ###