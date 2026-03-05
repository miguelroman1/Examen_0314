import flet as ft

def main(page: ft.Page):
    page.title = "Examen Final - Registros de Participantes"
    page.padding = 20
    page.scroll = "adaptive"
    
    titulo = ft.Text(
        "REGRISTRO DE PARTICIPANTES",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,


    )

    nombre = ft.TextField(
        label="Nombre Completo",
        hint_text="Ejemplo: Juan Pérez",
        width=400,
    )
    
    correo = ft.TextField(
        label="Correo Electrónico",
        hint_text="Ejemplo: juan.perez@example.com",
        width=400,
    )

    taller = ft.Dropdown(
        label="Taller De Interés",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ],
        value="Conferencia",
        width=400,
    )
    
    pago = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Pago completo", label="Pago completo"),
                ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
            ],
        ),
        value="Presencial",
    )

    inscripcion = ft.Checkbox(
        label="¿Requiere Computador Portátil?",
        value=False,
    )

    nivel = ft.Slider(
        min=1,
        max=5,
        divisions=4,
        value=3,
        label="Nivel de Experencia: {value}",
        width=400,
    )

    txt_duracion = ft.Text(
        "Nivel de experencia: 3",
    )

    def cambiar_nivel(e):
        txt_duracion.value = f"Nivel de experencia: {int(nivel.value)}"
        page.update()

    nivel.on_change = cambiar_nivel

    resumen = ft.Text(
        value="",
        size=16,
    )

    linea = ft.Divider(height=20)

    def mostrar_resumen(e):
        if not nombre.value or nombre.value.strip() == "":
            resumen.value = "ERROR: Su nombre no puede estar vacío"
            resumen.color = ft.Colors.RED
        else:
            resumen.value = f"""
--- FICHA DEL PARTICIPANTE ---

Nombre: {nombre.value}
Correo: {correo.value}
Taller: {taller.value}
pago: {pago.value}
Requiere portátil: {'Sí' if inscripcion.value else 'No'}
Nivel de Experencia: {int(nivel.value)}

--- Gracias por su registro ---
"""
            resumen.color = ft.Colors.BLACK

        page.update()

    

    boton = ft.ElevatedButton(
        "MOSTRAR RESUMEN",
        on_click=mostrar_resumen,
        width=200,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_500,
            color=ft.Colors.BLACK,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )


    contenido = ft.Column(
        [
            titulo,
            ft.Container(height=10),
            nombre,
            ft.Container(height=10),
            correo,
            ft.Container(height=10),
            taller,
            ft.Container(height=10),
            pago,
            ft.Container(height=10),
            inscripcion,
            ft.Container(height=10),
            nivel,
            txt_duracion,
            ft.Container(height=20),
            boton,
            linea,
            resumen,
        ]
    )

    page.add(contenido)

ft.run(main)
