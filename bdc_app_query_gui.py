import tkinter as tk
import ttkbootstrap as ttk
import mongoengine as me
import bdc.controller as ct
import bdc.model as md


def click_boto_sortir():
    me.disconnect()
    bdc.destroy()


def seleccio_municipi(evt):
    # Obtenim els establiments del municipi seleccionat.
    seleccionat = llista_municipis.focus()
    value = llista_municipis.item(seleccionat)["values"][0]
    establiments = ct.obtenir_establiments_municipi(int(value[1:6]))

    # Eliminem els establiments que hi pogués haver a la llista.
    llista_establiments.delete(*llista_establiments.get_children())

    # Afegim els establiments del municipi seleccionat, posant (B) si és una botiga,
    # o (R) si és un restaurant.
    for est in establiments:
        if isinstance(est, md.Botiga):
            llista_establiments.insert("", "end", values=("(B) %s" % est.nom,))
        elif isinstance(est, md.Restaurant):
            llista_establiments.insert("", "end", values=("(R) %s" % est.nom,))


if __name__ == "__main__":

    # Inicialitzacions generals de la GUI.
    bdc = ttk.Window(themename="yeti")
    bdc.title("Boccato di Cardinale")
    amplada = 1000
    altura = 700
    screen_width = bdc.winfo_screenwidth()
    screen_height = bdc.winfo_screenheight()
    x = (screen_width / 2) - (amplada / 2)
    y = (screen_height / 2) - (altura / 2)
    bdc.geometry('%dx%d+%d+%d' % (amplada, altura, x, y - 25))
    boto_quit = ttk.Button(bdc, text="Sortir de l'aplicació", command=click_boto_sortir)
    boto_quit.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    # Creació de les llistes i inserció de dades a la llista de municipis.

    # Connexió sobre la base de dades "boccato_di_cardinale".
    db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")

    # Creació de la llista de municipis i de la llista d'establiments.
    llista_municipis = ttk.Treeview(
            bdc, show="", columns=[0], height=15, selectmode='browse')
    llista_establiments = ttk.Treeview(
            bdc, show="", columns=[0], height=10, selectmode='browse')

    # Posem tots els municipis a la llista de municipis.
    municipis = ct.obtenir_municipis()
    for mun in municipis:
        llista_municipis.insert("", "end", values=[mun])

    # Configurem les llistes per a la seva visualització i resposta a esdeveniments.
    llista_municipis.place(relx=0.5, rely=0.05, anchor=tk.N, relw=0.5)
    llista_municipis.bind('<<TreeviewSelect>>', seleccio_municipi)
    llista_establiments.place(relx=0.5, rely=0.55, anchor=tk.N, relw=0.9)

    bdc.mainloop()
