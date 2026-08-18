from dataclasses import field
import flet as ft


# ============================================================
# BOTÓN BASE
# ============================================================

@ft.control
class CalcButton(ft.Button):

    # Permite que el botón ocupe el espacio disponible
    # Por defecto tiene un valor de 1
    expand: int = field(default_factory=lambda: 1)


# ============================================================
# BOTONES DE LOS NÚMEROS
# ============================================================

@ft.control
class DigitButton(CalcButton):

    # Color de fondo de los botones numéricos
    bgcolor: ft.Colors = ft.Colors.WHITE_24

    # Color del texto
    color: ft.Color = ft.Colors.WHITE


# ============================================================
# BOTONES DE LAS OPERACIONES
# ============================================================

@ft.control
class ActionButton(CalcButton):

    # Color de fondo de los botones de operaciones
    bgcolor: ft.Colors = ft.Colors.ORANGE

    # Color del texto
    color: ft.Color = ft.Colors.WHITE


# ============================================================
# BOTONES EXTRA
# ============================================================

@ft.control
class ExtraActionButton(CalcButton):

    # Color de fondo de AC, +/-, %
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100

    # Color del texto
    color: ft.Colors = ft.Colors.BLACK


# ============================================================
# CALCULADORA
# ============================================================

@ft.control
class CalculatorApp(ft.Container):

    # --------------------------------------------------------
    # COLOR DE FONDO
    #
    # Este es un parámetro opcional.
    #
    # Si hacemos:
    #
    # CalculatorApp()
    #
    # utilizará BLACK.
    #
    # Si hacemos:
    #
    # CalculatorApp(bgcolor=ft.Colors.PURPLE)
    #
    # utilizará PURPLE.
    # --------------------------------------------------------

    bgcolor: ft.Colors = field(default=ft.Colors.BLACK)

    # IMPORTANTE:
    # Con @ft.control utilizamos init() en lugar de __init__()
    def init(self):

        # Inicializamos las variables de la calculadora
        self.reset()

        # Ancho de la calculadora
        self.width = 350

        # Bordes redondeados
        self.border_radius = ft.BorderRadius.all(20)

        # Espacio interno
        self.padding = 20

        # ====================================================
        # PANTALLA DE RESULTADO
        # ====================================================

        self.result = ft.Text(
            value="0",
            color=ft.Colors.WHITE,
            size=20
        )

        # ====================================================
        # CONTENIDO DE LA CALCULADORA
        # ====================================================

        self.content = ft.Column(
            controls=[

                # ------------------------------------------------
                # PANTALLA
                # ------------------------------------------------

                ft.Row(
                    controls=[
                        self.result
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),

                # ------------------------------------------------
                # FILA 1
                # AC | +/- | % | /
                # ------------------------------------------------

                ft.Row(
                    controls=[

                        ExtraActionButton(
                            content="AC",
                            on_click=self.button_clicked
                        ),

                        ExtraActionButton(
                            content="+/-",
                            on_click=self.button_clicked
                        ),

                        ExtraActionButton(
                            content="%",
                            on_click=self.button_clicked
                        ),

                        ActionButton(
                            content="/",
                            on_click=self.button_clicked
                        ),
                    ]
                ),

                # ------------------------------------------------
                # FILA 2
                # 7 | 8 | 9 | *
                # ------------------------------------------------

                ft.Row(
                    controls=[

                        DigitButton(
                            content="7",
                            on_click=self.button_clicked
                        ),

                        DigitButton(
                            content="8",
                            on_click=self.button_clicked
                        ),

                        DigitButton(
                            content="9",
                            on_click=self.button_clicked
                        ),

                        ActionButton(
                            content="*",
                            on_click=self.button_clicked
                        ),
                    ]
                ),

                # ------------------------------------------------
                # FILA 3
                # 4 | 5 | 6 | -
                # ------------------------------------------------

                ft.Row(
                    controls=[

                        DigitButton(
                            content="4",
                            on_click=self.button_clicked
                        ),

                        DigitButton(
                            content="5",
                            on_click=self.button_clicked
                        ),

                        DigitButton(
                            content="6",
                            on_click=self.button_clicked
                        ),

                        ActionButton(
                            content="-",
                            on_click=self.button_clicked
                        ),
                    ]
                ),

                # ------------------------------------------------
                # FILA 4
                # 1 | 2 | 3 | +
                # ------------------------------------------------

                ft.Row(
                    controls=[

                        DigitButton(
                            content="1",
                            on_click=self.button_clicked
                        ),

                        DigitButton(
                            content="2",
                            on_click=self.button_clicked
                        ),

                        DigitButton(
                            content="3",
                            on_click=self.button_clicked
                        ),

                        ActionButton(
                            content="+",
                            on_click=self.button_clicked
                        ),
                    ]
                ),

                # ------------------------------------------------
                # FILA 5
                # 0 | . | =
                # ------------------------------------------------

                ft.Row(
                    controls=[

                        # El 0 ocupa el doble de espacio
                        DigitButton(
                            content="0",
                            expand=2,
                            on_click=self.button_clicked
                        ),

                        DigitButton(
                            content=".",
                            on_click=self.button_clicked
                        ),

                        ActionButton(
                            content="=",
                            on_click=self.button_clicked
                        ),
                    ]
                ),
            ]
        )

    # ========================================================
    # FUNCIÓN PARA LOS CLICS DE LOS BOTONES
    # ========================================================

    def button_clicked(self, e):

        # Obtenemos el contenido del botón presionado
        data = e.control.content

        print(f"Button clicked with data = {data}")

        # ====================================================
        # BOTÓN AC
        # ====================================================

        if self.result.value == "Error" or data == "AC":

            # Regresamos la pantalla a 0
            self.result.value = "0"

            # Reiniciamos las variables
            self.reset()

        # ====================================================
        # NÚMEROS Y PUNTO
        # ====================================================

        elif data in (
            "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "0", "."
        ):

            # Si la pantalla está en 0 o necesitamos
            # comenzar un nuevo número
            if self.result.value == "0" or self.new_operand:

                self.result.value = data

                # Ya no estamos esperando un nuevo operando
                self.new_operand = False

            else:

                # Agregamos el nuevo número al resultado
                self.result.value = self.result.value + data

        # ====================================================
        # OPERACIONES
        # ====================================================

        elif data in ("+", "-", "*", "/"):

            # Realizamos la operación anterior
            self.result.value = self.calculate(
                self.operand1,
                float(self.result.value),
                self.operator
            )

            # Guardamos la nueva operación
            self.operator = data

            # Si hubo un error
            if self.result.value == "Error":

                self.operand1 = 0

            else:

                # Guardamos el resultado como primer operando
                self.operand1 = float(self.result.value)

            # El siguiente número será un nuevo operando
            self.new_operand = True

        # ====================================================
        # BOTÓN =
        # ====================================================

        elif data == "=":

            # Realizamos la operación
            self.result.value = self.calculate(
                self.operand1,
                float(self.result.value),
                self.operator
            )

            # Reiniciamos las variables
            self.reset()

        # ====================================================
        # PORCENTAJE
        # ====================================================

        elif data == "%":

            # Dividimos el número entre 100
            self.result.value = float(self.result.value) / 100

            # Reiniciamos las variables
            self.reset()

        # ====================================================
        # CAMBIAR SIGNO +/-
        # ====================================================

        elif data == "+/-":

            # Si el número es positivo
            if float(self.result.value) > 0:

                # Lo convertimos en negativo
                self.result.value = "-" + str(
                    self.result.value
                )

            # Si el número es negativo
            elif float(self.result.value) < 0:

                # Lo convertimos nuevamente en positivo
                self.result.value = str(
                    self.format_number(
                        abs(float(self.result.value))
                    )
                )

        # Actualizamos la interfaz
        self.update()

    # ========================================================
    # FORMATEAR NÚMEROS
    # ========================================================

    def format_number(self, num):

        # Si el número no tiene decimales,
        # lo mostramos como entero.
        #
        # Ejemplo:
        # 5.0 → 5
        #
        # Si tiene decimales:
        # 5.5 → 5.5

        if num % 1 == 0:

            return int(num)

        else:

            return num

    # ========================================================
    # REALIZAR LAS OPERACIONES
    # ========================================================

    def calculate(self, operand1, operand2, operator):

        # ----------------------------------------------------
        # SUMA
        # ----------------------------------------------------

        if operator == "+":

            return self.format_number(
                operand1 + operand2
            )

        # ----------------------------------------------------
        # RESTA
        # ----------------------------------------------------

        elif operator == "-":

            return self.format_number(
                operand1 - operand2
            )

        # ----------------------------------------------------
        # MULTIPLICACIÓN
        # ----------------------------------------------------

        elif operator == "*":

            return self.format_number(
                operand1 * operand2
            )

        # ----------------------------------------------------
        # DIVISIÓN
        # ----------------------------------------------------

        elif operator == "/":

            # No permitimos dividir entre 0
            if operand2 == 0:

                return "Error"

            else:

                return self.format_number(
                    operand1 / operand2
                )

    # ========================================================
    # REINICIAR CALCULADORA
    # ========================================================

    def reset(self):

        # Operación inicial
        self.operator = "+"

        # Primer operando
        self.operand1 = 0

        # Indica que estamos esperando un nuevo número
        self.new_operand = True


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main(page: ft.Page):

    # Título de la ventana
    page.title = "Calc App"

    # --------------------------------------------------------
    # CREAR CALCULADORA
    #
    # bgcolor es opcional.
    #
    # Si escribimos:
    #
    #     CalculatorApp()
    #
    # el fondo será NEGRO.
    #
    # Si escribimos:
    #
    #     CalculatorApp(bgcolor=ft.Colors.PURPLE)
    #
    # el fondo será MORADO.
    # --------------------------------------------------------

    calc = CalculatorApp(
        bgcolor=ft.Colors.PURPLE
    )
    
    calc2 = CalculatorApp(bgcolor=ft.Colors.BLACK)
    

    # Agregamos la calculadora a la página
    page.add(calc, calc2)


# ============================================================
# EJECUTAR LA APLICACIÓN
# ============================================================

ft.run(main)