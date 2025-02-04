import mongoengine as me
import bdc.controller as ct

# Connexió a la base de dades
db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")

def eliminar_especialitat_establiment(establiment, index_especialitat):
    try:
        if index_especialitat < 0 or index_especialitat >= len(establiment.especialitats):
            print(" Número d'especialitat no vàlid.")
            return False

        especialitat_eliminada = establiment.especialitats.pop(index_especialitat)
        establiment.save()  # Desa els canvis a la base de dades
        print(f" Especialitat '{especialitat_eliminada}' eliminada correctament!")
        return True
    except me.errors.OperationError as e:
        print(f" Error en eliminar l'especialitat: {e}")
        return False


def mostrar_establiments():
    establiments = ct.obtenir_establiments()
    if not establiments:
        print(" No hi ha establiments disponibles.")
        return None

    for i, establiment in enumerate(establiments, start=1):
        municipi = establiment.municipi.nom if establiment.municipi else "Desconegut"
        print(f"{i}. {establiment.nom} | {establiment.municipi.codi_postal} | {municipi}")
    return establiments

def eliminar_especialitat():
    # Mostrem establiments a l'usuari
    establiments = mostrar_establiments()
    if not establiments:
        return

    # L'usuari selecciona l'establiment
    while True:
        try:
            index = int(input("\n Introdueix el número de l'establiment a modificar: ")) - 1
            if 0 <= index < len(establiments):
                break
            print(" Número no vàlid. Torna a provar.")
        except ValueError:
            print("️ Entrada no vàlida. Introdueix un número.")

    establiment = establiments[index]
    print(f"\n Has seleccionat: {establiment.nom}")

    # Si l'establiment no te especialitats
    if not establiment.especialitats:
        print("️ Aquest establiment no té especialitats actualment.")
        return

    # Mostrem especialitats del establiment que ha seleccionat l'usuari
    print("\n Especialitats actuals:")
    for i, esp in enumerate(establiment.especialitats, start=1):
        print(f"  {i}. {esp}")

    # Demanem al usuari l'especialitat que vol eliminar
    while True:
        try:
            index_especialitat = int(input("\n Introdueix el número de l'especialitat a eliminar: ")) - 1
            if 0 <= index_especialitat < len(establiment.especialitats):
                break
            print(" Número no vàlid. Torna a provar.")
        except ValueError:
            print("️ Entrada no vàlida. Introdueix un número.")

    # Crida la funció d'eliminar especialitat passant-hi el establiment i numero d'especialitat
    eliminar_especialitat_establiment(establiment, index_especialitat)


if __name__ == "__main__":

    # Aquesta funcio es crida i fa tot el procés cridant d'altres
    # funcions. Tant del mateix arxiu com del controller.
    eliminar_especialitat()