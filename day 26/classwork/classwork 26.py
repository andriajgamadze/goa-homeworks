import random 

goelebi = ["andria jgamadze", "nika soselia", "ilia lomitashvili", "giorgi wibliashvili", "iliko rajebashvili", "mate finriashvili", "luka gogoxia", "irakli dudashvili", "giorgi wyonidze", "irakli geladze", "nikoloz kotrikadze"]

for x in range(3):
     r = random.choices(goelebi)
     goelebi.remove(r)

print(r)