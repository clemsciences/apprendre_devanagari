# -*- coding: cp1252 -*-


from PIL import Image, ImageTk
# import Image
import tkinter as tk
# import ImageTk
import random
import os


def conversion(fichier):
    dico = {}
    with open(fichier) as f:
        texte = f.read()
        l_texte = texte.split("\n")
        for i in l_texte:
            # print i
            t = i.split(" ")

            dico[t[0]] = t[1]
    return dico


class Apprentissage:
    def __init__(self, chemin, dictionnaire):
        os.chdir(chemin)
        self.photos = os.listdir("photos")
        self.dictionnaire = dictionnaire

        self.fen1 = tk.Tk()
        self.fen1.title("Apprentissage")
        tk.Label(self.fen1, text="""Cliquez sur le bouton "PROCHAIN" pour faire apparaître le prochain caractère \n""",
                 fg='red').grid(row=0)
        self.C = tk.Canvas(self.fen1)
        self.D = tk.Canvas(self.fen1)

        self.nom_photo = random.choice(self.photos)
        print(self.nom_photo)

        a = Image.open(os.path.join("photos", self.nom_photo))
        b = a.size
        c = Image.open(os.path.join("photos_alpha", "alpha_" + self.nom_photo))
        d = c.size

        self.image = ImageTk.PhotoImage(a)
        self.image_alpha = ImageTk.PhotoImage(c)

        self.C.create_image(b[0], b[1], image=self.image)
        self.D.create_image(d[0], d[1], image=self.image_alpha)
        self.C.grid(row=1, column=0)
        self.D.grid(row=1, column=1)

        tk.Button(self.fen1, text="PROCHAIN", command=self.prochain).grid(row=2, column=0)
        # self.chaine1 = tk.Label(self.fen1)
        # self.chaine1.grid(row=3)
        tk.Button(self.fen1, text="QUITTER", command=self.fen1.destroy).grid(row=3)
        # Choix de l'image
        # self.chaine1.configure(text=self.dictionnaire[self.nom_photo])
        self.fen1.mainloop()

    def prochain(self):
        self.nom_photo = random.choice(self.photos)
        # self.chaine1.configure(text=self.dictionnaire[self.nom_photo])
        a = Image.open(os.path.join("photos", self.nom_photo))
        b = a.size
        c = Image.open(os.path.join("photos_alpha", "alpha_" + self.nom_photo))
        d = c.size
        self.image = ImageTk.PhotoImage(a)
        self.image_alpha = ImageTk.PhotoImage(c)
        self.C.create_image(b[0], b[1], image=self.image)
        self.D.create_image(d[0], d[1], image=self.image_alpha)
        # self.chaine1.configure(text=self.dictionnaire[self.nom_photo])


if __name__ == "__main__":
    Apprentissage(os.getcwd(), conversion("dico_devanagari.txt"))
