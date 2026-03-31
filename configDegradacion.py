from pathlib import Path

#Configuración de una serie de experimentos de formación de redes
#--------- Directorios para guardar resultados -----------
home_path = Path.home()
BASE_DIR = str(home_path) + "/Repositorios/ResultadosCN/"
DEGRADACION_DIR = BASE_DIR + "Degradacion"
#Configuración de una serie de experimentos de degradación de redes
#-------DEGRADACION------------
TIPO_DEGRADACION=["Fallas","Ataques"]  # Tipo de degradación: "Fallas", "Ataques"
SAVE_STEP=4                 #Cada cuántos ataques registra medidas