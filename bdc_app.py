import mongoengine as me
from bdc.model import (Municipi, FranjaHoraria, HorariDiari, Botiga,
                        TipusBotiga, Restaurant)
if __name__ == "__main__":
    # Connexió sobre la base de dades "boccato_di_cardinale".
    db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")

    db.drop_database("boccato_di_cardinale")

    # Creem dos objectes de tipus Botiga i un de tipus Restaurant, amb tots els
    # objectes referenciats i incrustats necessaris per completar-ne les dades.
    m1 = Municipi(nom="Folgueroles", codi_postal="08519")
    m2 = Municipi(nom="Taradell", codi_postal="08552")
    m3 = Municipi(nom="Toses", codi_postal="17536")

    t1 = TipusBotiga(nom="Forn", sinonims=["Fleca", "Forn de pa"])
    t2 = TipusBotiga(nom="Carnisseria", sinonims=["Cansaladeria", "Xarcuteria"])

    f1a = FranjaHoraria(hora_obertura="08:00", hora_tancament="13:30")
    f1b = FranjaHoraria(hora_obertura="16:30", hora_tancament="20:00")

    f2a = FranjaHoraria(hora_obertura="08:30", hora_tancament="13:30")
    f2b = FranjaHoraria(hora_obertura="17:00", hora_tancament="19:30")
    f2c = FranjaHoraria(hora_obertura="08:30", hora_tancament="14:00")

    f3a = FranjaHoraria(hora_obertura="09:00", hora_tancament="16:00")
    f3b = FranjaHoraria(hora_obertura="20:00", hora_tancament="22:00")

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

    e1 = Botiga(
        nom="Forn de Sant Jordi",
        coordenades=(2.318286, 41.938136),
        domicili="C. Atlàntida, 8",
        municipi=m1,
        localitat=None,
        lloc_web="http://www.cocadelmossen.cat",
        especialitats=["Coca de pa", "Coca de sucre", "Coca amb xocolata",
        "Coca de cabell d'àngel"],
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

    # Tanquem la connexió.
    me.disconnect()
