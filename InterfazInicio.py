import tkinter as tk
from InterfazSimulacion import InterfazSimulacion

# Crear la ventana principal
root = tk.Tk()
root.title("Archery Simulation")
root.geometry("800x600")

# Ajustar el tamaño de la ventana
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

# Crear un marco para el título
title_frame = tk.Frame(root, bg="white")
title_frame.pack(pady=40)

# Crear una etiqueta para el título
title_label = tk.Label(title_frame, text="ArcherySimulation", font=("Times", 36, "bold"))
title_label.pack()

# Crear una línea separadora
separator = tk.Frame(root, height=4, bd=2, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=10, pady=10)

# Crear un marco para los nombres
names_frame = tk.Frame(root)
names_frame.pack(pady=20)

# Crear etiquetas para los nombres de los colaboradores
name1_label = tk.Label(names_frame, text="Luis Carlos Castillo Martin", font=("Arial", 20))
name1_label.pack(pady=5)
name2_label = tk.Label(names_frame, text="Nicolas David Fajardo Acuña", font=("Arial", 20))
name2_label.pack(pady=5)
name3_label = tk.Label(names_frame, text="Edwin Alfredo Sichaca Gonzalez", font=("Arial", 20))
name3_label.pack(pady=5)

# Crear un marco para el botón
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=40)

# Abrir la ventana de la simulacion
def open_simulation_window():
    root.withdraw()  # Ocultar la ventana principal
    simulation_window = InterfazSimulacion(root)  # Crear una instancia de la clase InterfazSimulacion
    simulation_window.grab_set()  # Evitar que se pueda interactuar con la ventana principal
    simulation_window.start_simulation() 

# Crear un botón para iniciar la simulación
start_button = tk.Button(button_frame, text="Iniciar Simulacion", font=("Arial", 24, "bold"), bg="#182d4b", fg="white", padx=40, pady=20, command=open_simulation_window)
start_button.pack()

# Ejecutar el bucle principal de eventos
root.mainloop()