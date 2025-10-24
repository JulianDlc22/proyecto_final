import sqlite3
from Clases_Constructoras import Empleado, Rol


DB_NAME = "escuela.db"

class RepositorioEmpleado:

    def conexion(self):
        pass
    def crear_tabla(self):
        pass
    def guardar(self, empleado: Empleado):
        pass
    def listar(self):
        pass
    def eliminar(self):
        pass

class RepositorioEmpleadoSQLite(RepositorioEmpleado):

    def __init__(self , base_datos = DB_NAME):
        self.base_datos = base_datos
        self.crear_tabla()

    def conexion(self):
        conn = sqlite3.connect(self.base_datos)
        conn.row_factory = sqlite3.Row
        return conn

    def crear_tabla(self):
        with self.conexion() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS empleados(  
                        id_empleado INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        DPI INTEGER NOT NULL,
                        primer_nombre TEXT NOT NULL,
                        segundo_nombre TEXT NOT NULL,
                        otro_nombre TEXT NOT NULL,
                        primer_apellido TEXT NOT NULL,
                        segundo_apellido TEXT NOT NULL,
                        otro_apellido TEXT NOT NULL,
                        rol TEXT NOT NULL,
                        usuario TEXT NOT NULL,
                        contraseña TEXT NOT NULL,
                        fecha_nacimiento TEXT NOT NULL);
                        
                        """)

    def guardar(self, empleado: Empleado):
        with self.conexion() as conn:
            conn.execute(""" INSERT INTO empleados (DPI, primer_nombre, segundo_nombre, otro_nombre, primer_apellido, segundo_apellido, otro_apellido,rol, usuario, contraseña, fecha_nacimiento) 
                             VALUES (?,?,?,?,?,?,?,?,?,?,?)""",(empleado.DPI, empleado.primer_nombre, empleado.segundo_nombre,
                                                              empleado.otro_nombre, empleado.primer_apellido, empleado.segundo_apellido,
                                                              empleado.otro_apellido,empleado.rol ,empleado.usuario, empleado.contraseña, empleado.fecha_nacimiento ))
            conn.commit()

    def eliminar(self):
        with self.conexion() as conn:
            conn.execute("DELETE FROM empleados")
            conn.execute("DELETE FROM sqlite_sequence WHERE name='empleados'")
            conn.commit()

class RepositorioRol:

    def conexion(self):
        pass
    def crear_tabla(self):
        pass
    def guardar(self, rol: Rol):
        pass
    def listar(self):
        pass
    def eliminar(self):
        pass

class RepositorioRolSQLite(RepositorioRol):

    def __init__(self, base_datos = DB_NAME):
        self.base_datos = base_datos
        self.crear_tabla()

    def conexion(self):
        conn = sqlite3.connect(self.base_datos)
        conn.row_factory = sqlite3.Row
        return conn

    def crear_tabla(self):
        with self.conexion() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS rol(  
                               id_rol INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                               nombre TEXT NOT NULL
                               ); """)
    def guardar(self, rol: Rol):
        with self.conexion() as conn:
            conn.execute(""" INSERT INTO rol (nombre) VALUES (?)""", (rol.nombre,))
            conn.commit()

    def obtener_todos(self): #para la lista desplegable
        with self.conexion() as conn:
            cursor = conn.execute("SELECT id_rol, nombre FROM rol")
            roles = []
            for row in cursor:
                rol = Rol(row['nombre'])
                rol.id = row['id_rol']
                roles.append(rol)
            return roles
