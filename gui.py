import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Proceso completado", "El proceso ha finalizado con éxito.")

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Aplicación")

# Botón para mostrar el mensaje
# boton = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
# boton.pack()

# Iniciar el bucle de eventos
root.mainloop()
