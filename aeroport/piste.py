from dataclasses import dataclass

@dataclass
class Piste:
    numero: str
    longueur: int
    occupee: bool = False

    def occuper(self) -> None:
        self.occupee = True

    def liberer(self) -> None:
        self.occupee = False

    def __str__(self) -> str:
        etat = "occupée" if self.occupee else "libre"
        return f"Piste {self.numero} ({self.longueur}m) – {etat}"
