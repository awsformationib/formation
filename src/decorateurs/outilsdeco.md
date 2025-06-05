
# 🧩 Fiche Python – Décorateurs `benchmark` et `checker`

## 🎯 Objectif

Créer deux décorateurs réutilisables :

1. `@benchmark` – pour mesurer le temps d'exécution d'une fonction
2. `@checker` – pour vérifier les **types et noms** des arguments d'une fonction, utile pour la robustesse

---

## 📦 Structure générale d’un décorateur

Un décorateur est une **fonction qui prend une fonction en argument et retourne une nouvelle fonction** :

```
def mon_decorateur(fonction):
    def fonction_modifiee(*args, **kwargs):
        # code avant
        resultat = fonction(*args, **kwargs)
        # code après
        return resultat
    return fonction_modifiee
```

---

## ⏱️ 1. Décorateur `@benchmark`

### ✅ Usage

```
@benchmark
def operation():
    # traitement
```

### 🧪 Code

```
import time
from functools import wraps

def benchmark(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"[Benchmark] {f.__name__} exécutée en {(end - start):.6f} secondes")
        return result
    return wrapper
```

### 🧪 Exemple d’utilisation

```
@benchmark
def simulate_task(n):
    total = 0
    for i in range(n):
        total += i
    return total
```

---

## ✅ 2. Décorateur `@checker` (contrôle des types et noms attendus)

### ✅ Usage

```
@checker(expected_args={'x': int, 'y': int})
def addition(x, y):
    return x + y
```

### 🧪 Code

```
from functools import wraps
import inspect

def checker(expected_args: dict):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            for name, expected_type in expected_args.items():
                if name not in bound_args.arguments:
                    raise ValueError(f"[Checker] Argument manquant : {name}")
                if not isinstance(bound_args.arguments[name], expected_type):
                    raise TypeError(f"[Checker] Mauvais type pour '{name}': attendu {expected_type.__name__}, reçu {type(bound_args.arguments[name]).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### 🧪 Exemple

```
@checker(expected_args={'x': int, 'y': float})
def calcul(x, y):
    return x * y

# calcul(3, 2.5)  # ✅ OK
# calcul("abc", 2.5)  # ❌ TypeError
```

---

## 🧠 Bonus : Empiler les décorateurs

```
@benchmark
@checker(expected_args={'n': int})
def traitement(n):
    return sum(range(n))
```

---

## 📌 Résumé

| Décorateur   | Utilité                              | Avantages                    |
| ------------ | ------------------------------------ | ---------------------------- |
| `@benchmark` | Mesurer temps d’exécution            | Simple, utile pour profiling |
| `@checker`   | Valider types d’appel d’une fonction | Débogage rapide, pédagogique |
