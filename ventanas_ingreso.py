from datetime import datetime
import flet as ft
from Clases_Constructoras import Empleado, Rol
from repositorios import RepositorioEmpleadoSQLite , RepositorioRolSQLite

class Notificador:

    def notificar_exito(self):
        pass

    def notificar_error(self):
        pass

class NotificadorIngreso(Notificador):

    def __init__(self, page : ft.Page):
        self.page = page

    def notificar_exito(self, titulo, mensaje):
        color = "#0E4B40"
        snackbar = ft.SnackBar(content=ft.Text(f"{titulo}: {mensaje}", color="white"), bgcolor=color, duration=3000)
        self.page.open(snackbar)

    def notificar_error(self, titulo, mensaje):
        color = "#B00020"
        snackbar = ft.SnackBar(content=ft.Text(f"{titulo}: {mensaje}", color="white"), bgcolor=color, duration=3000)
        self.page.open(snackbar)


class Fecha():

    def __init__(self, page: ft.Page, label="Fecha", hint_text="DD/MM/YYYY", width=500, color="black", border_color="#0E4B40", text_size=15,first_date=None, last_date=None):
        self.page = page

        self.text_field = ft.TextField( label=label, read_only=True, width=width, color=color,border_color=border_color,text_size=text_size,hint_text=hint_text)

        if first_date is None:
            first_date = datetime(1900, 1, 1)
        if last_date is None:
            last_date = datetime.now()

        self.date_picker = ft.DatePicker(on_change=self.cambiar_fecha, first_date=first_date,last_date=last_date )

        self.page.overlay.append(self.date_picker)
        self.text_field.on_click = self.abrir_datepicker

    def cambiar_fecha(self, e):
        if self.date_picker.value:
            fecha = self.date_picker.value
            fecha_formateada = f"{fecha.day:02d}/{fecha.month:02d}/{fecha.year}"
            self.text_field.value = fecha_formateada
            self.page.update()

    def abrir_datepicker(self, e):
        self.page.open(self.date_picker)

    @property
    def value(self):
        return self.text_field.value

    @value.setter
    def value(self, nuevo_valor):
        self.text_field.value = nuevo_valor

    def get_control(self):
        return self.text_field

    def limpiar(self):
        self.text_field.value = ""
        self.page.update()


class IngresoRol:
    def __init__(self):
        self.repo = RepositorioRolSQLite()

    def ingreso_rol(self, page: ft.Page):
        self.notificador = NotificadorIngreso(page)
        page.title = "Ingreso Rol"
        page.bgcolor = "white"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        titulo = ft.Text("Ingreso Rol", size=25, weight=ft.FontWeight.BOLD, color="#0E4B40")
        page.add(titulo)

        # --- Campos de texto ---
        nombre = ft.TextField(label = "Nombre", width=500, color="black", border_color="#0E4B40", text_size=25,keyboard_type=ft.KeyboardType.TEXT )

        def guardar_rol(e):
            if not nombre.value:
                self.notificador.notificar_error("Error","Debe ingresar todos los campos" )
                return

            rol = Rol(nombre.value)
            self.repo.guardar(rol)
            self.notificador.notificar_exito("Éxito", "Rol guardado correctamente")

        boton_guardar = ft.ElevatedButton(text="Guardar Rol", on_click=guardar_rol, color="black",bgcolor="#0E4B40")

        page.add(nombre,boton_guardar)


class IngresoEmpleado:

    def __init__(self):
        self.repo = RepositorioEmpleadoSQLite()
        self.repo_rol = RepositorioRolSQLite()

    def ingreso_empleado(self, page: ft.Page):

        self.notificador = NotificadorIngreso(page)
        roles = self.repo_rol.obtener_todos()
        page.title = "Ingreso de Empleados"
        page.bgcolor = "white"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        titulo = ft.Text("Ingreso Empleados", size=25, weight=ft.FontWeight.BOLD, color="#0E4B40")
        page.add(titulo)

        # --- Campos de texto ---
        DPI = ft.TextField(label="DPI", width=500, color="black", border_color="#0E4B40", text_size=15,keyboard_type=ft.KeyboardType.TEXT)
        primer_nombre = ft.TextField(label="Primer Nombre", hint_text="", width=500, color="black",border_color="#0E4B40", text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        segundo_nombre = ft.TextField(label="Segundo Nombre", width=500, color="black", border_color="#0E4B40",text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        otro_nombre = ft.TextField(label="Otro Nombre", hint_text="Opcional", width=500, color="black",border_color="#0E4B40", text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        primer_apellido = ft.TextField(label="Primer Apellido", width=500, color="black", border_color="#0E4B40",text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        segundo_apellido = ft.TextField(label="Segundo Apellido", width=500, color="black", border_color="#0E4B40",text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        otro_apellido = ft.TextField(label="Apellido de Casada", hint_text="Opcional", width=500, color="black",border_color="#0E4B40", text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        rol = ft.Dropdown(label="Rol", width=500, color="black", border_color="#0E4B40", text_size=15,options=[ft.dropdown.Option(str(rol.id), rol.nombre) for rol in roles])
        usuario = ft.TextField(label="Usuario", width=500, color="black", border_color="#0E4B40", text_size=15,keyboard_type=ft.KeyboardType.TEXT)
        contraseña = ft.TextField(label="Contraseña", width=500, color="black", border_color="#0E4B40", text_size=15,keyboard_type=ft.KeyboardType.TEXT, password=True, can_reveal_password=True)
        fecha_nacimiento = Fecha(page=page, label="Fecha de Nacimiento",hint_text="DD/MM/YYYY", width=500, color="black",border_color="#0E4B40",text_size=15)

        # --- Función que se ejecuta al presionar el botón ---
        def guardar_empleado(e):
            if not (DPI.value and primer_nombre.value and segundo_nombre.value and primer_apellido.value and segundo_apellido.value and usuario.value and contraseña.value and fecha_nacimiento.value and rol.value):
                self.notificador.notificar_error("Error", "Debe ingresar todos los campos obligatorios")
                return

            empleado = Empleado(DPI.value, primer_nombre.value, segundo_nombre.value, otro_nombre.value, primer_apellido.value, segundo_apellido.value, otro_apellido.value, rol.value, usuario.value, contraseña.value, fecha_nacimiento.value)
            self.repo.guardar(empleado)
            self.notificador.notificar_exito("Éxito", "Empleado guardado correctamente")

        boton_guardar = ft.ElevatedButton(text="Guardar Empleado",on_click=guardar_empleado,color="black",bgcolor="#0E4B40")


        # aqui se agregan los campos a la pagina
        page.add(DPI, primer_nombre, segundo_nombre, otro_nombre, primer_apellido, segundo_apellido, otro_apellido,rol, usuario, contraseña,fecha_nacimiento.get_control(), boton_guardar)


if __name__ == "__main__":
    app = IngresoEmpleado()
    ft.app(target=app.ingreso_empleado)
