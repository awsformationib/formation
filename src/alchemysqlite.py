from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Base en mémoire (volatile)
engine = create_engine("sqlite:///:memory:", echo=True)

# OU base persistante dans un fichier local
# Base SQLite dans un fichier local
DATABASE_FILE = "ma_base_de_vols.sqlite"
engine = create_engine(f"sqlite:///{DATABASE_FILE}", echo=True)

# Création des tables
def init_db():
    Base.metadata.create_all(engine)