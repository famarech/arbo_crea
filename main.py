from os import listdir
from os.path import abspath

path_modele = abspath('./Modele/').replace('\\', '/')
path_copie = abspath('./Copie/').replace('\\', '/')

print(listdir(path_modele))