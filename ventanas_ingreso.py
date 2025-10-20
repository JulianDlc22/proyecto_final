import flet as ft
import Clases_Constructoras as Empleado

class IngresoEmpleado:

    def ingreso_empleado(page: ft.Page):
        page.title = "Ingreso de Empleados"
        page.bgcolor = "white"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        titulo = ft.Text("Ingreso Empleados", size=25, weight=ft.FontWeight.BOLD, color="#0E4B40")
        page.add(titulo)

        # --- Campos de texto ---
        primer_nombre = ft.TextField(label="Primer Nombre", hint_text="", width=500, color="black",border_color="#0E4B40", text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        segundo_nombre = ft.TextField(label="Segundo Nombre", width=500, color="black", border_color="#0E4B40",text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        otro_nombre = ft.TextField(label="Otro Nombre", hint_text="Opcional", width=500, color="black",border_color="#0E4B40", text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        primer_apellido = ft.TextField(label="Primer Apellido", width=500, color="black", border_color="#0E4B40",text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        segundo_apellido = ft.TextField(label="Segundo Apellido", width=500, color="black", border_color="#0E4B40",text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        otro_apellido = ft.TextField(label="Apellido de Casada", hint_text="Opcional", width=500, color="black",border_color="#0E4B40", text_size=15, keyboard_type=ft.KeyboardType.TEXT)
        user = ft.TextField(label="Usuario", width=500, color="black", border_color="#0E4B40", text_size=15,keyboard_type=ft.KeyboardType.TEXT)
        password = ft.TextField(label="Contraseña", width=500, color="black", border_color="#0E4B40", text_size=15,keyboard_type=ft.KeyboardType.TEXT)
        DPI = ft.TextField(label="DPI", width=500, color="black", border_color="#0E4B40", text_size=15, keyboard_type=ft.KeyboardType.TEXT)

        # --- Campo para mostrar resultados ---
        resultado = ft.Text()

        # --- Función que se ejecuta al presionar el botón ---
        def guardar_empleado(e):
            # Aquí podrías crear un objeto Empleado si lo tienes definido
            # emp = Empleado.Empleado(primer_nombre.value, segundo_nombre.value, ...)
            resultado.value = f"Empleado {primer_nombre.value} guardado"
            page.update()

        # --- Layout: agregamos los elementos a la página ---
        page.add(primer_nombre, segundo_nombre, otro_nombre, primer_apellido, segundo_apellido, otro_apellido, user,
                 password, DPI)


# Ejecutar la app
ft.app(target=IngresoEmpleado.ingreso_empleado)