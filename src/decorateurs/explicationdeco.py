import random
from functools import wraps


def controlvaleurs(fonction):
    @wraps(fonction)
    def fonction_modifiee(*args, **kwargs): # universelle
        print('DEBUT')
        res = fonction(*args,**kwargs)
        if res<0:
            res = 0
        print('FIN')
        return res

    return fonction_modifiee


@controlvaleurs
def fct_original(v):
    print("ORIGINAL")
    return random.randint(-180,180) * v

@controlvaleurs
def fct_autre(v,w,x):
    print("ORIGINAL")
    return random.randint(-18,18) * v * (w+x)

#fct_original = mon_decorateur(fct_original)

for _ in range(10):
    print(fct_autre(8,x=5, w=2))
    print(fct_autre.__name__)

for _ in range(10):
    print(fct_original(8))
    print(fct_original.__name__)












