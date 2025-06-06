from vol import Vol, StatutVol
from piste import Piste

class Affectation:
    def __init__(self, vol: Vol, piste: Piste):
        self.vol = vol
        self.piste = piste

    def effectuer(self) -> None:
        if not self.piste.occupee and self.vol.statut == StatutVol.PREVU:
            self.piste.occuper()
            self.vol.decoller()

    def liberer(self) -> None:
        if self.vol.statut == StatutVol.EN_COURS:
            self.vol.atterrir()
            self.piste.liberer()

    def __str__(self) -> str:
        return f"Affectation : {self.vol.numero} ←→ {self.piste.numero}"
