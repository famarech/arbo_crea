from os import walk
from os.path import abspath
from os import mkdir
from shutil import copyfile

path_modele = abspath('./Modele/')
path_copie = abspath('./Copie/')

prototype = '00 999 Abcdef'
chantier = '33 654 Eiffel'


for root, dirs, files in walk(path_modele):

    for dir in dirs:
        dirpath = root + '/' + dir
        dirpath = dirpath.replace(path_modele, path_copie)
        dirpath = dirpath.replace(prototype, chantier)
        mkdir(dirpath)

    for file in files:
        filename_src = root + '/' + file
        filename_dst = filename_src.replace(path_modele, path_copie)
        filename_dst = filename_dst.replace(prototype, chantier)
        copyfile(filename_src, filename_dst)