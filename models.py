# Crear clase modelo
import app
from werkzeug.security import generate_password_hash
import datetime
from app import db


class Usuario_cliente(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
    id_cliente = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    nombre_cliente = app.db.Column(app.db.String(255))
    apellido_cliente = app.db.Column(app.db.String(255))
    direccion_cliente = app.db.Column(app.db.String(255))
    correo_cliente = app.db.Column(app.db.String(255))
    telefono_cliente = app.db.Column(app.db.Integer)
    usuario_cliente = app.db.Column(app.db.String(255))
    contrasenia_cliente = app.db.Column(app.db.String(255))
    evaluacion_cliente = app.db.relationship('Evaluacion')
    listado_cliente = app.db.relationship('Listado')
    hora_registro_cliente = app.db.Column(app.db.DateTime, default=datetime.datetime.now)

    def __init__(self, nombre_cliente, apellido_cliente, correo_cliente, usuario_cliente, contrasenia_cliente):
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.direccion_cliente = direccion_cliente
        self.correo_cliente = correo_cliente
        self.telefono_cliente = telefono_cliente
        self.usuario_cliente = usuario_cliente
        self.contrasenia_cliente = self.__create_password(contrasenia_cliente)

    def __str__(self):
        return (
            f'Id:{self.id_cliente},'
            f'Nombre:{self.nombre_cliente},'
            f'Apellido:{self.apellido_cliente},'
            f'Direccion:{self.direccion_cliente},'
            f'Email:{self.correo_cliente},'
            f'Telefono:{self.telefono_cliente},'
            f'Usuario:{self.usuario_cliente},'
            f'Contraseña:{self.contrasenia_cliente}')

    def __create_password(self, contrasenia):
        return generate_password_hash(contrasenia)


class Usuario_trabajador(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
    id_trabajador = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    nombre_trabajador = app.db.Column(app.db.String(255))
    apellido_trabajador = app.db.Column(app.db.String(255))
    correo_trabajador = app.db.Column(app.db.String(255))
    usuario_trabajador = app.db.Column(app.db.String(255))
    contrasenia_trabajador = app.db.Column(app.db.String(255))
    rango_trabajador = app.db.Column(app.db.String(255))
    hora_registro_trabajador = app.db.Column(app.db.DateTime, default=datetime.datetime.now)

    def __init__(self, nombre_trabajador, apellido_trabajador, correo_trabajador, usuario_trabajador, rango_trabajador,
                 contrasenia_trabajador):
        self.nombre = nombre_trabajador
        self.apellido = apellido_trabajador
        self.correo = correo_trabajador
        self.usuario = usuario_trabajador
        self.rango_trabajador = rango_trabajador
        self.contrasenia_trabajador = self.__create_password(contrasenia_trabajador)

    def __str__(self):
        return (
            f'Id:{self.id_trabajador},'
            f'Nombre:{self.nombre_trabajador},'
            f'Apellido:{self.apellido_trabajador},'
            f'Email:{self.correo_trabajador},'
            f'Usuario:{self.usuario_trabajador},'
            f'Rango:{self.rango_trabajador},'
            f'Contraseña:{self.contrasenia_trabajador}')

    def __create_password(self, contrasenia):
        return generate_password_hash(contrasenia)


class Compras(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
    id_compras = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    id_prod_compras = app.db.Column(app.db.Integer, app.db.ForeignKey('catalogo_productos.id_prod'))
    cantidad_compras = app.db.Column(app.db.String(255))
    precio_compras = app.db.Column(app.db.String(255))
    caducidad_compras = app.db.Column(app.db.String(255))
    fecha_pedido = app.db.Column(app.db.DateTime, default=datetime.datetime.now)
    fecha_entrega = app.db.Column(app.db.DateTime, default=datetime.datetime.now)

    def __init__(self, id_prod_compras, cantidad_compras, precio_compras, caducidad_compras):
        self.id_prod_compras = id_prod_compras
        self.cantidad_compras = cantidad_compras
        self.precio_compras = precio_compras
        self.caducidad_compras = caducidad_compras

    def __str__(self):
        return (
            f'Id:{self.id_compras},'
            f'Nombre:{self.id_prod_compras},'
            f'Apellido:{self.cantidad_compras},'
            f'Email:{self.precio_compras},'
            f'Usuario:{self.caducidad_compras},'
        )


class Ventas(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
    id_ventas = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    id_producto = app.db.Column(app.db.Integer, app.db.ForeignKey('catalogo_productos.id_prod'))
    id_cliente = app.db.Column(app.db.Integer, app.db.ForeignKey('usuario_cliente.id_cliente'))
    cantidad_ventas = app.db.Column(app.db.String(255))
    ticket_ventas = app.db.Column(app.db.Float)
    estado_pago = app.db.Column(app.db.String(255))
    hora_pedido = app.db.Column(app.db.DateTime, default=datetime.datetime.now)
    hora_entrega = app.db.Column(app.db.DateTime, default=datetime.datetime.now)

    def __init__(self, id_ventas, id_producto, id_cliente, cantidad_ventas, ticket_ventas, estado_pago, hora_pedido,
                 hora_entrega):
        self.id_ventas = id_ventas
        self.id_producto = id_producto
        self.id_cliente = id_cliente
        self.cantidad_ventas = cantidad_ventas
        self.ticket_ventas = ticket_ventas
        self.estado_pago = estado_pago
        self.hora_pedido = hora_pedido
        self.hora_entrega = hora_entrega

    def __str__(self):
        return (
            f'Id:{self.id_ventas},'
            f'Producto:{self.id_producto},'
            f'Usuario:{self.id_cliente},'
            f'Producto cantidad:{self.cantidad_ventas},'
            f'Recibo de compra:{self.ticket_ventas},'
            f'¿Pagado?:{self.estado_pago}'
        )


class Evaluacion(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    usuario_id = app.db.Column(app.db.Integer, app.db.ForeignKey('usuario_cliente.id_cliente'))
    comentario = app.db.Column(app.db.Text())
    hora_Salida = app.db.Column(app.db.DateTime, default=datetime.datetime.now)

    def __init__(self, usuario_id, comentario):
        self.usuario_id = usuario_id
        self.comentario = comentario

    def __str__(self):
        return (
            f'Id:{self.id},'
            f'Nombre:{self.usuario_id},'
            f'Apellido:{self.comentario},'
        )


class Catalogo_productos(app.db.Model):  # Creamos la clase modelo para la macros de datos funcion model
    id_prod = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    nombre_productos = app.db.Column(app.db.String(255))
    presentacion_productos = app.db.Column(app.db.String(255))
    costo_productos = app.db.Column(app.db.Float)
    precio_productos = app.db.Column(app.db.Float)
    departamento_productos = app.db.Column(app.db.String(255))
    cantidad_productos = app.db.Column(app.db.Integer)
    imagen_productos = app.db.Column(app.db.LargeBinary)
    hora_registro_catalogo = app.db.Column(app.db.DateTime, default=datetime.datetime.now)

    def __init__(self, nombre_productos, presentacion_productos, costo_productos, precio_productos,
                 departamento_productos, cantidad_productos, imagen_productos):
        self.nombre_productos = nombre_productos
        self.presentacion_productos = presentacion_productos
        self.costo_productos = costo_productos
        self.precio_productos = precio_productos
        self.departamento_productos = departamento_productos
        self.cantidad_productos = cantidad_productos
        self.imagen_productos = imagen_productos

    def __str__(self):
        return (
            f'Id:{self.id_prod},'
            f'Nombre:{self.nombre_productos},'
            f'Presentacion:{self.presentacion_productos},'
            f'Costo:{self.costo_productos},'
            f'Precio:{self.precio_productos},'
            f'Departamento:{self.departamento_productos},'
            f'Cantidad:{self.cantidad_productos},'
            f'Imagen:{self.imagen_productos}'
        )


class Almacen(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
    id_almacen = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    id_compras = app.db.Column(app.db.Integer, app.db.ForeignKey('compras.id_compras'))
    id_producto = app.db.Column(app.db.Integer, app.db.ForeignKey('catalogo_productos.id_prod'))
    nombre_almacen = app.db.Column(app.db.String(255))
    cantidad_almacen = app.db.Column(app.db.Integer, app.db.ForeignKey('catalogo_productos.id_prod'))
    cant_entrada_almacen = app.db.Column(app.db.Integer, app.db.ForeignKey(Compras.id_compras))
    cant_salida_almacen = app.db.Column(app.db.Integer, app.db.ForeignKey(Ventas.id_ventas))
    ubicacion_almacen = app.db.Column(app.db.String(255))
    caducidad_almacen = app.db.Column(app.db.String(255))
    hora_registro_cliente = app.db.Column(app.db.DateTime, default=datetime.datetime.now)

    def __init__(self, id_compras, id_producto, nombre_almacen, cantidad_almacen, cant_entrada_almacen,
                 cant_salida_almacen, unibacion_almacen, caducidad_almacen):
        self.id_compras = id_compras
        self.id_producto = id_producto
        self.nombre_almacen = nombre_almacen
        self.cantidad_almacen = cantidad_almacen
        self.cant_entrada_almacen = cant_entrada_almacen
        self.cant_salida_almacen = cant_salida_almacen
        self.ubicacion_almacen = unibacion_almacen
        self.caducidad_almacen = caducidad_almacen

    def __str__(self):
        return (
            f'Id:{self.id_almacen},'
            f'Id de compra:{self.id_compras},'
            f'Id de producto:{self.id_producto},'
            f'Almacen:{self.nombre_almacen},'
            f'Cantidad en almacen:{self.cantidad_almacen},'
            f'Cantidad entrante:{self.cant_entrada_almacen},'
            f'Cantidad saliente:{self.cant_salida_almacen},'
            f'Localizacion de producto:{self.ubicacion_almacen}'
        )


class Proveedores(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
    id_proveedor = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    nombre_proveedor = app.db.Column(app.db.String(255))
    direccion_proveedor = app.db.Column(app.db.String(255))
    telefono_proveedor = app.db.Column(app.db.String(255))
    horarios_proveedor = app.db.Column(app.db.String(255))
    especialidad_proveedor = app.db.Column(app.db.String(255))
    costo_producto = app.db.Column(app.db.Float, app.db.ForeignKey('catalogo_productos.costo_productos'))
    evaluacion_proveedor = app.db.Column(app.db.Integer)

    def __init__(self, nombre_proveedor, direccion_proveedor, telefono_proveedor, horarios_proveedor,
                 especialidad_proveedor, costo_producto, evaluacion_proveedor):
        self.nombre_proveedor = nombre_proveedor
        self.direccion_proveedor = direccion_proveedor
        self.telefono_proveedor = telefono_proveedor
        self.horarios_proveedor = horarios_proveedor
        self.especialidad_proveedor = especialidad_proveedor
        self.costo_producto = costo_producto
        self.evaluacion_proveedor = evaluacion_proveedor

    def __str__(self):
        return (
            f'Id Proveedor:{self.id_proveedor},'
            f'Nombre de proveedor:{self.nombre_proveedor},'
            f'Direccion:{self.direccion_proveedor},'
            f'Telefono:{self.telefono_proveedor},'
            f'Horarios:{self.horarios_proveedor},'
            f'Especialidad:{self.especialidad_proveedor},'
            f'Costo de productos:{self.costo_producto},'
            f'Evaluacion:{self.evaluacion_proveedor}'
        )


class Tienda(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
    id_plaza = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    nombre_plaza = app.db.Column(app.db.String(255))
    direccion_plaza = app.db.Column(app.db.String(255))
    tel_plaza = app.db.Column(app.db.Integer)
    horario_plaza = app.db.Column(app.db.String(255))

    def __init__(self, nombre_plaza, direccopm_plaza, tel_plaza, horario_plaza):
        self.nombre_plaza = nombre_plaza
        self.direccion_plaza = direccopm_plaza
        self.tel_plaza = tel_plaza
        self.horario_plaza = horario_plaza

    def __str__(self):
        return (
            f'Id de tienda:{self.id_plaza},'
            f'Nombre de tienda:{self.nombre_plaza},'
            f'Direccion de tienda:{self.direccion_plaza},'
            f'Telefono de tienda:{self.tel_plaza},'
            f'Horario de tienda:{self.horario_plaza}'
        )

# class Comentarios(app.db.Model):
# caja_comentarios = app.db.Column(app.db.String(255))
# hora_registro = app.db.Column(app.db.DateTime, default=datetime.datetime.now)
