import customtkinter as ctk
import tkinter as tk
from PIL import Image

class TaskOverviewPage(ctk.CTk):
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

        for tarea in tareas: # cambiar
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
        VentanaAgregar(self) # lleva a NewTaskPage

if __name__ == "__main__":
    app = TaskOverviewPage()
    app.mainloop()