import tkinter as tk
import pandas as pd
from tkinter import ttk
import Simulacion
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Label
import sys


class InterfazSimulacion(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Simulación")
        self.geometry("800x600")

        # Centrar la ventana en la pantalla
        window_width = 1600
        window_height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

        # Crear un marco para los controles de la simulación
        control_frame = tk.Frame(self)
        control_frame.pack(pady=20)


        # Inicializar el atributo tabla
        self.tabla = None


        # Botón para cerrar la ventana
        btn_cerrar = tk.Button(control_frame, text="Cerrar", command=self.cerrar_programa)
        btn_cerrar.grid(row=0, column=2, padx=10)
    
    def cerrar_programa(self):
        sys.exit()
    
    # Empezar la simulacion
    def start_simulation(self):

        # Obtener el número de simulaciones del campo de entrada
        num_sims = 20000

        # Llamar a la función simular_juegos
        df_equipo_ganador, df_equipo_perdedor, df_jugador_suerte, df_jugador_experiencia, df_genero_ganador, equipo_mas_ganador, genero_mas_ganador = Simulacion.simular_juegos(num_sims)
        df_puntajes_equipo = self.puntajes_por_equipo(df_equipo_ganador, df_equipo_perdedor)
        texto_final = self.texto_calcular_resultado_final(equipo_mas_ganador.nombre, genero_mas_ganador, df_equipo_ganador)

        # Crear la gráfica
        self.crear_grafica(df_puntajes_equipo)

        # Mostrar el texto resultante
        label_texto_final = Label(self, text=texto_final, font=("Arial", 12))
        label_texto_final.place(relx=0.85, rely=0.1, anchor="n")

        # Crear la tabla
        self.crear_tabla(df_equipo_ganador, df_equipo_perdedor, df_jugador_suerte, df_jugador_experiencia, df_genero_ganador)

    # Dibujar la tabla
    def crear_tabla(self, df_equipo_ganador, df_equipo_perdedor, df_jugador_suerte, df_jugador_experiencia, df_genero_ganador):
        # Crear un marco para la tabla
        tabla_frame = tk.Frame(self)
        tabla_frame.pack(pady=20)

        # Crear la tabla
        self.tabla = ttk.Treeview(tabla_frame, columns=["Juego", "Equipo Ganador", "Puntaje", "Equipo Perdedor", "Puntaje", "Jugador con mas suerte", "Jugador con mas experiencia", "Genero ganador"], show='headings')

        # Configurar encabezados
        self.tabla.heading("Juego", text="Juego")
        self.tabla.heading("Equipo Ganador", text="Equipo Ganador")
        self.tabla.heading("Puntaje", text="Puntaje")
        self.tabla.heading("Equipo Perdedor", text="Equipo Perdedor")
        self.tabla.heading("Puntaje", text="Puntaje")
        self.tabla.heading("Jugador con mas suerte", text="Jugador con mas suerte")
        self.tabla.heading("Jugador con mas experiencia", text="Jugador con mas experiencia")
        self.tabla.heading("Genero ganador", text="Genero ganador")

        # Agregar filas a la tabla
        for index, fila in df_equipo_ganador.iterrows():
            juego = fila["Juego"]
            equipo_ganador = fila["Equipo Ganador"]
            equipo_ganador = fila["Equipo Ganador"]
            puntaje_ganador = fila["Puntaje"]
            equipo_perdedor = df_equipo_perdedor.iloc[index]["Equipo Perdedor"]
            puntaje_perdedor = df_equipo_perdedor.iloc[index]["Puntaje"]
            jugador_suerte = df_jugador_suerte.iloc[index]["Jugador con mas suerte"]
            jugador_experiencia = df_jugador_experiencia.iloc[index]["Jugador con mas experiencia"]
            genero_ganador = df_genero_ganador.iloc[index]["Genero ganador"]

            self.tabla.insert('', 'end', values=(juego, equipo_ganador, puntaje_ganador, equipo_perdedor, puntaje_perdedor, jugador_suerte, jugador_experiencia, genero_ganador))

        # Configurar la barra de desplazamiento
        scroll_y = ttk.Scrollbar(tabla_frame, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear dataframe para hacer la grafica
    def puntajes_por_equipo(self, df_equipo_ganador, df_equipo_perdedor):
        # Extraer los puntajes de los equipos ganadores y perdedores
        puntajes_equipo_ganador = df_equipo_ganador["Puntaje"]
        puntajes_equipo_perdedor = df_equipo_perdedor["Puntaje"]
        
        # Crear un DataFrame para almacenar los puntajes por equipo
        df_puntajes_equipo = pd.DataFrame()

        # Concatenar los DataFrames
        df_puntajes_equipo["PuntajesEquipoA"] = puntajes_equipo_ganador.values
        df_puntajes_equipo["PuntajesEquipoB"] = puntajes_equipo_perdedor.values

        return df_puntajes_equipo
    
    # Crear la grafica
    def crear_grafica(self, df_puntajes_equipo):
        # Crear una figura y un eje
        fig, ax = plt.subplots()

        # Graficar los puntajes de los equipos
        ax.plot(df_puntajes_equipo.index, df_puntajes_equipo['PuntajesEquipoA'], label='Equipo A')
        ax.plot(df_puntajes_equipo.index, df_puntajes_equipo['PuntajesEquipoB'], label='Equipo B')

        # Agregar leyenda y etiquetas
        ax.legend()
        ax.set_xlabel('Número de partidas')
        ax.set_ylabel('Puntaje por ronda')

        # Agregar la gráfica al frame de tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

    # Resultado final
    def texto_calcular_resultado_final(self, equipo_mas_ganador, genero_mas_ganador, df_equipo_ganador):
        # Calcular el número de juegos ganados por cada equipo
        juegos_ganados_equipo_a = (df_equipo_ganador['Equipo Ganador'] == 'EquipoA').sum()
        juegos_ganados_equipo_b = (df_equipo_ganador['Equipo Ganador'] == 'EquipoB').sum()

        # Generar el texto del resultado final
        resultado_final = f"Equipo mas ganador: {equipo_mas_ganador}\n" \
                        f"Genero mas ganador: {genero_mas_ganador}\n" \
                        f"# Juegos ganados Equipo A: {juegos_ganados_equipo_a}\n" \
                        f"# Juegos ganados Equipo B: {juegos_ganados_equipo_b}\n"

        return resultado_final
    

