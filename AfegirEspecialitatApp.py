import mongoengine as me
import bdc.model as md  # Importa el model definit a la teva aplicació
import bdc.controller as ct

# Connexió a la base de dades "boccato_di_cardinale"
db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")

def afegir_especialitat_establiment(establiment, nova_especialitat):

    # Es comprova si la especialitat ja existeix. Sinó, s'afegeix.
    try:
        if nova_especialitat in establiment.especialitats: # Si l'especialitat es troba al array
            print("Aquesta especialitat ja existeix.")
            return False

        establiment.especialitats.append(nova_especialitat) #S'afegeix l'especialitat
        establiment.save()  # Desa els canvis a la base de dades
        return True
    except me.errors.OperationError as e:
        print(f"Error en afegir l'especialitat: {e}")
        return False


def mostrar_establiments():

    # Mostra una llista numerada de tots els establiments i retorna la llista.
    establiments = ct.obtenir_establiments()
    if not establiments: # Si no hi ha establiments.
        print("No hi ha establiments disponibles.")
        return None

    for i, establiment in enumerate(establiments, start=1): # Per cada establiment amb contador
        municipi = establiment.municipi.nom if establiment.municipi else "Desconegut"
        print(f"{i}. {establiment.nom} | {establiment.municipi.codi_postal} | {municipi}")

    return establiments


def afegir_especialitat():

    # Afegeix una especialitat a un establiment existent.

    establiments = mostrar_establiments()
    if not establiments: # Si no hi ha establiments
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
        nova_especialitat = input("\nIntrodueix la nova especialitat: ").strip()
        if nova_especialitat:
            break
        print("L'especialitat no pot estar buida.")

    # Afegeix l'especialitat a través de la funció del controlador
    if afegir_especialitat_establiment(establiment, nova_especialitat):
        print(f"Especialitat '{nova_especialitat}' afegida correctament")
    else:
        print("No s'ha pogut afegir l'especialitat.")


if __name__ == "__main__":
    afegir_especialitat()