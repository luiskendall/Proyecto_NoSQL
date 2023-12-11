import pymongo
from pymongo import MongoClient, errors
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# ---------------------------------------CONEXION--------------------------------------- #
connectionString = "mongodb+srv://admin:admin@proyectog9.etru1b1.mongodb.net/?retryWrites=true&w=majority"

# ---------------------------------------MENSAJE DE ERROR--------------------------------------- #
try:
    client = pymongo.MongoClient(connectionString)
    print("Conexión exitosa.")
    
except pymongo.errors.ConnectionFailure as e:
    print("Error de conexión:", e)

# ---------------------------------------COLECCIONES--------------------------------------- #
db=client["Escuela"]
anunciosColeccion = db["Anuncios"]
asistenciaColeccion = db["Asistencia"]
calificacionesColeccion = db["Calificaciones"]
estudiantesColeccion = db["Estudiantes"]
gruposColeccion = db["Grupos"]
materiasColeccion = db["Materias"]
pagosMatriculaColeccion = db["Pagos_Matricula"]
profesoresColeccion = db["Profesores"]

# ---------------------------------------FORMULARIOS ANUNCIOS--------------------------------------- #
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

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

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

        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_agregar = ttk.Button(self.button_frame, text="Agregar", command=lambda: [callback_agregar(), master.destroy()])
        self.btn_agregar.grid(row=0, column=0)
        self.btn_agregar.config(width=15)

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

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

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

        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_editar = ttk.Button(self.button_frame, text="Editar", command=lambda: [callback_editar(), master.destroy()])
        self.btn_editar.grid(row=0, column=0)
        self.btn_editar.config(width=15)

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

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.label_id_anuncio = ttk.Label(master, text="ID Anuncio:")
        self.label_id_anuncio.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_anuncio = ttk.Entry(master)
        self.entry_id_anuncio.grid(row=0, column=1, padx=10, pady=10)

        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_eliminar = ttk.Button(self.button_frame, text="Eliminar", command=lambda: [callback_eliminar(self.entry_id_anuncio.get()), master.destroy()])
        self.btn_eliminar.grid(row=0, column=0)
        self.btn_eliminar.config(width=15)

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
        self.form_editar = None
        self.form_eliminar = None

    def mostrar_form_agregar(self):
        if self.form_agregar and self.form_agregar.master.winfo_exists():
            self.form_agregar.master.lift()
        else:
            ventana_form_agregar = tk.Toplevel(self.master)
            self.form_agregar = FormularioAgregarAnuncio(ventana_form_agregar, self.agregar_anuncio)
            ventana_form_agregar.wait_window(ventana_form_agregar)

    def mostrar_form_editar(self):
        if self.form_editar and self.form_editar.master.winfo_exists():
            self.form_editar.master.lift()
        else:
            ventana_form_editar = tk.Toplevel(self.master)
            self.form_editar = FormularioEditarAnuncio(ventana_form_editar, self.editar_anuncio)
            ventana_form_editar.wait_window(ventana_form_editar)

    def mostrar_form_eliminar(self):
        if self.form_eliminar and self.form_eliminar.master.winfo_exists():
            self.form_eliminar.master.lift()
        else:
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
                self.master.deiconify() 
                self.master.lift()
                return
            
            #Check Id Anuncio
            if anunciosColeccion.find_one({"id_anuncios": id_anuncio}):
                messagebox.showwarning("Advertencia", f"El ID del anuncio '{id_anuncio}' ya existe. Por favor, elige otro.")
                self.master.deiconify() 
                self.master.lift() 
            else:
                anuncio = {"id_anuncios": id_anuncio, "titulo": titulo, "contenido": contenido}
                anunciosColeccion.insert_one(anuncio)
                messagebox.showinfo("Éxito", "Se ingresó correctamente el anuncio.")

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
                self.master.deiconify() 
                self.master.lift()
                return

            # IF NOT EXISTS
            if not anunciosColeccion.find_one({"id_anuncios": id_anuncio}):
                messagebox.showwarning("Advertencia", f"El ID del anuncio '{id_anuncio}' no existe.")
                self.master.deiconify() 
                self.master.lift() 
            else:
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
                self.master.deiconify() 
                self.master.lift()
                return

        # IF NOT EXISTS
        anuncio = anunciosColeccion.find_one({"id_anuncios": id_anuncio})
        if not anuncio:
            messagebox.showwarning("Advertencia", f"No se encontró el anuncio con el ID '{id_anuncio}'.")
            self.master.deiconify() 
            self.master.lift() 
        else:
            anunciosColeccion.delete_one({"id_anuncios": id_anuncio})
            messagebox.showinfo("Éxito", f"Se eliminó correctamente el anuncio con el ID '{id_anuncio}'.")

            #Cerrar ventana gestión
            self.master.destroy() 

            if self.form_eliminar.master.winfo_exists():
                self.form_eliminar.master.destroy()

            self.interfaz_grafica.cargar_anuncios()


# ---------------------------------------FORMULARIOS ASISTENCIA--------------------------------------- #
class FormularioAgregarAsistencia:

    def __init__(self, master, callback_agregar_registro):
        self.master = master
        self.master.title("Agregar Nuevo Registro")

        window_width = 370 
        window_height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        #Datos ComboBox
        cedulas_estudiantes = self.get_cedulas_estudiantes()
        nombres_grupos = self.get_nombres_grupos()
        id_materias = self.get_id_materias()

        self.label_cedula_estudiante = ttk.Label(master, text="Cédula Estudiante:")
        self.label_cedula_estudiante.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.combo_cedula_estudiante = ttk.Combobox(master, values=cedulas_estudiantes)
        self.combo_cedula_estudiante.grid(row=0, column=1, padx=10, pady=10)

        self.label_nombre_grupo = ttk.Label(master, text="Nombre del Grupo:")
        self.label_nombre_grupo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.combo_nombre_grupo = ttk.Combobox(master, values=nombres_grupos)
        self.combo_nombre_grupo.grid(row=1, column=1, padx=10, pady=10)

        self.label_id_materia = ttk.Label(master, text="ID Materia:")
        self.label_id_materia.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.combo_id_materia = ttk.Combobox(master, values=id_materias)
        self.combo_id_materia.grid(row=2, column=1, padx=10, pady=10)

        self.label_fecha = ttk.Label(master, text="Fecha:")
        self.label_fecha.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        self.fecha_var = tk.StringVar()
        self.entry_fecha = ttk.Entry(master, textvariable=self.fecha_var, state="readonly")
        self.entry_fecha.grid(row=3, column=1, padx=10, pady=10)

        #Fecha actual
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        self.fecha_var.set(fecha_actual)

        self.label_asistio = ttk.Label(master, text="Asistió:")
        self.label_asistio.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.combo_asistio = ttk.Combobox(master, values=["Sí", "No"])
        self.combo_asistio.grid(row=4, column=1, padx=10, pady=10)

        self.btn_agregar_registro = ttk.Button(master, text="Agregar Registro", command=lambda: [callback_agregar_registro(), master.destroy()])
        self.btn_agregar_registro.grid(row=5, column=0, columnspan=2, pady=10)
    
    def obtener_id_grupo_por_nombre(self, nombre_grupo):
        grupo = gruposColeccion.find_one({"nombre": nombre_grupo}, {"_id": 0, "id_grupo": 1})
        return grupo["id_grupo"] if grupo else None

    def obtener_valor_asistio(self):
        valor_asistio = True if self.combo_asistio.get().lower() == "sí" else False
        return valor_asistio
    
    def get_nombres_grupos(self):
        nombres_grupos = gruposColeccion.distinct("nombre")
        return nombres_grupos

    def get_cedulas_estudiantes(self):
        cedulas_estudiantes = estudiantesColeccion.distinct("cedula_Est")
        return cedulas_estudiantes

    def get_id_grupos(self):
        id_grupos = gruposColeccion.distinct("id_grupo")
        return id_grupos

    def get_id_materias(self):
        id_materias = materiasColeccion.distinct("id_materia")
        return id_materias

    def obtener_valor_fecha(self):
        fecha_str = self.entry_fecha.get()

        #Fecha sin la hora 
        fecha_str = fecha_str.split(" ")[0] 
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        fecha_bson = datetime.combine(fecha, datetime.min.time())
        return fecha_bson

