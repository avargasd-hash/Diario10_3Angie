import flet as ft 


def main(page: ft.Page):
    page.title = "Mi primer programa con flet"
    mensaje = ft.Text("Aqui va un mensaje")
    nombre = ft.TextField(label = "Escriba su nombre", autofocus=True)

    def mostrar_mensaje(txt_mensaje):
        dialogo = ft.AlertDialog(
            title=ft.Text("mensaje"),
            content=ft.Text(txt_mensaje)
        )
        page.show_dialog(dialogo)
    def saludar(c):
            if nombre.value == "":
                mensaje.value = "Hola, desconocido"
            else:
                mensaje.value = "Hola, " + nombre.value
            mostrar_mensaje(mensaje.value)
    page.add(
        ft.Button("Click me", on_click = saludar),
        mensaje,
        nombre
        
    )
    def saludar(c):
        mensaje.value = "Gracias por ese click!"
ft.run(main)

