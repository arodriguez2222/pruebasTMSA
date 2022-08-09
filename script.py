import pandas as pd
import numpy as np
from pathlib import Path

base = Path.cwd()
baseDir = base / 'data'
file = baseDir / 'PSO20220223.xls'
data = pd.read_excel(file,sheet_name=1)

data2 = data.groupby(['linea','sentido','tipodia','trayecto']).agg({'tr_optimo':'min','tr_minimo':'min','tr_maximo':'max','nodo_1':'first','nodo_2':'last'})
data2.rename(columns={'trayecto':'sublinea','nodo_2':'ultimo'},inplace=True)
data2.to_csv('resultadoprueba.csv')
print("realizado")