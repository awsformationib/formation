import json
import uuid
from datetime import datetime

from aeroport.avions import Avion
from aeroport.vols import Vol, StatutVol

# VOL -> (ENCODER) -> JSON
class VolEncoder(json.JSONEncoder):
    def default(self, obj):
        cname = obj.__class__.__name__.lower()
        match cname:
            case 'vol':
                return {
                    "numero": obj.numero,
                    "destination": obj.destination,
                    "statut": self.default(obj.statut),
                    "avion" : self.default(obj.avion)
                }
            case "avion":
                return {
                    "id": obj.id,
                    "immatriculation":obj.immatriculation,
                    "vitesse" : obj.vitesse
                }
            case "statutvol":
                return obj.value
            case "datetime":
                return obj.strftime("%Y-%m-%d %H:%M:%S")
        return super().default(obj)



