 #Primera asignación 

 #Correr este código (se trata de un módulo(tkinter) que se importa para crear un programa visualmente estético, totalmente con Python

import tkinter as tk
from tkinter import messagebox

# Funciones para la lógica de la aplicación
def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def limpiar_lista():
    respuesta = messagebox.askyesno("Confirmación", "¿Seguro que quieres limpiar toda la lista?")
    if respuesta:
        lista_tareas.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")
ventana.config(bg="#F0F0F0")

# Crear y colocar la etiqueta para el título
label_titulo = tk.Label(ventana, text="Mis Tareas", font=("Helvetica", 18), bg="#F0F0F0")
label_titulo.pack(pady=10)

# Crear y colocar el cuadro de entrada para agregar tareas
entry_tarea = tk.Entry(ventana, width=30)
entry_tarea.pack(pady=10)

# Botón para agregar tareas
boton_agregar = tk.Button(ventana, text="Agregar Tarea", width=30, command=agregar_tarea)
boton_agregar.pack(pady=5)

# Crear y colocar el Listbox para mostrar las tareas
lista_tareas = tk.Listbox(ventana, height=10, width=40, bd=0, font=("Helvetica", 12))
lista_tareas.pack(pady=10)

# Botón para eliminar tareas seleccionadas
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", width=30, command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Botón para limpiar la lista de tareas
boton_limpiar = tk.Button(ventana, text="Limpiar Lista", width=30, command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Bucle principal para ejecutar la ventana
ventana.mainloop()