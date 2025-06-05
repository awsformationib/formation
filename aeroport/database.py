from abc import ABC, abstractmethod

import logging
import mysql.connector
import sqlite3
import config

class SqlGenerique(ABC):

    def __init__(self, **params):
        self.params = params
        self.cnx = None

    def __del__(self):
        try :
            if self.cnx:
                self.cnx.close()
                logging.info("Connextion Base fermee")
        except:
            logging.error("Connexion NON fermee")

    @abstractmethod

    def ouvrebase(self):
        pass

    @abstractmethod
    def creer_base(self):
        pass

    @abstractmethod
    def lire_vols(self):
        pass

    @abstractmethod
    def ecrire_vol(obj):
        pass

# ----

class VolSqlLite(SqlGenerique):
    def creer_base(self):
        try:
            chemin = self.params["chemin"]
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

    def ouvrebase(self):
        fullpath = config.PATHEXP / self.params["chemin"]
        self.cnx = sqlite3.connect(fullpath)

    def lire_vol(self,cnx, numero):
        cursor = cnx.cursor()
        # Création de la table conforme à ta structure
        query = f"SELECT * FROM vols where numero='{numero}'"
        result = cursor.execute(query)
        return result.fetchone()


    def lire_vols(self,cnx):
        cursor = cnx.cursor()
        # Création de la table conforme à ta structure
        query = f"SELECT * FROM vols"
        result = cursor.execute(query)
        return result.fetchall()

    def ecrire_vol(self,cnx, obj):
        cursor = cnx.cursor()
        # Création de la table conforme à ta structure

        champs = tuple(obj.__dict__.keys())
        champs = [ "'" + str(obj.__getattribute__(champ)) + "'" for champ in champs]
        values = ",".join(champs)
        query = "INSERT INTO vols VALUES (" + values + ")"
        cursor.execute(query)
        cnx.commit()

class VolMySql(SqlGenerique):

    def ouvrebase(self):
        if not self.cnx:
            self.cnx = mysql.connector.connect(
                host=self.params["host"],
                user=self.params["login"],
                password=self.params["password"],
                database=self.params["database"]
            )

    def creer_base(self):
        try:
            self.ouvrebase()
        # Connexion à la base Mysql
            cursor = self.cnx.cursor()
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
            self.cnx.commit()
            logging.debug(f"Base MySql cree")
        except Exception as ex:
            logging.error(ex)




    def lire_vols(self):
        self.ouvrebase()
        cursor = self.cnx.cursor()
        query = f"SELECT * FROM vols"
        cursor.execute(query)
        return cursor.fetchall()

    def ecrire_vol(self, obj):
        self.ouvrebase()
        cursor = self.cnx.cursor()
        champs = tuple(obj.__dict__.keys())
        champs = [ "'" + str(obj.__getattribute__(champ)) + "'" for champ in champs]
        values = ",".join(champs)
        query = "INSERT INTO vols VALUES (" + values + ")"
        cursor.execute(query)
        self.cnx.commit()
