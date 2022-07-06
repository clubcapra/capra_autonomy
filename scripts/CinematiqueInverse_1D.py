import CinematiqueDirecte

#constante
v = 1

#pose initiale
x0=0

#pose finale
x1=10

#calcul trajectoire
x = x1-x0 

#calcul du temps pour la commande
t = x/v

t0 = time.now

while time.now > t0
    avancer(v)

arrêter()