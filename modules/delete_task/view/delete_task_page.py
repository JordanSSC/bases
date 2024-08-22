import customtkinter as ctk
import tkinter as tk


class DeleteTaskPage(ctk.CTkFrame):
    def __init__(self, master, tarea):
        self.toplevel = tk.Toplevel(master)
        super().__init__(self.toplevel)
        self.master = master
        self.tarea = tarea
        self.build()

    def build(self):
        self.title("Confirmar Eliminación")
        self.geometry("500x150")

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
        tareas.remove(self.tarea) # acá va la lista de tareas del usuario, actualizar
        self.master.actualizar_tareas()
        self.toplevel.destroy()

if __name__ == "__main__":
    app = DeleteTaskPage()
    app.mainloop()