import tkinter
from tkinter import ttk
from tkinter import filedialog
from os.path import abspath

def main():
    icone = abspath('./ressources/logo.ico')
    fenetre = tkinter.Tk()
    fenetre.geometry("800x300")
    fenetre.iconbitmap(icone)
    fenetre.title("ArboCréa v3.1" + "                                           " +\
                                            "Créez simplement des arborescences " +\
                                    "personnalisés pour la gestion de vos affaires")
    systeme_onglet = ttk.Notebook(fenetre)
    systeme_onglet.pack()

    onglet = ttk.Frame(systeme_onglet)
    onglet.pack()

    systeme_onglet.add(onglet, text="A partir d'un modele")

    ecran_gauche = tkinter.LabelFrame(onglet,
                                    text="Source et destination du chantier",
                                    bd=2, padx=50, pady=50)

    lb_chemin_source_onglet = tkinter.Label(ecran_gauche, text="Chercher la source du modèle : ")
    chemin_acces_source_onglet = tkinter.StringVar()
    saisie_chemin_source_onglet = tkinter.Entry(ecran_gauche, textvariable=chemin_acces_source_onglet)
    btn_chemin_source_onglet = tkinter.Button(ecran_gauche, text="Rechercher")
    # , command=explorateur_source_onglet)

    lb_chemin_dest_onglet = tkinter.Label(ecran_gauche, text="Définir la destination de la copie : ")
    chemin_acces_dest_onglet = tkinter.StringVar()
    saisie_chemin_dest_onglet = tkinter.Entry(ecran_gauche, textvariable=chemin_acces_dest_onglet)
    btn_chemin_dest_onglet = tkinter.Button(ecran_gauche, text="Rechercher")
    # , command=explorateur_dest_onglet)

    lb_chemin_source_onglet.grid(row=0, column=0)
    saisie_chemin_source_onglet.grid(row=1, column=0)
    btn_chemin_source_onglet.grid(row=1, column=1)
    lb_chemin_dest_onglet.grid(row=2, column=0)
    saisie_chemin_dest_onglet.grid(row=3, column=0)
    btn_chemin_dest_onglet.grid(row=3, column=1)
    ecran_gauche.grid(row=0, column=0)



    ecran_droite = tkinter.LabelFrame(onglet,
                                    text="Saisir les informations du chantier",
                                    width=380, height=240, bd=2, padx=50, pady=50)

    lb_annee_onglet = tkinter.Label(ecran_droite, text="Année en 2 chiffres : ")
    annee_onglet = tkinter.IntVar()
    # annee_onglet.trace("w", create_auto)
    saisie_annee_onglet = tkinter.Entry(ecran_droite, textvariable=annee_onglet)
    saisie_annee_onglet.insert(0, "9")
    lb_num_onglet = tkinter.Label(ecran_droite, text="Numéro de l'affaire en 3 chiffres : ")
    num_chantier_onglet = tkinter.IntVar()
    # num_chantier_onglet.trace("w", create_auto)
    saisie_num_onglet = tkinter.Entry(ecran_droite, textvariable=num_chantier_onglet)
    saisie_num_onglet.insert(0, "66")
    lb_nom_onglet = tkinter.Label(ecran_droite, text="Nom du chantier : ")
    nom_chantier_onglet = tkinter.StringVar()
    # nom_chantier_onglet.trace("w", create_auto)
    saisie_nom_onglet = tkinter.Entry(ecran_droite, textvariable=nom_chantier_onglet)
    saisie_nom_onglet.insert(0, "Eiffel")

    lb_annee_onglet.grid(row=0, column=0)
    saisie_annee_onglet.grid(row=0, column=1)
    lb_num_onglet.grid(row=1, column=0)
    saisie_num_onglet.grid(row=1, column=1)
    lb_nom_onglet.grid(row=2, column=0)
    saisie_nom_onglet.grid(row=2, column=1)
    ecran_droite.grid(row=0, column=1)

    btn_crea_onglet = tkinter.Button(onglet, text="Creation des dossiers")
    # , command=create_manu_modele)
    btn_crea_onglet.grid(row=1, column=1)

    fenetre.mainloop()



def explorateur_source_onglet():
    global chemin_acces_source_onglet
    global src_onglet
    chemin = filedialog.askdirectory()
    chemin_acces_source_onglet.set(chemin)
    src_onglet = chemin
    src_onglet = src_onglet.replace("/", "\\\\")




main()