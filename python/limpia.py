#%%
from pathlib import Path
import re

archivo = Path('/home/ger/GerDrive/Documentos/UNAM/proba/docs/notas/Probabilidad_1.tex')


texto = re.sub(r'[\r\n][\r\n]{2,}', '\n\n', archivo.read_text())

#with archivo.open() as f:
#    for linea in f.readlines():
#        print(f"{len(linea)} -- " + linea)
#


archivo_salida =  Path('/home/ger/GerDrive/Documentos/UNAM/proba/docs/notas/notas_de_proba_1.tex')

archivo_salida.write_text(texto)




# %%
