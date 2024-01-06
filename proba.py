import pandas
from pathlib import Path
import openpyxl


for i, fo in enumerate(Path.cwd().iterdir()):
	print(i, fo.name)


