import pandas as pd
from pathlib import Path
import openpyxl
import datetime as dt
import numpy as np
import yaml

hoy = dt.datetime.today().date()


rng = pd.bdate_range(start='1/22/2024', end='2/08/2024')


s = pd.Series(index = rng, name='cupones')



print(rng)








