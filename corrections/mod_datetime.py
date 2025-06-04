import time
from datetime import datetime, timedelta

# Heure actuelle
now = datetime.now()

print(now)

# Affichage formaté
date1_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(now.strftime("%d %B %Y %H:%M"))

# Durée entre deux moments
start = datetime.now()
time.sleep(1)
end = datetime.now()
duree = end - start
print(duree.total_seconds(), "secondes écoulées")

d1_now = datetime.strptime(date1_str , "%Y-%m-%d %H:%M:%S")
date2_str = "2023-05-04"
d2_old = datetime.strptime(date2_str , "%Y-%m-%d")


difference = d1_now - d2_old
print(difference)

print(difference.days)

td = timedelta(difference.days / 2)
milieu = d2_old + td
print(milieu)