class FormularioEditarAsistencia:

    def __init__(self, master, datos_registro, nombre_grupo, id_materia, callback_editar_registro):
        self.master = master
        self.master.title("Editar Registro de Asistencia")
    
        window_width = 340
        window_height = 350
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.label_cedula_estudiante = ttk.Label(master, text="Cédula Estudiante:")
        self.label_cedula_estudiante.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_cedula_estudiante = ttk.Entry(master)
        self.entry_cedula_estudiante.grid(row=0, column=1, padx=10, pady=10)
        self.entry_cedula_estudiante.insert(0, datos_registro['cedula_Est'])
        self.entry_cedula_estudiante.config(state="readonly")

        self.label_nombre_grupo = ttk.Label(master, text="Nombre del Grupo:")
        self.label_nombre_grupo.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_nombre_grupo_valor = ttk.Label(master, text=nombre_grupo)
        self.label_nombre_grupo_valor.grid(row=1, column=1, padx=10, pady=10)

        self.label_id_materia = ttk.Label(master, text="ID Materia:")
        self.label_id_materia.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.label_id_materia_valor = ttk.Label(master, text=id_materia)
        self.label_id_materia_valor.grid(row=2, column=1, padx=10, pady=10)

        self.label_fecha = ttk.Label(master, text="Fecha:")
        self.label_fecha.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.fecha_var = tk.StringVar()
        self.entry_fecha = ttk.Entry(master, textvariable=self.fecha_var, state="readonly")
        self.entry_fecha.grid(row=3, column=1, padx=10, pady=10)
        self.fecha_var.set(datos_registro['fecha'])

        self.label_asistio = ttk.Label(master, text="Asistió:")
        self.label_asistio.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.combo_asistio = ttk.Combobox(master, values=["Sí", "No"])
        self.combo_asistio.grid(row=4, column=1, padx=10, pady=10)
        self.combo_asistio.set(datos_registro['asistio'])

        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_editar_registro = ttk.Button(self.button_frame, text="Editar Registro", command=lambda: [callback_editar_registro(), master.destroy()])
        self.btn_editar_registro.grid(row=0, column=0) 
        self.btn_editar_registro.config(width=15)  

    def obtener_valor_asistio(self):
        valor_asistio = True if self.combo_asistio.get().lower() == "sí" else False
        return valor_asistio

    def obtener_valor_fecha(self):
        fecha_str = self.entry_fecha.get()

        #Fecha sin la hora 
        fecha_str = fecha_str.split(" ")[0] 
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        fecha_bson = datetime.combine(fecha, datetime.min.time())
        return fecha_bson
    
    def obtener_nombres_grupos(self):
        nombres_grupos = gruposColeccion.distinct("nombre")
        return nombres_grupos

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
        self.id_grupo_seleccionado = id_grupo_seleccionado
        self.master.title(f"Gestión de Asistencia - Grupo: {grupo_seleccionado}")
        
        self.btn_frame = ttk.Frame(master)
        self.btn_frame.pack(pady=10)

        self.form_agregar_registro = None
        self.form_editar_registro = None

        #AGREGAR Asistencia
        self.btn_agregar_registro = ttk.Button(self.btn_frame, text="Agregar Registro", command=self.mostrar_form_agregar_registro)
        self.btn_agregar_registro.pack(side=tk.LEFT, padx=5)

        #EDITAR Asistencia
        self.btn_editar_registro = ttk.Button(self.btn_frame, text="Editar Registro", command=self.mostrar_form_editar_registro)
        self.btn_editar_registro.pack(side=tk.LEFT, padx=5)

        #ELIMINAR Asistencia
        self.btn_eliminar_registro = ttk.Button(self.btn_frame, text="Eliminar Registro", command=self.eliminar_registro)
        self.btn_eliminar_registro.pack(side=tk.LEFT, padx=5)

        
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

        self.last_selected_item = None
        self.tree_asistencia.bind('<ButtonRelease-1>', lambda event: self.seleccionar_registro(event))
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    #Abrir Seleccion de grupos
    def on_close(self):
        self.master.destroy()
        self.interfaz_grafica.abrir_ventana_seleccion_grupo()
    
    def seleccionar_registro(self, event):
        #Registro seleccionado
        selected_item = self.tree_asistencia.selection()

        #Desmarcar si es el mismo registro
        if selected_item == self.last_selected_item:
            self.tree_asistencia.selection_remove(selected_item)
            self.last_selected_item = None
        else:
            
            self.last_selected_item = selected_item

    def obtener_id_grupo_por_nombre(self, nombre_grupo):
        grupo = gruposColeccion.find_one({"nombre": nombre_grupo}, {"_id": 0, "id_grupo": 1})
        return grupo["id_grupo"] if grupo else None

    def obtener_nombre_grupo_por_id(self, id_grupo):
        grupo = gruposColeccion.find_one({"id_grupo": id_grupo}, {"_id": 0, "nombre": 1})
        return grupo["nombre"] if grupo else None

    def mostrar_form_agregar_registro(self):
        if self.form_agregar_registro and self.form_agregar_registro.master.winfo_exists():
            self.form_agregar_registro.master.lift()
        else:
            ventana_form_agregar_registro = tk.Toplevel(self.master)
            self.form_agregar_registro = FormularioAgregarAsistencia(ventana_form_agregar_registro, self.agregar_registro)
            ventana_form_agregar_registro.wait_window(ventana_form_agregar_registro)

    def mostrar_form_editar_registro(self):
        if self.form_editar_registro and self.form_editar_registro.master.winfo_exists():
            self.form_editar_registro.master.lift()
        else:
            selected_item = self.tree_asistencia.selection()
            if not selected_item:
                messagebox.showwarning("Advertencia", "Por favor, selecciona un registro de asistencia.")
                self.actualizar_tabla_asistencia()
                return

            datos_registro = self.obtener_datos_registro_seleccionado(selected_item)
            print("Datos del registro seleccionado:", datos_registro)

            #Nombre grupo por id_grupo
            nombre_grupo = self.obtener_nombre_grupo_por_id(datos_registro['id_grupo'])

            ventana_form_editar_registro = tk.Toplevel(self.master)
            self.form_editar_registro = FormularioEditarAsistencia(
            ventana_form_editar_registro,
            datos_registro,
            nombre_grupo,
            datos_registro['id_materia'],
            self.editar_registro
            )
            ventana_form_editar_registro.wait_window(ventana_form_editar_registro)

    def obtener_datos_registro_seleccionado(self, selected_item):
        item_values = self.tree_asistencia.item(selected_item, 'values')
        cedula_estudiante = item_values[0]
        id_grupo = int(item_values[1])
        id_materia = item_values[2]
        fecha_str = item_values[3].split(" ")[0]
        asistio = item_values[4]

        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")

        datos_registro = {
            'cedula_Est': cedula_estudiante,
            'id_grupo': id_grupo,
            'id_materia': id_materia,
            'fecha': fecha,
            'asistio': asistio
        }

        return datos_registro

    def actualizar_tabla_asistencia(self):
        #Get datos y mostrarlos
        datos_asistencia = self.interfaz_grafica.obtener_datos_asistencia(self.grupo_seleccionado, self.id_grupo_seleccionado)

        for item in self.tree_asistencia.get_children():
            self.tree_asistencia.delete(item)

        for registro in datos_asistencia:
            self.tree_asistencia.insert('', 'end', values=(
                registro['cedula_Est'],
                registro['id_grupo'],
                registro['id_materia'],
                registro['fecha'],
                registro['asistio']
            ))
        self.master.lift()

    def agregar_registro(self):
        if self.form_agregar_registro:

            #Datos form
            cedula_estudiante = self.form_agregar_registro.combo_cedula_estudiante.get()
            nombre_grupo = self.form_agregar_registro.combo_nombre_grupo.get()
            id_materia = self.form_agregar_registro.combo_id_materia.get()
            fecha = self.form_agregar_registro.obtener_valor_fecha()
            asistio = self.form_agregar_registro.obtener_valor_asistio()

            id_grupo = self.obtener_id_grupo_por_nombre(nombre_grupo)

            #NOT NULL
            if not (cedula_estudiante and id_grupo and id_materia and fecha):
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                self.actualizar_tabla_asistencia()
                return

            if not estudiantesColeccion.find_one({"cedula_Est": cedula_estudiante}):
                messagebox.showwarning("Advertencia", f"No existe un estudiante con la cédula '{cedula_estudiante}'.")
                return

            if not materiasColeccion.find_one({"id_materia": id_materia}):
                messagebox.showwarning("Advertencia", f"No existe una materia con el ID '{id_materia}'.")
                return

            #INSERT Asistencia
            nuevo_registro = {
                'cedula_Est': cedula_estudiante,
                'id_grupo': id_grupo,  
                'id_materia': id_materia,
                'fecha': fecha,
                'asistio': asistio
            }

            asistenciaColeccion.insert_one(nuevo_registro)
            messagebox.showinfo("Éxito", "Se agregó correctamente el registro de asistencia.")

            self.actualizar_tabla_asistencia()

            if self.form_agregar_registro.master.winfo_exists():
                self.form_agregar_registro.master.destroy()

    def editar_registro(self):
        if self.form_editar_registro:
            # Datos del formulario
            cedula_estudiante = self.form_editar_registro.entry_cedula_estudiante.get()
            id_materia = self.form_editar_registro.label_id_materia_valor["text"]
            fecha = self.form_editar_registro.obtener_valor_fecha()
            asistio = self.form_editar_registro.obtener_valor_asistio()

            # id_grupo
            id_grupo_seleccionado = self.id_grupo_seleccionado if hasattr(self, 'id_grupo_seleccionado') else None

            if not cedula_estudiante or not id_grupo_seleccionado or not id_materia or not fecha:
                messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
                return
            
            filtro = {
                'cedula_Est': cedula_estudiante,
                'id_grupo': id_grupo_seleccionado,
                'id_materia': id_materia,
                'fecha': fecha
            }

            nuevo_registro = {
                'cedula_Est': cedula_estudiante,
                'id_grupo': id_grupo_seleccionado,
                'id_materia': id_materia,
                'fecha': fecha,
                'asistio': asistio
            }

            #EDITAR Asistencia
            asistenciaColeccion.update_one(filtro, {"$set": nuevo_registro}, upsert=True)

            messagebox.showinfo("Éxito", "Se editó correctamente el registro de asistencia.")
            self.actualizar_tabla_asistencia()

            if self.form_editar_registro.master.winfo_exists():
                self.form_editar_registro.master.destroy()

    def eliminar_registro(self):
        selected_item = self.tree_asistencia.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un registro para eliminar.")
            self.actualizar_tabla_asistencia()
            return

        #Get datos registro seleccionado
        datos_registro = self.obtener_datos_registro_seleccionado(selected_item[0])

        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres eliminar este registro?")
        if respuesta:
            try:
                filtro = {
                    'cedula_Est': datos_registro['cedula_Est'],
                    'id_grupo': datos_registro['id_grupo'],
                    'id_materia': datos_registro['id_materia'],
                    'fecha': datos_registro['fecha']
                }

                #DELETE Asistencia
                asistenciaColeccion.delete_one(filtro)

                self.actualizar_tabla_asistencia()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
                self.master.lift()

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al eliminar el registro: {e}")

