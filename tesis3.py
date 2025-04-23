# Tesis Ary
import tkinter as tk
from tkinter import ttk, messagebox

sum_p_i = None
# Ejemplo general para abrir una nueva ventana
def abrir_ventana(titulo):
    """Crea una nueva ventana con el título especificado"""
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title(titulo)
    nueva_ventana.geometry("800x400")
    # Añadir validación al cerrar esta ventana secundaria
    def on_closing_child():
        if messagebox.askyesno("Confirmar cierre", f"¿Cerrar ventana de {titulo}?", parent=nueva_ventana):
            nueva_ventana.destroy()
    
    nueva_ventana.protocol("WM_DELETE_WINDOW", on_closing_child)
    label = ttk.Label(nueva_ventana, text=f"Ventana de {titulo}")
    label.pack(pady=50)
"""    
def ayuda_para_comenzar(titulo):
    messagebox.showinfo(titulo, "Esta ventana aun esta en construcción", parent=root)
"""
def ayuda_para_comenzar():
    # Crear una nueva ventana emergente
    ventana_explicacion = tk.Toplevel(root)
    ventana_explicacion.title("Explicación")
    ventana_explicacion.geometry("1200x400")

    # Crear un widget Text para mostrar el contenido
    texto = tk.Text(ventana_explicacion, wrap=tk.WORD)
    
    # Crear una barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(ventana_explicacion, orient=tk.VERTICAL, command=texto.yview)
    
    # Conectar la barra de desplazamiento con el widget Text
    texto.configure(yscrollcommand=scrollbar.set)

    # Posicionar el widget Text y la barra de desplazamiento en la ventana
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Insertar el texto de explicación
    explicacion = """Para comenzar debe conocer que este programa es version Free para conocer las diferentes versiones puede ir al menu--> informacion--> ayuda.
   
    - Punto 1: Debe comenzar a calcular las operaciones de las perdidas indirectas y suplementarias,pues las perdidas directas y totales dependen de valores de las indirectas.
    - Punto 2: No usar comas(,) para teclear numeros fraccionarios en lugar de esto utilizar punto(.).
    - Punto 3: Guiese para identificar las nomensclaturas por las leyendas de cada ventana de operaciones.
    - Punto 4: Para una mayor profundidad de detalles y explicaciones ir  al menu--> informacion--> Ayuda.
    - Punto 5: Esta ventana aun esta en construccion.

    
    - Punto 6: Explicación detallada del sexto aspecto.
    - Punto 7: Explicación detallada del séptimo aspecto.
    - Punto 8: Explicación detallada del octavo aspecto.
    - Punto 9: Explicación detallada del noveno aspecto.
    - Punto 10: Explicación detallada del décimo aspecto.
    """
    texto.insert(tk.END, explicacion)
    texto.config(state=tk.DISABLED)  # Hacer el texto de solo lectura

def abrir_ventana_ayuda():
    # Crear una nueva ventana emergente
    ventana_ayuda = tk.Toplevel(root)
    ventana_ayuda.title("Ayuda")
    ventana_ayuda.geometry("1200x400")

    # Crear un widget Text para mostrar el contenido
    texto = tk.Text(ventana_ayuda, wrap=tk.WORD)
    
    # Crear una barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(ventana_ayuda, orient=tk.VERTICAL, command=texto.yview)
    
    # Conectar la barra de desplazamiento con el widget Text
    texto.configure(yscrollcommand=scrollbar.set)

    # Posicionar el widget Text y la barra de desplazamiento en la ventana
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Insertar el texto de explicación
    ayuda_explicacion = """Este programa es la version Free, a fecha de hoy 5 de marzo del 2025 se esta elaborando la Version Pro la cual contendra las siguientes opciones:

    - Opcion 1: Guardar los datos para posteriormente poder consultarlos por filtros.
    - Opcion 2: Graficar las perdidas por intervalos de fechas.
    - Opcion 3: Ordenar en tablas los datos guardados. 
    - Opcion 4: Elegir entre diferentes normas (lib, kg ,metros, pulgadas etc...).
    - Opcion 5: Imprimir resultados.
    - Opcion 6: Otras opciones asi como toda la ventana ayuda aun esta en construccion.
    - Opcion 7: Puede contactar con los especialistas y el programador de esta aplicacion en menu--> informacion--> Acerca de:
    - Opcion 8: Explicación detallada del octavo aspecto.
    - Opcion 9: Explicación detallada del noveno aspecto.
    - Opcion 10: Explicación detallada del décimo aspecto.
    """
    texto.insert(tk.END, ayuda_explicacion)
    texto.config(state=tk.DISABLED)  # Hacer el texto de solo lectura        
    
