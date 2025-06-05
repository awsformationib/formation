import logging

import mysql.connector

def creer_base(conn):
    try:
    # Connexion à la base Mysql
        cursor = conn.cursor()
        # Création de la table conforme à ta structure
        cursor.execute("""
            CREATE TABLE vols (
                numero VARCHAR(10) PRIMARY KEY,
                destination VARCHAR(50),
                avion VARCHAR(50),
                statut VARCHAR(20),
                heure_creation DATETIME,
                heure_decollage DATETIME,
                heure_arrivee DATETIME
            );
        """)
        conn.commit()
        logging.debug(f"Base MySql cree")
    except Exception as ex:
        logging.error(ex)

def ouvrebase(host,login="root",pwd="", database="formation"):
    return mysql.connector.connect(
        host=host,
        user=login,
        password=pwd,
        database=database
    )

def lire_vols(cnx):
    cursor = cnx.cursor()
    query = f"SELECT * FROM vols"
    cursor.execute(query)
    return cursor.fetchall()

def ecrire_vol(cnx, obj):

    cursor = cnx.cursor()
    champs = tuple(obj.__dict__.keys())
    champs = [ "'" + str(obj.__getattribute__(champ)) + "'" for champ in champs]
    values = ",".join(champs)
    query = "INSERT INTO vols VALUES (" + values + ")"
    cursor.execute(query)
    cnx.commit()


