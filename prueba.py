import os
# os.rename("./archivos/indicadores_dengue_diario_distrito.xlsx", "./archivos/holi.xlsx")
from datetime import datetime


dt = datetime.now()
str_time = dt.strftime("%d-%m-%Y-%H-%M-%S")
os.rename("./archivos/holi.xlsx", f"./archivos/dengue-diario{str_time}.xlsx")

