
from dataclasses import dataclass
from typing import Union

class Personnel:
    pass

class NonNaviguant:
    pass


@dataclass(init=True, repr=True, frozen=True)
class Pilote:
    login: str
    rang: str
    password:str

    def est_correct(self, pwd) -> Union[True, None]:
        if not pwd:
            return None
        return self.password == pwd


if __name__=="__main__":
    p = Pilote("manon","pilote principal","12345")
    p2 = Pilote("manon","pilote principal","12345")
    print(p)
    print(p==p2)
    print(p.login)
    print(p.est_correct("12345"))