# ---------------------------------------FORMULARIOS ESTUDIANTES--------------------------------------- #
class FormularioAgregarEstudiante:

    def __init__(self, master, callback_agregar, callback_editar=None):
        self.master = master
        self.master.title("Agregar Nuevo Estudiante")

        window_width = 380 
        window_height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        #CEDULA
        self.label_cedula_Est = ttk.Label(master, text="Cédula del Estudiante:")
        self.label_cedula_Est.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_cedula_Est = ttk.Entry(master)
        self.entry_cedula_Est.grid(row=0, column=1, padx=10, pady=10)
        #NOMBRE
        self.label_nombre = ttk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = ttk.Entry(master)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)
        #EDAD
        self.label_edad = ttk.Label(master, text="Edad:")
        self.label_edad.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_edad = ttk.Entry(master)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=10)
        #GRUPO
        self.label_id_grupo = ttk.Label(master, text="Grupo:")
        self.label_id_grupo.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_grupo = ttk.Entry(master)
        self.entry_id_grupo.grid(row=3, column=1, padx=10, pady=10)
        #CORREO
        self.label_correo = ttk.Label(master, text="Correo Electrónico:")
        self.label_correo.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.entry_correo = ttk.Entry(master)
        self.entry_correo.grid(row=4, column=1, padx=10, pady=10)

        #Button Volver
        self.btn_agregar = ttk.Button(master, text="Volver", command=lambda: [master.destroy()])
        self.btn_agregar.grid(row=5, column=0, columnspan=1, pady=10)

        #Button Agregar
        self.btn_agregar = ttk.Button(master, text="Agregar", command=lambda: [callback_agregar(), master.destroy()])
        self.btn_agregar.grid(row=5, column=1, columnspan=2, pady=10)

class FormularioEditarEstudiante:

    def __init__(self, master, callback_editar):
        self.master = master
        self.master.title("Editar Anuncio")

        window_width = 380 
        window_height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        #CEDULA
        self.label_cedula_Est = ttk.Label(master, text="Cédula del Estudiante:")
        self.label_cedula_Est.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_cedula_Est = ttk.Entry(master)
        self.entry_cedula_Est.grid(row=0, column=1, padx=10, pady=10)
        #NOMBRE
        self.label_nombre = ttk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = ttk.Entry(master)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)
        #EDAD
        self.label_edad = ttk.Label(master, text="Edad:")
        self.label_edad.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_edad = ttk.Entry(master)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=10)
        #GRUPO
        self.label_id_grupo = ttk.Label(master, text="Grupo:")
        self.label_id_grupo.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_grupo = ttk.Entry(master)
        self.entry_id_grupo.grid(row=3, column=1, padx=10, pady=10)
        #CORREO
        self.label_correo = ttk.Label(master, text="Correo Electrónico:")
        self.label_correo.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.entry_correo = ttk.Entry(master)
        self.entry_correo.grid(row=4, column=1, padx=10, pady=10)

        #Button Volver
        self.btn_agregar = ttk.Button(master, text="Volver", command=lambda: [master.destroy()])
        self.btn_agregar.grid(row=5, column=0, columnspan=1, pady=10)

        #Button Editar
        self.btn_editar = ttk.Button(master, text="Editar", command=lambda: [callback_editar(), master.destroy()])
        self.btn_editar.grid(row=5, column=1, columnspan=2, pady=10)

class FormularioEliminarEstudiante:

    def __init__(self, master, callback_eliminar):
        self.master = master
        self.master.title("Eliminar Estudiante")

        window_width = 350
        window_height = 150
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.label_cedula_Est = ttk.Label(master, text="Cédula de estudiante:")
        self.label_cedula_Est.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_cedula_Est = ttk.Entry(master)
        self.entry_cedula_Est.grid(row=0, column=1, padx=10, pady=10)

        #Button Volver
        self.btn_agregar = ttk.Button(master, text="Volver", command=lambda: [master.destroy()])
        self.btn_agregar.grid(row=1, column=0, columnspan=1, pady=10)

        #Button Eliminar
        self.btn_eliminar = ttk.Button(master, text="Eliminar", command=lambda: [callback_eliminar(self.entry_cedula_Est.get()), master.destroy()])
        self.btn_eliminar.grid(row=1, column=1, columnspan=2, pady=10)

