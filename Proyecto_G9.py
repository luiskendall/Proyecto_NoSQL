import pymongo
from pymongo import MongoClient, errors
import tkinter as tk
from tkinter import messagebox, ttk

connectionString = "mongodb+srv://admin:admin@proyectog9.etru1b1.mongodb.net/?retryWrites=true&w=majority"

try:
    client = pymongo.MongoClient(connectionString)
    print("Conexión exitosa.")
    
except pymongo.errors.ConnectionFailure as e:
    print("Error de conexión:", e)

db=client["Escuela"]
anunciosColeccion = db["Anuncios"]
asistenciaColeccion = db["Asistencia"]
calificacionesColeccion = db["Calificaciones"]
estudiantesColeccion = db["Estudiantes"]
gruposColeccion = db["Grupos"]
materiasColeccion = db["Materias"]
pagosMatriculaColeccion = db["Pagos_Matricula"]
profesoresColeccion = db["Profesores"]


class FormularioAgregarAnuncio:

    def __init__(self, master, callback_agregar, callback_editar=None):
        self.master = master
        self.master.title("Agregar Nuevo Anuncio")

        window_width = 300 
        window_height = 200
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.label_id_anuncio = ttk.Label(master, text="ID Anuncio:")
        self.label_id_anuncio.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_anuncio = ttk.Entry(master)
        self.entry_id_anuncio.grid(row=0, column=1, padx=10, pady=10)

        self.label_titulo = ttk.Label(master, text="Título:")
        self.label_titulo.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_titulo = ttk.Entry(master)
        self.entry_titulo.grid(row=1, column=1, padx=10, pady=10)

        self.label_contenido = ttk.Label(master, text="Contenido:")
        self.label_contenido.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_contenido = ttk.Entry(master)
        self.entry_contenido.grid(row=2, column=1, padx=10, pady=10)

        self.btn_agregar = ttk.Button(master, text="Agregar", command=lambda: [callback_agregar(), master.destroy()])
        self.btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

class FormularioEditarAnuncio:

    def __init__(self, master, callback_editar):
        self.master = master
        self.master.title("Editar Anuncio")

        window_width = 300
        window_height = 200
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.label_id_anuncio = ttk.Label(master, text="ID Anuncio:")
        self.label_id_anuncio.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_anuncio = ttk.Entry(master)
        self.entry_id_anuncio.grid(row=0, column=1, padx=10, pady=10)

        self.label_titulo = ttk.Label(master, text="Título:")
        self.label_titulo.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_titulo = ttk.Entry(master)
        self.entry_titulo.grid(row=1, column=1, padx=10, pady=10)

        self.label_contenido = ttk.Label(master, text="Contenido:")
        self.label_contenido.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_contenido = ttk.Entry(master)
        self.entry_contenido.grid(row=2, column=1, padx=10, pady=10)

        self.btn_editar = ttk.Button(master, text="Editar", command=lambda: [callback_editar(), master.destroy()])
        self.btn_editar.grid(row=3, column=0, columnspan=2, pady=10)

class FormularioEliminarAnuncio:

    def __init__(self, master, callback_eliminar):
        self.master = master
        self.master.title("Eliminar Anuncio")

        window_width = 300
        window_height = 150
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.label_id_anuncio = ttk.Label(master, text="ID Anuncio:")
        self.label_id_anuncio.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_anuncio = ttk.Entry(master)
        self.entry_id_anuncio.grid(row=0, column=1, padx=10, pady=10)

        self.btn_eliminar = ttk.Button(master, text="Eliminar", command=lambda: [callback_eliminar(self.entry_id_anuncio.get()), master.destroy()])
        self.btn_eliminar.grid(row=1, column=0, columnspan=2, pady=10)

