import hashlib
import flet as ft
from repositorios import RepositorioEmpleadoSQLite
from ventanas_ingreso import IngresoEmpleado

# Paleta de colores
primary = "#0E4B40"
secondary = "#48D8D2"
highlight = "#FF6FB5"
light = "#F2FBFA"
dark = "#2C3E3A"
gray = "#7B7B7B"
red = "#FF0000"

class Login:
    def __init__(self):
        self.repo = RepositorioEmpleadoSQLite()

    def login_pantalla(self, page: ft.Page):
        page.title = "Login - Escuela"
        page.bgcolor = light
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        logo = ft.Image(src="Logo U.png", width=220, height=220)
        usuario = ft.TextField(
            label="Usuario",
            width=320,
            color=dark,
            border_color=primary,
            focused_border_color=secondary,
            text_size=18,
            bgcolor=light,
            border_radius=10,
            prefix=ft.Icon(ft.Icons.PERSON, color=dark),
        )

        contraseña = ft.TextField(
            label="Contraseña",
            width=320,
            color=dark,
            border_color=primary,
            focused_border_color=secondary,
            text_size=18,
            password=True,
            can_reveal_password=True,
            bgcolor=light,
            border_radius=10,
            prefix=ft.Icon(ft.Icons.LOCK, color=dark),
        )
        notificacion = ft.Text(size=16, color=highlight)

        def validar_login(e):
            user = usuario.value
            pwd_hash = hashlib.sha256(contraseña.value.encode()).hexdigest()
            empleado = self.repo.conexion().execute(
                "SELECT * FROM empleados WHERE usuario=? AND contraseña=?",
                (user, pwd_hash)
            ).fetchone()
            if empleado:
                notificacion.value = "¡Login exitoso!"
                notificacion.color = secondary
                page.update()
                page.clean()
                IngresoEmpleado().ingreso_empleado(page)
            else:
                notificacion.value = "Usuario o contraseña incorrectos"
                notificacion.color = red
                page.update()

        boton = ft.ElevatedButton(
            "Ingresar",
            bgcolor=primary,
            color=light,
            width=200,
            height=48,
            on_click=validar_login
        )

        container = ft.Container(
            bgcolor="white",
            border_radius=20,
            padding=100,
            shadow=ft.BoxShadow(blur_radius=20, color=gray, offset=ft.Offset(0, 8)),
            alignment=ft.alignment.center,
            content=ft.Column([
                ft.Container(logo, alignment=ft.alignment.center, padding=ft.Padding(0, 0, 0, 24)),
                usuario,
                contraseña,
                ft.Container(boton, padding=ft.Padding(0, 20, 0, 0)),
                notificacion,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16)
        )

        page.add(container)

if __name__ == "__main__":
    app = Login()
    ft.app(target=app.login_pantalla, assets_dir="assets")
