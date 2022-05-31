import os


class Fichier:

    def __init__(self, path, file):
        self.path = path.replace('\\', '/')
        self.file = file
        self.extension = self.file[self.file.index('.'):]
        self.year = self.file.split(' ')[0]
        self.number = self.file.split(' ')[1]
        self.site = self.file.split(' ')[2]
        self.name = self.file.split(' ')[3].replace(self.extension, '')



modele = 'C:/00 999 Abcdef'
copie_du_modele = 'C:/22 666 Eiffel'
arborescence = []
fichiers = []

for root, dir, files in os.walk(modele):
    arborescence.append(root.replace(modele, '').replace('\\', '/'))
    for file in files:
        fichiers.append(Fichier(root.replace(modele, ''), file))

del arborescence[0]
os.mkdir(copie_du_modele)
for dir in arborescence:
    # print(copie_du_modele + '/' + dir)
    os.mkdir(copie_du_modele + dir)


for file in fichiers:
    # file_in et file_out

    file.year = '22'
    file.number = '666'
    file.site = 'Eiffel'
    file_in = file.year + ' ' +\
                file.number + ' ' +\
                file.site + ' ' +\
                file.name +\
                file.extension
    open(copie_du_modele + file.path + '/' + file_in, 'a').close()





# attention il créer les fichiers alors qu'il faudrait les copier !!!!!


