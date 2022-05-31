from os import walk
from os.path import abspath
from os import mkdir
from os import rename
from shutil import copyfile

path_modele = abspath('./Modele/')
path_copie = abspath('./Copie/')

prototype = '00 999 Abcdef'
chantier = '22 666 Montparnasse'


for root, dirs, files in walk(path_modele):
    # print(root)
    # print(dirs)
    # print(files)
    # print()

    for dir in dirs:
        dirpath = root + '/' + dir
        dirpath = dirpath.replace(path_modele, path_copie)
        dirpath = dirpath.replace(prototype, chantier)
        print(dirpath)
        mkdir(dirpath)

    # for file in files:
    #     filename_src = root + '/' + file
    #     filename_dst = filename_src.replace(path_modele, path_copie)
    #     filename_dst = filename_dst.replace(prototype, chantier)
    #     print(filename_src)
    #     print(filename_dst)
    #     print()
    #     rename(filename_src, filename_dst)

    for file in files:
        filename_src = root + '/' + file
        filename_dst = filename_src.replace(path_modele, path_copie)
        filename_dst = filename_dst.replace(prototype, chantier)
        print(filename_src)
        print(filename_dst)
        print()
        copyfile(filename_src, filename_dst)