#"""Funcion que abre la ventana para el calculo de perdidas indirectas y suplementarias"""    	    
def perdidas_indirectas(titulo):
    """Crea una nueva ventana con el título especificado"""
    ventana_perdidas_indirectas = tk.Toplevel(root)
    ventana_perdidas_indirectas.title(titulo)
    ventana_perdidas_indirectas.geometry("1350x670")
    ventana_perdidas_indirectas.configure(bg="#b3cac7")
    
    # Maximizar la ventana
    #ventana_perdidas_indirectas.wm_state('zoomed')
    
    
    
    ventana_perdidas_indirectas.columnconfigure(0, weight=0)  # Columna 0 NO se expande para luego poder alinear a la izquierda los frame de esa columna
    ventana_perdidas_indirectas.columnconfigure(1, weight=0)  # Columna 1 NO se expande , con weight=1 se expande y centra lo que tu pongas es mejor asi para luego con padx correlo 
    ventana_perdidas_indirectas.columnconfigure(2, weight=0)  # Columna 2 NO se expande 
    ventana_perdidas_indirectas.columnconfigure(3, weight=1)  # Columna 3 NO se expande , con weight=1 se expande y centra lo que tu pongas es mejor asi para luego con padx correlo 
    
    
    etiqueta_indirecta = tk.Label(
        ventana_perdidas_indirectas, 
        text="Cálculo para la estimación de las pérdidas de", 
        font=("Arial", 13,), 
        fg="#1A1A1A", 
        bg="#f1c5ef", 
        borderwidth=0, 
        relief="sunken"
    )
    etiqueta_indirecta.grid(row=0, column=1, sticky="e", pady=5)  # Con sticky="nsew" se alinea el marco en el centro
    
    etiqueta_indirecta1 = tk.Label(
        ventana_perdidas_indirectas, 
        text=" vapor indirectas y suplementarias", 
        font=("Arial", 13,), 
        fg="#1A1A1A", 
        bg="#f1c5ef", 
        borderwidth=0, 
        relief="sunken"
    )
    etiqueta_indirecta1.grid(row=0, column=2, sticky="w", pady=5)  # Con sticky="nsew" se alinea el marco en el centro
   
    etiqueta_tuberias_equipos = tk.Label(ventana_perdidas_indirectas, text="--------Pérdidas en tuberias y equipos------------", font=("Arial", 12,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_tuberias_equipos.grid(row=1, column=1, sticky="w", padx=(0,0), pady=(10,5))

    etiqueta_leyenda_pindirecta = tk.Label(ventana_perdidas_indirectas, text="Leyenda:", font=("Arial", 12,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_leyenda_pindirecta.grid(row=5, column=1, sticky="w", padx=(40,0), pady=(10,5))

    

    #etiqueta_leyenda_pindirecta1 = tk.Label(ventana_perdidas_indirectas, text="-------Leyenda------------------------------------------------", font=("Arial", 12,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    #etiqueta_leyenda_pindirecta1.grid(row=5, column=2, sticky="e", padx=(0,0), pady=(10,5))
    

    etiqueta_perdida_evaporacion = tk.Label(ventana_perdidas_indirectas, text="-----------Pérdida por evaporación------------", font=("Arial", 12,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_perdida_evaporacion.grid(row=1, column=3, sticky="w", padx=(45,10), pady=(10,5))
    
    etiqueta_superficie_vertical = tk.Label(ventana_perdidas_indirectas, text="Superficie vertical planas y cilíndricas", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_superficie_vertical.grid(row=2, column=0, sticky="w", padx=(50,0))
    
    etiqueta_superficie_horizontal_c = tk.Label(ventana_perdidas_indirectas, text="Superficie horizontal cilíndrica", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_superficie_horizontal_c.grid(row=2, column=1, sticky="w", padx=(65,0)) 
    
    etiqueta_superficie_horizontal_pa = tk.Label(ventana_perdidas_indirectas, text="Superficie horizontal planas hacia arriba ", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_superficie_horizontal_pa.grid(row=2, column=2, sticky="w", padx=(35,0)) 
    
    etiqueta_superficie_horizontal_pab = tk.Label(ventana_perdidas_indirectas, text="Superficie horizontal plana hacia abajo", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_superficie_horizontal_pab.grid(row=4, column=0, sticky="w", padx=(35,0), pady=(10,0))
    
    
   

    def calcular_sumatoria_c_r(Ws_texto, Ws1_texto, Ws2_texto, Ws3_texto, ΣWs_c_r_texto, l5_texto, l20_texto, l25_texto):
        try:
            valor_Ws_texto = float(Ws_texto.get("1.0", tk.END))
            valor_Ws1_texto = float(Ws1_texto.get("1.0", tk.END))
            valor_Ws2_texto = float(Ws2_texto.get("1.0", tk.END))
            valor_Ws3_texto = float(Ws3_texto.get("1.0", tk.END))
            
            resultado_ΣWs_c_r_texto = valor_Ws_texto + valor_Ws1_texto + valor_Ws2_texto + valor_Ws3_texto
            ΣWs_c_r_texto.config(state="normal")  # Habilitar temporalmente para editar
            ΣWs_c_r_texto.delete("1.0", tk.END)   # Borrar contenido previo
            ΣWs_c_r_texto.insert(tk.END, f"{resultado_ΣWs_c_r_texto}")
            ΣWs_c_r_texto.config(state="disabled") # Deshabilitar nuevamente

            resultado_l5_texto = resultado_ΣWs_c_r_texto * 1.15
            l5_texto.config(state="normal")  # Habilitar temporalmente para editar
            l5_texto.delete("1.0", tk.END)   # Borrar contenido previo
            l5_texto.insert(tk.END, f"{resultado_l5_texto}")
            l5_texto.config(state="disabled") # Deshabilitar nuevamente

            resultado_l20_texto = resultado_ΣWs_c_r_texto * 1.20
            l20_texto.config(state="normal")  # Habilitar temporalmente para editar
            l20_texto.delete("1.0", tk.END)   # Borrar contenido previo
            l20_texto.insert(tk.END, f"{resultado_l20_texto}")
            l20_texto.config(state="disabled") # Deshabilitar nuevamente

            resultado_l25_texto = resultado_ΣWs_c_r_texto * 1.25
            l25_texto.config(state="normal")  # Habilitar temporalmente para editar
            l25_texto.delete("1.0", tk.END)   # Borrar contenido previo
            l25_texto.insert(tk.END, f"{resultado_l25_texto}")
            l25_texto.config(state="disabled") # Deshabilitar nuevamente
            
        except ValueError:
            # Mostrar error en la caja de texto
            ΣWs_c_r_texto.config(state="normal")
            ΣWs_c_r_texto.delete("1.0", tk.END)
            ΣWs_c_r_texto.insert(tk.END, "Error: ")
            ΣWs_c_r_texto.config(state="disabled")
            messagebox.showerror("Error","Calcule todas las Ws(kg) de las pérdidas en tuberias y equipos",  parent=ventana_perdidas_indirectas)

    def calcular_sumatoria_p_i(Ws4_texto, ΣWs_p_i_texto, l20_texto):
        try:
            valor_Ws4_texto = float(Ws4_texto.get("1.0", tk.END))
            valor_l20_texto = float(l20_texto.get("1.0", tk.END))

            
            resultado_ΣWs_p_i_texto = valor_l20_texto + valor_Ws4_texto
            ΣWs_p_i_texto.config(state="normal")  # Habilitar temporalmente para editar
            ΣWs_p_i_texto.delete("1.0", tk.END)   # Borrar contenido previo
            ΣWs_p_i_texto.insert(tk.END, f"{resultado_ΣWs_p_i_texto}")
            ΣWs_p_i_texto.config(state="disabled") # Deshabilitar nuevamente
            # actualizo variable global
            global sum_p_i
            sum_p_i = resultado_ΣWs_p_i_texto
            

            
            
        except ValueError:
            # Mostrar error en la caja de texto
            ΣWs_p_i_texto.config(state="normal")
            ΣWs_p_i_texto.delete("1.0", tk.END)
            ΣWs_p_i_texto.insert(tk.END, "Error: ")
            ΣWs_p_i_texto.config(state="disabled")
            messagebox.showerror("Error","Calcule la ΣWs_c_r (kg) y Ws(kg) en las perdidas por evaporacion",  parent=ventana_perdidas_indirectas)
            
             
            
    
    
 
       
    def calcular_supvert_pc(Tw, Ta, A, d, L, λ, PV, Ɛ, σ, t, hc_texto, hr_texto, ha_texto, Qp_texto, Wsf_texto, Ws_texto):
        try:
            # Obtener valores de las cajas de texto
            valor_Tw = float(Tw.get())
            valor_Ta = float(Ta.get())
            valor_A = float(A.get())
            valor_d = float(d.get())
            valor_L = float(L.get())
            valor_λ = float(λ.get())
            valor_PV = float(PV.get())
            valor_Ɛ = float(Ɛ.get())
            valor_σ = float(σ.get())
            valor_t = float(t.get())
            
           
            # Realizar la operación (hc)
            resultado_hc = 1.42 * ((valor_Tw - valor_Ta) / valor_L) ** 0.25
            hc_texto.config(state="normal")  # Habilitar temporalmente para editar
            hc_texto.delete("1.0", tk.END)   # Borrar contenido previo
            hc_texto.insert(tk.END, f"{resultado_hc}")
            hc_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (hr)
            resultado_hr = valor_Ɛ * valor_σ * ((valor_Tw + valor_Ta) * ((valor_Tw ** 2) + (valor_Ta ** 2)))
            hr_texto.config(state="normal")  # Habilitar temporalmente para editar
            hr_texto.delete("1.0", tk.END)   # Borrar contenido previo
            hr_texto.insert(tk.END, f"{resultado_hr}")
            hr_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (ha)
            resultado_ha = resultado_hc + resultado_hr
            ha_texto.config(state="normal")  # Habilitar temporalmente para editar
            ha_texto.delete("1.0", tk.END)   # Borrar contenido previo
            ha_texto.insert(tk.END, f"{resultado_ha}")
            ha_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Qp)
            resultado_Qp = resultado_ha * valor_A * (valor_Tw - valor_Ta)
            Qp_texto.config(state="normal")  # Habilitar temporalmente para editar
            Qp_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Qp_texto.insert(tk.END, f"{resultado_Qp}")
            Qp_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Wsf)
            resultado_Wsf = (resultado_Qp * 3.6) / valor_λ
            Wsf_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wsf_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wsf_texto.insert(tk.END, f"{resultado_Wsf}")
            Wsf_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Ws)
            resultado_Ws = resultado_Wsf * valor_t
            Ws_texto.config(state="normal")  # Habilitar temporalmente para editar
            Ws_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Ws_texto.insert(tk.END, f"{resultado_Ws}")
            Ws_texto.config(state="disabled") # Deshabilitar nuevamente   
        
        except ValueError:
            # Mostrar error en la caja de texto
            hc_texto.config(state="normal")
            hc_texto.delete("1.0", tk.END)
            hc_texto.insert(tk.END, "Error: ")
            hc_texto.config(state="disabled")
            
            hr_texto.config(state="normal")
            hr_texto.delete("1.0", tk.END)
            hr_texto.insert(tk.END, "Error: ")
            hr_texto.config(state="disabled")
            
            ha_texto.config(state="normal")
            ha_texto.delete("1.0", tk.END)
            ha_texto.insert(tk.END, "Error: ")
            ha_texto.config(state="disabled")
            
            Qp_texto.config(state="normal")
            Qp_texto.delete("1.0", tk.END)
            Qp_texto.insert(tk.END, "Error: ")
            Qp_texto.config(state="disabled")
            
            Wsf_texto.config(state="normal")
            Wsf_texto.delete("1.0", tk.END)
            Wsf_texto.insert(tk.END, "Error: ")
            Wsf_texto.config(state="disabled")
            
            Ws_texto.config(state="normal")
            Ws_texto.delete("1.0", tk.END)
            Ws_texto.insert(tk.END, "Error: ")
            Ws_texto.config(state="disabled")
            
            messagebox.showerror("Error","Ingrese solo números y en todas las casillas y no use comas (,)",  parent=ventana_perdidas_indirectas)
            #Ws_texto.config(state="disabled")
   
    # Creamos el marco de Superficie Vertical planas y cilindricas
    marco_supvert_pc = tk.Frame(ventana_perdidas_indirectas, bg="#dae3f3", borderwidth=1, relief="sunken", width=315, height=270)
    marco_supvert_pc.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 4 columnas 
    marco_supvert_pc.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_supvert_pc.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_supvert_pc.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_supvert_pc.columnconfigure(3, weight=0)  # Columna 3 No se expande
    
    marco_supvert_pc.grid(row=3, column=0, sticky="w", padx=5, pady=1)  # Con sticky="w" se alinea el marco a la izquierda
   
    # Cajas de texto para entrada de datos
    tk.Label(marco_supvert_pc, text="Tw(K):").grid(row=0, column=0, sticky="w", padx=(10,1), pady=(5,2))
    Tw = tk.Entry(marco_supvert_pc, width=10)
    Tw.grid(row=0, column=1, sticky="w", pady=(5,2))
    
    tk.Label(marco_supvert_pc, text="Ta(K):").grid(row=1, column=0, sticky="w", padx=(10,1), pady=2)
    Ta = tk.Entry(marco_supvert_pc, width=10)
    Ta.grid(row=1, column=1, sticky="w", padx=1, pady=2)
   
    tk.Label(marco_supvert_pc, text="A(m²):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=2)
    A = tk.Entry(marco_supvert_pc, width=10)
    A.grid(row=2, column=1, sticky="w", padx=1, pady=2)
    
    
    tk.Label(marco_supvert_pc, text="dext(m):").grid(row=3, column=0, sticky="w", padx=(10,1), pady=2)
    d = tk.Entry(marco_supvert_pc, width=10)
    d.grid(row=3, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="L(m):").grid(row=4, column=0, sticky="w", padx=(10,1), pady=2)
    L = tk.Entry(marco_supvert_pc, width=10)
    L.grid(row=4, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="λv(kJ/kg):").grid(row=5, column=0, sticky="w", padx=(10,1), pady=2)
    λ = tk.Entry(marco_supvert_pc, width=10)
    λ.grid(row=5, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="PV (barG):").grid(row=6, column=0, sticky="w", padx=(10,1), pady=2) # poner en la leyenda Presión de vapor = PV
    PV = tk.Entry(marco_supvert_pc, width=10)
    PV.grid(row=6, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="Ɛ:").grid(row=7, column=0, sticky="w", padx=(10,1), pady=2)
    Ɛ = tk.Entry(marco_supvert_pc, width=10)
    Ɛ.grid(row=7, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="σ:").grid(row=8, column=0, sticky="w", padx=(10,1), pady=2)
    σ = tk.Entry(marco_supvert_pc, width=10)
    σ.grid(row=8, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="t (h)").grid(row=9, column=0, sticky="w", padx=(10,1), pady=2)
    t = tk.Entry(marco_supvert_pc, width=10)
    t.grid(row=9, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="hc(W/m² K):").grid(row=0, column=2, sticky="e", padx=(10,1), pady=(5,2))
    hc_texto = tk.Text(marco_supvert_pc, width=10, height=1, state="disabled")
    hc_texto.grid(row=0, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_supvert_pc, text="hr(W/m² K):").grid(row=1, column=2, sticky="e", padx=1, pady=2)
    hr_texto = tk.Text(marco_supvert_pc, width=10, height=1, state="disabled")
    hr_texto.grid(row=1, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="ha(W/m² K):").grid(row=2, column=2, sticky="e", padx=(10,1), pady=(5,2))
    ha_texto = tk.Text(marco_supvert_pc, width=10, height=1, state="disabled")
    ha_texto.grid(row=2, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_supvert_pc, text="Qp(W):").grid(row=3, column=2, sticky="e", padx=1, pady=2)
    Qp_texto = tk.Text(marco_supvert_pc, width=10, height=1, state="disabled")
    Qp_texto.grid(row=3, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_supvert_pc, text="Ws(kg/h):").grid(row=4, column=2, sticky="e", padx=(10,1), pady=(5,2))
    Wsf_texto = tk.Text(marco_supvert_pc, width=10, height=1, state="disabled")
    Wsf_texto.grid(row=4, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_supvert_pc, text="Ws(kg):").grid(row=5, column=2, sticky="e", padx=1, pady=2)
    Ws_texto = tk.Text(marco_supvert_pc, width=10, height=1, state="disabled")
    Ws_texto.grid(row=5, column=3, sticky="w", padx=1, pady=2)

   
    
   
    # Creo el botón calcular para las pérdidas por Superficie vertical planas y cilindricas
    boton_supvert_pc = tk.Button(marco_supvert_pc, text="Calcular", command=lambda: calcular_supvert_pc(Tw, Ta, A, d, L, λ, PV, Ɛ, σ, t, hc_texto, hr_texto, ha_texto, Qp_texto, Wsf_texto, Ws_texto))
    boton_supvert_pc.grid(row=9, column=3, sticky="w", padx=1, pady=2)
   
    
     
    # Funcion Calculo para Superficie horizontal (cilíndrica)
    def calcular_sup_horiz_c(Tw1, Ta1, A1, d1, L1, λ1, PV1, Ɛ1, σ1, t1, hc1_texto, hr1_texto, ha1_texto, Qp1_texto, Wsf1_texto, Ws1_texto):
        try:
            # Obtener valores de las cajas de texto
            valor_Tw1 = float(Tw1.get())
            valor_Ta1 = float(Ta1.get())
            valor_A1 = float(A1.get())
            valor_d1 = float(d1.get())
            valor_L1 = float(L1.get())
            valor_λ1 = float(λ1.get())
            valor_PV1 = float(PV1.get())
            valor_Ɛ1 = float(Ɛ1.get())
            valor_σ1 = float(σ1.get())
            valor_t1 = float(t1.get())
            
           
            # Realizar la operación (hc)
            resultado_hc1 = 1.32 * ((valor_Tw1 - valor_Ta1) / valor_d1) ** 0.25
            hc1_texto.config(state="normal")  # Habilitar temporalmente para editar
            hc1_texto.delete("1.0", tk.END)   # Borrar contenido previo
            hc1_texto.insert(tk.END, f"{resultado_hc1}")
            hc1_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (hr)
            resultado_hr1 = valor_Ɛ1 * valor_σ1 * ((valor_Tw1 + valor_Ta1) * ((valor_Tw1 ** 2) + (valor_Ta1 ** 2)))
            hr1_texto.config(state="normal")  # Habilitar temporalmente para editar
            hr1_texto.delete("1.0", tk.END)   # Borrar contenido previo
            hr1_texto.insert(tk.END, f"{resultado_hr1}")
            hr1_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (ha)
            resultado_ha1 = resultado_hc1 + resultado_hr1
            ha1_texto.config(state="normal")  # Habilitar temporalmente para editar
            ha1_texto.delete("1.0", tk.END)   # Borrar contenido previo
            ha1_texto.insert(tk.END, f"{resultado_ha1}")
            ha1_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Qp)
            resultado_Qp1 = resultado_ha1 * valor_A1 * (valor_Tw1 - valor_Ta1)
            Qp1_texto.config(state="normal")  # Habilitar temporalmente para editar
            Qp1_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Qp1_texto.insert(tk.END, f"{resultado_Qp1}")
            Qp1_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Wsf)
            resultado_Wsf1 = (resultado_Qp1 * 3.6) / valor_λ1
            Wsf1_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wsf1_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wsf1_texto.insert(tk.END, f"{resultado_Wsf1}")
            Wsf1_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Ws)
            resultado_Ws1 = resultado_Wsf1 * valor_t1
            Ws1_texto.config(state="normal")  # Habilitar temporalmente para editar
            Ws1_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Ws1_texto.insert(tk.END, f"{resultado_Ws1}")
            Ws1_texto.config(state="disabled") # Deshabilitar nuevamente   
        
        except ValueError:
            # Mostrar error en la caja de texto
            hc1_texto.config(state="normal")
            hc1_texto.delete("1.0", tk.END)
            hc1_texto.insert(tk.END, "Error: ")
            hc1_texto.config(state="disabled")
            
            hr1_texto.config(state="normal")
            hr1_texto.delete("1.0", tk.END)
            hr1_texto.insert(tk.END, "Error: ")
            hr1_texto.config(state="disabled")
            
            ha1_texto.config(state="normal")
            ha1_texto.delete("1.0", tk.END)
            ha1_texto.insert(tk.END, "Error: ")
            ha1_texto.config(state="disabled")
            
            Qp1_texto.config(state="normal")
            Qp1_texto.delete("1.0", tk.END)
            Qp1_texto.insert(tk.END, "Error: ")
            Qp1_texto.config(state="disabled")
            
            Wsf1_texto.config(state="normal")
            Wsf1_texto.delete("1.0", tk.END)
            Wsf1_texto.insert(tk.END, "Error: ")
            Wsf1_texto.config(state="disabled")
            
            Ws1_texto.config(state="normal")
            Ws1_texto.delete("1.0", tk.END)
            Ws1_texto.insert(tk.END, "Error: ")
            Ws1_texto.config(state="disabled")
            
            messagebox.showerror("Error","Ingrese solo números y en todas las casillas y no use comas (,)",  parent=ventana_perdidas_indirectas)
            #Ws1_texto.config(state="disabled")
    
    
    
    # Creamos el marco de Superficie horizontal (cilíndrica)
    marco_sup_horiz_c = tk.Frame(ventana_perdidas_indirectas, bg="#dae3f3", borderwidth=1, relief="sunken", width=315, height=270)
    marco_sup_horiz_c.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 4 columnas 
    marco_sup_horiz_c.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_sup_horiz_c.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_sup_horiz_c.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_sup_horiz_c.columnconfigure(3, weight=0)  # Columna 3 No se expande
    
    marco_sup_horiz_c.grid(row=3, column=1, sticky="w", padx=(5,0), pady=1)  # Con sticky="w" se alinea el marco a la izquierda
   
    
    
    # Cajas de texto para entrada de datos
    tk.Label(marco_sup_horiz_c, text="Tw(K):").grid(row=0, column=0, sticky="w", padx=(10,1), pady=(5,2))
    Tw1 = tk.Entry(marco_sup_horiz_c, width=10)
    Tw1.grid(row=0, column=1, sticky="w", pady=(5,2))
    
    tk.Label(marco_sup_horiz_c, text="Ta(K):").grid(row=1, column=0, sticky="w", padx=(10,1), pady=2)
    Ta1 = tk.Entry(marco_sup_horiz_c, width=10)
    Ta1.grid(row=1, column=1, sticky="w", padx=1, pady=2)
   
    tk.Label(marco_sup_horiz_c, text="A(m²):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=2)
    A1 = tk.Entry(marco_sup_horiz_c, width=10)
    A1.grid(row=2, column=1, sticky="w", padx=1, pady=2)
    
    
    tk.Label(marco_sup_horiz_c, text="dext(m):").grid(row=3, column=0, sticky="w", padx=(10,1), pady=2)
    d1 = tk.Entry(marco_sup_horiz_c, width=10)
    d1.grid(row=3, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="L(m):").grid(row=4, column=0, sticky="w", padx=(10,1), pady=2)
    L1 = tk.Entry(marco_sup_horiz_c, width=10)
    L1.grid(row=4, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="λv(kJ/kg):").grid(row=5, column=0, sticky="w", padx=(10,1), pady=2)
    λ1 = tk.Entry(marco_sup_horiz_c, width=10)
    λ1.grid(row=5, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="PV (barG):").grid(row=6, column=0, sticky="w", padx=(10,1), pady=2) # poner en la leyenda Presión de vapor = PV
    PV1 = tk.Entry(marco_sup_horiz_c, width=10)
    PV1.grid(row=6, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="Ɛ:").grid(row=7, column=0, sticky="w", padx=(10,1), pady=2)
    Ɛ1 = tk.Entry(marco_sup_horiz_c, width=10)
    Ɛ1.grid(row=7, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="σ:").grid(row=8, column=0, sticky="w", padx=(10,1), pady=2)
    σ1 = tk.Entry(marco_sup_horiz_c, width=10)
    σ1.grid(row=8, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="t (h)").grid(row=9, column=0, sticky="w", padx=(10,1), pady=2)
    t1 = tk.Entry(marco_sup_horiz_c, width=10)
    t1.grid(row=9, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="hc(W/m² K):").grid(row=0, column=2, sticky="e", padx=(10,1), pady=(5,2))
    hc1_texto = tk.Text(marco_sup_horiz_c, width=10, height=1, state="disabled")
    hc1_texto.grid(row=0, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_c, text="hr(W/m² K):").grid(row=1, column=2, sticky="e", padx=1, pady=2)
    hr1_texto = tk.Text(marco_sup_horiz_c, width=10, height=1, state="disabled")
    hr1_texto.grid(row=1, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="ha(W/m² K):").grid(row=2, column=2, sticky="e", padx=(10,1), pady=(5,2))
    ha1_texto = tk.Text(marco_sup_horiz_c, width=10, height=1, state="disabled")
    ha1_texto.grid(row=2, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_c, text="Qp(W):").grid(row=3, column=2, sticky="e", padx=1, pady=2)
    Qp1_texto = tk.Text(marco_sup_horiz_c, width=10, height=1, state="disabled")
    Qp1_texto.grid(row=3, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_c, text="Ws(kg/h):").grid(row=4, column=2, sticky="e", padx=(10,1), pady=(5,2))
    Wsf1_texto = tk.Text(marco_sup_horiz_c, width=10, height=1, state="disabled")
    Wsf1_texto.grid(row=4, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_c, text="Ws(kg):").grid(row=5, column=2, sticky="e", padx=1, pady=2)
    Ws1_texto = tk.Text(marco_sup_horiz_c, width=10, height=1, state="disabled")
    Ws1_texto.grid(row=5, column=3, sticky="w", padx=1, pady=2)

   
    
   
    # Creo el botón calcular para las pérdidas por Superficie horizontal cilindricas
    boton_horiz_a = tk.Button(marco_sup_horiz_c, text="Calcular", command=lambda: calcular_sup_horiz_c(Tw1, Ta1, A1, d1, L1, λ1, PV1, Ɛ1, σ1, t1, hc1_texto, hr1_texto, ha1_texto, Qp1_texto, Wsf1_texto, Ws1_texto))
    boton_horiz_a.grid(row=9, column=3, sticky="w", padx=1, pady=2)

    
    
     
   
    # Funcion Calculo para Superficie horizontal (planas hacia arriba )
    def calcular_sup_horiz_pa(Tw2, Ta2, A2, d2, L2, λ2, PV2, Ɛ2, σ2, t2, hc2_texto, hr2_texto, ha2_texto, Qp2_texto, Wsf2_texto, Ws2_texto):
        try:
            # Obtener valores de las cajas de texto
            valor_Tw2 = float(Tw2.get())
            valor_Ta2 = float(Ta2.get())
            valor_A2 = float(A2.get())
            valor_d2 = float(d2.get())
            valor_L2 = float(L2.get())
            valor_λ2 = float(λ2.get())
            valor_PV2 = float(PV2.get())
            valor_Ɛ2 = float(Ɛ2.get())
            valor_σ2 = float(σ2.get())
            valor_t2 = float(t2.get())
            
           
            # Realizar la operación (hc)
            resultado_hc2 = 1.32 * ((valor_Tw2 - valor_Ta2) / valor_L2) ** 0.25
            hc2_texto.config(state="normal")  # Habilitar temporalmente para editar
            hc2_texto.delete("1.0", tk.END)   # Borrar contenido previo
            hc2_texto.insert(tk.END, f"{resultado_hc2}")
            hc2_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (hr)
            resultado_hr2 = valor_Ɛ2 * valor_σ2 * ((valor_Tw2 + valor_Ta2) * ((valor_Tw2 ** 2) + (valor_Ta2 ** 2)))
            hr2_texto.config(state="normal")  # Habilitar temporalmente para editar
            hr2_texto.delete("1.0", tk.END)   # Borrar contenido previo
            hr2_texto.insert(tk.END, f"{resultado_hr2}")
            hr2_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (ha)
            resultado_ha2 = resultado_hc2 + resultado_hr2
            ha2_texto.config(state="normal")  # Habilitar temporalmente para editar
            ha2_texto.delete("1.0", tk.END)   # Borrar contenido previo
            ha2_texto.insert(tk.END, f"{resultado_ha2}")
            ha2_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Qp)
            resultado_Qp2 = resultado_ha2 * valor_A2 * (valor_Tw2 - valor_Ta2)
            Qp2_texto.config(state="normal")  # Habilitar temporalmente para editar
            Qp2_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Qp2_texto.insert(tk.END, f"{resultado_Qp2}")
            Qp2_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Wsf)
            resultado_Wsf2 = (resultado_Qp2 * 3.6) / valor_λ2
            Wsf2_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wsf2_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wsf2_texto.insert(tk.END, f"{resultado_Wsf2}")
            Wsf2_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Ws)
            resultado_Ws2 = resultado_Wsf2 * valor_t2
            Ws2_texto.config(state="normal")  # Habilitar temporalmente para editar
            Ws2_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Ws2_texto.insert(tk.END, f"{resultado_Ws2}")
            Ws2_texto.config(state="disabled") # Deshabilitar nuevamente   
        
        except ValueError:
            # Mostrar error en la caja de texto
            hc2_texto.config(state="normal")
            hc2_texto.delete("1.0", tk.END)
            hc2_texto.insert(tk.END, "Error: ")
            hc2_texto.config(state="disabled")
            
            hr2_texto.config(state="normal")
            hr2_texto.delete("1.0", tk.END)
            hr2_texto.insert(tk.END, "Error: ")
            hr2_texto.config(state="disabled")
            
            ha2_texto.config(state="normal")
            ha2_texto.delete("1.0", tk.END)
            ha2_texto.insert(tk.END, "Error: ")
            ha2_texto.config(state="disabled")
            
            Qp2_texto.config(state="normal")
            Qp2_texto.delete("1.0", tk.END)
            Qp2_texto.insert(tk.END, "Error: ")
            Qp2_texto.config(state="disabled")
            
            Wsf2_texto.config(state="normal")
            Wsf2_texto.delete("1.0", tk.END)
            Wsf2_texto.insert(tk.END, "Error: ")
            Wsf2_texto.config(state="disabled")
            
            Ws2_texto.config(state="normal")
            Ws2_texto.delete("1.0", tk.END)
            Ws2_texto.insert(tk.END, "Error: ")
            Ws2_texto.config(state="disabled")
            
            messagebox.showerror("Error","Ingrese solo números y en todas las casillas y no use comas(,)",  parent=ventana_perdidas_indirectas)
            #Ws2_texto.config(state="disabled")
    
   
    
    
    # Creamos el marco de Superficie horizontal (planas hacia arriba )
    marco_sup_horiz_pa = tk.Frame(ventana_perdidas_indirectas, bg="#dae3f3", borderwidth=1, relief="sunken", width=315, height=270)
    marco_sup_horiz_pa.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 4 columnas 
    marco_sup_horiz_pa.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_sup_horiz_pa.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_sup_horiz_pa.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_sup_horiz_pa.columnconfigure(3, weight=0)  # Columna 3 No se expande
    
    marco_sup_horiz_pa.grid(row=3, column=2, sticky="w", padx=(0,5), pady=1)  # Con sticky="w" se alinea el marco a la izquierda
    
    
    
    # Cajas de texto para entrada de datos
    tk.Label(marco_sup_horiz_pa, text="Tw(K):").grid(row=0, column=0, sticky="w", padx=(10,1), pady=(5,2))
    Tw2 = tk.Entry(marco_sup_horiz_pa, width=10)
    Tw2.grid(row=0, column=1, sticky="w", pady=(5,2))
    
    tk.Label(marco_sup_horiz_pa, text="Ta(K):").grid(row=1, column=0, sticky="w", padx=(10,1), pady=2)
    Ta2 = tk.Entry(marco_sup_horiz_pa, width=10)
    Ta2.grid(row=1, column=1, sticky="w", padx=1, pady=2)
   
    tk.Label(marco_sup_horiz_pa, text="A(m²):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=2)
    A2 = tk.Entry(marco_sup_horiz_pa, width=10)
    A2.grid(row=2, column=1, sticky="w", padx=1, pady=2)
    
    
    tk.Label(marco_sup_horiz_pa, text="dext(m):").grid(row=3, column=0, sticky="w", padx=(10,1), pady=2)
    d2 = tk.Entry(marco_sup_horiz_pa, width=10)
    d2.grid(row=3, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="L(m):").grid(row=4, column=0, sticky="w", padx=(10,1), pady=2)
    L2 = tk.Entry(marco_sup_horiz_pa, width=10)
    L2.grid(row=4, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="λv(kJ/kg):").grid(row=5, column=0, sticky="w", padx=(10,1), pady=2)
    λ2 = tk.Entry(marco_sup_horiz_pa, width=10)
    λ2.grid(row=5, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="PV (barG):").grid(row=6, column=0, sticky="w", padx=(10,1), pady=2) # poner en la leyenda Presión de vapor = PV
    PV2 = tk.Entry(marco_sup_horiz_pa, width=10)
    PV2.grid(row=6, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="Ɛ:").grid(row=7, column=0, sticky="w", padx=(10,1), pady=2)
    Ɛ2 = tk.Entry(marco_sup_horiz_pa, width=10)
    Ɛ2.grid(row=7, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="σ:").grid(row=8, column=0, sticky="w", padx=(10,1), pady=2)
    σ2 = tk.Entry(marco_sup_horiz_pa, width=10)
    σ2.grid(row=8, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="t (h)").grid(row=9, column=0, sticky="w", padx=(10,1), pady=2)
    t2 = tk.Entry(marco_sup_horiz_pa, width=10)
    t2.grid(row=9, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="hc(W/m² K):").grid(row=0, column=2, sticky="e", padx=(10,1), pady=(5,2))
    hc2_texto = tk.Text(marco_sup_horiz_pa, width=10, height=1, state="disabled")
    hc2_texto.grid(row=0, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_pa, text="hr(W/m² K):").grid(row=1, column=2, sticky="e", padx=1, pady=2)
    hr2_texto = tk.Text(marco_sup_horiz_pa, width=10, height=1, state="disabled")
    hr2_texto.grid(row=1, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="ha(W/m² K):").grid(row=2, column=2, sticky="e", padx=(10,1), pady=(5,2))
    ha2_texto = tk.Text(marco_sup_horiz_pa, width=10, height=1, state="disabled")
    ha2_texto.grid(row=2, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_pa, text="Qp(W):").grid(row=3, column=2, sticky="e", padx=1, pady=2)
    Qp2_texto = tk.Text(marco_sup_horiz_pa, width=10, height=1, state="disabled")
    Qp2_texto.grid(row=3, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pa, text="Ws(kg/h):").grid(row=4, column=2, sticky="e", padx=(10,1), pady=(5,2))
    Wsf2_texto = tk.Text(marco_sup_horiz_pa, width=10, height=1, state="disabled")
    Wsf2_texto.grid(row=4, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_pa, text="Ws(kg):").grid(row=5, column=2, sticky="e", padx=1, pady=2)
    Ws2_texto = tk.Text(marco_sup_horiz_pa, width=10, height=1, state="disabled")
    Ws2_texto.grid(row=5, column=3, sticky="w", padx=1, pady=2)

   
    
    
    # Creo el botón calcular para las pérdidas por Superficie horizontal planas hacia arriba
    boton_horiz_pa = tk.Button(marco_sup_horiz_pa, text="Calcular", command=lambda: calcular_sup_horiz_pa(Tw2, Ta2, A2, d2, L2, λ2, PV2, Ɛ2, σ2, t2, hc2_texto, hr2_texto, ha2_texto, Qp2_texto, Wsf2_texto, Ws2_texto))
    boton_horiz_pa.grid(row=9, column=3, sticky="w", padx=1, pady=2)
    
    
    
    # Funcion Calculo para Superficie horizontal (planas hacia abajo )
    def calcular_sup_horiz_pab(Tw3, Ta3, A3, d3, L3, λ3, PV3, Ɛ3, σ3, t3, hc3_texto, hr3_texto, ha3_texto, Qp3_texto, Wsf3_texto, Ws3_texto):
        try:
            # Obtener valores de las cajas de texto
            valor_Tw3 = float(Tw3.get())
            valor_Ta3 = float(Ta3.get())
            valor_A3 = float(A3.get())
            valor_d3 = float(d3.get())
            valor_L3 = float(L3.get())
            valor_λ3 = float(λ3.get())
            valor_PV3 = float(PV3.get())
            valor_Ɛ3 = float(Ɛ3.get())
            valor_σ3 = float(σ3.get())
            valor_t3 = float(t3.get())
            
           
            # Realizar la operación (hc)
            resultado_hc3 = 0.61 * (((valor_Tw3 - valor_Ta3) / (valor_L3 ** 2)) ** 0.33)
            hc3_texto.config(state="normal")  # Habilitar temporalmente para editar
            hc3_texto.delete("1.0", tk.END)   # Borrar contenido previo
            hc3_texto.insert(tk.END, f"{resultado_hc3}")
            hc3_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (hr)
            resultado_hr3 = valor_Ɛ3 * valor_σ3 * ((valor_Tw3 + valor_Ta3) * ((valor_Tw3 ** 2) + (valor_Ta3 ** 2)))
            hr3_texto.config(state="normal")  # Habilitar temporalmente para editar
            hr3_texto.delete("1.0", tk.END)   # Borrar contenido previo
            hr3_texto.insert(tk.END, f"{resultado_hr3}")
            hr3_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (ha)
            resultado_ha3 = resultado_hc3 + resultado_hr3
            ha3_texto.config(state="normal")  # Habilitar temporalmente para editar
            ha3_texto.delete("1.0", tk.END)   # Borrar contenido previo
            ha3_texto.insert(tk.END, f"{resultado_ha3}")
            ha3_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Qp)
            resultado_Qp3 = resultado_ha3 * valor_A3 * (valor_Tw3 - valor_Ta3)
            Qp3_texto.config(state="normal")  # Habilitar temporalmente para editar
            Qp3_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Qp3_texto.insert(tk.END, f"{resultado_Qp3}")
            Qp3_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Wsf)
            resultado_Wsf3 = (resultado_Qp3 * 3.6) / valor_λ3
            Wsf3_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wsf3_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wsf3_texto.insert(tk.END, f"{resultado_Wsf3}")
            Wsf3_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Ws)
            resultado_Ws3 = resultado_Wsf3 * valor_t3
            Ws3_texto.config(state="normal")  # Habilitar temporalmente para editar
            Ws3_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Ws3_texto.insert(tk.END, f"{resultado_Ws3}")
            Ws3_texto.config(state="disabled") # Deshabilitar nuevamente   
        
        except ValueError:
            # Mostrar error en la caja de texto
            hc3_texto.config(state="normal")
            hc3_texto.delete("1.0", tk.END)
            hc3_texto.insert(tk.END, "Error: ")
            hc3_texto.config(state="disabled")
            
            hr3_texto.config(state="normal")
            hr3_texto.delete("1.0", tk.END)
            hr3_texto.insert(tk.END, "Error: ")
            hr3_texto.config(state="disabled")
            
            ha3_texto.config(state="normal")
            ha3_texto.delete("1.0", tk.END)
            ha3_texto.insert(tk.END, "Error: ")
            ha3_texto.config(state="disabled")
            
            Qp3_texto.config(state="normal")
            Qp3_texto.delete("1.0", tk.END)
            Qp3_texto.insert(tk.END, "Error: ")
            Qp3_texto.config(state="disabled")
            
            Wsf3_texto.config(state="normal")
            Wsf3_texto.delete("1.0", tk.END)
            Wsf3_texto.insert(tk.END, "Error: ")
            Wsf3_texto.config(state="disabled")
            
            Ws3_texto.config(state="normal")
            Ws3_texto.delete("1.0", tk.END)
            Ws3_texto.insert(tk.END, "Error: ")
            Ws3_texto.config(state="disabled")
            
            messagebox.showerror("Error","Ingrese solo números y en todas las casillas y no use comas (,)",  parent=ventana_perdidas_indirectas)
            #Ws3_texto.config(state="disabled")
    
   
    
    
    # Creamos el marco de Superficie horizontal (planas hacia abajo )
    marco_sup_horiz_pab = tk.Frame(ventana_perdidas_indirectas, bg="#dae3f3", borderwidth=1, relief="sunken", width=315, height=270)
    marco_sup_horiz_pab.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 4 columnas 
    marco_sup_horiz_pab.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_sup_horiz_pab.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_sup_horiz_pab.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_sup_horiz_pab.columnconfigure(3, weight=0)  # Columna 3 No se expande
    
    marco_sup_horiz_pab.grid(row=5, column=0, sticky="w", padx=5, pady=1)  # Con sticky="w" se alinea el marco a la izquierda
    
    
    
    # Cajas de texto para entrada de datos
    tk.Label(marco_sup_horiz_pab, text="Tw(K):").grid(row=0, column=0, sticky="w", padx=(10,1), pady=(5,2))
    Tw3 = tk.Entry(marco_sup_horiz_pab, width=10)
    Tw3.grid(row=0, column=1, sticky="w", pady=(5,2))
    
    tk.Label(marco_sup_horiz_pab, text="Ta(K):").grid(row=1, column=0, sticky="w", padx=(10,1), pady=2)
    Ta3 = tk.Entry(marco_sup_horiz_pab, width=10)
    Ta3.grid(row=1, column=1, sticky="w", padx=1, pady=2)
   
    tk.Label(marco_sup_horiz_pab, text="A(m²):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=2)
    A3 = tk.Entry(marco_sup_horiz_pab, width=10)
    A3.grid(row=2, column=1, sticky="w", padx=1, pady=2)
    
    
    tk.Label(marco_sup_horiz_pab, text="dext(m):").grid(row=3, column=0, sticky="w", padx=(10,1), pady=2)
    d3 = tk.Entry(marco_sup_horiz_pab, width=10)
    d3.grid(row=3, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="L(m):").grid(row=4, column=0, sticky="w", padx=(10,1), pady=2)
    L3 = tk.Entry(marco_sup_horiz_pab, width=10)
    L3.grid(row=4, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="λv(kJ/kg):").grid(row=5, column=0, sticky="w", padx=(10,1), pady=2)
    λ3 = tk.Entry(marco_sup_horiz_pab, width=10)
    λ3.grid(row=5, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="PV (barG):").grid(row=6, column=0, sticky="w", padx=(10,1), pady=2) # poner en la leyenda Presión de vapor = PV
    PV3 = tk.Entry(marco_sup_horiz_pab, width=10)
    PV3.grid(row=6, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="Ɛ:").grid(row=7, column=0, sticky="w", padx=(10,1), pady=2)
    Ɛ3 = tk.Entry(marco_sup_horiz_pab, width=10)
    Ɛ3.grid(row=7, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="σ:").grid(row=8, column=0, sticky="w", padx=(10,1), pady=2)
    σ3 = tk.Entry(marco_sup_horiz_pab, width=10)
    σ3.grid(row=8, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="t (h)").grid(row=9, column=0, sticky="w", padx=(10,1), pady=2)
    t3 = tk.Entry(marco_sup_horiz_pab, width=10)
    t3.grid(row=9, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="hc(W/m² K):").grid(row=0, column=2, sticky="e", padx=(10,1), pady=(5,2))
    hc3_texto = tk.Text(marco_sup_horiz_pab, width=10, height=1, state="disabled")
    hc3_texto.grid(row=0, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_pab, text="hr(W/m² K):").grid(row=1, column=2, sticky="e", padx=1, pady=2)
    hr3_texto = tk.Text(marco_sup_horiz_pab, width=10, height=1, state="disabled")
    hr3_texto.grid(row=1, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="ha(W/m² K):").grid(row=2, column=2, sticky="e", padx=(10,1), pady=(5,2))
    ha3_texto = tk.Text(marco_sup_horiz_pab, width=10, height=1, state="disabled")
    ha3_texto.grid(row=2, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_pab, text="Qp(W):").grid(row=3, column=2, sticky="e", padx=1, pady=2)
    Qp3_texto = tk.Text(marco_sup_horiz_pab, width=10, height=1, state="disabled")
    Qp3_texto.grid(row=3, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_sup_horiz_pab, text="Ws(kg/h):").grid(row=4, column=2, sticky="e", padx=(10,1), pady=(5,2))
    Wsf3_texto = tk.Text(marco_sup_horiz_pab, width=10, height=1, state="disabled")
    Wsf3_texto.grid(row=4, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_sup_horiz_pab, text="Ws(kg):").grid(row=5, column=2, sticky="e", padx=1, pady=2)
    Ws3_texto = tk.Text(marco_sup_horiz_pab, width=10, height=1, state="disabled")
    Ws3_texto.grid(row=5, column=3, sticky="w", padx=1, pady=2)

   
    
    
    # Creo el botón calcular para las pérdidas por Superficie horizontal planas hacia arriba
    boton_horiz_pab = tk.Button(marco_sup_horiz_pab, text="Calcular", command=lambda: calcular_sup_horiz_pab(Tw3, Ta3, A3, d3, L3, λ3, PV3, Ɛ3, σ3, t3, hc3_texto, hr3_texto, ha3_texto, Qp3_texto, Wsf3_texto, Ws3_texto))
    boton_horiz_pab.grid(row=9, column=3, sticky="w", padx=1, pady=2)


    

    tk.Label(ventana_perdidas_indirectas, text="Pérdidas suplementarias",  font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken").grid(row=4, column=1, sticky="w", padx=(80,0), pady=(10,0))
    tk.Label(ventana_perdidas_indirectas, text="Tuberías y equipos").grid(row=5, column=1, sticky="nw", padx=(60,5), pady=(5,1))
    tk.Label(ventana_perdidas_indirectas, text="Ws (kg)").grid(row=5, column=1, sticky="nw", padx=(205,5), pady=(5,1))
    tk.Label(ventana_perdidas_indirectas, text="El  15% del vapor perdido:").grid(row=5, column=1, sticky="nw", padx=(45,1), pady=(35,1))
    l5_texto = tk.Text(ventana_perdidas_indirectas, width=10, height=1, state="disabled")
    l5_texto.grid(row=5, column=1, sticky="nw", padx=(190,0), pady=(35,1))
    tk.Label(ventana_perdidas_indirectas, text="El  20% del vapor perdido:").grid(row=5, column=1, sticky="nw", padx=(45,1), pady=(65,1))
    l20_texto = tk.Text(ventana_perdidas_indirectas, width=10, height=1, state="disabled")
    l20_texto.grid(row=5, column=1, sticky="nw", padx=(190,5), pady=(65,1))
    tk.Label(ventana_perdidas_indirectas, text="El  25% del vapor perdido:").grid(row=5, column=1, sticky="nw", padx=(45,1), pady=(95,1))
    l25_texto = tk.Text(ventana_perdidas_indirectas, width=10, height=1, state="disabled")
    l25_texto.grid(row=5, column=1, sticky="nw", padx=(190,5), pady=(95,1))
    

    
    tk.Label(ventana_perdidas_indirectas, text="Sumatoria del vapor perdido por convección-radiación ", font=("Arial", 9)).grid(row=5, column=2, sticky="nw", padx=(15,1), pady=(16,1))
    ΣWs_c_r_texto = tk.Text(ventana_perdidas_indirectas, width=23, height=1, font=("TkDefaultFont", 12, "bold"), state="disabled")
    ΣWs_c_r_texto.grid(row=5, column=2, sticky="nw", padx=(55,1), pady=(46,1))
    #boton para calcular la sumatoria  del vapor perdido por convección-radiación
    boton_sumatoria_c_r = tk.Button(ventana_perdidas_indirectas, text="Calcular ΣWs_c-r (kg)", font=("TkDefaultFont", 12, "bold"), width=20, height=1, command=lambda: calcular_sumatoria_c_r(Ws_texto, Ws1_texto, Ws2_texto, Ws3_texto, ΣWs_c_r_texto, l5_texto, l20_texto, l25_texto))
    boton_sumatoria_c_r.grid(row=5, column=2, sticky="nw", padx=(56,1), pady=(76,1))
    
    
    def calcular_perdida_evaporacion(As, PVp, PVa, Hr, Va, Da, λat, λap, Pc, t4, Ke_texto, Wae_texto, Wsc_texto, Ws4_texto):
        try:
            # Obtener valores de las cajas de texto
            valor_As = float(As.get())
            valor_PVp = float(PVp.get())
            valor_PVa = float(PVa.get())
            valor_Hr = float(Hr.get())
            valor_Va = float(Va.get())
            valor_Da = float(Da.get())
            valor_λat = float(λat.get())
            valor_λap = float(λap.get())
            valor_Pc = float(Pc.get())
            valor_t4 = float(t4.get())
            
           
            # Realizar la operación (Ke_texto)
            resultado_Ke = 0.0745 * ((valor_Va * valor_Da) ** 0.8)
            Ke_texto.config(state="normal")  # Habilitar temporalmente para editar
            Ke_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Ke_texto.insert(tk.END, f"{resultado_Ke}")
            Ke_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (Wae)
            resultado_Wae = resultado_Ke * valor_As * (valor_PVp - ((valor_Hr * valor_PVa) / 100))
            Wae_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wae_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wae_texto.insert(tk.END, f"{resultado_Wae}")
            Wae_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Wsc)
            resultado_Wsc = (resultado_Wae * valor_λat) / valor_λap
            Wsc_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wsc_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wsc_texto.insert(tk.END, f"{resultado_Wsc}")
            Wsc_texto.config(state="disabled") # Deshabilitar nuevamente
            
            # Realizar la operación (Ws4)
            resultado_Ws4 = resultado_Wsc * valor_t4
            Ws4_texto.config(state="normal")  # Habilitar temporalmente para editar
            Ws4_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Ws4_texto.insert(tk.END, f"{resultado_Ws4}")
            Ws4_texto.config(state="disabled") # Deshabilitar nuevamente
            
            
        
        except ValueError:
            # Mostrar error en la caja de texto
            Ke_texto.config(state="normal")
            Ke_texto.delete("1.0", tk.END)
            Ke_texto.insert(tk.END, "Error: ")
            Ke_texto.config(state="disabled")
            
            Wae_texto.config(state="normal")
            Wae_texto.delete("1.0", tk.END)
            Wae_texto.insert(tk.END, "Error: ")
            Wae_texto.config(state="disabled")
            
            Wsc_texto.config(state="normal")
            Wsc_texto.delete("1.0", tk.END)
            Wsc_texto.insert(tk.END, "Error: ")
            Wsc_texto.config(state="disabled")
            
            Ws4_texto.config(state="normal")
            Ws4_texto.delete("1.0", tk.END)
            Ws4_texto.insert(tk.END, "Error: ")
            Ws4_texto.config(state="disabled")
            
          
            
            messagebox.showerror("Error","Ingrese solo números y en todas las casillas y no use comas (,)",  parent=ventana_perdidas_indirectas)
            #Ws_texto.config(state="disabled")
  

   
    # Creamos el marco de perdidas por evaporacion
    marco_perdida_evaporacion = tk.Frame(ventana_perdidas_indirectas, bg="#dae3f3", borderwidth=1, relief="sunken", width=365, height=270)
    marco_perdida_evaporacion.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 4 columnas 
    marco_perdida_evaporacion.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_perdida_evaporacion.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_perdida_evaporacion.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_perdida_evaporacion.columnconfigure(3, weight=0)  # Columna 3 No se expande
    
    marco_perdida_evaporacion.grid(row=3, column=3, sticky="w", padx=5, pady=1)  # Con sticky="w" se alinea el marco a la izquierda
    

    
    # Cajas de texto para entrada de datos
    tk.Label(marco_perdida_evaporacion, text="As(m²):").grid(row=0, column=0, sticky="w", padx=(10,1), pady=(5,2))
    As = tk.Entry(marco_perdida_evaporacion, width=10)
    As.grid(row=0, column=1, sticky="w", pady=(5,2))
    
    tk.Label(marco_perdida_evaporacion, text="PVp(mmhg):").grid(row=1, column=0, sticky="w", padx=(10,1), pady=2)
    PVp = tk.Entry(marco_perdida_evaporacion, width=10)
    PVp.grid(row=1, column=1, sticky="w", padx=1, pady=2)
   
    tk.Label(marco_perdida_evaporacion, text="PVa(mmhg):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=2)
    PVa = tk.Entry(marco_perdida_evaporacion, width=10)
    PVa.grid(row=2, column=1, sticky="w", padx=1, pady=2)
    
    
    tk.Label(marco_perdida_evaporacion, text="Hr(%):").grid(row=3, column=0, sticky="w", padx=(10,1), pady=2)
    Hr = tk.Entry(marco_perdida_evaporacion, width=10)
    Hr.grid(row=3, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_perdida_evaporacion, text="Va(m/s):").grid(row=4, column=0, sticky="w", padx=(10,1), pady=2)
    Va = tk.Entry(marco_perdida_evaporacion, width=10)
    Va.grid(row=4, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_perdida_evaporacion, text="Da(kg/m³):").grid(row=5, column=0, sticky="w", padx=(10,1), pady=2)
    Da = tk.Entry(marco_perdida_evaporacion, width=10)
    Da.grid(row=5, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_perdida_evaporacion, text="λat(kJ/kg):").grid(row=6, column=0, sticky="w", padx=(10,1), pady=2) # poner en la leyenda Presión de vapor = PV
    λat = tk.Entry(marco_perdida_evaporacion, width=10)
    λat.grid(row=6, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_perdida_evaporacion, text="λap(kJ/kg):").grid(row=7, column=0, sticky="w", padx=(10,1), pady=2)
    λap = tk.Entry(marco_perdida_evaporacion, width=10)
    λap.grid(row=7, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_perdida_evaporacion, text="Pc(bar):").grid(row=8, column=0, sticky="w", padx=(10,1), pady=2)
    Pc = tk.Entry(marco_perdida_evaporacion, width=10)
    Pc.grid(row=8, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_perdida_evaporacion, text="t(h)").grid(row=9, column=0, sticky="w", padx=(10,1), pady=2)
    t4 = tk.Entry(marco_perdida_evaporacion, width=10)
    t4.grid(row=9, column=1, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_perdida_evaporacion, text="Ke(kg/m²h mmHg):").grid(row=0, column=2, sticky="e", padx=(10,1), pady=(5,2))
    Ke_texto = tk.Text(marco_perdida_evaporacion, width=10, height=1, state="disabled")
    Ke_texto.grid(row=0, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_perdida_evaporacion, text="Wae(kg/h):").grid(row=1, column=2, sticky="e", padx=1, pady=2)
    Wae_texto = tk.Text(marco_perdida_evaporacion, width=10, height=1, state="disabled")
    Wae_texto.grid(row=1, column=3, sticky="w", padx=1, pady=2)
    
    tk.Label(marco_perdida_evaporacion, text="Wsc(kg/h):").grid(row=2, column=2, sticky="e", padx=(10,1), pady=(5,2))
    Wsc_texto = tk.Text(marco_perdida_evaporacion, width=10, height=1, state="disabled")
    Wsc_texto.grid(row=2, column=3, sticky="w", pady=(5,2))
 
    tk.Label(marco_perdida_evaporacion, text="Ws(kg):").grid(row=3, column=2, sticky="e", padx=1, pady=2)
    Ws4_texto = tk.Text(marco_perdida_evaporacion, width=10, height=1, state="disabled")
    Ws4_texto.grid(row=3, column=3, sticky="w", padx=1, pady=2)
    
    

   
   
   
    # Creo el botón calcular para las pérdidas por evaporacion
    boton_perdida_evaporacion = tk.Button(marco_perdida_evaporacion, text="Calcular", command=lambda: calcular_perdida_evaporacion(As, PVp, PVa, Hr, Va, Da, λat, λap, Pc, t4, Ke_texto, Wae_texto, Wsc_texto, Ws4_texto))
    boton_perdida_evaporacion.grid(row=9, column=3, sticky="w", padx=1, pady=2) 
   

    tk.Label(ventana_perdidas_indirectas, text="Sumatoria de las pérdidas indirectas", font=("Arial", 9)).grid(row=5, column=3, sticky="nw", padx=(70,1), pady=(16,0))
    # Caja de texto de la Sumatoria de las pérdidas indirectas
    ΣWs_p_i_texto = tk.Text(ventana_perdidas_indirectas, width=23, height=1, font=("TkDefaultFont", 12, "bold"), state="disabled")
    ΣWs_p_i_texto.grid(row=5, column=3, sticky="nw", padx=(70,1), pady=(46,0))
    
    #boton para calcular la Sumatoria de las pérdidas indirectas
    boton_sumatoria_p_i = tk.Button(ventana_perdidas_indirectas, text="Calcular ΣWs_p-i (kg)", font=("TkDefaultFont", 12, "bold"), width=20, height=1, command=lambda: calcular_sumatoria_p_i(Ws4_texto, ΣWs_p_i_texto, l20_texto))
    boton_sumatoria_p_i.grid(row=5, column=3, sticky="nw", padx=(70,1), pady=(76,0))
    

   

    def cerrar_ventana_indirecta():
        if messagebox.askyesno("Confirmar cierre", f"¿Cerrar ventana de {titulo}?", parent=ventana_perdidas_indirectas):
            ventana_perdidas_indirectas.destroy()
    
    ventana_perdidas_indirectas.protocol("WM_DELETE_WINDOW", cerrar_ventana_indirecta)
    


           
        
        
#"""Funcion que abre la ventana para el calculo de perdidas directas"""    	    
def perdidas_directas(titulo):
    #sum_p_i = perdidas_indirectas("Perdidas Indirectas y Suplementarias")
    """Crea una nueva ventana con el título especificado"""
    ventana_perdidas_directas = tk.Toplevel(root)
    ventana_perdidas_directas.title(titulo)
    ventana_perdidas_directas.geometry("845x570")
    ventana_perdidas_directas.configure(bg="#b3cac7")
    
    ventana_perdidas_directas.columnconfigure(0, weight=0)  # Columna 0 NO se expande para luego poder alinear a la izquierda los frame de esa columna
    ventana_perdidas_directas.columnconfigure(1, weight=0)  # Columna 1 NO se expande , con weight=1 se expande y centra lo que tu pongas es mejor asi para luego con padx correlo 
     
    
    etiqueta00 = tk.Label(
        ventana_perdidas_directas, 
        text="Cálculo para la  ", 
        font=("Arial", 13,), 
        fg="#1A1A1A", 
        bg="#f1c5ef", 
        borderwidth=0, 
        relief="sunken"
    )
    etiqueta00.grid(row=0, column=0, sticky="e", pady=5)  # Con sticky="w" se alinea el marco a la izquierda

    etiqueta11 = tk.Label(
        ventana_perdidas_directas, 
        text="estimación de las pérdidas de vapor directas", 
        font=("Arial", 13,), 
        fg="#1A1A1A", 
        bg="#f1c5ef", 
        borderwidth=0, 
        relief="sunken"
    )
    etiqueta11.grid(row=0, column=1, sticky="w", pady=5)  # Con sticky="w" se alinea el marco a la izquierda
    
    etiqueta_orificios = tk.Label(ventana_perdidas_directas, text="Pérdida por orificios", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_orificios.grid(row=1, column=0, pady=(10,0))
    
    etiqueta_equivalencia_combustible = tk.Label(ventana_perdidas_directas, text="Equivalencia en combustible", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_equivalencia_combustible.grid(row=1, column=1, pady=(10,0))

    etiqueta_altura_vapor = tk.Label(ventana_perdidas_directas, text="Altura de la nube de vapor ", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_altura_vapor.grid(row=3, column=0, pady=(10,0))

    etiqueta_perdida_economica = tk.Label(ventana_perdidas_directas, text="Pérdida económica ", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_perdida_economica.grid(row=3, column=1, pady=(10,0))

    etiqueta_leyenda_Pdirecta = tk.Label(ventana_perdidas_directas, text="Leyenda:", font=("Arial", 11,), fg="#1A1A1A", bg="#f1c5ef", borderwidth=0, relief="sunken")
    etiqueta_leyenda_Pdirecta.grid(row=5, column=1, pady=(10,0))
    
    def calcular_perdidas_orificios(PVP, AO, t, FPV_texto, Ws_texto):
        try:
            # Obtener valores de las cajas de texto
            valor_PVP = float(PVP.get())
            valor_AO = float(AO.get())
            valor_t = float(t.get())
           
            # Realizar la operación (FPV)
            resultado_FPV = ((0.695 * valor_AO * valor_PVP) / 2.2)
            FPV_texto.config(state="normal")  # Habilitar temporalmente para editar
            FPV_texto.delete("1.0", tk.END)   # Borrar contenido previo
            FPV_texto.insert(tk.END, f"{resultado_FPV}")
            FPV_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (Ws)
            resultado_Ws = (valor_t * resultado_FPV)
            Ws_texto.config(state="normal")  # Habilitar temporalmente para editar
            Ws_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Ws_texto.insert(tk.END, f"{resultado_Ws}")
            Ws_texto.config(state="disabled") # Deshabilitar nuevamente 
        
        except ValueError:
            # Mostrar error en la caja de texto
            FPV_texto.config(state="normal")
            FPV_texto.delete("1.0", tk.END)
            FPV_texto.insert(tk.END, "Error: ")
            FPV_texto.config(state="disabled")
            
            Ws_texto.config(state="normal")
            Ws_texto.delete("1.0", tk.END)
            Ws_texto.insert(tk.END, "Error: ")
            messagebox.showerror("Error","Ingrese solo números y no use comas (,)",  parent=ventana_perdidas_directas)
            Ws_texto.config(state="disabled")
    
    # Creamos el marco de perdida por orificios
    marco_perdidas_orificios = tk.Frame(ventana_perdidas_directas, bg="#dae3f3", borderwidth=1, relief="sunken", width=315, height=140)
    marco_perdidas_orificios.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 4 columnas 
    marco_perdidas_orificios.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_perdidas_orificios.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_perdidas_orificios.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_perdidas_orificios.columnconfigure(3, weight=0)  # Columna 3 No se expande
    
    marco_perdidas_orificios.grid(row=2, column=0, sticky="w", padx=5, pady=1)  # Con sticky="w" se alinea el marco a la izquierda
    
    # Cajas de texto para entrada de datos
    tk.Label(marco_perdidas_orificios, text="PVP(bar):").grid(row=1, column=0, sticky="w", padx=(10,1), pady=5)
    PVP = tk.Entry(marco_perdidas_orificios, width=10)
    PVP.grid(row=1, column=1, sticky="w", pady=5)
    
    tk.Label(marco_perdidas_orificios, text="AO(mm²):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=5)
    AO = tk.Entry(marco_perdidas_orificios, width=10)
    AO.grid(row=2, column=1, sticky="w", padx=1, pady=5)
    
    tk.Label(marco_perdidas_orificios, text="t(h):").grid(row=3, column=0, sticky="w", padx=(10,1), pady=5)
    t = tk.Entry(marco_perdidas_orificios, width=10)
    t.grid(row=3, column=1, sticky="w", padx=1, pady=5)
    
    tk.Label(marco_perdidas_orificios, text="FPV(kg/h):").grid(row=1, column=2, sticky="e", padx=(20,1), pady=5)
    FPV_texto = tk.Text(marco_perdidas_orificios, width=10, height=1, state="disabled")
    FPV_texto.grid(row=1, column=3, sticky="w", pady=5)
    
    tk.Label(marco_perdidas_orificios, text="Ws(kg):").grid(row=2, column=2, sticky="e", padx=1, pady=5)
    Ws_texto = tk.Text(marco_perdidas_orificios, width=10, height=1, state="disabled")
    Ws_texto.grid(row=2, column=3, sticky="w", padx=1, pady=5)
    
    # Creo el botón calcular para las pérdidas por orificio con llamada a función calcular_perdidas_orificios
    boton_orificios = tk.Button(marco_perdidas_orificios, text="Calcular", command=lambda: calcular_perdidas_orificios(PVP, AO, t, FPV_texto, Ws_texto))
    boton_orificios.grid(row=4, column=0, sticky="w", padx=(10,1), pady=(10,1))


   

    # Funcion altura de la nube de vapor 
   
    def calcular_altura_vapor(An, t5, Wfvapor_texto, Wvapor_texto):
        try:
            # Obtener valores de las cajas de texto
            valor_An = float(An.get())
            valor_t5 = float(t5.get())
            
            
           
            # Realizar la operación (Wfvapor_texto)
            resultado_Wfvapor_texto = 0.0006 * ((valor_An) ** 2.3412)
            Wfvapor_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wfvapor_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wfvapor_texto.insert(tk.END, f"{resultado_Wfvapor_texto}")
            Wfvapor_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (Wvapor_texto)
            resultado_Wvapor_texto = (resultado_Wfvapor_texto * valor_t5)
            Wvapor_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wvapor_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wvapor_texto.insert(tk.END, f"{resultado_Wvapor_texto}")
            Wvapor_texto.config(state="disabled") # Deshabilitar nuevamente 
        
        except ValueError:
            # Mostrar error en la caja de texto
            Wfvapor_texto.config(state="normal")
            Wfvapor_texto.delete("1.0", tk.END)
            Wfvapor_texto.insert(tk.END, "Error: ")
            Wfvapor_texto.config(state="disabled")
            
            Wvapor_texto.config(state="normal")
            Wvapor_texto.delete("1.0", tk.END)
            Wvapor_texto.insert(tk.END, "Error: ")
            messagebox.showerror("Error","Ingrese solo números y si son fraccionarios no use comas(,) use punto(.), ejemplo 2.33",  parent=ventana_perdidas_directas)
            Wvapor_texto.config(state="disabled")
            
    
 
    
    # Creamos el marco Altura de la nube de vapor 
    marco_altura_vapor = tk.Frame(ventana_perdidas_directas, bg="#dae3f3", borderwidth=1, relief="sunken", width=315, height=125)
    marco_altura_vapor.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 6 columnas 
    marco_altura_vapor.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_altura_vapor.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_altura_vapor.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_altura_vapor.columnconfigure(3, weight=0)  # Columna 3 No se expande
    
    
    
    marco_altura_vapor.grid(row=4, column=0, sticky="w", padx=5)  # Con sticky="w" se alinea el marco a la izquierda

    # Cajas de texto para entrada de datos
    tk.Label(marco_altura_vapor, text="An(cm):").grid(row=1, column=0, sticky="w", padx=(10,1), pady=5)
    An = tk.Entry(marco_altura_vapor, width=10)
    An.grid(row=1, column=1, sticky="w", pady=5)
    
    tk.Label(marco_altura_vapor, text="t(h):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=5)
    t5  = tk.Entry(marco_altura_vapor, width=10)
    t5.grid(row=2, column=1, sticky="w", padx=1, pady=5)
    
   
    
    tk.Label(marco_altura_vapor, text="Wvapor(kg/h):").grid(row=1, column=3, sticky="w", padx=(20,1), pady=5)
    Wfvapor_texto = tk.Text(marco_altura_vapor, width=8, height=1, state="disabled")
    Wfvapor_texto.grid(row=1, column=5, sticky="w", pady=5)
    
    tk.Label(marco_altura_vapor, text="Wvapor(kg):").grid(row=2, column=3, sticky="e", padx=1, pady=5)
    Wvapor_texto = tk.Text(marco_altura_vapor, width=8, height=1, state="disabled")
    Wvapor_texto.grid(row=2, column=5, sticky="w", padx=1, pady=5)

    
    
    
    # Creo el botón calcular para Altura de la nube de vapor con llamada a función calcular_altura_vapor
    boton_altura_vapor = tk.Button(marco_altura_vapor, text="Calcular", command=lambda: calcular_altura_vapor(An, t5, Wfvapor_texto, Wvapor_texto))
    boton_altura_vapor.grid(row=4, column=0, sticky="w", padx=(10,1), pady=(27,1))


    
    
    

    
    # Funcion calcular_sumatoria perdidas directas 
    def calcular_sumatoria_p_d(Ws_texto, Wvapor_texto, ΣWs_p_d_texto):
        try:
            # Obtener valores de las cajas de texto     get("1.0", tk.END): Obtiene todo el texto desde el primer carácter (1.0) hasta el final (END)
            #.strip(): Elimina espacios en blanco y saltos de línea al final del texto obtenido.
            valor_Ws_texto = float(Ws_texto.get("1.0", tk.END).strip())
            valor_Wvapor_texto = float(Wvapor_texto.get("1.0", tk.END).strip())
            
            
           
            # Realizar la operación (ΣWs_p_d_texto)
            resultado_ΣWs_p_d_texto = (valor_Ws_texto + valor_Wvapor_texto)
            ΣWs_p_d_texto.config(state="normal")  # Habilitar temporalmente para editar
            ΣWs_p_d_texto.delete("1.0", tk.END)   # Borrar contenido previo
            ΣWs_p_d_texto.insert(tk.END, f"{resultado_ΣWs_p_d_texto}")
            ΣWs_p_d_texto.config(state="disabled") # Deshabilitar nuevamente
           
           
        
        except ValueError:
            # Mostrar error en la caja de texto

            ΣWs_p_d_texto.config(state="normal")
            ΣWs_p_d_texto.delete("1.0", tk.END)
            ΣWs_p_d_texto.insert(tk.END, "Error: ")
            messagebox.showerror("Error","Primero calcule las perdidas por orificios y Altura de vapor , en los calulos ingrese solo números y si son fraccionarios no use comas(,) use punto(.), ejemplo 2.33",  parent=ventana_perdidas_directas)
            ΣWs_p_d_texto.config(state="disabled")

       

        
    tk.Label(ventana_perdidas_directas, text="Sumatoria de las pérdidas directas", font=("Arial", 9)).grid(row=5, column=0, sticky="nw", padx=(12,0), pady=(15,0))
    ΣWs_p_d_texto = tk.Text(ventana_perdidas_directas, width=23, height=1, font=("TkDefaultFont", 12, "bold"), state="disabled")
    ΣWs_p_d_texto.grid(row=6, column=0, sticky="nw", padx=(5,0), pady=(5,0))
    
    #boton para calcular la sumatoria  de las perdidas directas
    boton_sumatoria_p_d = tk.Button(ventana_perdidas_directas, text="Calcular ΣWs_p_d (kg)", font=("TkDefaultFont", 12, "bold"), width=20, height=1, command=lambda: calcular_sumatoria_p_d(Ws_texto, Wvapor_texto, ΣWs_p_d_texto))
    boton_sumatoria_p_d.grid(row=7, column=0, sticky="nw", padx=(6,0), pady=(5,0))



    # Funcion calcular_sumatoria perdidas directas e indirectas
    def calcular_sumatoria_p_di(ΣWs_p_d_texto, resultado_ΣWs_p_i_texto):
        global sum_p_i
        try:
            if sum_p_i == None:
             ΣWs_p_di_texto.config(state="normal")
             ΣWs_p_di_texto.delete("1.0", tk.END)
             ΣWs_p_di_texto.insert(tk.END, "Error: ")   
             messagebox.showerror("Error","Para calcular las sumas de las perdidas directa mas indirectas debe primero realizar todos los calculos en las operaciones Indirectas y Suplementarias",  parent=ventana_perdidas_directas)
             ΣWs_p_di_texto.config(state="disabled")
            else:
             # Obtener valores de las cajas de texto get("1.0", tk.END): Obtiene todo el texto desde el primer carácter (1.0) hasta el final (END)
             #.strip(): Elimina espacios en blanco y saltos de línea al final del texto obtenido.
             #valor_ΣWs_p_i_texto = float(ΣWs_p_i_texto.get("1.0", tk.END).strip())
             valor_ΣWs_p_d_texto = float(ΣWs_p_d_texto.get("1.0", tk.END).strip())
            
             # Realizar la operación (ΣWs_p_d_texto)
             resultado_ΣWs_p_di_texto = (sum_p_i + valor_ΣWs_p_d_texto)
             ΣWs_p_di_texto.config(state="normal")  # Habilitar temporalmente para editar
             ΣWs_p_di_texto.delete("1.0", tk.END)   # Borrar contenido previo
             ΣWs_p_di_texto.insert(tk.END, f"{resultado_ΣWs_p_di_texto}")
             ΣWs_p_di_texto.config(state="disabled") # Deshabilitar nuevamente
            
           
           
        
        except ValueError:
            # Mostrar error en la caja de texto

            ΣWs_p_di_texto.config(state="normal")
            ΣWs_p_di_texto.delete("1.0", tk.END)
            ΣWs_p_di_texto.insert(tk.END, "Error: ")
            messagebox.showerror("Error"," Primero calcule las sumatoria de las perdidas indirectas y luego las directas y en los calulos ingrese solo números y si son fraccionarios no use comas(,) use punto(.), ejemplo 2.33",  parent=ventana_perdidas_directas)
            ΣWs_p_di_texto.config(state="disabled")
        

    tk.Label(ventana_perdidas_directas, text="Vapor total perdido", font=("Arial", 9)).grid(row=8, column=0, sticky="nw", padx=(42,0), pady=(15,0))
    ΣWs_p_di_texto = tk.Text(ventana_perdidas_directas, width=23, height=1, font=("TkDefaultFont", 12, "bold"), state="disabled")
    ΣWs_p_di_texto.grid(row=9, column=0, sticky="nw", padx=(5,0), pady=(5,0))

    
    #boton para calcular la sumatoria  Vapor total perdido
    boton_sumatoria_p_di = tk.Button(ventana_perdidas_directas, text="Calcular ΣWs_p_di (kg)", font=("TkDefaultFont", 12, "bold"), width=20, height=1, command=lambda: calcular_sumatoria_p_di(ΣWs_p_d_texto, ΣWs_p_di_texto))
    boton_sumatoria_p_di.grid(row=10, column=0, sticky="nw", padx=(6,0), pady=(5,0))


    '''
    
    # Funcion equivalencia en combustible 
    def calcular_equivalencia_combustible(n, VCI, λvapor, PV, Tiempo, Wcombustible_texto, Wfcombustible_texto):
        messagebox.showinfo("En Construccion","Esta funcion aun se esta programando",  parent=ventana_perdidas_directas) 
    '''
    def calcular_equivalencia_combustible(n, VCI, λvapor, PV, Tiempo, Wcombustible_texto, Wfcombustible_texto, ΣWs_p_di_texto):
        try:
            # Obtener valores de las cajas de texto
            valor_n = float(n.get())
            valor_VCI = float(VCI.get())
            valor_λvapor = float(λvapor.get())
            valor_PV = float(PV.get())
            valor_Tiempo = float(Tiempo.get())
            valor_ΣWs_p_di_texto = float(ΣWs_p_di_texto.get("1.0", tk.END).strip())
           
            # Realizar la operación (Wcombustible_texto)
            resultado_Wcombustible_texto = (valor_ΣWs_p_di_texto * valor_λvapor)/(valor_n *  valor_VCI)
            Wcombustible_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wcombustible_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wcombustible_texto.insert(tk.END, f"{resultado_Wcombustible_texto}")
            Wcombustible_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (Wfcombustible_texto)
            resultado_Wfcombustible_texto = (resultado_Wcombustible_texto * valor_Tiempo)
            Wfcombustible_texto.config(state="normal")  # Habilitar temporalmente para editar
            Wfcombustible_texto.delete("1.0", tk.END)   # Borrar contenido previo
            Wfcombustible_texto.insert(tk.END, f"{resultado_Wfcombustible_texto}")
            Wfcombustible_texto.config(state="disabled") # Deshabilitar nuevamente 
        
        except ValueError:
            # Mostrar error en la caja de texto
            Wcombustible_texto.config(state="normal")
            Wcombustible_texto.delete("1.0", tk.END)
            Wcombustible_texto.insert(tk.END, "Error: ")
            Wcombustible_texto.config(state="disabled")
            
            Wfcombustible_texto.config(state="normal")
            Wfcombustible_texto.delete("1.0", tk.END)
            Wfcombustible_texto.insert(tk.END, "Error: ")
            messagebox.showerror("Error","Verifique que los calculos del valor total perdido este realizado, que las entradas de datos sean solo numeros y los fraccionarios esten representadoscon punto(.) no con coma(,), ejemplo 2.44 .",  parent=ventana_perdidas_directas)
            Wfcombustible_texto.config(state="disabled")
    

    
   
    # Creamos el marco Equivalencia en combustible
    marco_equivalencia_combustible = tk.Frame(ventana_perdidas_directas, bg="#dae3f3", borderwidth=1, relief="sunken", width=505, height=140)
    marco_equivalencia_combustible.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 6 columnas 
    marco_equivalencia_combustible.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_equivalencia_combustible.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_equivalencia_combustible.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_equivalencia_combustible.columnconfigure(3, weight=0)  # Columna 3 No se expande
    marco_equivalencia_combustible.columnconfigure(4, weight=0)  # Columna 4 No se expande
    marco_equivalencia_combustible.columnconfigure(5, weight=0)  # Columna 5 No se expande
    
    
    marco_equivalencia_combustible.grid(row=2, column=1, sticky="w", padx=5, pady=1)  # Con sticky="w" se alinea el marco a la izquierda
   
    
    
    # Cajas de texto para entrada de datos
    tk.Label(marco_equivalencia_combustible, text="ɳ:").grid(row=1, column=0, sticky="w", padx=(10,1), pady=5)
    n = tk.Entry(marco_equivalencia_combustible, width=10)
    n.grid(row=1, column=1, sticky="w", pady=5)
    
    tk.Label(marco_equivalencia_combustible, text="VCI(kJ/kg):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=5)
    VCI  = tk.Entry(marco_equivalencia_combustible, width=10)
    VCI.grid(row=2, column=1, sticky="w", padx=1, pady=5)
    
    tk.Label(marco_equivalencia_combustible, text="λvapor:").grid(row=3, column=0, sticky="w", padx=(10,1), pady=5)
    λvapor = tk.Entry(marco_equivalencia_combustible, width=10)
    λvapor.grid(row=3, column=1, sticky="w", padx=1, pady=5)
    
    tk.Label(marco_equivalencia_combustible, text="PV(barG):").grid(row=1, column=2, sticky="e", padx=(10,1), pady=5)
    PV = tk.Entry(marco_equivalencia_combustible, width=10)
    PV.grid(row=1, column=3, sticky="w", padx=1, pady=5)
    
    tk.Label(marco_equivalencia_combustible, text="Tiempo(h):").grid(row=2, column=2, sticky="w", padx=(10,1), pady=5)
    Tiempo = tk.Entry(marco_equivalencia_combustible, width=10)
    Tiempo.grid(row=2, column=3, sticky="w", padx=1, pady=5)
    
    tk.Label(marco_equivalencia_combustible, text="Wcombustible(kg):").grid(row=1, column=4, sticky="w", padx=(20,1), pady=5)
    Wcombustible_texto = tk.Text(marco_equivalencia_combustible, width=10, height=1, state="disabled")
    Wcombustible_texto.grid(row=1, column=5, sticky="w", pady=5)
    
    tk.Label(marco_equivalencia_combustible, text="Wcomustible(kg/h):").grid(row=2, column=4, sticky="e", padx=1, pady=5)
    Wfcombustible_texto = tk.Text(marco_equivalencia_combustible, width=10, height=1, state="disabled")
    Wfcombustible_texto.grid(row=2, column=5, sticky="w", padx=1, pady=5)

    
    
    
    # Creo el botón calcular para las pérdidas por orificio con llamada a función calcular_perdidas_orificios
    boton_equivalencia_combustible = tk.Button(marco_equivalencia_combustible, text="Calcular", command=lambda: calcular_equivalencia_combustible(n, VCI, λvapor, PV, Tiempo, Wcombustible_texto, Wfcombustible_texto, ΣWs_p_di_texto))
    boton_equivalencia_combustible.grid(row=4, column=0, sticky="w", padx=(10,1), pady=(10,1))



    # Funcion Perdidas economicas 
    def calcular_perdidas_economicas(Dn, Tt, CUP, USD, CUPk, USDk, CUP_texto, USD_texto, CUPa_texto, USDa_texto, Wfcombustible_texto, Wcombustible_texto):
        #messagebox.showinfo("En Construccion","Esta funcion aun se esta programando",  parent=ventana_perdidas_directas)
        try:
            # Obtener valores de las cajas de texto
            valor_Dn = float(Dn.get())
            valor_Tt = float(Tt.get())
            valor_CUP = float(CUP.get())
            valor_USD = float(USD.get())
            valor_CUPk = float(CUPk.get())
            valor_USDk = float(USDk.get())
            
            valor_Wfcombustible_texto = float(Wfcombustible_texto.get("1.0", tk.END).strip())
            valor_Wcombustible_texto = float(Wfcombustible_texto.get("1.0", tk.END).strip())
           
            # Realizar la operación (CUP_texto)
            resultado_CUP_texto = (valor_Wfcombustible_texto * valor_CUPk * valor_Tt)
            CUP_texto.config(state="normal")  # Habilitar temporalmente para editar
            CUP_texto.delete("1.0", tk.END)   # Borrar contenido previo
            CUP_texto.insert(tk.END, f"{resultado_CUP_texto}")
            CUP_texto.config(state="disabled") # Deshabilitar nuevamente

            # Realizar la operación (USD_texto)
            resultado_USD_texto = (valor_Wcombustible_texto * valor_USDk * valor_Tt)
            USD_texto.config(state="normal")  # Habilitar temporalmente para editar
            USD_texto.delete("1.0", tk.END)   # Borrar contenido previo
            USD_texto.insert(tk.END, f"{resultado_USD_texto}")
            USD_texto.config(state="disabled") # Deshabilitar nuevamente
           
            # Realizar la operación (CUPa_texto)
            resultado_CUPa_texto = (resultado_CUP_texto * 250)
            CUPa_texto.config(state="normal")  # Habilitar temporalmente para editar
            CUPa_texto.delete("1.0", tk.END)   # Borrar contenido previo
            CUPa_texto.insert(tk.END, f"{resultado_CUPa_texto}")
            CUPa_texto.config(state="disabled") # Deshabilitar nuevamente

            # Realizar la operación (USDa_texto)
            resultado_USDa_texto = (resultado_USD_texto * 250)
            USDa_texto.config(state="normal")  # Habilitar temporalmente para editar
            USDa_texto.delete("1.0", tk.END)   # Borrar contenido previo
            USDa_texto.insert(tk.END, f"{resultado_USDa_texto}")
            USDa_texto.config(state="disabled") # Deshabilitar nuevamente 
        
        except ValueError:
            # Mostrar error en la caja de texto
            CUP_texto.config(state="normal")
            CUP_texto.delete("1.0", tk.END)
            CUP_texto.insert(tk.END, "Error: ")
            CUP_texto.config(state="disabled")

            USD_texto.config(state="normal")
            USD_texto.delete("1.0", tk.END)
            USD_texto.insert(tk.END, "Error: ")
            USD_texto.config(state="disabled")

            CUPa_texto.config(state="normal")
            CUPa_texto.delete("1.0", tk.END)
            CUPa_texto.insert(tk.END, "Error: ")
            CUPa_texto.config(state="disabled")

            USDa_texto.config(state="normal")
            USDa_texto.delete("1.0", tk.END)
            USDa_texto.insert(tk.END, "Error: ")
            messagebox.showerror("Error","Verifique que los calculos en Equivalencia de combustible esten realizados, que las entradas de datos sean solo numeros y los fraccionarios esten representadoscon punto(.) no con coma(,), ejemplo 2.44 .",  parent=ventana_perdidas_directas)
            USDa_texto.config(state="disabled")
    
    # Creamos el marco Pérdida económica  
    marco_perdida_economica = tk.Frame(ventana_perdidas_directas, bg="#dae3f3", borderwidth=1, relief="sunken", width=505, height=125)
    marco_perdida_economica.grid_propagate(False)  # Importante: desactiva el ajuste automático
    
    # Defino que el marco va tener 6 columnas 
    marco_perdida_economica.columnconfigure(0, weight=0)  # Columna 0 No se expande
    marco_perdida_economica.columnconfigure(1, weight=0)  # Columna 1 No se expande
    marco_perdida_economica.columnconfigure(2, weight=0)  # Columna 2 No se expande
    marco_perdida_economica.columnconfigure(3, weight=0)  # Columna 3 No se expande
    marco_perdida_economica.columnconfigure(4, weight=0)  # Columna 4 No se expande
    marco_perdida_economica.columnconfigure(5, weight=0)  # Columna 5 No se expande
    

    marco_perdida_economica.grid(row=4, column=1, sticky="w", padx=5, pady=1)  # Con sticky="w" se alinea el marco a la izquierda

    # Cajas de texto para entrada de datos
    tk.Label(marco_perdida_economica, text="Dn(Kg/L):").grid(row=1, column=0, sticky="w", padx=(10,1), pady=5)
    Dn = tk.Entry(marco_perdida_economica, width=5)
    Dn.grid(row=1, column=1, sticky="w", pady=5)
    
    tk.Label(marco_perdida_economica, text="Tt(h/día/):").grid(row=2, column=0, sticky="w", padx=(10,1), pady=5)
    Tt  = tk.Entry(marco_perdida_economica, width=5)
    Tt.grid(row=2, column=1, sticky="w", padx=1, pady=5)

    tk.Label(marco_perdida_economica, text="Pc($/L/)-->").grid(row=3, column=0, sticky="w", padx=(10,1), pady=5)
    tk.Label(marco_perdida_economica, text="CUP:").grid(row=3, column=1, sticky="w", padx=(3,1), pady=5)
    CUP = tk.Entry(marco_perdida_economica, width=7)
    CUP.grid(row=3, column=1, sticky="w", padx=(35,1), pady=5)

    tk.Label(marco_perdida_economica, text="USD:").grid(row=3, column=1, sticky="w", padx=(85,1), pady=5)
    USD = tk.Entry(marco_perdida_economica, width=4)
    USD.grid(row=3, column=1, sticky="w",padx=(117,0), pady=5)

    tk.Label(marco_perdida_economica, text="Pc($/Kg)-->").grid(row=4, column=0, sticky="w", padx=(10,1), pady=5)
    tk.Label(marco_perdida_economica, text="CUP:").grid(row=4, column=1, sticky="w", padx=(3,1), pady=5)
    CUPk = tk.Entry(marco_perdida_economica, width=7)
    CUPk.grid(row=4, column=1, sticky="w", padx=(35,1), pady=5)

    tk.Label(marco_perdida_economica, text="USD:").grid(row=4, column=1, sticky="w", padx=(85,0), pady=5)
    USDk = tk.Entry(marco_perdida_economica, width=4)
    USDk.grid(row=4, column=1, sticky="w",padx=(117,0), pady=5)


    tk.Label(marco_perdida_economica, text="Ccp($/día)-->").grid(row=1, column=1, sticky="w", padx=(60,1), pady=5)
    tk.Label(marco_perdida_economica, text="CUP:").grid(row=1, column=2, sticky="e", padx=(1,0), pady=5)
    CUP_texto = tk.Text(marco_perdida_economica, width=12, height=1, state="disabled")
    CUP_texto.grid(row=1, column=3, sticky="w", padx=(3,1), pady=5)

    tk.Label(marco_perdida_economica, text="USD:").grid(row=1, column=4, sticky="e", padx=(1,0), pady=5)
    USD_texto = tk.Text(marco_perdida_economica, width=12, height=1, state="disabled")
    USD_texto.grid(row=1, column=5, sticky="w", padx=(3,1), pady=5)

    tk.Label(marco_perdida_economica, text="Ccp($/año)-->").grid(row=2, column=1, sticky="w", padx=(60,1), pady=5)
    tk.Label(marco_perdida_economica, text="CUP:").grid(row=2, column=2, sticky="e", padx=(1,0), pady=5)
    CUPa_texto = tk.Text(marco_perdida_economica, width=12, height=1, state="disabled")
    CUPa_texto.grid(row=2, column=3, sticky="w", padx=(3,1), pady=5)

    tk.Label(marco_perdida_economica, text="USD:").grid(row=2, column=4, sticky="e", padx=(1,0), pady=5)
    USDa_texto = tk.Text(marco_perdida_economica, width=12, height=1, state="disabled")
    USDa_texto.grid(row=2, column=5, sticky="w", padx=(3,1), pady=5)

    
    # Creo el botón calcular las perdidas economicas
    boton_perdidas_economicas = tk.Button(marco_perdida_economica, text="Calcular", command=lambda: calcular_perdidas_economicas(Dn, Tt, CUP, USD, CUPk, USDk, CUP_texto, USD_texto, CUPa_texto, USDa_texto, Wfcombustible_texto, Wcombustible_texto))
    boton_perdidas_economicas.grid(row=4, column=5, sticky="w", padx=(50,1), pady=(1,5)) 

    
   
  
    
    
    # Añadir validación al cerrar esta ventana secundaria
    def on_closing_child():
        if messagebox.askyesno("Confirmar cierre", f"¿Cerrar ventana de {titulo}?", parent=ventana_perdidas_directas):
            ventana_perdidas_directas.destroy()
    
    ventana_perdidas_directas.protocol("WM_DELETE_WINDOW", on_closing_child)
        
#"""Funcion que cierra la ventana principal root"""    
def confirmar_salir():
    """Muestra un cuadro de diálogo de confirmación para salir"""
    respuesta = messagebox.askyesno(
        "Confirmar salida",
        "¿Estás seguro de que quieres salir de la aplicación?\nSe cerrarán todas las ventanas."
    )
    if respuesta:
        root.destroy()


 
#""" Funcion que muestra la informacion de la ventana acerca de"""        
def mostrar_acerca_de():
    """Muestra información sobre la aplicación"""
    messagebox.showinfo(
        "Acerca de",
        "Calculadora EPV\n"
        "Versión 1.0\n"
        "Especialista Ing. Quimica Arianne Almaguer Mulet\n"
        "Telefono: 58075762\n"
        "Programador Ing.Automatico Orlando Orlandovich Serrano Zivienko\n"
        "Telefono: 52161864\n"
        "© 2025" 
    )    



# Crear ventana principal
root = tk.Tk()
root.title("Calculadora EPV")
root.geometry("910x145")
root.configure(bg="#b3cac7")

etiqueta = tk.Label(root, text="Aplicación de cálculo para la estimación de las pérdidas de vapor en procesos industriales y de servicios", font=("Arial", 13, "bold"), fg="#1A1A1A", bg="#dae3f3", borderwidth=0, relief="sunken")
etiqueta.pack(side="top", pady=5, anchor="center")  # 1px de espacio del menú

etiqueta1 = tk.Label(root, text="© Version Free ", font=("Arial", 11, "bold"), fg="gray", relief="sunken")
etiqueta1.pack(side="bottom", anchor="w", padx=1, pady=1)

# Boton de ayuda en el cuerpo de la ventana root
boton_ayuda = tk.Button(root, text="Ayuda para comenzar", command=ayuda_para_comenzar, font=("TkDefaultFont", 12, "bold"), fg="#1A1A1A", bg="#dae3f3")
boton_ayuda.pack(side="bottom", anchor="center")

# Configurar validación para el cierre de la ventana principal
root.protocol("WM_DELETE_WINDOW", confirmar_salir)



# Crear la barra de menú
menu_principal = tk.Menu(root)
menu_principal = tk.Menu(root, font=("Arial", 13))

# Menú Archivo
menu_archivo = tk.Menu(menu_principal, font=("Arial", 13), tearoff=0)
menu_archivo.add_command(label="Abrir", command=lambda: abrir_ventana("Abrir"))
menu_archivo.add_command(label="Guardar", command=lambda: abrir_ventana("Guardar"))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=confirmar_salir)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo, underline=0) # Se puede usar underline=0 es para subrayar la primera letra del Label y acceder a esta con alt + letra subrayada

# Menú Operaciones de Calculo
menu_clasificacion = tk.Menu(menu_principal, font=("Arial", 13), tearoff=0)
menu_clasificacion.add_command(label="Pérdidas Indirectas y Suplementarias", command=lambda: perdidas_indirectas("Perdidas Indirectas y Suplementarias"))
menu_clasificacion.add_command(label="Pérdidas Directas y Totales", command=lambda: perdidas_directas("Pérdidas Directas"))
menu_principal.add_cascade(label="Operaciones de Cálculo", menu=menu_clasificacion, underline=0)

# Menú Informacion y Ayuda
menu_informacion = tk.Menu(menu_principal, font=("Arial", 13), tearoff=0)
menu_informacion.add_command(label="Ayuda", command=abrir_ventana_ayuda)
menu_informacion.add_command(label="Acerca de", command=mostrar_acerca_de)
menu_principal.add_cascade(label="Información", menu=menu_informacion, underline=0)

# Configurar la barra de menú en la ventana principal
root.config(menu=menu_principal)

# Ejecutar el bucle principal
root.mainloop()

#Pendientes
'''
1) ademas de Poner un boton en cada tipo de perdida que de la opcion de un boton de calcular todo ( Valorar eso)
2) Poner el parametro underline a todos los submenus
3) Aclarar con el profe en las perdidas suplementarias lo del 15%, 20% y 25% aclarar que es mas el 15% y asi con los demas %
'''
