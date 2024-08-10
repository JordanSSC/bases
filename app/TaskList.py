import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Clase placeholder para representar una tarea xd
class Tarea:
    def __init__(self, nombre, descripcion, subtareas=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.subtareas = subtareas if subtareas else []

# Clase principal para la lista de tareas
class TaskList(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.build()

    def build(self):
        self.title("Tareas")
        self.state('zoomed') 

        self.frame = ctk.CTkFrame(self, corner_radius=0)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.top_frame = ctk.CTkFrame(self.frame, corner_radius=0)
        self.top_frame.pack(side="top", fill="x", pady=20)

        self.label_tareas = ctk.CTkLabel(self.top_frame, text="TAREAS", font=("Arial", 36))
        self.label_tareas.pack(side="left", padx=20)

        self.imagen_regresar_path = "imagenes/regresar.png" 
        self.imagen_regresar = Image.open(self.imagen_regresar_path)
        self.imagen_regresar = self.imagen_regresar.resize((60, 60), Image.LANCZOS)
        self.imagen_regresar_tk = ImageTk.PhotoImage(self.imagen_regresar)

        self.icono_regresar = ctk.CTkButton(self.top_frame, image=self.imagen_regresar_tk, text="", width=60, height=60, command=self.regresar_menu_principal)
        self.icono_regresar.pack(side="right", padx=10)

        self.imagen_agregar_path = "imagenes/agregar.png" 
        self.imagen_agregar = Image.open(self.imagen_agregar_path)
        self.imagen_agregar = self.imagen_agregar.resize((60, 60), Image.LANCZOS)
        self.imagen_agregar_tk = ImageTk.PhotoImage(self.imagen_agregar)

        self.boton_agregar = ctk.CTkButton(self.top_frame, image=self.imagen_agregar_tk, text="", width=60, height=60, command=self.abrir_ventana_agregar)
        self.boton_agregar.pack(side="right", padx=10)

        self.frame_tareas = ctk.CTkFrame(self.frame, corner_radius=0)
        self.frame_tareas.pack(pady=20, padx=20, fill="both", expand=True)

        self.actualizar_tareas()

    def regresar_menu_principal(self):
        messagebox.showinfo("Regreso al menú principal", "Has regresado al menú principal") # esto falta por unirlo al dashboard y lo demás

    def confirmar_eliminar(self, tarea):
        def eliminar():
            tareas.remove(tarea)
            self.actualizar_tareas()
            confirmacion.destroy()

        def cancelar():
            confirmacion.destroy()

        confirmacion = tk.Toplevel(self)
        confirmacion.title("Confirmar Eliminación")
        confirmacion.geometry("500x150")
        confirmacion.configure(bg='#f0f0f0')

        ventana_x = self.winfo_screenwidth() // 2 - 250
        ventana_y = self.winfo_screenheight() // 2 - 100
        confirmacion.geometry(f"+{ventana_x}+{ventana_y}")

        mensaje = tk.Label(confirmacion, text="¿Estás seguro de que quieres eliminar esta tarea?", font=("Arial", 12), bg='#f0f0f0')
        mensaje.pack(pady=20)

        boton_confirmar = tk.Button(confirmacion, text="Confirmar", font=("Arial", 12), command=eliminar)
        boton_confirmar.pack(side="left", padx=20, pady=10)

        boton_cancelar = tk.Button(confirmacion, text="Cancelar", font=("Arial", 12), command=cancelar)
        boton_cancelar.pack(side="right", padx=20, pady=10)

    def abrir_ventana_tarea(self, tarea):
        ventana_tarea = tk.Toplevel(self)
        ventana_tarea.title(tarea.nombre)
        ventana_tarea.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        ventana_tarea.state('zoomed') 

        frame_tarea = ctk.CTkFrame(ventana_tarea, corner_radius=0)
        frame_tarea.pack(pady=0, padx=0, fill="both", expand=True)

        top_frame_tarea = ctk.CTkFrame(frame_tarea, corner_radius=0)
        top_frame_tarea.pack(side="top", fill="x", pady=20)

        label_tarea = ctk.CTkLabel(top_frame_tarea, text=tarea.nombre, font=("Arial", 36))
        label_tarea.pack(side="left", padx=20)

        icono_regresar = ctk.CTkButton(top_frame_tarea, image=self.imagen_regresar_tk, text="", width=60, height=60, command=ventana_tarea.destroy)
        icono_regresar.pack(side="right", padx=10)

        descripcion_label = ctk.CTkLabel(frame_tarea, text=f"Descripción: {tarea.descripcion}", font=("Arial", 18))
        descripcion_label.pack(pady=20, padx=20, anchor="w")

        if tarea.subtareas:
            subtareas_label = ctk.CTkLabel(frame_tarea, text="Subtareas:", font=("Arial", 24))
            subtareas_label.pack(pady=10, padx=20, anchor="w")

            for subtarea in tarea.subtareas:
                subtarea_frame = ctk.CTkFrame(frame_tarea, corner_radius=0)
                subtarea_frame.pack(pady=5, fill="x", padx=20)

                subtarea_nombre_label = ctk.CTkLabel(subtarea_frame, text=subtarea.nombre, font=("Times New Roman", 20, "bold"))
                subtarea_nombre_label.pack(side="top", anchor="w", pady=5, padx=5)

                subtarea_descripcion_label = ctk.CTkLabel(subtarea_frame, text=subtarea.descripcion, font=("Times New Roman", 16))
                subtarea_descripcion_label.pack(side="top", anchor="w", pady=5, padx=5)

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

            eliminar_img = Image.open("imagenes/basura.png")
            eliminar_img = eliminar_img.resize((30, 30), Image.LANCZOS)
            eliminar_tk = ImageTk.PhotoImage(eliminar_img)
            
            boton_eliminar = ctk.CTkButton(tarea_frame, image=eliminar_tk, text="", width=30, height=30, command=lambda t=tarea: self.confirmar_eliminar(t))
            boton_eliminar.image = eliminar_tk
            boton_eliminar.pack(side="right", padx=10)

            tarea_frame.bind("<Button-1>", lambda e, t=tarea: self.abrir_ventana_tarea(t))
            nombre_label.bind("<Button-1>", lambda e, t=tarea: self.abrir_ventana_tarea(t))
            descripcion_label.bind("<Button-1>", lambda e, t=tarea: self.abrir_ventana_tarea(t))

    def abrir_ventana_agregar(self):
        ventana_agregar = tk.Toplevel(self)
        ventana_agregar.title("Agregar Tarea")
        ventana_agregar.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        ventana_agregar.state('zoomed')

        frame_agregar = ctk.CTkFrame(ventana_agregar, corner_radius=0)
        frame_agregar.pack(pady=0, padx=0, fill="both", expand=True)

        top_frame_agregar = ctk.CTkFrame(frame_agregar, corner_radius=0)
        top_frame_agregar.pack(side="top", fill="x", pady=20)

        label_agregar = ctk.CTkLabel(top_frame_agregar, text="AGREGAR TAREA", font=("Arial", 36))
        label_agregar.pack(side="left", padx=20)

        icono_regresar = ctk.CTkButton(top_frame_agregar, image=self.imagen_regresar_tk, text="", width=60, height=60, command=ventana_agregar.destroy)
        icono_regresar.pack(side="right", padx=10)


# Lista de tareas para probar :V
tareas = [
    Tarea("Tarea 1", "Descripción de la tarea 1", [Tarea("Subtarea 1.1", "Descripción de la subtarea 1.1"), Tarea("Subtarea 1.2", "Descripción de la subtarea 1.2")]),
    Tarea("Tarea 2", "Descripción de la tarea 2", [Tarea("Subtarea 2.1", "Descripción de la subtarea 2.1")]),
    Tarea("Tarea 3", "Descripción de la tarea 3", [])
]

if __name__ == "__main__":
    app = TaskList()
    app.mainloop()