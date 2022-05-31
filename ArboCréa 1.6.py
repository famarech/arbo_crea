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
    fenetre.title("ArboCréa v1.0" + "                                           " +\
                                            "Créez simplement des arborescences " +\
                                    "personnalisés pour la gestion de vos affaires")

    global systeme_onglet
    systeme_onglet = tkinter.ttk.Notebook(fenetre)
    systeme_onglet.pack()
    onglet1()
    onglet2()

    fenetre.mainloop()








def onglet1():

    # /-------------------\
    # |  onglet 1 gauche  |
    # \-------------------/

    global systeme_onglet
    global annee_onglet1
    global num_chantier_onglet1
    global nom_chantier_onglet1
    global chemin_acces_dest_onglet1

    onglet1 = tkinter.ttk.Frame(systeme_onglet, width=750, height=250)
    onglet1.pack()
    systeme_onglet.add(onglet1, text="Automatique")

    ecran_gauche = tkinter.LabelFrame(onglet1, text="Saisir les informations " +\
                    "du chantier", width=300, height=200, bd=2, padx=50, pady=50)

    lb_chemin_dest = tkinter.Label(ecran_gauche, text="Définir la destination")
    chemin_acces_dest_onglet1 = tkinter.StringVar()
    chemin_acces_dest_onglet1.trace("w", create_auto)
    saisie_chemin_dest = tkinter.Entry(ecran_gauche, textvariable=chemin_acces_dest_onglet1)
    btn_chemin_dest = tkinter.Button(ecran_gauche, text="Rechercher", command=explorateur_dest_onglet1)

    lb_annee_onglet1 = tkinter.Label(ecran_gauche, text="Année en 2 chiffres : ")
    annee_onglet1 = tkinter.IntVar()
    annee_onglet1.trace("w", create_auto)
    saisie_annee_onglet1 = tkinter.Entry(ecran_gauche, textvariable=annee_onglet1)
    saisie_annee_onglet1.insert(0, "9")

    lb_num = tkinter.Label(ecran_gauche, text="Numéro de l'affaire en 3 chiffres : ")
    num_chantier_onglet1 = tkinter.IntVar()
    num_chantier_onglet1.trace("w", create_auto)
    saisie_num = tkinter.Entry(ecran_gauche, textvariable=num_chantier_onglet1)
    saisie_num.insert(0, "66")

    lb_nom = tkinter.Label(ecran_gauche, text="Nom du chantier : ")
    nom_chantier_onglet1 = tkinter.StringVar()
    nom_chantier_onglet1.trace("w", create_auto)
    saisie_nom = tkinter.Entry(ecran_gauche, textvariable=nom_chantier_onglet1)
    saisie_nom.insert(0, "Eiffel")

    lb_chemin_dest.grid(row=0, column=0)
    saisie_chemin_dest.grid(row=1, column=1)
    btn_chemin_dest.grid(row=1, column=0)
    lb_annee_onglet1.grid(row=2, column=0)
    saisie_annee_onglet1.grid(row=2, column=1)
    lb_num.grid(row=3, column=0)
    saisie_num.grid(row=3, column=1)
    lb_nom.grid(row=4, column=0)
    saisie_nom.grid(row=4, column=1)
    ecran_gauche.grid(row=0, column=0)


    # /-------------------\
    # |  onglet 1 droite  |
    # \-------------------/

    ecran_droite = tkinter.LabelFrame(onglet1, text="Cocher les sous-dossiers " +\
                    "nécessaires", width=300, height=200, bd=2, padx=100, pady=22)

    global contrat
    global fournisseur
    global planning
    global etudes
    global prod
    global transport
    global sav

    contrat = tkinter.BooleanVar()
    contrat.set(True)
    check_contrat = tkinter.Checkbutton(ecran_droite, text="Contrats et Infos Clients", var=contrat)
    fournisseur = tkinter.BooleanVar()
    fournisseur.set(False)
    check_fournisseur = tkinter.Checkbutton(ecran_droite, text="Devis et Consultations", var=fournisseur)
    planning = tkinter.BooleanVar()
    planning.set(False)
    check_planning = tkinter.Checkbutton(ecran_droite, text="Planning, Gantt et PERT", var=planning)
    etudes = tkinter.BooleanVar()
    etudes.set(False)
    check_etudes = tkinter.Checkbutton(ecran_droite, text="Etudes et notes de calculs", var=etudes)
    prod = tkinter.BooleanVar()
    prod.set(True)
    check_prod = tkinter.Checkbutton(ecran_droite, text="Production", var=prod)
    transport = tkinter.BooleanVar()
    transport.set(False)
    check_transport = tkinter.Checkbutton(ecran_droite, text="Transports", var=transport)
    sav = tkinter.BooleanVar()
    sav.set(True)
    check_sav = tkinter.Checkbutton(ecran_droite, text="SAV", var=sav)

    check_contrat.pack()
    check_fournisseur.pack()
    check_planning.pack()
    check_etudes.pack()
    check_prod.pack()
    check_transport.pack()
    check_sav.pack()
    ecran_droite.grid(row=0, column=1)


    # /-------------------\
    # |  onglet 1 centre  |
    # \-------------------/

    btn_crea = tkinter.Button(onglet1, text="Creation des dossiers", command=create_auto)
    btn_crea.grid(row=1)








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

    onglet2 = tkinter.ttk.Frame(systeme_onglet, width=750, height=250)
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
    annee_onglet2.trace("w", create_auto)
    saisie_annee_onglet2 = tkinter.Entry(ecran_droite, textvariable=annee_onglet2)
    saisie_annee_onglet2.insert(0, "9")
    lb_num_onglet2 = tkinter.Label(ecran_droite, text="Numéro de l'affaire en 3 chiffres : ")
    num_chantier_onglet2 = tkinter.IntVar()
    num_chantier_onglet2.trace("w", create_auto)
    saisie_num_onglet2 = tkinter.Entry(ecran_droite, textvariable=num_chantier_onglet2)
    saisie_num_onglet2.insert(0, "66")
    lb_nom_onglet2 = tkinter.Label(ecran_droite, text="Nom du chantier : ")
    nom_chantier_onglet2 = tkinter.StringVar()
    nom_chantier_onglet2.trace("w", create_auto)
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
    # # # |                  |fonctions creation|       Auto       | # # #
    # # # \------------------|------------------|------------------/ # # #

