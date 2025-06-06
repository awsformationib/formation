![Logo](images\logo.png)

---
SQLAlchemy est compatible avec un grand nombre de **moteurs de base de données relationnelles** grâce à son architecture en "dialects". Voici un **tableau des principaux moteurs** compatibles avec SQLAlchemy, leur nom de dialecte, et leurs caractéristiques :

---

## ✅ Moteurs compatibles avec SQLAlchemy

| Moteur                   | Dialecte SQLAlchemy     | Connecteur Python recommandé         | Caractéristiques principales                 |
| ------------------------ | ----------------------- | ------------------------------------ | -------------------------------------------- |
| **SQLite**               | `sqlite://`             | Aucun (intégré à Python)             | Léger, fichier local, parfait pour tests     |
| **PostgreSQL**           | `postgresql://`         | `psycopg2`, `asyncpg`, `pg8000`      | Avancé, open-source, support JSON, Full-Text |
| **MySQL**                | `mysql://`              | `pymysql`, `mysqlclient`, `mariadb`  | Populaire, rapide, très utilisé en web       |
| **MariaDB**              | `mariadb://` (>=1.4)    | `mariadb` (connecteur natif)         | Fork communautaire de MySQL                  |
| **Oracle**               | `oracle://`             | `cx_Oracle` ou `oracledb`            | Entreprise, robuste, plus complexe           |
| **Microsoft SQL Server** | `mssql://`              | `pyodbc`, `pymssql`                  | Bonne intégration Windows, outil BI          |
| **Firebird**             | `firebird://`           | `fdb` ou `firebirdsql`               | Moins courant mais supporté                  |
| **Sybase**               | `sybase://`             | `pyodbc` (rarement utilisé)          | Obsolète dans de nombreux contextes          |
| **IBM DB2**              | `ibm_db_sa://`          | `ibm_db`                             | Supporté avec extension tierce               |
| **Snowflake**            | `snowflake://`          | `snowflake-sqlalchemy`               | Cloud data warehouse, via plugin             |
| **Google BigQuery**      | `bigquery://`           | `pybigquery` + `sqlalchemy-bigquery` | Cloud, via dialect externe                   |
| **CockroachDB**          | `cockroachdb://`        | `psycopg2` (PostgreSQL compatible)   | Résilient, SQL distribué                     |
| **DuckDB**               | `duckdb://`             | `duckdb-engine`                      | In-memory & local, idéal data science        |
| **Trino / Presto**       | `trino://`, `presto://` | `trino` ou `pyhive`                  | SQL distribué (OLAP), via dialect tiers      |
| **Redshift** (AWS)       | `redshift+psycopg2://`  | `psycopg2` (PostgreSQL compatible)   | Data warehouse cloud                         |

---

## 🔍 Exemples d'URL de connexion

| Base de données      | URL SQLAlchemy exemple                                                          |
| -------------------- | ------------------------------------------------------------------------------- |
| SQLite (fichier)     | `sqlite:///data.db`                                                             |
| PostgreSQL           | `postgresql+psycopg2://user:pwd@localhost/dbname`                               |
| MySQL (avec PyMySQL) | `mysql+pymysql://user:pwd@localhost/dbname`                                     |
| SQL Server (ODBC)    | `mssql+pyodbc://user:pwd@localhost/dbname?driver=ODBC+Driver+17+for+SQL+Server` |
| Oracle               | `oracle+cx_oracle://user:pwd@host:1521/dbname`                                  |

---

## ⚠️ Attention

* **Certains dialectes nécessitent des packages tiers** à installer (non inclus par défaut).
* Les dialectes les plus *robustes et maintenus officiellement* sont : **PostgreSQL, MySQL/MariaDB, SQLite**.
* Pour les moteurs *big data* ou *cloud* (Redshift, BigQuery, Snowflake), un **dialecte SQLAlchemy externe** est souvent requis.

---