class VentanaGestionEstudiantes:
    
    def __init__(self, master, interfaz_grafica):
        self.master = master
        self.interfaz_grafica=interfaz_grafica

        self.master.title("Gestión de Estudiantes")

        self.master.geometry("400x200")

        widthScreen = root.winfo_screenwidth()
        heightScreen = root.winfo_screenheight()

        x_pos = (widthScreen - 400) // 2
        y_pos = (heightScreen - 200) // 2
        self.master.geometry(f"400x200+{x_pos}+{y_pos}")

        self.label_titulo = tk.Label(master, text="Gestión de Estudiantes", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        #AGREGAR ESTUDIANTE
        self.btn_agregar_estudiante = tk.Button(master, text="Agregar Estudiante", command=self.mostrar_form_agregar_estudiante)
        self.btn_agregar_estudiante.pack(pady=10)

        #EDITAR ESTUDIANTE
        self.btn_editar_estudiante = tk.Button(master, text="Editar Estudiante", command=self.mostrar_form_editar_estudiante)
        self.btn_editar_estudiante.pack(pady=10)

        #ELIMINAR ESTUDIANTE
        self.btn_eliminar_estudiante = tk.Button(master, text="Eliminar Estudiante", command=self.mostrar_form_eliminar_estudiante)
        self.btn_eliminar_estudiante.pack(pady=10)

        self.form_agregar_estudiante = None
        self.form_editar_estudiante = None
        self.form_eliminar_estudiante= None 

    def mostrar_form_agregar_estudiante(self):
        ventana_form_agregar_estudiante = tk.Toplevel(self.master)
        self.form_agregar_estudiante = FormularioAgregarEstudiante(
            ventana_form_agregar_estudiante, self.agregar_estudiante)
        ventana_form_agregar_estudiante.wait_window(ventana_form_agregar_estudiante)

    def mostrar_form_editar_estudiante(self):
        ventana_form_editar_estudiante = tk.Toplevel(self.master)
        self.form_editar_estudiante = FormularioEditarEstudiante(ventana_form_editar_estudiante, self.editar_estudiante)
        ventana_form_editar_estudiante.wait_window(ventana_form_editar_estudiante)

    def mostrar_form_eliminar_estudiante(self):
        ventana_form_eliminar_estudiante = tk.Toplevel(self.master)
        self.form_eliminar_estudiante = FormularioEliminarEstudiante(ventana_form_eliminar_estudiante, self.eliminar_estudiante)

    #AGREGAR ESTUDIANTE
    def agregar_estudiante(self):
        print("Adding student...")
        if self.form_agregar_estudiante:
            # Get datos form
            cedula_Est = self.form_agregar_estudiante.entry_cedula_Est.get()
            nombre = self.form_agregar_estudiante.entry_nombre.get()
            edad = self.form_agregar_estudiante.entry_edad.get()
            id_grupo = self.form_agregar_estudiante.entry_id_grupo.get()
            correo = self.form_agregar_estudiante.entry_correo.get()

            # NOT NULL
            if not cedula_Est or not nombre or not edad or not id_grupo or not correo:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            # Check cedula estudiante
            if estudiantesColeccion.find_one({"cedula_Est": cedula_Est}):
                messagebox.showwarning(
                    "Advertencia", f"La cédula '{cedula_Est}' ya existe. Por favor, elige otra."
                )
                return

            estudiante = {
                "cedula_Est": cedula_Est,
                "nombre": nombre,
                "edad": edad,
                "id_grupo": id_grupo,
                "correo": correo,
            }

            try:
                estudiantesColeccion.insert_one(estudiante)
                print("Student added successfully!")
                messagebox.showinfo("Éxito", "Se ingresó correctamente al estudiante.")

                # Cerrar ventana gestión
                self.master.destroy()

                if self.form_agregar_estudiante.master.winfo_exists():
                    self.form_agregar_estudiante.master.destroy()
            except Exception as e:
                print(f"Error adding student: {e}")
                messagebox.showerror("Error", f"Error adding student: {e}")
                return

    #EDITAR ESTUDIANTE
    def editar_estudiante(self):
        if self.form_editar_estudiante:
            # Get datos form
            cedula_Est = self.form_editar_estudiante.entry_cedula_Est.get()
            nombre = self.form_editar_estudiante.entry_nombre.get()
            edad = self.form_editar_estudiante.entry_edad.get()
            id_grupo = self.form_editar_estudiante.entry_id_grupo.get()
            correo = self.form_editar_estudiante.entry_correo.get()

            # NOT NULL
            if not cedula_Est or not nombre or not edad or not id_grupo or not correo:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            # IF NOT EXISTS
            if not estudiantesColeccion.find_one({"cedula_Est": cedula_Est}):
                messagebox.showwarning("Advertencia", f"La cédula '{cedula_Est}' no existe.")
                return

            estudiantesColeccion.update_one(
                {"cedula_Est": cedula_Est},
                {"$set": {"nombre": nombre, "edad": edad, "id_grupo": id_grupo, "correo": correo}},
            )

            messagebox.showinfo("Éxito", "Se modificó correctamente al estudiante.")

            # Cerrar ventana gestión
            self.master.destroy()

            if self.form_editar_estudiante.master.winfo_exists():
                self.form_editar_estudiante.master.destroy()


    # ELIMINAR ESTUDIANTE
    def eliminar_estudiante(self, cedula_Est):
        if self.form_eliminar_estudiante:
            # NOT NULL
            if not cedula_Est:
                messagebox.showwarning("Advertencia", "Por favor, ingresa la cédula del estudiante.")
                return

            # IF NOT EXISTS
            estudiante = estudiantesColeccion.find_one({"cedula_Est": cedula_Est})
            if not estudiante:
                messagebox.showwarning("Advertencia", f"No se encontró la cédula '{cedula_Est}'.")
                return

            estudiantesColeccion.delete_one({"cedula_Est": cedula_Est})
            messagebox.showinfo("Éxito", f"Se eliminó correctamente al estudiante con la cédula '{cedula_Est}'.")

            # Cerrar ventana gestión
            self.master.destroy()

            if self.form_eliminar_estudiante.master.winfo_exists():
                self.form_eliminar_estudiante.master.destroy()

# ---------------------------------------FORMULARIOS MATERIAS--------------------------------------- #
class FormularioAgregarMateria:

    def __init__(self, master, callback_agregar_registro):
        self.master = master
        self.master.title("Agregar nueva materia")

        window_width = 340 
        window_height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.label_nombre = ttk.Label(master, text="Nombre de la materia:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ttk.Entry(master)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_descripcion = ttk.Label(master, text="Descripcion de la materia:")
        self.label_descripcion.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_descripcion = ttk.Entry(master)
        self.entry_descripcion.grid(row=0, column=1, padx=10, pady=10)


        self.label_id_materia = ttk.Label(master, text="ID Materia:")
        self.label_id_materia.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_id_materia = ttk.Entry(master)
        self.entry_id_materia.grid(row=0, column=1, padx=10, pady=10)

        self.btn_agregar_materia = ttk.Button(master, text="Agregar materia", command=lambda:
        [callback_agregar_registro(), master.destroy()])
        self.btn_agregar_materia.grid(row=5, column=0, columnspan=2, pady=10)

class FormularioActualizarMateria:

    def __init__(self, master, descripcion, nombre, id_materia, callback_editar):
        self.master = master
        self.master.title("Editar Registro de Asistencia")
    
        window_width = 340
        window_height = 350
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.label_nombre = ttk.Label(master, text="Nombre de la materia:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = ttk.Entry(master)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)


        self.label_descripcion = ttk.Label(master, text="Descripcion:")
        self.label_descripcion.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_descripcion_valor = ttk.Label(master, text=descripcion)
        self.label_descripcion_valor.grid(row=1, column=1, padx=10, pady=10)


        self.label_id_materia = ttk.Label(master, text="ID Materia:")
        self.label_id_materia.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.label_id_materia_valor = ttk.Label(master, text=id_materia)
        self.label_id_materia_valor.grid(row=2, column=1, padx=10, pady=10)


        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_editar_registro = ttk.Button(self.button_frame, text="Actualizar materia", command=lambda: [callback_editar(), master.destroy()])
        self.btn_editar_registro.grid(row=0, column=0) 
        self.btn_editar_registro.config(width=15)  

class FormularioEliminarMateria:

    def __init__(self, master, callback_eliminar):
        self.master = master
        self.master.title("Eliminar Materia")

        window_width = 300
        window_height = 150
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")


        self.label_id_materia = ttk.Label(master, text="ID Materia:")
        self.label_id_materia.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_materia = ttk.Entry(master)
        self.entry_id_materia.grid(row=0, column=1, padx=10, pady=10)

        #Button Volver
        self.btn_agregar = ttk.Button(master, text="Volver", command=lambda: [master.destroy()])
        self.btn_agregar.grid(row=1, column=0, columnspan=1, pady=10)

        #Button Eliminar
        self.btn_eliminar = ttk.Button(master, text="Eliminar", command=lambda: [callback_eliminar(self.entry_cedula_Est.get()), master.destroy()])
        self.btn_eliminar.grid(row=1, column=1, columnspan=2, pady=10)

class VentanaGestionMaterias:
    
    def __init__(self, master, interfaz_grafica):
        self.master = master
        self.interfaz_grafica=interfaz_grafica

        self.master.title("Gestión de materias")

        self.master.geometry("400x200")

        widthScreen = root.winfo_screenwidth()
        heightScreen = root.winfo_screenheight()

        x_pos = (widthScreen - 400) // 2
        y_pos = (heightScreen - 200) // 2
        self.master.geometry(f"400x200+{x_pos}+{y_pos}")

        self.label_titulo = tk.Label(master, text="Gestión de materias", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        #Agregar materia
        self.btn_agregar_materia = tk.Button(master, text="Agregar materia", command=self.mostrar_form_agregar_materia)
        self.btn_agregar_materia.pack(pady=10)

        #Actualizar materia
        self.btn_editar_materia = tk.Button(master, text="Actualizar materia", command=self.mostrar_form_editar_materia)
        self.btn_editar_materia.pack(pady=10)

        #Eliminar materia
        self.btn_eliminar_materia = tk.Button(master, text="Eliminar materia", command=self.mostrar_form_eliminar_materia)
        self.btn_eliminar_materia.pack(pady=10)



        self.form_agregar_materia = None
        self.form_editar_materia = None
        self.form_eliminar_materia = None

    def mostrar_form_agregar_materia(self):
        ventana_form_agregar_materia = tk.Toplevel(self.master)
        self.form_agregar_materia = FormularioAgregarMateria(
        ventana_form_agregar_materia, self.agregar_materia)
        ventana_form_agregar_materia.wait_window(ventana_form_agregar_materia)


    def mostrar_form_editar_materia(self):
        ventana_form_editar_materias = tk.Toplevel(self.master)
        self.form_editar_materias = FormularioActualizarMateria(ventana_form_editar_materias, self.editar_materias)
        ventana_form_editar_materias.wait_window(ventana_form_editar_materias)


    def mostrar_form_eliminar_materia(self):
        ventana_form_eliminar_materia = tk.Toplevel(self.master)
        self.form_eliminar_materia = FormularioEliminarMateria(ventana_form_eliminar_materia, self.eliminar_materia)


    def agregar_materia(self):
        if self.form_agregar_materia:
            # Get
            id_materia =self.form_agregar_materia.entry_id_materia.get()
            nombre = self.form_agregar_materia.entry_nombre.get()
            descripcion = self.form_agregar_materia.entry_descripcion.get()

            # No null
            if not id_materia or not nombre or not descripcion:
                messagebox.showwarning("Por favor, complete todos los campos.")
                return
            
            #Revisar Id materia
            if materiasColeccion.find_one({"id_materia": id_materia}):
                messagebox.showwarning(
                    "Advertencia", f"El id '{id_materia}' ya existe. Por favor, elige otro."
                )
                return

            estudiante = {
                "id_materia": id_materia,
                "nombre": nombre,
                "descripcion": descripcion,
            }

            try:
                materiasColeccion.insert_one(id_materia) 
                print("Materia added successfully!")
                messagebox.showinfo("Éxito", "Se ingresó correctamente.")


                #Cerrar ventana gestión
                self.master.destroy() 

                if self.form_agregar_materia.master.winfo_exists():
                    self.form_agregar_materia.master.destroy()

            except Exception as e:
                print(f"Error adding materia: {e}")
                messagebox.showerror("Error", f"Error adding materia: {e}")
                return

    def editar_materia(self):
        if self.form_editar:
            # Get
            id_materia = self.form_editar_materia.entry_id_materia.get()
            nombre = self.form_editar_materia.entry_nombre.get()
            descripcion = self.form_editar_materia.entry_descripcion.get()

            # No null
            if not id_materia or not nombre or not descripcion:
                messagebox.showwarning("Por favor, complete todos los campos.")
                return

            # If no existe
            if not materiasColeccion.find_one({"id_materia": id_materia}):
                messagebox.showwarning("El ID del anuncio '{id_materia}' no existe.")
            else:
                materiasColeccion.update_one({"id_materia": id_materia}, {"$set": {"nombre": nombre, "descripcion": descripcion}})
                messagebox.showinfo("Se modificó correctamente la materia.")

                #Cerrar ventana gestión
                self.master.destroy() 

                if self.form_editar_materia.master.winfo_exists():
                    self.form_editar_materia.master.destroy()


    def eliminar_materia(self, id_materia):
        if self.form_eliminar:
        # No null
            if not id_materia:
                messagebox.showwarning("Por favor, ingresa el ID de la materia.")
                self.master.deiconify() 
                self.master.lift()
                return

        # If no existe
        materia = materiasColeccion.find_one({"id_materia": id_materia})
        if not materia:
            messagebox.showwarning(f"No se encontró la materia con el ID '{id_materia}'.")
            self.master.deiconify() 
            self.master.lift() 
        else:
            materiasColeccion.delete_one({"id_materia": id_materia})
            messagebox.showinfo(f"Se eliminó correctamente la materia con el ID '{id_materia}'.")

            #Cerrar ventana gestión
            self.master.destroy() 

            if self.form_eliminar.master.winfo_exists():
                self.form_eliminar.master.destroy()
 
# ---------------------------------------FORMULARIOS GRUPOS--------------------------------------- #
class FormularioAgregarGrupo:

    def __init__(self, master, callback_agregar, callback_editar=None):
        self.master = master
        self.master.title("Agregar nuevo Grupo")

        window_width = 300 
        window_height = 200
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.label_id_grupo = ttk.Label(master, text="ID Grupo:")
        self.label_id_grupo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_grupo = ttk.Entry(master)
        self.entry_id_grupo.grid(row=0, column=1, padx=10, pady=10)

        self.label_nombre = ttk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = ttk.Entry(master)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.label_cantidad = ttk.Label(master, text="Cantidad:")
        self.label_cantidad.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_cantidad = ttk.Entry(master)
        self.entry_cantidad.grid(row=2, column=1, padx=10, pady=10)

        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_agregar = ttk.Button(self.button_frame, text="Agregar grupo", command=lambda: [callback_agregar(), master.destroy()])
        self.btn_agregar.grid(row=0, column=0)
        self.btn_agregar.config(width=15)

class FormularioActualizarGrupo:

    def __init__(self, master, callback_editar):
        self.master = master
        self.master.title("Actualizar Grupo")

        window_width = 300
        window_height = 200
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.label_id_grupo = ttk.Label(master, text="ID Geupo:")
        self.label_id_grupo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_grupo = ttk.Entry(master)
        self.entry_id_grupo.grid(row=0, column=1, padx=10, pady=10)

        self.label_nombre = ttk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = ttk.Entry(master)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.label_cantidad = ttk.Label(master, text="Cantidad:")
        self.label_cantidad.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_cantidad = ttk.Entry(master)
        self.entry_cantidad.grid(row=2, column=1, padx=10, pady=10)

        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_editar = ttk.Button(self.button_frame, text="Actualizar", command=lambda: [callback_editar(), master.destroy()])
        self.btn_editar.grid(row=0, column=0)
        self.btn_editar.config(width=15)

class FormularioEliminarGrupo:

    def __init__(self, master, callback_eliminar):
        self.master = master
        self.master.title("EliminarGrupo")

        window_width = 300
        window_height = 150
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.label_id_grupo = ttk.Label(master, text="ID Grupo:")
        self.label_id_grupo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_id_grupo = ttk.Entry(master)
        self.entry_id_grupo.grid(row=0, column=1, padx=10, pady=10)

        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_eliminar = ttk.Button(self.button_frame, text="Eliminar Grupo", command=lambda: [callback_eliminar(self.entry_id_grupo.get()), master.destroy()])
        self.btn_eliminar.grid(row=0, column=0)
        self.btn_eliminar.config(width=15)

class VentanaGestionGrupo:
    
    def __init__(self, master, interfaz_grafica):
        self.master = master
        self.interfaz_grafica=interfaz_grafica

        self.master.title("Gestión de Grupos")

        self.master.geometry("400x200")

        widthScreen = root.winfo_screenwidth()
        heightScreen = root.winfo_screenheight()

        x_pos = (widthScreen - 400) // 2
        y_pos = (heightScreen - 200) // 2
        self.master.geometry(f"400x200+{x_pos}+{y_pos}")

        self.label_titulo = tk.Label(master, text="Gestión de Grupos", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        #AGREGAR GRUPO
        self.btn_agregar_estudiante = tk.Button(master, text="Agregar Grupo", command=self.mostrar_form_agregar_grupo)
        self.btn_agregar_estudiante.pack(pady=10)

        #EDITAR GRUPO
        self.btn_editar_grupo = tk.Button(master, text="Editar Grupo", command=self.mostrar_form_editar_grupo)
        self.btn_editar_grupo.pack(pady=10)

        #ELIMINAR GRUPO
        self.btn_eliminar_grupo = tk.Button(master, text="Eliminar Grupo", command=self.mostrar_form_eliminar_grupo)
        self.btn_eliminar_grupo.pack(pady=10)

        self.form_agregar_grupo = None
        self.form_editar_grupo = None
        self.form_eliminar_grupo = None 

    def mostrar_form_agregar_grupo(self):
        ventana_form_agregar_grupo = tk.Toplevel(self.master)
        self.form_agregar_grupo = FormularioAgregarGrupo(
        ventana_form_agregar_grupo, self.agregar_estudiante)
        ventana_form_agregar_grupo.wait_window(ventana_form_agregar_grupo)

    def mostrar_form_editar_grupo(self):
        ventana_form_editar_grupo = tk.Toplevel(self.master)
        self.form_editar_grupo = FormularioActualizarGrupo(ventana_form_editar_grupo, self.editar_grupo)
        ventana_form_editar_grupo.wait_window(ventana_form_editar_grupo)

    def mostrar_form_eliminar_grupo(self):
        ventana_form_eliminar_grupo = tk.Toplevel(self.master)
        self.form_eliminar_grupo = FormularioEliminarGrupo(ventana_form_eliminar_grupo, self.eliminar_grupo)

    #AGREGAR GRUPO
    def agregar_grupo(self):
        print("Adding group...")
        if self.form_agregar_grupo:
            # Get datos form
            nombre = self.form_agregar_grupo.entry_nombre.get()
            cantidad = self.form_agregar_grupo.entry_cantidad.get()
            id_grupo = self.form_agregar_grupo.entry_id_grupo.get()

            # NOT NULL
            if not nombre or not cantidad or not id_grupo:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            # Check id
            if gruposColeccion.find_one({"id_grupo": id_grupo}):
                messagebox.showwarning(
                    "Advertencia", f"El id '{id_grupo}' ya existe. Por favor, elige otra."
                )
                return

            grupo = {
                "nombre": nombre,
                "cantidad": cantidad,
                "id_grupo": id_grupo
            }

            try:
                gruposColeccion.insert_one(grupo)
                print("Group added successfully!")
                messagebox.showinfo("Éxito", "Se ingresó correctamente.")

                # Cerrar ventana gestión
                self.master.destroy()

                if self.form_agregar_grupo.master.winfo_exists():
                    self.form_agregar_grupo.master.destroy()
            except Exception as e:
                print(f"Error adding group: {e}")
                messagebox.showerror("Error", f"Error adding group: {e}")
                return

    #EDITAR GRUPO
    def editar_grupo(self):
        if self.form_editar_grupo:
            # Get datos form
            nombre = self.form_editar_grupo.entry_nombre.get()
            cantidad = self.form_editar_grupo.entry_cantidad.get()
            id_grupo = self.form_editar_grupo.entry_id_grupo.get()

            # NOT NULL
            if not nombre or not cantidad or not id_grupo:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            # IF NOT EXISTS
            if not gruposColeccion.find_one({"id_grupo": id_grupo}):
                messagebox.showwarning("Advertencia", f"El id '{id_grupo}' no existe.")
                return

            gruposColeccion.update_one(
                {"id_grupo": id_grupo},
                {"$set": {"nombre": nombre, "cantidad": cantidad, "id_grupo": id_grupo}},
            )

            messagebox.showinfo("Éxito", "Se modificó correctamente.")

            # Cerrar ventana gestión
            self.master.destroy()

            if self.form_editar_grupo.master.winfo_exists():
                self.form_editar_grupo.master.destroy()


    # ELIMINAR GRUPO
    def eliminar_grupo(self, id_grupo):
        if self.form_eliminar_estudiante:
            # NOT NULL
            if not id_grupo:
                messagebox.showwarning("Advertencia", "Por favor, ingresa el id del grupo.")
                return

            # IF NOT EXISTS
            grupo = gruposColeccion.find_one({"id_grupo": id_grupo})
            if not grupo:
                messagebox.showwarning("Advertencia", f"No se encontró el id del grupo '{id_grupo}'.")
                return

            gruposColeccion.delete_one({"id_grupo": id_grupo})
            messagebox.showinfo("Éxito", f"Se eliminó correctamente el grupo con el id '{id_grupo}'.")

            # Cerrar ventana gestión
            self.master.destroy()

            if self.form_eliminar_grupo.master.winfo_exists():
                self.form_eliminar_grupo.master.destroy()

# ---------------------------------------FORMULARIOS PROFESORES--------------------------------------- #
class FormularioAgregarProfesor:

    def __init__(self, master, callback_agregar):
        self.master = master
        self.master.title("Agregar Profesor")

        window_width = 380
        window_height = 240
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        #Datos ComboBox
        id_materias = self.get_id_materias()

        # CEDULA_PROF
        self.label_cedula_Prof = ttk.Label(master, text="Cédula del Profesor:")
        self.label_cedula_Prof.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_cedula_Prof = ttk.Entry(master)
        self.entry_cedula_Prof.grid(row=0, column=1, padx=10, pady=10)
        # NOMBRE
        self.label_nombre = ttk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = ttk.Entry(master)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)
        # MATERIAS
        self.label_id_materia = ttk.Label(master, text="ID Materia:")
        self.label_id_materia.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.combo_id_materia = ttk.Combobox(master, values=id_materias)
        self.combo_id_materia.grid(row=2, column=1, padx=10, pady=10)
        # CORREO
        self.label_correo = ttk.Label(master, text="Correo Electrónico:")
        self.label_correo.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_correo = ttk.Entry(master)
        self.entry_correo.grid(row=3, column=1, padx=10, pady=10)

        # Button Volver
        self.btn_volver = ttk.Button(master, text="Volver", command=lambda: [master.destroy()])
        self.btn_volver.grid(row=4, column=0, columnspan=1, pady=10)

        # Button Agregar
        self.btn_agregar = ttk.Button(master, text="Agregar", command=lambda: [callback_agregar(), master.destroy()])
        self.btn_agregar.grid(row=4, column=1, columnspan=2, pady=10)

    def get_id_materias(self):
        id_materias = materiasColeccion.distinct("id_materia")
        return id_materias

class FormularioEditarProfesor:

    def __init__(self, master, callback_editar):
        self.master = master
        self.master.title("Editar Profesor")

        window_width = 380
        window_height = 240
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        #Datos ComboBox
        id_materias = self.get_id_materias()

        # CEDULA_PROF
        self.label_cedula_Prof = ttk.Label(master, text="Cédula del Profesor:")
        self.label_cedula_Prof.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_cedula_Prof = ttk.Entry(master)
        self.entry_cedula_Prof.grid(row=0, column=1, padx=10, pady=10)

        # NOMBRE
        self.label_nombre = ttk.Label(master, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = ttk.Entry(master)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        # MATERIAS
        self.label_id_materia = ttk.Label(master, text="ID Materia:")
        self.label_id_materia.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.combo_id_materia = ttk.Combobox(master, values=id_materias)
        self.combo_id_materia.grid(row=2, column=1, padx=10, pady=10)

        # CORREO
        self.label_correo = ttk.Label(master, text="Correo Electrónico:")
        self.label_correo.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_correo = ttk.Entry(master)
        self.entry_correo.grid(row=3, column=1, padx=10, pady=10)

        # Button Volver
        self.btn_volver = ttk.Button(master, text="Volver", command=lambda: [master.destroy()])
        self.btn_volver.grid(row=4, column=0, columnspan=1, pady=10)

        # Button Editar
        self.btn_editar = ttk.Button(master, text="Editar", command=lambda: [callback_editar(), master.destroy()])
        self.btn_editar.grid(row=4, column=1, columnspan=2, pady=10)

    def get_id_materias(self):
        id_materias = materiasColeccion.distinct("id_materia")
        return id_materias

class FormularioEliminarProfesor:

    def __init__(self, master, callback_eliminar):
        self.master = master
        self.master.title("Eliminar Profesor")

        window_width = 370
        window_height = 100
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        # CEDULA_PROF
        self.label_cedula_Prof = ttk.Label(master, text="Cédula del Profesor:")
        self.label_cedula_Prof.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_cedula_Prof = ttk.Entry(master)
        self.entry_cedula_Prof.grid(row=0, column=1, padx=10, pady=5)

        # Button Volver
        self.btn_volver = ttk.Button(master, text="Volver", command=lambda: [master.destroy()])
        self.btn_volver.grid(row=1, column=0, columnspan=1, pady=10)

        # Button Eliminar
        self.btn_eliminar = ttk.Button(master, text="Eliminar", command=lambda: [callback_eliminar(self.entry_cedula_Prof.get()), master.destroy()])
        self.btn_eliminar.grid(row=1, column=1, columnspan=2, pady=10)

class VentanaGestionProfesores:

    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Profesores")
        self.master.geometry("400x200")

        width_screen = master.winfo_screenwidth()
        height_screen = master.winfo_screenheight()

        x_pos = (width_screen - 400) // 2
        y_pos = (height_screen - 200) // 2
        self.master.geometry(f"400x200+{x_pos}+{y_pos}")

        self.label_titulo = tk.Label(master, text="Gestión de Profesores", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # AGREGAR PROFESOR
        self.btn_agregar_profesor = tk.Button(master, text="Agregar Profesor", command=self.mostrar_form_agregar_profesor)
        self.btn_agregar_profesor.pack(pady=10)

        # EDITAR PROFESOR
        self.btn_editar_profesor = tk.Button(master, text="Editar Profesor", command=self.mostrar_form_editar_profesor)
        self.btn_editar_profesor.pack(pady=10)

        # ELIMINAR PROFESOR
        self.btn_eliminar_profesor = tk.Button(master, text="Eliminar Profesor", command=self.mostrar_form_eliminar_profesor)
        self.btn_eliminar_profesor.pack(pady=10)

        self.form_agregar_profesor = None
        self.form_editar_profesor = None
        self.form_eliminar_profesor = None

    def mostrar_form_agregar_profesor(self):
        ventana_form_agregar_profesor = tk.Toplevel(self.master)
        self.form_agregar_profesor = FormularioAgregarProfesor(
            ventana_form_agregar_profesor, self.agregar_profesor)
        ventana_form_agregar_profesor.wait_window(ventana_form_agregar_profesor)

    def mostrar_form_editar_profesor(self):
        ventana_form_editar_profesor = tk.Toplevel(self.master)
        self.form_editar_profesor = FormularioEditarProfesor(
            ventana_form_editar_profesor, self.editar_profesor)
        ventana_form_editar_profesor.wait_window(ventana_form_editar_profesor)

    def mostrar_form_eliminar_profesor(self):
        ventana_form_eliminar_profesor = tk.Toplevel(self.master)
        self.form_eliminar_profesor = FormularioEliminarProfesor(
            ventana_form_eliminar_profesor, self.eliminar_profesor)

    # AGREGAR PROFESOR
    def agregar_profesor(self):
        print("Adding professor...")
        if self.form_agregar_profesor:
            # Get datos form
            cedula_Prof = self.form_agregar_profesor.entry_cedula_Prof.get()
            nombre = self.form_agregar_profesor.entry_nombre.get()
            id_materia = self.form_agregar_profesor.combo_id_materia.get()
            correo = self.form_agregar_profesor.entry_correo.get()

            # NOT NULL
            if not cedula_Prof or not nombre or not id_materia or not correo:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            # Check cedula profesor
            if profesoresColeccion.find_one({"cedula_Prof": cedula_Prof}):
                messagebox.showwarning(
                    "Advertencia", f"La cédula '{cedula_Prof}' ya existe. Por favor, elige otra."
                )
                return

            profesor = {
                "cedula_Prof": cedula_Prof,
                "nombre": nombre,
                "id_materia": id_materia,
                "correo": correo,
            }

            try:
                profesoresColeccion.insert_one(profesor)
                print("Professor added successfully!")
                messagebox.showinfo("Éxito", "Se ingresó correctamente al profesor.")

                # Cerrar ventana gestión
                self.master.destroy()

                if self.form_agregar_profesor.master.winfo_exists():
                    self.form_agregar_profesor.master.destroy()
            except Exception as e:
                print(f"Error adding professor: {e}")
                messagebox.showerror("Error", f"Error adding professor: {e}")
                return

    # EDITAR PROFESOR
    def editar_profesor(self):
        if self.form_editar_profesor:
            # Get datos form
            cedula_Prof = self.form_editar_profesor.entry_cedula_Prof.get()
            nombre = self.form_editar_profesor.entry_nombre.get()
            id_materia = self.form_editar_profesor.combo_id_materia.get()
            correo = self.form_editar_profesor.entry_correo.get()

            # NOT NULL
            if not cedula_Prof or not nombre or not id_materia or not correo:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            # Check if the professor exists
            if not profesoresColeccion.find_one({"cedula_Prof": cedula_Prof}):
                messagebox.showwarning("Advertencia", f"La cédula '{cedula_Prof}' no existe.")
                return

            profesoresColeccion.update_one(
                {"cedula_Prof": cedula_Prof},
                {"$set": {"nombre": nombre, "id_materia": id_materia, "correo": correo}},
            )

            messagebox.showinfo("Éxito", "Se modificó correctamente al profesor.")

            # Cerrar ventana gestión
            self.master.destroy()

            if self.form_editar_estudiante.master.winfo_exists():
                self.form_editar_estudiante.master.destroy()

    # ELIMINAR PROFESOR
    def eliminar_profesor(self, cedula_Prof):
        if self.form_eliminar_profesor:
            # Get datos form
            cedula_Prof = self.form_eliminar_profesor.entry_cedula_Prof.get()

            # NOT NULL
            if not cedula_Prof:
                messagebox.showwarning("Advertencia", "Por favor, ingresa la cédula del profesor.")
                return

            # IF NOT EXISTS
            profesor = profesoresColeccion.find_one({"cedula_Prof": cedula_Prof})
            if not profesor:
                messagebox.showwarning("Advertencia", f"No se encontró la cédula '{cedula_Prof}'.")
                return

            profesoresColeccion.delete_one({"cedula_Prof": cedula_Prof})
            messagebox.showinfo("Éxito", f"Se eliminó correctamente al profesor con la cédula '{cedula_Prof}'.")

            # Cerrar ventana gestión
            self.master.destroy()

            if self.form_eliminar_profesor.master.winfo_exists():
                self.form_eliminar_profesor.master.destroy()
# ---------------------------------------INTERFAZ GRAFICA--------------------------------------- #
class InterfazGrafica:

    def __init__(self, master):
        self.master = master
        self.master.title("Gestión Centro Educativo")

        self.label_titulo = tk.Label(master, text="Anuncios del Centro Educativo", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # ---------------------------------------SHOW ANUNCIOS--------------------------------------- #
        self.text_anuncios = tk.Text(master, wrap=tk.WORD, height=10, width=60, state=tk.DISABLED)
        self.text_anuncios.pack(padx=10, pady=10)

        self.frame_botones_gestion = tk.Frame(master)
        self.frame_botones_gestion.pack(pady=10)

        # ---------------------------------------BOTONES DE GESTION--------------------------------------- #
        # Button Estudiantes
        self.btn_gestion_anuncios = tk.Button(master, text="Gestionar Estudiantes", command=self.abrir_ventana_gestion_estudiantes)
        self.btn_gestion_anuncios.pack(pady=10, padx=10)

        # Button Profesores
        self.btn_gestion_profesores = tk.Button(master, text="Gestionar Profesores", command=self.abrir_ventana_gestion_profesores)
        self.btn_gestion_profesores.pack(pady=10, padx=10)

        # Button Anuncios
        self.btn_gestion_anuncios = tk.Button(self.frame_botones_gestion, text="Gestionar Anuncios", command=self.abrir_ventana_gestion_anuncios)
        self.btn_gestion_anuncios.pack(side=tk.LEFT, padx=5)

        self.form_seleccion_grupo = None  

        # Button Anuncios
        self.btn_gestion_asistencia = tk.Button(self.frame_botones_gestion, text="Gestionar Asistencia", command=self.abrir_ventana_seleccion_grupo)
        self.btn_gestion_asistencia.pack(side=tk.LEFT, padx=5)

        self.cargar_anuncios()
    # ---------------------------------------MOSTRAR ANUNCIOS--------------------------------------- #
    def cargar_anuncios(self):
        self.text_anuncios.config(state=tk.NORMAL)  
        self.text_anuncios.delete(1.0, tk.END)

        # ---------------------------------------GET ANUNCIOS--------------------------------------- #
        anuncios = anunciosColeccion.find()

        for anuncio in anuncios:
            contenido_anuncio = f"{anuncio['id_anuncios']}. {anuncio['titulo']} - {anuncio['contenido']}\n\n"
            self.text_anuncios.insert(tk.END, contenido_anuncio)

        self.text_anuncios.config(state=tk.DISABLED)  
        self.text_anuncios.config(font=("Arial", 12), fg="black")

    # ---------------------------------------DATOS ASISTENCIA--------------------------------------- #
    def obtener_datos_asistencia(self, grupo_seleccionado, id_grupo_seleccionado):
     #Depende del nombre del grupo, traigo el Id
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
                'asistio': "Sí" if registro['asistio'] else "No"
            }
            datos_asistencia.append(datos_registro)

        return datos_asistencia
     else:
        print("No se ha seleccionado un grupo.")
        return []
    
    # ---------------------------------------VENTANA GESTION ANUNCIOS--------------------------------------- #
    def abrir_ventana_gestion_anuncios(self):
        if hasattr(self, 'ventana_gestion_anuncios') and self.ventana_gestion_anuncios.winfo_exists():
            self.ventana_gestion_anuncios.lift()
        else:
            self.ventana_gestion_anuncios = tk.Toplevel(self.master)
            app_gestion_anuncios = VentanaGestionAnuncios(self.ventana_gestion_anuncios, self)

    # ---------------------------------------SELECCION DE GRUPO--------------------------------------- #
    def abrir_ventana_seleccion_grupo(self):
       if self.form_seleccion_grupo and self.form_seleccion_grupo.master.winfo_exists():
        self.form_seleccion_grupo.master.lift()
       else:
        ventana_seleccion_grupo = tk.Toplevel(self.master)
        self.form_seleccion_grupo = VentanaSeleccionGrupo(ventana_seleccion_grupo, self.abrir_ventana_gestion_asistencia)
        ventana_seleccion_grupo.wait_window(ventana_seleccion_grupo)

    # ---------------------------------------VENTANA GESTION ASISTENCIA--------------------------------------- #
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

    # ---------------------------------------VENTANA GESTION ESTUDIANTES--------------------------------------- #
    def abrir_ventana_gestion_estudiantes(self):
        if hasattr(self, 'ventana_gestion_estudiantes') and self.ventana_gestion_estudiantes.winfo_exists():
            self.ventana_gestion_estudiantes.lift()
        else:
            self.ventana_gestion_estudiantes = tk.Toplevel(self.master)
            app_gestion_estudiantes = VentanaGestionEstudiantes(self.ventana_gestion_estudiantes, self)

    # ---------------------------------------VENTANA GESTION PROFESORES--------------------------------------- #
    def abrir_ventana_gestion_profesores(self):
        if hasattr(self, 'ventana_gestion_profesores') and self.ventana_gestion_profesores.winfo_exists():
            self.ventana_gestion_profesores.lift()
        else:
            self.ventana_gestion_profesores = tk.Toplevel(self.master)
            app_gestion_profesores = VentanaGestionProfesores(self.ventana_gestion_profesores)

    # ---------------------------------------VENTANA GESTION MATERIAS--------------------------------------- #
    def abrir_ventana_gestion_materias(self):
        if hasattr(self, 'ventana_gestion_materias') and self.ventana_gestion_materias.winfo_exists():
            self.ventana_gestion_materias.lift()
        else:
            self.ventana_gestion_materias = tk.Toplevel(self.master)
            app_gestion_materias = VentanaGestionMaterias(self.ventana_gestion_materias, self)


     # ---------------------------------------VENTANA GESTION GRUPOS--------------------------------------- #

    def abrir_ventana_gestion_grupo(self):
        if hasattr(self, 'ventana_gestion_grupo') and self.ventana_gestion_grupo.winfo_exists():
            self.ventana_gestion_grupo.lift()
        else:
            self.ventana_gestion_grupo = tk.Toplevel(self.master)
            app_gestion_grupos = VentanaGestionGrupo(self.ventana_gestion_grupo, self)

# ---------------------------------------MAIN WINDOW--------------------------------------- #
root = tk.Tk()

widthScreen = root.winfo_screenwidth()
heightScreen = root.winfo_screenheight()

pos_x = (widthScreen - 1200) // 2
pos_y = (heightScreen - 600) // 2

root.geometry("1200x600+{}+{}".format(pos_x, pos_y))
app = InterfazGrafica(root)

root.mainloop()
client.close()