def create_auto():
    global lecteur_onglet1
    year = annee_onglet1.get()
    number = num_chantier_onglet1.get()
    name = nom_chantier_onglet1.get()
    repertoire = str(year) + ' ' + str(number) + ' ' + name

    create_dir(lecteur_onglet1, repertoire)
    create_folder(lecteur_onglet1, repertoire)
    confirmation()


def create_dir(lecteur, repertoire):
    commande = 'mkdir "' + lecteur + '\\\\' + repertoire  + '"'
    print(commande)
    crea_dos = os.popen(commande)


def create_folder(lecteur, repertoire):
    i = 1
    folder = {"Contrat Infos Client": contrat.get(),
                "Devis Consultations": fournisseur.get(),
                "Planning": planning.get(),
                "Etudes": etudes.get(),
                "Production": prod.get(),
                "Transport": transport.get(),
                "SAV": sav.get()}

    for key, value in folder.items():
        print(key, ' : ', value)

    for key, value in folder.items():
        if value == True:
            sous_repertoire = '\\\\' + repertoire + '\\\\0' + str(i) + " " + key
            create_dir(lecteur, sous_repertoire)
            create_file(lecteur, repertoire, sous_repertoire)
        i += 1


def create_file(lecteur, repertoire, sous_repertoire):
    i = 1
    while i <=4:
        fichier = repertoire + ' fichier' + str(i) + '.txt'
        commande = 'echo > "' + lecteur + sous_repertoire  + '\\\\' + fichier + '"'
        print(commande)
        crea_dos = os.popen(commande)
        i += 1


