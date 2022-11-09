#%% [markdown]
# ## Definimos clase para el mazo
import collections
import random

Carta = collections.namedtuple('Carta', ['numero', 'palo'])

class mazo:
    numeros = [str(n) for n in range(2, 11)] + list('JQKA')
    palos = 'espadas diamantes treboles corazones'.split()
    
    def __init__(self):
        self._cartas = [Carta(numero, palo) for palo in self.palos
                                            for numero in self.numeros]
        
    def __len__(self):
        return len(self._cartas)

    def __getitem__(self, posicion):
        return self._cartas[posicion]
    
    def shuffle(self):
        random.shuffle(self._cartas)


#%% [markdown]
# ## Simulacion 

mi_mazo = mazo()

n = 10000

num_favorables = 0
for i in range(n):
    mi_mazo.shuffle()
    as_uno, as_dos, as_tres, as_cuatro = [i +1 for i, c in enumerate(mi_mazo) if c.numero == 'A']
    favorable = all([as_uno <= 13, 
                     13 < as_dos <= 26 , 
                     26 < as_tres <= 39, 
                     39 <as_cuatro])
    
    num_favorables = num_favorables + favorable
    

proba = num_favorables / n

print(proba)

# %% 
