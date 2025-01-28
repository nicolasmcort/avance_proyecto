# Modulos generales
import flet as ft # type: ignore 

# Modulo propio de app de Flet
from moduleFlet.fletApp import *  # type: ignore 

# Requerimientos iniciales (variables globales que no cambian) ####################################################

# Variables

# Funciones ###################################################################


###############################################################################
def app(page: ft.Page) -> None:
    # Requerimientos iniciales (variables mutables locales)
    page.title = "Organizador de horarios" # Título de la app
    page.bgcolor = ft.Colors.with_opacity(1, '#222831') # Color de fondo  (opacidad de 0 a 1, código de color en hexádecimal) 
    # Paleta de colores de Flet: https://flet.dev/docs/reference/colors/
    # Página para obtener el código hexádecimal de los colores: https://www.colorhexa.com/77b2d0
    # Algunas ideas de colores: https://cdn.mos.cms.futurecdn.net/HNugbHkQZXCDmyyweTy2Xg.png

    # Instancias fundamentales
    page_manager = PageManager(page)

    # Lógica principal
    


    # Parte visual de página "principal"
    rec1_right = Rectangle(left=965, top=0, width=285, height=705, color=ft.Colors.with_opacity(1, '#393E46'))    # Barra derecha gris
    rect2_right = Rectangle(left=965, top=0, width=285, height=140, color=ft.Colors.with_opacity(1, '#00ADB5'))    # Barra derecha azul
    rect1_up = Rectangle(left=10, top=0, width=900, height=140, color=ft.Colors.with_opacity(1, '#393E46'))    # Barra superior gris
    label_codes = TextElement(value="Códigos", size=20, left=30, top=140, width=240, height=490, page=page, text_color=ft.Colors.WHITE, bg_color=None)   # Label que dice "Códigos"
    label_doc = TextElement(value="Grupos", size=20, left=370, top=140, width=240, height=490, page=page, text_color=ft.Colors.WHITE, bg_color=None)   # Label que dice "Docentes"
    label_hor = TextElement(value="Horario", size=20, left=700, top=140, width=240, height=490, page=page, text_color=ft.Colors.WHITE, bg_color=None)   # Label que dice "Horario"
    label_days = TextElement(value="Días", size=20, left=700, top=320, width=240, height=490, page=page, text_color=ft.Colors.WHITE, bg_color=None)   # Label que dice "Días"
    rect1_down = Rectangle(left=10, top=190, width=300, height=515, color=ft.Colors.with_opacity(1, '#393E46'))    # Barra inferior gris
    rect2_down = Rectangle(left=350, top=190, width=300, height=515, color=ft.Colors.with_opacity(1, '#393E46'))    # Barra inferior gris

    # Widgets de página "principal"
    text_inf = TextElement(value="Materias:\nNúmero de créditos:", size=20, left=985, top=170, width=240, height=220, page=page, text_color=ft.Colors.with_opacity(1, '#4ad0d4'), bg_color=None)   # Se visualiza información de los horarios
    text_process = TextElement(value="Bienvenido!", size=16, left=640, top=20, width=240, height=90, page=page, text_color=ft.Colors.WHITE, bg_color=ft.Colors.with_opacity(1, '#11999E'))   # Texto que muestra los procesos que van ocurriendo en la app
    button_user = Button(label="Info. usuario", action=lambda e: page_manager.show_page("user_data"), left=35, top=13, width=210, height=50, text_color=ft.Colors.with_opacity(1, '#4ad0d4'), bg_color=ft.Colors.with_opacity(0, '#393E46')) # Botón que lleva a la página "user_data" 
    button_delete = Button(label="Borrar datos", action=None, left=35, top=77, width=570, height=50, text_color=ft.Colors.with_opacity(1, '#4ad0d4'), bg_color=ft.Colors.with_opacity(0, '#393E46')) # Botón que borra los datos 
    button_exc = Button(label="Excepciones horario", action=None, left=260, top=13, width=345, height=50, text_color=ft.Colors.with_opacity(1, '#4ad0d4'), bg_color=ft.Colors.with_opacity(0, '#393E46')) # Botón que lleva a la página ... Sin determinar todavía
    button_inst = Button(label="⚙️ Instrucciones", action=lambda e: page_manager.show_page("instructions"), left=1000, top=630, width=220, height=50, text_color=ft.Colors.with_opacity(1, '#4ad0d4'), bg_color=ft.Colors.with_opacity(0, '#393E46')) # Botón que lleva a la página "instructions" 
    button_plus = Button(label="+", action=None, left=135, top=150, width=30, height=30, font_size=20, text_color=ft.Colors.with_opacity(1, '#4ad0d4'), bg_color=ft.Colors.with_opacity(0, '#393E46')) # Botón que añade un código a la lista ### Añadir funcionalidad de aumentar la lista de códigos
    button_hor = Button(label="Generar\nhorarios", action=lambda e: page_manager.show_page("schedule"), left=965, top=0, width=285, height=140, bg_color=ft.Colors.with_opacity(1, '#00ADB5'), text_color="white", font_size=24) # Botón que añade un código a la lista ### Añadir funcionalidad de ver horarios
    menu_doc = PopupMenu(options=["Acá van las opciones", ":)"], icon="  Materia                                 ▼", left=370, top=210, width=265, bg_color=ft.Colors.with_opacity(1, '#00ADB5'), tooltip="Mostrar materias", border_radius=4) # PopupMenu para seleccionar el docente
    rg_hor = RadioGroup(options=["Mañana", "Tarde"], left=720, top=200) # Opciones de horario
    cbg_days = CheckBoxGroup(
            options=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
            left=720,
            top=390
        )

    # Widgets de página "instrucciones"
    button1_return = Button(label="Volver", action=lambda e: page_manager.show_page("principal"), left=20, top=30, width=170, height=30, font_size=20, text_color=ft.Colors.with_opacity(1, '#393E46'), bg_color=ft.Colors.with_opacity(1, '#4ad0d4')) # Botón para volver a la página "principal"
    text_inst = TextElement(value="Acá irán las instrucciones de la app", size=30, left=100, top=100, width=1060, height=500, page=page, text_color=ft.Colors.with_opacity(1, '#393E46'), bg_color=ft.Colors.with_opacity(1, '#d5d0d0'))   # Se muestran las instrucciones de la app

    # Widgtes de página "schedule"
    # Acá también va button1_return

    principal_widgtes = [rec1_right, rect2_right, rect1_up, rect1_down, rect2_down,
                        label_codes, label_doc, label_hor, label_days,
                        text_inf, text_process, 
                        button_user, button_inst, button_plus, button_hor, button_delete, button_exc,
                        menu_doc,
                        rg_hor,
                        cbg_days]
    instructions_widgets = [text_inst,
                        button1_return]
    user_data_widgets = []
    schedule_widgets = [button1_return]

    
    # Agregar páginas al PageManager
    page_manager.add_page("principal", principal_widgtes)
    page_manager.add_page("instructions", instructions_widgets)
    page_manager.add_page("user_data", user_data_widgets)
    page_manager.add_page("schedule", schedule_widgets)


    # Mostrar la primera página (principal)
    page_manager.show_page("principal")



ft.app(target=app)



