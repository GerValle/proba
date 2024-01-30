#%%
from pathlib import Path

working_dir = Path('/home/ger/Insync/german.valle.trujillo@gmail.com/OneDrive/unam/proba/docs/presentacion')

archivo_a_limpiar = working_dir / 'proba_1.tex'
archivo_limpio = working_dir / 'proba_1_limpio.tex'

#%%


def remove_duplicate_blank_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        previous_line = None
        for line in infile:
            # Skip repeated blank lines
            if not line.isspace() or line != previous_line:
                outfile.write(line)
            previous_line = line


remove_duplicate_blank_lines(archivo_a_limpiar, archivo_limpio)

#%%

with open(archivo_a_limpiar, 'r') as infile:
    previous_line = None
    for i,  line in enumerate(infile):
        # Skip repeated blank lines
        if line != '\n' or line != previous_line:
            print(line)
        previous_line = line


#%%



# %%