def confirmation():
    # FAIRE UNE FONCTION QUI VERIFIE QUE TOUT A ETE COPIE
    confirmation = tkinter.Tk()
    confirmation.geometry("300x100")
    label_confirmation = tkinter.Label(confirmation, text="Votre arborescence à " +\
                                                                    "bien été créée")
    label_confirmation.pack()
    confirmation.mainloop()


def explorateur_dest_onglet1():
    global chemin_acces_dest_onglet1
    global lecteur_onglet1
    chemin = filedialog.askdirectory()
    chemin_acces_dest_onglet1.set(chemin)
    lecteur_onglet1 = chemin
    lecteur_onglet1 = lecteur_onglet1.replace("/", "\\\\")








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
    lecteur = src_onglet2

    year = annee_onglet2.get()
    number = num_chantier_onglet2.get()
    name = nom_chantier_onglet2.get()




    racine = '00 999 Abcdef'

    nouveau_lecteur = dest_onglet2

    nouvelle_racine = '\\' + str(year) + ' ' + str(number) + ' ' + name

    modele = recup_modele(lecteur, racine)
    print(modele)
    modele = formating(modele)

    ancien_modele = arborescence(modele, lecteur, racine)
    ancien_modele = fusion(ancien_modele)
    nouveau_modele = arborescence(modele, nouveau_lecteur, nouvelle_racine)
    nouveau_modele = replace_name(nouveau_modele, racine, nouvelle_racine)
    nouveau_modele = fusion(nouveau_modele)

    tab_de_commande = prepare_cmd(modele, ancien_modele, nouveau_modele)
    copie(tab_de_commande)


def launch_cmd(commande):
    cmd = os.popen(commande).read()
    return cmd


def recup_modele(lecteur, racine):
    commande = 'tree "' + lecteur + racine + '" /F /A | find "Structure" /V | find "Le num" /V'
    list = launch_cmd(commande)
    return list


def formating(list_dirty):
    retour_chariot = []
    for pos,char in enumerate(list_dirty):
        if(char == '\n'):
            retour_chariot.append(pos)

    list_clean = []
    size = len(retour_chariot) - 1
    i = 0
    while i < size:
        j = retour_chariot[i] + 1
        k = retour_chariot[i+1]
        str = []
        while j < k:
            str.append(list_dirty[j])
            j += 1
        list_clean.append(str)
        i += 1

    i = 0
    size_i = len(list_clean) - 1
    while i < size_i:
        j = 0
        size_j = len(list_clean[i]) - 1
        while j < size_j:
            if(list_clean[i][j] == '+'):
                list_clean[i][j] = '+'
            elif(list_clean[i][j] == '\\'):
                list_clean[i][j] = '+'
            elif(list_clean[i][j] == '-'):
                list_clean[i][j] = ' '
            elif(list_clean[i][j] == '|'):
                list_clean[i][j] = ' '
            j+= 1
        i += 1

    new_list_clean = []
    for pos in list_clean:
        str = []
        for char in pos:
            str.append(char)
        str = ''.join(str)
        new_list_clean.append(str)

    for pos in new_list_clean:
        if pos[len(pos) - 1] == " ":
            new_list_clean.remove(pos)

    return new_list_clean


