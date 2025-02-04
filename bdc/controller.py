import mongoengine.errors
import bdc.model as md


def obtenir_municipis():
    """
    Funció que retorna tots els municipis de la base de dades, ordenats per nom.

    :returns: llista d'objectes de tipus Municipi amb tots els municipis que tenim
              a la base de dades, ordenats per nom. En cas que es produeixi un
              error durant la realització de la consulta, es retornarà None.
    :rtype: [md.Municipi]
    """



def obtenir_establiments_municipi(id_municipi=None):
    """
    Funció que retorna tots els establiments que hi ha en un municipi determinat.

    :param id_municipi: identificador del municipi sobre el qual volem fer la consulta.

    :return: llista d'objectes de tipus Establiment amb tots els establiments que tenim
              a la base de dades que es troben en el municipi indicat. En cas que es
              produeixi un error durant la realització de la consulta, es retornarà None.

    :rtype: [md.Establiment]
    """

