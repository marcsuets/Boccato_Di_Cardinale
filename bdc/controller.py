import mongoengine.errors
import bdc.model as md

import mongoengine as me


def obtenir_municipis():
    """
    Funció que retorna tots els municipis de la base de dades, ordenats per nom.

    :returns: llista d'objectes de tipus Municipi amb tots els municipis que tenim
              a la base de dades, ordenats per nom. En cas que es produeixi un
              error durant la realització de la consulta, es retornarà None.
    :rtype: [md.Municipi]
    """
    # Obtenim els municipis ordenats per nom.
    try:
        # Obtenim els municipis ordenats per nom.
        municipis = md.Municipi.objects.order_by("nom")
        return list(municipis)
    except Exception as e:
        print(f"Error obtenint municipis: {e}")
        return None


def obtenir_establiments_municipi(id_municipi=None):
    """
    Funció que retorna tots els establiments que hi ha en un municipi determinat.

    :param id_municipi: identificador del municipi sobre el qual volem fer la consulta.

    :return: llista d'objectes de tipus Establiment amb tots els establiments que tenim
              a la base de dades que es troben en el municipi indicat. En cas que es
              produeixi un error durant la realització de la consulta, es retornarà None.

    :rtype: [md.Establiment]
    """

    try:
        if id_municipi is None:
            # Si no es proporciona cap identificador, es retornen tots els establiments
            establiments = md.Establiment.objects.order_by("nom")
        else:
            # Es filtra per municipi.
            establiments = md.Establiment.objects(municipi=id_municipi).order_by("nom")
        return list(establiments)
    except Exception as e:
        print(f"Error obtenint establiments per al municipi {id_municipi}: {e}")
        return None

def obtenir_establiments():
    """
    Retorna una llista d'establiments ordenats per nom.

    :return: Llista d'objectes Establiment o None si hi ha un error.
    """
    try:
        return list(md.Establiment.objects.order_by("nom"))
    except me.errors.OperationError as e:
        print(f"Error accedint a la base de dades: {e}")
        return None