def arborescence(arborescence, lecteur, racine):

    level_max = 0
    size = 0

    for pos in arborescence:
        if pos.find("+") >= 0:
            if level_max <= int(pos.find("+") / 4):
                level_max = int(pos.find("+") / 4)
        else:
            size += 1

    # level_max comprend tous les niveaux de dossiers + le niveau de fichier
    # y compris le lecteur et la racine
    # n0 pour lecteur + racine
    # nlevel_max pour fichier
    # de n1 à nlevelmax pour les dossiers et sous-dossiers
    # donc levelmax est au moins de 2

    level_max = level_max + 3
    arbo = []
    arbo = len(arborescence)*[0]
    for i in range(len(arbo)):
        arbo[i]=level_max*[0]

    #remplissage dossier
    i = 0
    while i < len(arborescence):
        arbo[i][0] = lecteur + racine
        if arborescence[i].find("+") >= 0:
            level = int(arborescence[i].find("+") / 4) + 1
            arbo[i][level] = arborescence[i]
        i += 1

    # remplissage fichier
    i = 0
    while i < len(arborescence):
        if arborescence[i].find("+") < 0:
            arbo[i][-1] = arborescence[i]
        i += 1

    # partie recursive A TRAVAILLER BORDEL
    i = 0
    while i < len(arbo):
        if arbo[i][1] == 0:
            arbo[i][1] =arbo[i-1][1]
        i += 1

    i = 0
    while i < len(arbo):
        if arbo[i-1][1] == arbo[i][1]:
            if arbo[i][2] == 0:
                arbo[i][2] = arbo[i-1][2]
        else:
            arbo[i][2] = 0
        i += 1

    arbo = clean_char(arbo, "+", "")
    arbo = clean_char(arbo, " ", "")
    arbo = clean_char(arbo, "+", "")
    arbo = clean_char(arbo, " ", "")

    return arbo


def clean_char(arborescence, char, new_char):
    # FAIRE UNE FONCTION RECURSIVE JUSQU'A CE QU'IL N'Y AI PLUS DE CHAR A ENLEVER
    # avec une variable d'arret qui indique qu'elle n'a rien trouvé
    i = 0
    while i < len(arborescence):
        j = 0
        while j < 4:
            if arborescence[i][j] != 0:
                k = 0
                while arborescence[i][j][k] == char:
                    k += 1
                arborescence[i][j] = arborescence[i][j].replace(char, new_char, k)
            j += 1
        i += 1
    return arborescence


def fusion(arborescence):
    arborescence = del_int_zero(arborescence)
    i = 0
    while i < len(arborescence):
        arborescence[i] = '\\\\'.join(arborescence[i])
        i += 1
    return arborescence


def del_int_zero(arborescence):
    i = 0
    while i < len(arborescence):
        # choppé sur internet, je comprends pas encore
        arborescence[i] = [elem for elem in arborescence[i] if elem != 0]
        i += 1
    return arborescence


def replace_name(arborescence, racine, nouvelle_racine):
    i = 0
    while i < len(arborescence):
        j = 0
        while j < 4:
            if arborescence[i][j] != 0:
                arborescence[i][j] = arborescence[i][j].replace(racine, nouvelle_racine, 1)
            j += 1
        i += 1
    return arborescence


def prepare_cmd(modele, ancien_modele, nouveau_modele):
    tab_de_commande = len(modele) * [0]
    i = 0
    while i < len(modele):
        tab_de_commande[i]=[0,0,0]
        i += 1

    i = 0
    while i < len(modele):

        if  modele[i].find("+") >= 0:
            tab_de_commande[i][0] = 'md'
            tab_de_commande[i][1] = nouveau_modele[i]
        else:
            tab_de_commande[i][0] = "cp"
            tab_de_commande[i][1] = ancien_modele[i]
            tab_de_commande[i][2] = nouveau_modele[i]
        i += 1

    tab_de_commande = del_int_zero(tab_de_commande)

    return tab_de_commande


def copie(tab_de_commande):
    i = 0
    while i < len(tab_de_commande):
        if tab_de_commande[i][0] == "md":
            commande = 'mkdir "' + tab_de_commande[i][1] + '"'
        elif tab_de_commande[i][0] == "cp":
            commande = 'copy /Y "' + tab_de_commande[i][1] + '" "' +\
                                            tab_de_commande[i][2] + '"'
        print(commande)
        launch_cmd(commande)
        i += 1


# nombre de fichier dans l'arborescence
# tree /F | find "90 660 Eiffel" /I /C
# pour vérifier entre les deux arborescences si tout est ok
# et si c'est bon, une fenetre de confirmation

# faire une fenetre pour le temps d'attente de la copie










main()