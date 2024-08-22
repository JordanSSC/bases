import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
from PIL import Image
from packages.models.src.task import Task
# Clase placeholder para representar una tarea
class Tarea:
    def __init__(self, nombre, descripcion, subtareas=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.subtareas = subtareas if subtareas else []

class TaskList(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.build()

    def build(self):
        self.title("Tareas")
        self._state_before_windows_set_titlebar_color = 'zoomed'
        
        self.frame = ctk.CTkFrame(self, corner_radius=0)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.top_frame = ctk.CTkFrame(self.frame, corner_radius=0)
        self.top_frame.pack(side="top", fill="x", pady=20)

        self.label_tareas = ctk.CTkLabel(self.top_frame, text="TAREAS", font=("Times New Roman", 36))
        self.label_tareas.pack(side="left", padx=20)

        self.imagen_regresar_tk = ctk.CTkImage(light_image=Image.open("imagenes/regresar.png"), size=(60, 60))
        self.icono_regresar = ctk.CTkButton(self.top_frame, image=self.imagen_regresar_tk, text="", fg_color='transparent',width=60, height=60, command=self.regresar_menu_principal)
        self.icono_regresar.pack(side="right", padx=10)

        self.imagen_agregar_tk = ctk.CTkImage(light_image=Image.open("imagenes/agregar.png"), size=(60, 60))
        self.boton_agregar = ctk.CTkButton(self.top_frame, image=self.imagen_agregar_tk, text="",fg_color='transparent', width=60, height=60, command=self.abrir_ventana_agregar)
        self.boton_agregar.pack(side="right", padx=10)

        self.frame_tareas = ctk.CTkFrame(self.frame, corner_radius=0)
        self.frame_tareas.pack(pady=20, padx=20, fill="both", expand=True)

        self.actualizar_tareas()

    def regresar_menu_principal(self):
        tk.messagebox.showinfo("Regreso al menú principal", "Has regresado al menú principal")

    def confirmar_eliminar(self, tarea):
        confirmacion = ConfirmarEliminacion(self, tarea)

    def abrir_ventana_tarea(self, tarea):
        VentanaTarea(self, tarea)

    def actualizar_tareas(self):
        for widget in self.frame_tareas.winfo_children():
            widget.destroy()

        for tarea in tareas:
            tarea_frame = ctk.CTkFrame(self.frame_tareas, corner_radius=0)
            tarea_frame.pack(pady=10, fill="x", padx=10)

            nombre_label = ctk.CTkLabel(tarea_frame, text=tarea.nombre, font=("Times New Roman", 24, "bold"))
            nombre_label.pack(side="top", anchor="w", pady=5, padx=5)

            descripcion_label = ctk.CTkLabel(tarea_frame, text=tarea.descripcion, font=("Times New Roman", 18))
            descripcion_label.pack(side="top", anchor="w", pady=5, padx=5)

            eliminar_tk = ctk.CTkImage(light_image=Image.open("imagenes/basura.png"), size=(30, 30))
            boton_eliminar = ctk.CTkButton(tarea_frame, image=eliminar_tk, text="", width=30,fg_color='transparent', height=30, command=lambda t=tarea: self.confirmar_eliminar(t))
            boton_eliminar.pack(side="right", padx=10)

            tarea_frame.bind("<Button-1>", lambda e, t=tarea: self.abrir_ventana_tarea(t))
            nombre_label.bind("<Button-1>", lambda e, t=tarea: self.abrir_ventana_tarea(t))
            descripcion_label.bind("<Button-1>", lambda e, t=tarea: self.abrir_ventana_tarea(t))

    def abrir_ventana_agregar(self):
        VentanaAgregar(self)

class DeleteTaskPage(ctk.CTkFrame):
    def __init__(self, master, tarea):
        self.toplevel = tk.Toplevel(master)
        super().__init__(self.toplevel)
        self.master = master
        self.tarea = tarea
        self.build()

    def build(self):
        self.toplevel.title("Confirmar Eliminación")
        self.toplevel.geometry("500x150")

        ventana_x = self.master.winfo_screenwidth() // 2 - 250
        ventana_y = self.master.winfo_screenheight() // 2 - 100
        self.toplevel.geometry(f"+{ventana_x}+{ventana_y}")

        self.pack(pady=20, padx=20, fill="both", expand=True)

        mensaje = ctk.CTkLabel(self, text="¿Estás seguro de que quieres eliminar esta tarea?", font=("Arial", 12))
        mensaje.pack(pady=10)

        boton_confirmar = ctk.CTkButton(self, text="Confirmar", font=("Arial", 12), command=self.eliminar)
        boton_confirmar.pack(side="left", padx=20, pady=10)

        boton_cancelar = ctk.CTkButton(self, text="Cancelar", font=("Arial", 12), command=self.toplevel.destroy)
        boton_cancelar.pack(side="right", padx=20, pady=10)

    def eliminar(self):
        tareas.remove(self.tarea)
        self.master.actualizar_tareas()
        self.toplevel.destroy()

# Clase para la ventana de ver detalles de una tarea
class VentanaTarea(ctk.CTkFrame):
    def __init__(self, master, tarea):
        self.toplevel = tk.Toplevel(master)
        super().__init__(self.toplevel)
        self.master = master
        self.tarea = tarea
        self.build()

    def build(self):
        self.toplevel.title(self.tarea.nombre)
        self.toplevel.state('zoomed')

        self.pack(pady=0, padx=0, fill="both", expand=True)

        top_frame_tarea = ctk.CTkFrame(self, corner_radius=0)
        top_frame_tarea.pack(side="top", fill="x", pady=20)

        label_tarea = ctk.CTkLabel(top_frame_tarea, text=self.tarea.nombre, font=("Arial", 36))
        label_tarea.pack(side="left", padx=20)

        icono_regresar = ctk.CTkButton(top_frame_tarea, image=self.master.imagen_regresar_tk,fg_color='transparent', text="", width=60, height=60, command=self.toplevel.destroy)
        icono_regresar.pack(side="right", padx=10)

        descripcion_label = ctk.CTkLabel(self, text=f"Descripción: {self.tarea.descripcion}", font=("Arial", 18))
        descripcion_label.pack(pady=20, padx=20, anchor="w")

        if self.tarea.subtareas:
            subtareas_label = ctk.CTkLabel(self, text="Subtareas:", font=("Arial", 24))
            subtareas_label.pack(pady=10, padx=20, anchor="w")

            for subtarea in self.tarea.subtareas:
                subtarea_frame = ctk.CTkFrame(self, corner_radius=0)
                subtarea_frame.pack(pady=5, fill="x", padx=20)

                subtarea_nombre_label = ctk.CTkLabel(subtarea_frame, text=subtarea.nombre, font=("Times New Roman", 20, "bold"))
                subtarea_nombre_label.pack(side="top", anchor="w", pady=5, padx=5)

                subtarea_descripcion_label = ctk.CTkLabel(subtarea_frame, text=subtarea.descripcion, font=("Times New Roman", 16))
                subtarea_descripcion_label.pack(side="top", anchor="w", pady=5, padx=5)

# Clase para la ventana de agregar una nueva tarea
class VentanaAgregar(ctk.CTkFrame):
    def __init__(self, master):
        self.toplevel = tk.Toplevel(master)
        super().__init__(self.toplevel)
        self.master = master
        self.build()

    def build(self):
        self.toplevel.title("Agregar Tarea")
        self.toplevel.state('zoomed')

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
        tareas.append(nueva_tarea)
        self.master.actualizar_tareas()
        self.toplevel.destroy()

class EditTask(ctk.CTkFrame):
    def __init__(self,master,tarea):
        self.toplevel = tk.Toplevel(master)
        super().__init__(self.toplevel)
        self.master = master
        self.build()
    def build(self):
        self.toplevel.title("Editar Tarea")
        self.toplevel.state('zoomed')
        top_frame_editar = ctk.CTkFrame(self, corner_radius=0)
        top_frame_editar.pack(side="top", fill="x", pady=20)

        label_editar = ctk.CTkLabel(top_frame_editar, text="Editar los parámetros de la tarea", font=("Times New Roman", 36))
        label_editar.pack(side="left", padx=20)
        icono_regresar = ctk.CTkButton(top_frame_editar, image=self.master.imagen_regresar_tk, fg_color='transparent',text="", width=60, height=60, command=self.toplevel.destroy)
        icono_regresar.pack(side="right", padx=10)



# Lista de tareas para probar
tareas = [
    Tarea("Tarea 1", "Descripción de la tarea 1", [Tarea("Subtarea 1.1", "Descripción de la subtarea 1.1"), Tarea("Subtarea 1.2", "Descripción de la subtarea 1.2")]),
    Tarea("Tarea 2", "Descripción de la tarea 2", [Tarea("Subtarea 2.1", "Descripción de la subtarea 2.1")]),
    Tarea("Tarea 3", "Descripción de la tarea 3", [])
]

if __name__ == "__main__":
    app = TaskList()
    app.mainloop()
