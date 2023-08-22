import tkinter as tk
from tkinter import filedialog
from script import separar_guias


def generar_app():

    def open_file():
        # Almacena el path del archivo en una variable global
        global file_path
        file_path = filedialog.askopenfilename()
        # Actualiza la etiqueta con el path del archivo seleccionado, sólo muestra el nombre del archivo
        lbl_file_path.config(text=f'Archivo seleccionado: {file_path.split("/")[-1]}')
        

    # Al presionar boton "Separar guías" ejecuta la función separar_guias
    def separate():

        # agregar un status bar para mostrar el progreso del proceso
        lbl_notification.config(text='Procesando...', fg='black')
        # inactiva el botón de separar guías
        btn_separate.config(state='disabled')
        # inactiva el entry_output_file_name
        entry_output_file_name.config(state='disabled')
        # inactiva el botón de seleccionar archivo
        btn_open_file.config(state='disabled')

        # Actualiza la ventana para inactivar los botones y mostrar el mensaje "Procesando...
        root.update() 
        

        # Almacena el nombre del archivo de salida en una variable global
        global file_name
        file_name = entry_output_file_name.get()
        try:
            separar_guias(file_path, file_name)
            # lbl_file_path.config(text='¡Proceso terminado!')
            lbl_notification.config(text='¡Proceso terminado!', fg='green')
            # activa el botón de separar guías
            btn_separate.config(state='normal')
            # activa el entry_output_file_name
            entry_output_file_name.config(state='normal')
            # activa el botón de seleccionar archivo
            btn_open_file.config(state='normal')

        except Exception as e:
            lbl_file_path.config(text=f'Error: {e}', fg='red')
        


    root = tk.Tk()


    # Agregar título a la ventana
    root.title('Separador de guías')
    # Define el tamaño de la ventana
    root.geometry('350x200')
    # Define el tamaño mínimo de la ventana
    root.minsize(350, 200)
    # Define el tamaño máximo de la ventana
    root.maxsize(350, 200)


    # Crea un botón para abrir el archivo
    btn_open_file = tk.Button(root, text='Seleccionar archivo', command=open_file)
    btn_open_file.grid(row=0, column=0, columnspan=2, pady=20)  


    # Crea una etiqueta para mostrar el archivo seleccionado
    lbl_file_path = tk.Label(root, text='Ningún archivo seleccionado')
    lbl_file_path.grid(row=1, column=0, columnspan=2)

    # Captura el nombre para el archivo de salida
    lbl_output_file_name = tk.Label(root, text='Nombre del archivo de salida:')
    lbl_output_file_name.grid(row=3, column=0, sticky='w', padx=10, pady=5)  # Agrega sticky para alinear a la izquierda

    # Crea un campo de texto para capturar el nombre del archivo de salida
    entry_output_file_name = tk.Entry(root)
    entry_output_file_name.grid(row=3, column=1, padx=10, pady=5)  # Alineación automática a la derecha

    # Crea otro boton para ejecutar el script que diga "Separar guías"
    btn_separate = tk.Button(root, text='Separar guías', command=separate)
    btn_separate.grid(row=4, column=0, columnspan=2, pady=10)

    # Crea una etiqueta para mostrar el resultado del proceso
    lbl_notification = tk.Label(root, text='', fg='black')
    lbl_notification.grid(row=5, column=0, columnspan=2)


    # Ejecuta el mainloop
    root.mainloop()