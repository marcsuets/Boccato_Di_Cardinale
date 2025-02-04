import mongoengine as me
from bdc.model import (Municipi, FranjaHoraria, HorariDiari, Botiga,
                       TipusBotiga, Restaurant, Establiment)

print("Carregant el mòdul.....: %s" % __name__)

if __name__ == "__main__":

    # Connexió sobre la base de dades "boccato_di_cardinale".
    db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")

    db.drop_database("boccato_di_cardinale")

    # Creem uns quants objectes a la base de dades, amb tots els
    # objectes referenciats i incrustats necessaris per completar-ne les dades.
    m1 = Municipi(nom="Folgueroles", codi_postal="08519")
    m2 = Municipi(nom="Taradell", codi_postal="08552")
    m3 = Municipi(nom="Toses", codi_postal="17536")
    m4 = Municipi(nom="Odèn", codi_postal="25283")
    m5 = Municipi(nom="Solsona", codi_postal="25280")
    m6 = Municipi(nom="Les Llosses", codi_postal="17512")

    t1 = TipusBotiga(nom="Forn", sinonims=["Fleca", "Forn de pa"])
    t2 = TipusBotiga(nom="Carnisseria", sinonims=["Cansaladeria", "Xarcuteria"])
    t3 = TipusBotiga(nom="Botiga casa de pagès", sinonims=["Agrobotiga de poble", "Botiga de poble"])
    t4 = TipusBotiga(nom="Pastisseria", sinonims=["Confiteria", "Rebosteria"])

    f1a = FranjaHoraria(hora_obertura="08:00", hora_tancament="13:30")
    f1b = FranjaHoraria(hora_obertura="16:30", hora_tancament="20:00")
    f2a = FranjaHoraria(hora_obertura="08:30", hora_tancament="13:30")
    f2b = FranjaHoraria(hora_obertura="17:00", hora_tancament="19:30")
    f2c = FranjaHoraria(hora_obertura="08:30", hora_tancament="14:00")
    f3a = FranjaHoraria(hora_obertura="09:00", hora_tancament="16:00")
    f3b = FranjaHoraria(hora_obertura="20:00", hora_tancament="22:00")
    f4a = FranjaHoraria(hora_obertura="09:00", hora_tancament="20:00")
    f5a = FranjaHoraria(hora_obertura="08:00", hora_tancament="13:00")
    f5b = FranjaHoraria(hora_obertura="17:00", hora_tancament="20:00")
    f6a = FranjaHoraria(hora_obertura="08:30", hora_tancament="14:00")
    f6b = FranjaHoraria(hora_obertura="17:00", hora_tancament="20:00")
    f6c = FranjaHoraria(hora_obertura="08:30", hora_tancament="14:30")
    f6d = FranjaHoraria(hora_obertura="17:00", hora_tancament="20:30")
    f7a = FranjaHoraria(hora_obertura="08:00", hora_tancament="20:00")
    f8a = FranjaHoraria(hora_obertura="08:30", hora_tancament="13:30")
    f8b = FranjaHoraria(hora_obertura="17:00", hora_tancament="20:00")
    f9a = FranjaHoraria(hora_obertura="09:00", hora_tancament="14:00")
    f9b = FranjaHoraria(hora_obertura="16:00", hora_tancament="19:00")

    h1dl = HorariDiari(dia=1, franges=None)
    h1dm = HorariDiari(dia=2, franges=[f1a, f1b])
    h1dc = HorariDiari(dia=3, franges=[f1a, f1b])
    h1dj = HorariDiari(dia=4, franges=[f1a, f1b])
    h1dv = HorariDiari(dia=5, franges=[f1a, f1b])
    h1ds = HorariDiari(dia=6, franges=[f1a, f1b])
    h1dg = HorariDiari(dia=7, franges=[f1a])

    h2dl = HorariDiari(dia=1, franges=None)
    h2dm = HorariDiari(dia=2, franges=[f2a, f2b])
    h2dc = HorariDiari(dia=3, franges=[f2a, f2b])
    h2dj = HorariDiari(dia=4, franges=[f2a, f2b])
    h2dv = HorariDiari(dia=5, franges=[f2c, f2b])
    h2ds = HorariDiari(dia=6, franges=[f2c])
    h2dg = HorariDiari(dia=7, franges=None)

    h3dl = HorariDiari(dia=1, franges=[f3a])
    h3dm = HorariDiari(dia=2, franges=None)
    h3dc = HorariDiari(dia=3, franges=[f3a])
    h3dj = HorariDiari(dia=4, franges=[f3a])
    h3dv = HorariDiari(dia=5, franges=[f3a, f3b])
    h3ds = HorariDiari(dia=6, franges=[f3a, f3b])
    h3dg = HorariDiari(dia=7, franges=[f3a])

    h4dl = HorariDiari(dia=1, franges=[f4a])
    h4dm = HorariDiari(dia=2, franges=[f4a])
    h4dc = HorariDiari(dia=3, franges=[f4a])
    h4dj = HorariDiari(dia=4, franges=[f4a])
    h4dv = HorariDiari(dia=5, franges=[f4a])
    h4ds = HorariDiari(dia=6, franges=[f4a])
    h4dg = HorariDiari(dia=7, franges=[f4a])

    h5dl = HorariDiari(dia=1, franges=[f5a, f5b])
    h5dm = HorariDiari(dia=2, franges=[f5a, f5b])
    h5dc = HorariDiari(dia=3, franges=[f5a, f5b])
    h5dj = HorariDiari(dia=4, franges=[f5a, f5b])
    h5dv = HorariDiari(dia=5, franges=[f5a, f5b])
    h5ds = HorariDiari(dia=6, franges=[f5a, f5b])
    h5dg = HorariDiari(dia=7, franges=[f5a, f5b])

    h6dl = HorariDiari(dia=1, franges=None)
    h6dm = HorariDiari(dia=2, franges=[f6a, f6b])
    h6dc = HorariDiari(dia=3, franges=[f6a, f6b])
    h6dj = HorariDiari(dia=4, franges=[f6a, f6b])
    h6dv = HorariDiari(dia=5, franges=[f6a, f6b])
    h6ds = HorariDiari(dia=6, franges=[f6a, f6d])
    h6dg = HorariDiari(dia=7, franges=[f6c])

    h7dl = HorariDiari(dia=1, franges=[f7a])
    h7dm = HorariDiari(dia=2, franges=[f7a])
    h7dc = HorariDiari(dia=3, franges=[f7a])
    h7dj = HorariDiari(dia=4, franges=[f7a])
    h7dv = HorariDiari(dia=5, franges=[f7a])
    h7ds = HorariDiari(dia=6, franges=[f7a])
    h7dg = HorariDiari(dia=7, franges=None)

    h8dl = HorariDiari(dia=1, franges=[f8a, f8b])
    h8dm = HorariDiari(dia=2, franges=[f8a, f8b])
    h8dc = HorariDiari(dia=3, franges=[f8a, f8b])
    h8dj = HorariDiari(dia=4, franges=[f8a, f8b])
    h8dv = HorariDiari(dia=5, franges=[f8a, f8b])
    h8ds = HorariDiari(dia=6, franges=[f8a, f8b])
    h8dg = HorariDiari(dia=7, franges=None)

    h9dl = HorariDiari(dia=1, franges=[f9a, f9b])
    h9dm = HorariDiari(dia=2, franges=[f9a, f9b])
    h9dc = HorariDiari(dia=3, franges=[f9a, f9b])
    h9dj = HorariDiari(dia=4, franges=[f9a, f9b])
    h9dv = HorariDiari(dia=5, franges=[f9a, f9b])
    h9ds = HorariDiari(dia=6, franges=[f9a, f9b])
    h9dg = HorariDiari(dia=7, franges=[f9a, f9b])

    e1 = Botiga(
        nom="Forn de Sant Jordi",
        coordenades=(2.318286, 41.938136),
        domicili="C. Atlàntida, 8",
        municipi=m1,
        localitat=None,
        lloc_web="http://www.cocadelmossen.cat",
        especialitats=["Coca de pa", "Coca de sucre", "Coca amb xocolata", "Coca de cabell d'àngel"],
        observacions=None,
        actiu=True,
        telefons=["93 888 72 25"],
        emails=["info@cocadelmossen.cat"],
        horari=[h1dl, h1dm, h1dc, h1dj, h1dv, h1ds, h1dg],
        tipus=t1
    ).save(cascade=True)

    e2 = Botiga(
        nom="Carnisseria cansaladeria Codina",
        coordenades=(2.287847, 41.873690),
        domicili="C. de Sant Sebastià, 18",
        municipi=m2,
        localitat=None,
        lloc_web="https://carnisseriacodina.cat",
        especialitats=["Botifarra d'ou", "Llonganissa", "Bull de ratafia amb tòfona"],
        observacions=None,
        actiu=True,
        telefons=["93 880 11 75"],
        emails=["info@carnisseriacodina.com"],
        horari=[h2dl, h2dm, h2dc, h2dj, h2dv, h2ds, h2dg],
        tipus=t2
    ).save(cascade=True)

    e3 = Restaurant(
        nom="Can Casanova",
        coordenades=(2.047425, 42.323665),
        domicili="Camí de Toses, 2",
        municipi=m3,
        localitat="Fornells de la Muntanya",
        lloc_web="https://www.restaurantcancasanova.cat/ca",
        especialitats=["Escudella barrejada", "Carn d'olla"],
        observacions="Veure detalls de l'oferta gastronòmica a la web.",
        actiu=True,
        telefons=["972 73 60 75", "972 73 63 01"],
        emails=None,
        horari=[h3dl, h3dm, h3dc, h3dj, h3dv, h3ds, h3dg],
        oferta_gastronomica=["Menú diari (laborables)", "Carta",
                             "Carta de temporada", "Menús de grup"]
    ).save(cascade=True)

    e4 = Botiga(
        nom="La Botiga de ca l'Àngel",
        coordenades=(1.387033, 42.133716),
        domicili="Ctra. de Solsona a Cambrils, 31, vora l'església",
        municipi=m4,
        localitat="Cambrils",
        lloc_web="https://www.instagram.com/botigacalangel/",
        especialitats=["Patates de cambrils", "Llonganissa", "Varietat de productes locals"],
        observacions="Consultar l'horari abans d'anar-hi",
        actiu=True,
        telefons=["697 586 952", "973 489 015"],
        emails=[],
        horari=[h4dl, h4dm, h4dc, h4dj, h4dv, h4ds, h4dg],
        tipus=t3
    ).save(cascade=True)

    e5 = Botiga(
        nom="Pastisseria Sant Antoni",
        coordenades=(1.519312, 41.994773),
        domicili="C. Sant Llorenç, 3 i 6",
        municipi=m5,
        localitat=None,
        lloc_web=None,
        especialitats=["Coca de croissant", "Coca de cabell d'àngel"],
        observacions=None,
        actiu=True,
        telefons=["973 48 02 92"],
        emails=[],
        horari=[h5dl, h5dm, h5dc, h5dj, h5dv, h5ds, h5dg],
        tipus=t4
    ).save(cascade=True)

    e6 = Botiga(
        nom="Pastisseria can Massana",
        coordenades=(1.518224, 41.994378),
        domicili="Pl. Major, 7",
        municipi=m5,
        localitat=None,
        lloc_web="http://pastisseriacanmassana.cat",
        especialitats=["Coca de croissant", "Coca de cabell d'àngel"],
        observacions=None,
        actiu=True,
        telefons=["973 48 01 69"],
        emails=["info@pastisseriacanmassana.cat"],
        horari=[h6dl, h6dm, h6dc, h6dj, h6dv, h6ds, h6dg],
        tipus=t4
    ).save(cascade=True)

    e7 = Botiga(
        nom="Forn de pa Cal Jaumet del Forn",
        coordenades=(1.518019, 41.994633),
        domicili="C. de la Mare de Déu, 4",
        municipi=m5,
        localitat=None,
        lloc_web=None,
        especialitats=["Pa"],
        observacions=None,
        actiu=True,
        telefons=["973 48 08 07"],
        emails=["jaumetdelforndesolsona@gmail.com"],
        horari=[h7dl, h7dm, h7dc, h7dj, h7dv, h7ds, h7dg],
        tipus=t1
    ).save(cascade=True)

    e8 = Botiga(
        nom="Carnisseria Teresa",
        coordenades=(1.518537, 41.994304),
        domicili="Pl. Major, 4",
        municipi=m5,
        localitat=None,
        lloc_web="https://www.instagram.com/carnisseria_teresa",
        especialitats=["Botifarra negra", "Botifarra negra amb ceba"],
        observacions="Tenen botiga al carrer de la Bòfia, 9, Solsona, 973 48 28 50 - 621 125 096",
        actiu=True,
        telefons=["973 48 02 64", "621 295 265"],
        emails=None,
        horari=[h8dl, h8dm, h8dc, h8dj, h8dv, h8ds, h8dg],
        tipus=t1
    ).save(cascade=True)

    e9 = Botiga(
        nom="Mas el Lladré",
        coordenades=(2.088247, 42.160687),
        domicili="Mas el Lladré",
        municipi=m6,
        localitat="Santa Maria de Matamala",
        lloc_web="https://www.masellladre.cat",
        especialitats=["Flams d'ou, de mató i de cafè", "Pastís de formatge",
                       "Llonganissa", "Costella de porc", "Mató"],
        observacions="Acostumen a atendre fora de l'horari establert. Ofereixen venda online.",
        actiu=True,
        telefons=["650 960 865", "620 278 194", "620 070 413"],
        emails=["info@masellladre.cat"],
        horari=[h9dl, h9dm, h9dc, h9dj, h9dv, h9ds, h9dg],
        tipus=t3
    ).save(cascade=True)

    # Tanquem la connexió.
    me.disconnect()
