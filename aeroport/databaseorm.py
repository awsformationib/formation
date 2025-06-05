import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

# PHASE DESCRIPTIVE
Base = declarative_base()

class VolORM(Base):
    __tablename__ = 'volsorm'

    numero = Column(String(10), primary_key=True)
    destination = Column(String(50))
    avion = Column(String(50))
    statut = Column(String(20))
    heure_creation = Column(DateTime)
    heure_decollage = Column(DateTime)
    heure_arrivee = Column(DateTime)

#PHASE ACTIVE

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Adapter avec vos identifiants
DATABASE_URL = "mysql+mysqlconnector://root:@localhost/formation"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

# 4. Créer la base si elle n'existe pas encore (optionnel)
Base.metadata.create_all(engine)

# 5. Créer une session
session = Session()

auj = datetime.datetime.now()
v= VolORM()
v.numero = "XYZZ2"

session.add(v)          # equivalent de insert into...
session.commit()

session.close()