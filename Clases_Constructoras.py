class Rol:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado:
    def __init__(self, primer_nombre, segundo_nombre, otro_nombre, primer_apellido, segundo_apellido, otro_apellido, usuario, contraseña, DPI, fecha_nacimiento ):
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.otro_nombre = otro_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.otro_apellido = otro_apellido
        self.usuario = usuario
        self.contraseña = contraseña
        self.DPI = DPI
        self.fecha_nacimiento = fecha_nacimiento

class Grado:
    def __init__(self, nombre, seccion ):
        self.nombre = nombre
        self.seccion = seccion

class Estudiante:
    def __init__(self, primer_nombre, segundo_nombre, otro_nombre, primer_apellido, segundo_apellido, CUI, edad, fecha_nacimiento):
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.otro_nombre = otro_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.CUI = CUI
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento





