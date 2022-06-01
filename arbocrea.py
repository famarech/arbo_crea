import tkinter
from tkinter import ttk
from tkinter import filedialog
from os.path import abspath
from os import walk
from os import mkdir
from shutil import copyfile



    # # # /------------------|------------------|------------------\ # # #
    # # # |                  |variables globales|                  | # # #
    # # # \------------------|------------------|------------------/ # # #

global chemin_acces_source
global annee_onglet2
global num_chantier_onglet2
global nom_chantier_onglet2




    # # # /------------------|------------------|------------------\ # # #
    # # # |                  |fenetre principale|                  | # # #
    # # # \------------------|------------------|------------------/ # # #

def main():
    fenetre = tkinter.Tk()
    fenetre.geometry("800x300")
    icone = abspath('./Ressources/logo.ico')
    try:
        fenetre.iconbitmap(icone)
    except:
        pass
    fenetre.title("ArboCréa v3.2" + "                                           " +\
                                            "Créez simplement des arborescences " +\
                                    "personnalisés pour la gestion de vos affaires")
    global systeme_onglet
    systeme_onglet = ttk.Notebook(fenetre)
    systeme_onglet.pack()
    onglet2()
    fenetre.mainloop()




def onglet2():

    # /-------------------\
    # |  onglet 2 gauche  |
    # \-------------------/

    global systeme_onglet
    global annee_onglet2
    global num_chantier_onglet2
    global nom_chantier_onglet2
    global chemin_acces_source_onglet2
    global chemin_acces_dest_onglet2

    onglet2 = ttk.Frame(systeme_onglet, width=750, height=250)
    onglet2.pack()
    systeme_onglet.add(onglet2, text="A partir d'un modele")

    ecran_gauche = tkinter.LabelFrame(onglet2,
                                    text="Source et destination du chantier",
                                    width=300, height=200, bd=2, padx=50, pady=50)

    lb_chemin_source_onglet2 = tkinter.Label(ecran_gauche, text="Chercher la source du modèle : ")
    chemin_acces_source_onglet2 = tkinter.StringVar()
    chemin_acces_source_onglet2.set(abspath('./Ressources/Modele/'))
    saisie_chemin_source_onglet2 = tkinter.Entry(ecran_gauche, textvariable=chemin_acces_source_onglet2)
    btn_chemin_source_onglet2 = tkinter.Button(ecran_gauche, text="Rechercher", command=explorateur_source_onglet2)

    lb_chemin_dest_onglet2 = tkinter.Label(ecran_gauche, text="Définir la destination de la copie : ")
    chemin_acces_dest_onglet2 = tkinter.StringVar()
    saisie_chemin_dest_onglet2 = tkinter.Entry(ecran_gauche, textvariable=chemin_acces_dest_onglet2)
    btn_chemin_dest_onglet2 = tkinter.Button(ecran_gauche, text="Rechercher", command=explorateur_dest_onglet2)

    lb_chemin_source_onglet2.grid(row=0, column=0)
    saisie_chemin_source_onglet2.grid(row=1, column=0)
    btn_chemin_source_onglet2.grid(row=1, column=1)
    lb_chemin_dest_onglet2.grid(row=2, column=0)
    saisie_chemin_dest_onglet2.grid(row=3, column=0)
    btn_chemin_dest_onglet2.grid(row=3, column=1)
    ecran_gauche.grid(row=0, column=0)

    # /-------------------\
    # |  onglet 2 droite  |
    # \-------------------/

    ecran_droite = tkinter.LabelFrame(onglet2,
                                    text="Saisir les informations du chantier",
                                    width=300, height=200, bd=2, padx=50, pady=50)

    lb_nom_onglet2 = tkinter.Label(ecran_droite, text="Nom du chantier : ")
    nom_chantier_onglet2 = tkinter.StringVar()
    saisie_nom_onglet2 = tkinter.Entry(ecran_droite, textvariable=nom_chantier_onglet2)
    saisie_nom_onglet2.insert(0, "99 666 Eiffel")

    lb_nom_onglet2.grid(row=2, column=0)
    saisie_nom_onglet2.grid(row=2, column=1)
    ecran_droite.grid(row=0, column=1)

    # /-------------------\
    # |  onglet 2 centre  |
    # \-------------------/

    btn_crea_onglet2 = tkinter.Button(onglet2, text="Creation des dossiers", command=create_manu_modele)
    btn_crea_onglet2.grid(row=1, column=1)




    # # # /------------------|------------------|------------------\ # # #
    # # # |                  |fonctions creation|      Manuel      | # # #
    # # # \------------------|------------------|------------------/ # # #

def explorateur_source_onglet2():
    global chemin_acces_source_onglet2
    global src_onglet2
    chemin = filedialog.askdirectory()
    chemin_acces_source_onglet2.set(chemin)
    src_onglet2 = chemin

def explorateur_dest_onglet2():
    global chemin_acces_dest_onglet2
    global dest_onglet2
    chemin = filedialog.askdirectory()
    chemin_acces_dest_onglet2.set(chemin)
    dest_onglet2 = chemin

def create_manu_modele():

    path_modele = chemin_acces_source_onglet2.get()
    path_copie = chemin_acces_dest_onglet2.get()

    prototype = '00 999 Abcdef'
    chantier = nom_chantier_onglet2.get()

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




main()