from operator import truediv

import flet as ft
from Clases_Constructoras import Empleado
from repositorios import RepositorioEmpleadoSQLite

class IngresoEmpleado:

    def __init__(self):
        self.repo = RepositorioEmpleadoSQLite()

    def ingreso_empleado(self, page: ft.Page):
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
        usuario = ft.TextField(label="Usuario", width=500, color="black", border_color="#0E4B40", text_size=15,keyboard_type=ft.KeyboardType.TEXT)
        contraseña = ft.TextField(label="Contraseña", width=500, color="black", border_color="#0E4B40", text_size=15,keyboard_type=ft.KeyboardType.TEXT)

        def mostrar_mensaje(titulo, mensaje, tipo="info"):
            color = "#0E4B40" if tipo == "exito" else "#B00020"  # verde para éxito, rojo para error
            snackbar = ft.SnackBar(
                ft.Text(f"{titulo}: {mensaje}", color="white"),
                bgcolor=color,
                open=True,
                duration=5000  # milisegundos: 3 segundos
            )
            page.snack_bar = snackbar
            page.snack_bar.open = True
            page.update()

        # --- Función que se ejecuta al presionar el botón ---

        def guardar_empleado(e):
            if not (DPI.value or primer_nombre.value or segundo_nombre.value or primer_apellido.value or segundo_apellido.value or usuario.value or contraseña.value ):
                mostrar_mensaje("Error", "Debe ingresar todos los campos obligatorios")
                return

            empleado = Empleado(DPI.value, primer_nombre.value, segundo_nombre.value, otro_nombre.value, primer_apellido.value, segundo_apellido.value,otro_apellido.value, usuario.value, contraseña.value, "")
            self.repo.guardar(empleado)
            mostrar_mensaje("Exito", "Empleado guardado correctamente", tipo="exito")

        boton_guardar = ft.ElevatedButton(text="Guardar Empleado", on_click=guardar_empleado, color="black", bgcolor="#0E4B40")


        # --- agregamos los elementos a la página ---
        page.add( DPI, primer_nombre, segundo_nombre, otro_nombre, primer_apellido, segundo_apellido, otro_apellido, usuario,
                 contraseña, boton_guardar)


# Ejecutar la app
if __name__ == "__main__":
    app = IngresoEmpleado()
    ft.app(target=app.ingreso_empleado)