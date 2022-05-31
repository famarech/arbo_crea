# pyinstaller --onefile --windowed '.\ArboCréa 1.6.py'
import tkinter
import os
from tkinter import ttk
from tkinter import filedialog








    # # # /------------------|------------------|------------------\ # # #
    # # # |                  |variables globales|                  | # # #
    # # # \------------------|------------------|------------------/ # # #

global annee_onglet1
global num_chantier_onglet1
global nom_chantier_onglet1
global contrat
global fournisseur
global planning
global etudes
global prod
global transport
global sav
global chemin_acces_source
global chemin_acces_dest_onglet1
global lecteur_onglet1
global annee_onglet2
global num_chantier_onglet2
global nom_chantier_onglet2








    # # # /------------------|------------------|------------------\ # # #
    # # # |                  |fenetre principale|                  | # # #
    # # # \------------------|------------------|------------------/ # # #

def main():
    fenetre = tkinter.Tk()
    fenetre.geometry("800x300")
    # fenetre.iconbitmap("G:\Reconversion Pro\00_formations\Formation Python appronfondie\Projet ArboCréa\logo.ico")
    fenetre.title("ArboCréa v3.1" + "                                           " +\
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

    ecran_gauche = tkinter.LabelFrame(onglet2, text="Source et destination" +\
                    "du chantier", width=300, height=200, bd=2, padx=50, pady=50)

    lb_chemin_source_onglet2 = tkinter.Label(ecran_gauche, text="Chercher la source du modèle : ")
    chemin_acces_source_onglet2 = tkinter.StringVar()
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

    ecran_droite = tkinter.LabelFrame(onglet2, text="Saisir les informations " +\
                    "du chantier", width=300, height=200, bd=2, padx=50, pady=50)

    lb_annee_onglet2 = tkinter.Label(ecran_droite, text="Année en 2 chiffres : ")
    annee_onglet2 = tkinter.IntVar()
    # annee_onglet2.trace("w", create_auto)
    saisie_annee_onglet2 = tkinter.Entry(ecran_droite, textvariable=annee_onglet2)
    saisie_annee_onglet2.insert(0, "9")
    lb_num_onglet2 = tkinter.Label(ecran_droite, text="Numéro de l'affaire en 3 chiffres : ")
    num_chantier_onglet2 = tkinter.IntVar()
    # num_chantier_onglet2.trace("w", create_auto)
    saisie_num_onglet2 = tkinter.Entry(ecran_droite, textvariable=num_chantier_onglet2)
    saisie_num_onglet2.insert(0, "66")
    lb_nom_onglet2 = tkinter.Label(ecran_droite, text="Nom du chantier : ")
    nom_chantier_onglet2 = tkinter.StringVar()
    # nom_chantier_onglet2.trace("w", create_auto)
    saisie_nom_onglet2 = tkinter.Entry(ecran_droite, textvariable=nom_chantier_onglet2)
    saisie_nom_onglet2.insert(0, "Eiffel")

    lb_annee_onglet2.grid(row=0, column=0)
    saisie_annee_onglet2.grid(row=0, column=1)
    lb_num_onglet2.grid(row=1, column=0)
    saisie_num_onglet2.grid(row=1, column=1)
    lb_nom_onglet2.grid(row=2, column=0)
    saisie_nom_onglet2.grid(row=2, column=1)
    ecran_droite.grid(row=0, column=1)

    # /-------------------\
    # |  onglet 2 centre  |
    # \-------------------/

    btn_crea_onglet2 = tkinter.Button(onglet2, text="Creation des dossiers", command=create_manu_modele)
    btn_crea_onglet2.grid(row=1)









    # # # /------------------|------------------|------------------\ # # #
    # # # |                  |fonctions creation|      Manuel      | # # #
    # # # \------------------|------------------|------------------/ # # #

def explorateur_source_onglet2():
    global chemin_acces_source_onglet2
    global src_onglet2
    chemin = filedialog.askdirectory()
    chemin_acces_source_onglet2.set(chemin)
    src_onglet2 = chemin
    src_onglet2 = src_onglet2.replace("/", "\\\\")


def explorateur_dest_onglet2():
    global chemin_acces_dest_onglet2
    global dest_onglet2
    chemin = filedialog.askdirectory()
    chemin_acces_dest_onglet2.set(chemin)
    dest_onglet2 = chemin
    dest_onglet2 = dest_onglet2.replace("/", "\\\\")

def create_manu_modele():
    return 0

main()