class VentanaGestionAnuncios:
    
    def __init__(self, master, interfaz_grafica):
        self.master = master
        self.interfaz_grafica=interfaz_grafica

        self.master.title("Gestión de Anuncios")

        self.master.geometry("400x200")

        widthScreen = root.winfo_screenwidth()
        heightScreen = root.winfo_screenheight()

        x_pos = (widthScreen - 400) // 2
        y_pos = (heightScreen - 200) // 2
        self.master.geometry(f"400x200+{x_pos}+{y_pos}")

        self.label_titulo = tk.Label(master, text="Gestión de Anuncios", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        #AGREGAR ANUNCIO
        self.btn_agregar_anuncio = tk.Button(master, text="Agregar Anuncio", command=self.mostrar_form_agregar)
        self.btn_agregar_anuncio.pack(pady=10)

        #EDITAR ANUNCIO
        self.btn_editar_anuncio = tk.Button(master, text="Editar Anuncio", command=self.mostrar_form_editar)
        self.btn_editar_anuncio.pack(pady=10)

        #ELIMINAR ANUNCIO
        self.btn_eliminar_anuncio = tk.Button(master, text="Eliminar Anuncio", command=self.mostrar_form_eliminar)
        self.btn_eliminar_anuncio.pack(pady=10)

        self.form_agregar = None

    def mostrar_form_agregar(self):
        ventana_form_agregar = tk.Toplevel(self.master)
        self.form_agregar = FormularioAgregarAnuncio(ventana_form_agregar, self.agregar_anuncio)
        ventana_form_agregar.wait_window(ventana_form_agregar)

    def mostrar_form_editar(self):
        ventana_form_editar = tk.Toplevel(self.master)
        self.form_editar = FormularioEditarAnuncio(ventana_form_editar, self.editar_anuncio)
        ventana_form_editar.wait_window(ventana_form_editar)

    def mostrar_form_eliminar(self):
        ventana_form_eliminar = tk.Toplevel(self.master)
        self.form_eliminar = FormularioEliminarAnuncio(ventana_form_eliminar, self.eliminar_anuncio)

    def agregar_anuncio(self):
        if self.form_agregar:
            # Get datos form
            id_anuncio =self.form_agregar.entry_id_anuncio.get()
            titulo = self.form_agregar.entry_titulo.get()
            contenido = self.form_agregar.entry_contenido.get()

            # NOT NULL
            if not id_anuncio or not titulo or not contenido:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return
            
            #Check Id Anuncio
            if anunciosColeccion.find_one({"id_anuncios": id_anuncio}):
                messagebox.showwarning("Advertencia", f"El ID del anuncio '{id_anuncio}' ya existe. Por favor, elige otro.")
                return

            anuncio = {"id_anuncios": id_anuncio,"titulo": titulo, "contenido": contenido}
            anunciosColeccion.insert_one(anuncio)
            messagebox.showinfo("Éxito","Se ingresó correctamente el anuncio.")

            #Cerrar ventana gestión
            self.master.destroy() 

            if self.form_agregar.master.winfo_exists():
                self.form_agregar.master.destroy()

            self.interfaz_grafica.cargar_anuncios()

    def editar_anuncio(self):
        if self.form_editar:
            # Get datos form
            id_anuncio = self.form_editar.entry_id_anuncio.get()
            titulo = self.form_editar.entry_titulo.get()
            contenido = self.form_editar.entry_contenido.get()

            # NOT NULL
            if not id_anuncio or not titulo or not contenido:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            # IF NOT EXISTS
            if not anunciosColeccion.find_one({"id_anuncios": id_anuncio}):
                messagebox.showwarning("Advertencia", f"El ID del anuncio '{id_anuncio}' no existe.")
                return
            
            anunciosColeccion.update_one({"id_anuncios": id_anuncio}, {"$set": {"titulo": titulo, "contenido": contenido}})

            messagebox.showinfo("Éxito", "Se modificó correctamente el anuncio.")

            #Cerrar ventana gestión
            self.master.destroy() 

            if self.form_editar.master.winfo_exists():
                self.form_editar.master.destroy()

            self.interfaz_grafica.cargar_anuncios()

    def eliminar_anuncio(self, id_anuncio):
        if self.form_eliminar:
        # NOT NULL
            if not id_anuncio:
                messagebox.showwarning("Advertencia", "Por favor, ingresa el ID del anuncio.")
                return

        # IF NOT EXISTS
        anuncio = anunciosColeccion.find_one({"id_anuncios": id_anuncio})
        if not anuncio:
            messagebox.showwarning("Advertencia", f"No se encontró el anuncio con el ID '{id_anuncio}'.")
            return
        
        anunciosColeccion.delete_one({"id_anuncios": id_anuncio})
        messagebox.showinfo("Éxito", f"Se eliminó correctamente el anuncio con el ID '{id_anuncio}'.")

        #Cerrar ventana gestión
        self.master.destroy() 

        if self.form_eliminar.master.winfo_exists():
            self.form_eliminar.master.destroy()

        self.interfaz_grafica.cargar_anuncios()

class VentanaSeleccionGrupo:

    def __init__(self, master, callback_seleccionar_grupo):
        self.master = master
        self.master.title("Seleccionar Grupo")

        self.master.geometry("400x200")

        widthScreen = root.winfo_screenwidth()
        heightScreen = root.winfo_screenheight()

        x_pos = (widthScreen - 400) // 2
        y_pos = (heightScreen - 200) // 2
        self.master.geometry(f"400x200+{x_pos}+{y_pos}")

        self.label_seleccionar_grupo = ttk.Label(master, text="Selecciona un Grupo:")
        self.label_seleccionar_grupo.pack(pady=10)

        self.grupos_info = self.get_grupos() 

        self.combo_grupos = ttk.Combobox(master, values=[grupo["nombre"] for grupo in self.grupos_info])
        self.combo_grupos.pack(pady=10)

        self.btn_seleccionar = ttk.Button(master, text="Seleccionar", command=lambda: [callback_seleccionar_grupo(self.combo_grupos.get(), self.obtener_id_grupo())])
        
        self.btn_seleccionar.pack(pady=10)

    #Get nombre grupos
    def get_grupos(self):
        grupos = gruposColeccion.find({}, {"_id": 0, "nombre": 1, "id_grupo": 1})
        return list(grupos)

    def obtener_id_grupo(self):
        # Get id_grupo
        grupo_seleccionado = self.combo_grupos.get()
        for grupo in self.grupos_info:
            if grupo["nombre"] == grupo_seleccionado:
                return grupo["id_grupo"]
        return None 

class VentanaGestionAsistencia:
 
 def __init__(self, master, interfaz_grafica, grupo_seleccionado, id_grupo_seleccionado):
        self.master = master
        self.interfaz_grafica = interfaz_grafica
        self.grupo_seleccionado = grupo_seleccionado
        self.master.title(f"Gestión de Asistencia - Grupo: {grupo_seleccionado}")

        
        window_width = 1050
        window_height = 300  
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2
        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
        

        self.tree_asistencia = ttk.Treeview(master)
        self.tree_asistencia['columns'] = (1, 2, 3, 4, 5)
        self.tree_asistencia.heading("#0", text="ID")
        self.tree_asistencia.column("#0", width=0, stretch=tk.NO)
        self.tree_asistencia.heading(1, text="Cédula Estudiante")
        self.tree_asistencia.heading(2, text="ID Grupo")
        self.tree_asistencia.heading(3, text="ID Materia")
        self.tree_asistencia.heading(4, text="Fecha")
        self.tree_asistencia.heading(5, text="Asistió")
        self.tree_asistencia.pack()

        for col in (1, 2, 3, 4, 5):
            self.tree_asistencia.column(col, anchor='center')

        self.tree_asistencia.pack(padx=10, pady=10)

        # Get datos y mostrarlos
        datos_asistencia = interfaz_grafica.obtener_datos_asistencia(grupo_seleccionado, id_grupo_seleccionado)

        for registro in datos_asistencia:
            self.tree_asistencia.insert('', 'end', values=(
                registro['cedula_Est'],
                registro['id_grupo'],
                registro['id_materia'],
                registro['fecha'],
                registro['asistio']
            ))

class InterfazGrafica:

    def __init__(self, master):
        self.master = master
        self.master.title("Gestión Centro Educativo")

        self.label_titulo = tk.Label(master, text="Anuncios del Centro Educativo", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # Show Anuncios
        self.text_anuncios = tk.Text(master, wrap=tk.WORD, height=10, width=60, state=tk.DISABLED)
        self.text_anuncios.pack(padx=10, pady=10)

        self.frame_botones_gestion = tk.Frame(master)
        self.frame_botones_gestion.pack(pady=10)

        self.btn_gestion_anuncios = tk.Button(self.frame_botones_gestion, text="Gestionar Anuncios", command=self.abrir_ventana_gestion_anuncios)
        self.btn_gestion_anuncios.pack(side=tk.LEFT, padx=5)

        self.form_seleccion_grupo = None  

        self.btn_gestion_asistencia = tk.Button(self.frame_botones_gestion, text="Gestionar Asistencia", command=self.abrir_ventana_seleccion_grupo)
        self.btn_gestion_asistencia.pack(side=tk.LEFT, padx=5)

        self.cargar_anuncios()

    
    def cargar_anuncios(self):
        self.text_anuncios.config(state=tk.NORMAL)  
        self.text_anuncios.delete(1.0, tk.END)

        #Get Anuncios
        anuncios = anunciosColeccion.find()

        for anuncio in anuncios:
            contenido_anuncio = f"{anuncio['id_anuncios']}. {anuncio['titulo']} - {anuncio['contenido']}\n\n"
            self.text_anuncios.insert(tk.END, contenido_anuncio)

        self.text_anuncios.config(state=tk.DISABLED)  
        self.text_anuncios.config(font=("Arial", 12), fg="black")

    def obtener_datos_asistencia(self, grupo_seleccionado, id_grupo_seleccionado):
     id_grupo = gruposColeccion.find_one({"nombre": grupo_seleccionado}, {"_id": 0, "id_grupo": 1})

     if id_grupo is not None:
        asistencia = asistenciaColeccion.find({"id_grupo": id_grupo["id_grupo"]})

        datos_asistencia = []

        for registro in asistencia:
            datos_registro = {
                'cedula_Est': registro['cedula_Est'],
                'id_grupo': registro['id_grupo'],
                'id_materia': registro['id_materia'],
                'fecha': registro['fecha'],
                'asistio': registro['asistio']
            }
            datos_asistencia.append(datos_registro)

        return datos_asistencia
     else:
        print("No se ha seleccionado un grupo.")
        return []


    def abrir_ventana_gestion_anuncios(self):
        if hasattr(self, 'ventana_gestion_anuncios') and self.ventana_gestion_anuncios.winfo_exists():
            self.ventana_gestion_anuncios.lift()
        else:
            self.ventana_gestion_anuncios = tk.Toplevel(self.master)
            app_gestion_anuncios = VentanaGestionAnuncios(self.ventana_gestion_anuncios, self)

    def abrir_ventana_seleccion_grupo(self):
       if self.form_seleccion_grupo and self.form_seleccion_grupo.master.winfo_exists():
        self.form_seleccion_grupo.master.lift()
       else:
        ventana_seleccion_grupo = tk.Toplevel(self.master)
        self.form_seleccion_grupo = VentanaSeleccionGrupo(ventana_seleccion_grupo, self.abrir_ventana_gestion_asistencia)
        ventana_seleccion_grupo.wait_window(ventana_seleccion_grupo)

    def abrir_ventana_gestion_asistencia(self, grupo_seleccionado, id_grupo_seleccionado):
     if self.form_seleccion_grupo is not None:
        grupo_seleccionado = self.form_seleccion_grupo.combo_grupos.get()
        id_grupo_seleccionado = self.form_seleccion_grupo.obtener_id_grupo()

        if grupo_seleccionado and id_grupo_seleccionado:
            if hasattr(self, 'ventana_gestion_asistencia') and self.ventana_gestion_asistencia.winfo_exists():
                self.ventana_gestion_asistencia.lift()
            else:
                self.ventana_gestion_asistencia = tk.Toplevel(self.master)
                app_gestion_asistencia = VentanaGestionAsistencia(self.ventana_gestion_asistencia, self, grupo_seleccionado, id_grupo_seleccionado)
#Main Window
root = tk.Tk()

widthScreen = root.winfo_screenwidth()
heightScreen = root.winfo_screenheight()

pos_x = (widthScreen - 1200) // 2
pos_y = (heightScreen - 600) // 2

root.geometry("1200x600+{}+{}".format(pos_x, pos_y))
app = InterfazGrafica(root)

root.mainloop()
client.close()