import logging
import sqlite3

import config

def creer_base(chemin):
    try:
        fullpath = config.PATHEXP / chemin
        if not fullpath.is_file():
        # Connexion à la base SQLite
            conn = sqlite3.connect(fullpath)
            cursor = conn.cursor()

            # Création de la table conforme à ta structure
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS vols (
                numero TEXT PRIMARY KEY,
                destination TEXT,
                avion TEXT,
                statut TEXT,
                heure_creation TEXT,
                heure_decollage TEXT,
                heure_arrivee TEXT
            )
            """)
            conn.commit()
            logging.debug(f"Base cree {fullpath}")
        else:
            logging.debug(f"Base deja existante {fullpath}")
    except Exception as ex:
        logging.error(ex)

def ouvrebase(chemin):
    fullpath = config.PATHEXP / chemin
    return sqlite3.connect(fullpath)

def lire_vol(cnx, numero):
    cursor = cnx.cursor()
    # Création de la table conforme à ta structure
    query = f"SELECT * FROM vols where numero='{numero}'"
    result = cursor.execute(query)
    x = result.fetchone()
    print("LU EN BASE ", x)

def lire_vols(cnx):
    cursor = cnx.cursor()
    # Création de la table conforme à ta structure
    query = f"SELECT * FROM vols"
    result = cursor.execute(query)
    return result.fetchall()

def ecrire_vol(cnx, obj):
    cursor = cnx.cursor()
    # Création de la table conforme à ta structure

    champs = tuple(obj.__dict__.keys())
    champs = [ "'" + str(obj.__getattribute__(champ)) + "'" for champ in champs]
    values = ",".join(champs)
    query = "INSERT INTO vols VALUES (" + values + ")"
    cursor.execute(query)
    cnx.commit()

