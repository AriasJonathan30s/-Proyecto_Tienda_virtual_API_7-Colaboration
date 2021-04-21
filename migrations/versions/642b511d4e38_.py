"""empty message

Revision ID: 642b511d4e38
Revises: 
Create Date: 2021-04-21 02:17:19.647577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642b511d4e38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catalogo_productos',
    sa.Column('id_prod', sa.Integer(), nullable=False),
    sa.Column('nombre_productos', sa.String(length=255), nullable=True),
    sa.Column('presentacion_productos', sa.String(length=255), nullable=True),
    sa.Column('costo_productos', sa.Float(), nullable=True),
    sa.Column('precio_productos', sa.Float(), nullable=True),
    sa.Column('departamento_productos', sa.String(length=255), nullable=True),
    sa.Column('cantidad_productos', sa.Integer(), nullable=True),
    sa.Column('imagen_productos', sa.LargeBinary(), nullable=True),
    sa.Column('hora_registro_catalogo', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_prod')
    )
    op.create_table('tienda',
    sa.Column('id_plaza', sa.Integer(), nullable=False),
    sa.Column('nombre_plaza', sa.String(length=255), nullable=True),
    sa.Column('direccion_plaza', sa.String(length=255), nullable=True),
    sa.Column('tel_plaza', sa.Integer(), nullable=True),
    sa.Column('horario_plaza', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id_plaza')
    )
    op.create_table('usuario_cliente',
    sa.Column('id_cliente', sa.Integer(), nullable=False),
    sa.Column('nombre_cliente', sa.String(length=255), nullable=True),
    sa.Column('apellido_cliente', sa.String(length=255), nullable=True),
    sa.Column('direccion_cliente', sa.String(length=255), nullable=True),
    sa.Column('correo_cliente', sa.String(length=255), nullable=True),
    sa.Column('telefono_cliente', sa.Integer(), nullable=True),
    sa.Column('usuario_cliente', sa.String(length=255), nullable=True),
    sa.Column('contrasenia_cliente', sa.String(length=255), nullable=True),
    sa.Column('hora_registro_cliente', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_cliente')
    )
    op.create_table('usuario_trabajador',
    sa.Column('id_trabajador', sa.Integer(), nullable=False),
    sa.Column('nombre_trabajador', sa.String(length=255), nullable=True),
    sa.Column('apellido_trabajador', sa.String(length=255), nullable=True),
    sa.Column('correo_trabajador', sa.String(length=255), nullable=True),
    sa.Column('usuario_trabajador', sa.String(length=255), nullable=True),
    sa.Column('contrasenia_trabajador', sa.String(length=255), nullable=True),
    sa.Column('rango_trabajador', sa.String(length=255), nullable=True),
    sa.Column('hora_registro_trabajador', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_trabajador')
    )
    op.create_table('compras',
    sa.Column('id_compras', sa.Integer(), nullable=False),
    sa.Column('id_prod_compras', sa.Integer(), nullable=True),
    sa.Column('cantidad_compras', sa.String(length=255), nullable=True),
    sa.Column('precio_compras', sa.String(length=255), nullable=True),
    sa.Column('caducidad_compras', sa.String(length=255), nullable=True),
    sa.Column('fecha_pedido', sa.DateTime(), nullable=True),
    sa.Column('fecha_entrega', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_prod_compras'], ['catalogo_productos.id_prod'], ),
    sa.PrimaryKeyConstraint('id_compras')
    )
    op.create_table('evaluacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('comentario', sa.Text(), nullable=True),
    sa.Column('hora_Salida', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario_cliente.id_cliente'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proveedores',
    sa.Column('id_proveedor', sa.Integer(), nullable=False),
    sa.Column('nombre_proveedor', sa.String(length=255), nullable=True),
    sa.Column('direccion_proveedor', sa.String(length=255), nullable=True),
    sa.Column('telefono_proveedor', sa.String(length=255), nullable=True),
    sa.Column('horarios_proveedor', sa.String(length=255), nullable=True),
    sa.Column('especialidad_proveedor', sa.String(length=255), nullable=True),
    sa.Column('costo_producto', sa.Float(), nullable=True),
    sa.Column('evaluacion_proveedor', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['costo_producto'], ['catalogo_productos.costo_productos'], ),
    sa.PrimaryKeyConstraint('id_proveedor')
    )
    op.create_table('ventas',
    sa.Column('id_ventas', sa.Integer(), nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=True),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('cantidad_ventas', sa.String(length=255), nullable=True),
    sa.Column('ticket_ventas', sa.Float(), nullable=True),
    sa.Column('estado_pago', sa.String(length=255), nullable=True),
    sa.Column('hora_pedido', sa.DateTime(), nullable=True),
    sa.Column('hora_entrega', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['usuario_cliente.id_cliente'], ),
    sa.ForeignKeyConstraint(['id_producto'], ['catalogo_productos.id_prod'], ),
    sa.PrimaryKeyConstraint('id_ventas')
    )
    op.create_table('almacen',
    sa.Column('id_almacen', sa.Integer(), nullable=False),
    sa.Column('id_compras', sa.Integer(), nullable=True),
    sa.Column('id_producto', sa.Integer(), nullable=True),
    sa.Column('nombre_almacen', sa.String(length=255), nullable=True),
    sa.Column('cantidad_almacen', sa.Integer(), nullable=True),
    sa.Column('cant_entrada_almacen', sa.Integer(), nullable=True),
    sa.Column('cant_salida_almacen', sa.Integer(), nullable=True),
    sa.Column('ubicacion_almacen', sa.String(length=255), nullable=True),
    sa.Column('caducidad_almacen', sa.String(length=255), nullable=True),
    sa.Column('hora_registro_cliente', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cant_entrada_almacen'], ['compras.id_compras'], ),
    sa.ForeignKeyConstraint(['cant_salida_almacen'], ['ventas.id_ventas'], ),
    sa.ForeignKeyConstraint(['cantidad_almacen'], ['catalogo_productos.id_prod'], ),
    sa.ForeignKeyConstraint(['id_compras'], ['compras.id_compras'], ),
    sa.ForeignKeyConstraint(['id_producto'], ['catalogo_productos.id_prod'], ),
    sa.PrimaryKeyConstraint('id_almacen')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('almacen')
    op.drop_table('ventas')
    op.drop_table('proveedores')
    op.drop_table('evaluacion')
    op.drop_table('compras')
    op.drop_table('usuario_trabajador')
    op.drop_table('usuario_cliente')
    op.drop_table('tienda')
    op.drop_table('catalogo_productos')
    # ### end Alembic commands ###
