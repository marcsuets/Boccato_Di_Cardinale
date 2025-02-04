import mongoengine as me
import bdc.model as md  # Importa el model definit a la teva aplicació

# Connexió a la base de dades "boccato_di_cardinale"
db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")


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


def afegir_especialitat_establiment(establiment, nova_especialitat):
    """
    Afegeix una nova especialitat a un establiment existent.

    :param establiment: Objecte Establiment seleccionat.
    :param nova_especialitat: Especialitat a afegir.
    :return: True si s'ha afegit correctament, False si ja existia.
    """
    try:
        if nova_especialitat in establiment.especialitats:
            print("Aquesta especialitat ja existeix.")
            return False

        establiment.especialitats.append(nova_especialitat)
        establiment.save()  # Desa els canvis a la base de dades
        return True
    except me.errors.OperationError as e:
        print(f"Error en afegir l'especialitat: {e}")
        return False


def mostrar_establiments():
    """
    Mostra una llista numerada de tots els establiments i retorna la llista.
    """
    establiments = obtenir_establiments()
    if not establiments:
        print("No hi ha establiments disponibles.")
        return None

    for i, establiment in enumerate(establiments, start=1):
        municipi = establiment.municipi.nom if establiment.municipi else "Desconegut"
        print(f"{i}. {establiment.nom} | {establiment.municipi.codi_postal} | {municipi}")

    return establiments


def afegir_especialitat():
    """
    Permet afegir una especialitat a un establiment existent.
    """
    establiments = mostrar_establiments()
    if not establiments:
        return

    while True:
        try:
            index = int(input("\nIntrodueix el número de l'establiment a modificar: ")) - 1
            if 0 <= index < len(establiments):
                break  # Sortim del bucle si el número és vàlid
            else:
                print("Número no vàlid. Torna a intentar-ho.")
        except ValueError:
            print("Entrada no vàlida. Introdueix un número.")

    establiment = establiments[index]
    print(f"\nHas seleccionat: {establiment.nom}")

    # Mostra especialitats actuals
    print("\nEspecialitats actuals:")
    if establiment.especialitats:
        for i, esp in enumerate(establiments[index].especialitats, start=1):
            print(f"  {i}. {esp}")
    else:
        print("  (No té especialitats actualment)")

    # Demana la nova especialitat
    while True:
        nova_especialitat = input("\n➕ Introdueix la nova especialitat: ").strip()
        if nova_especialitat:
            break
        print("L'especialitat no pot estar buida.")

    # Afegeix l'especialitat a través de la funció del controlador
    if afegir_especialitat_establiment(establiment, nova_especialitat):
        print(f"Especialitat '{nova_especialitat}' afegida correctament!")
    else:
        print("No s'ha pogut afegir l'especialitat.")


if __name__ == "__main__":
    afegir_especialitat()