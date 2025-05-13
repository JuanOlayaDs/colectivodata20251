import pandas as pd
analisisUsuarios=pd.read_excel("./data/usuarios_sistema_completo.xlsx")

medellin = analisisUsuarios[analisisUsuarios['direccion'].str.contains('medellin', case=False)]
print(medellin)
