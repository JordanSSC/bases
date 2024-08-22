import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
from PIL import Image
from packages.models.src.task import Task

class NewTaskPage(ctk.CTkFrame):
    def __init__(self, master):
        self.toplevel = tk.Toplevel(master)
        super().__init__(self.toplevel)
        self.master = master
        self.build()

    def build(self):
        self.toplevel.title("Agregar Tarea")
        self._state_before_windows_set_titlebar_color = 'zoomed'

        self.pack(pady=0, padx=0, fill="both", expand=True)

        top_frame_agregar = ctk.CTkFrame(self, corner_radius=0)
        top_frame_agregar.pack(side="top", fill="x", pady=20)

        label_agregar = ctk.CTkLabel(top_frame_agregar, text="AGREGAR TAREA", font=("Arial", 36))
        label_agregar.pack(side="left", padx=20)

        icono_regresar = ctk.CTkButton(top_frame_agregar, image=self.master.imagen_regresar_tk, fg_color='transparent',text="", width=60, height=60, command=self.toplevel.destroy)
        icono_regresar.pack(side="right", padx=10)

        # Campos de entrada para el nombre y descripción de la tarea
        nombre_label = ctk.CTkLabel(self, text="Título de la Tarea:", font=("Arial", 18))
        nombre_label.pack(pady=10, padx=20, anchor="w")
        self.nombre_entry = ctk.CTkEntry(self, font=("Arial", 16))
        self.nombre_entry.pack(pady=10, padx=20, fill="x")

        descripcion_label = ctk.CTkLabel(self, text="Descripción de la Tarea:", font=("Arial", 18))
        descripcion_label.pack(pady=10, padx=20, anchor="w")
        self.descripcion_entry = ctk.CTkEntry(self, font=("Arial", 16))
        self.descripcion_entry.pack(pady=10, padx=20, fill="x")

        cal = Calendar(self, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
        cal.pack(pady = 20)

        dueDate_label = ctk.CTkLabel(self, text="Fecha de Vencimiento:" , font=("Arial", 18))
        dueDate_label.pack(pady=10, padx=20, anchor="w")
        cal = Calendar(self, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
        cal.pack(pady = 20)

        estado_label = ctk.CTkLabel(self, text="Estado Actual de la Tarea:", font=("Arial", 18))
        estado_label.pack(pady=10, padx=20, anchor="w")
        self.descripcion_entry = ctk.CTkEntry(self, font=("Arial", 16))
        self.descripcion_entry.pack(pady=10, padx=20, fill="x")

        nombre_label = ctk.CTkLabel(self, text="Prioridad Actual de la Tarea:", font=("Arial", 18))
        nombre_label.pack(pady=10, padx=20, anchor="w")
        self.nombre_entry = ctk.CTkEntry(self, font=("Arial", 16))
        self.nombre_entry.pack(pady=10, padx=20, fill="x")


        # Botones de confirmar y cancelar
        boton_confirmar = ctk.CTkButton(self, text="Confirmar", font=("Arial", 16), command=self.confirmar)
        boton_confirmar.pack(side="left", padx=20, pady=20)

        boton_cancelar = ctk.CTkButton(self, text="Cancelar", font=("Arial", 16), command=self.toplevel.destroy)
        boton_cancelar.pack(side="right", padx=20, pady=20)

    def confirmar(self):
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        dueDate = self.cal.get_date()

        nueva_tarea = Task(nombre, descripcion)
        tareas.append(nueva_tarea) # lista que hay que cambiar xd
        self.master.actualizar_tareas()
        self.toplevel.destroy()

if __name__ == "__main__":
    app = NewTaskPage()
    app.mainloop()