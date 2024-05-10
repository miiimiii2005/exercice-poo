class Case:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _str_(self):
        return f"Case({self.x}, {self.y})"

    def adjacentes(self, jeu):
        adj = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    x, y = self.x + dx, self.y + dy
                    if 0 <= x < jeu.taille_x and 0 <= y < jeu.taille_y:
                        adj.append(jeu.listeDesCases[x][y])
        return adj


class Creature:
    def _init_(self, nom, position):
        self.nom = nom
        self.position = position

    def _str_(self):
        return f"Creature({self.nom}, {self.position})"


self.nom = nom
self.position = position


def _str_(self):
    return f"Creature({self.nom}, {self.position})"


def choisirCible(self, jeu):
    cases_adjacentes = self.position.adjacentes(jeu)
    cases_occupees = [case for case in cases_adjacentes if jeu.estOccupee(case)]
    if cases_occupees:
        return random.choice(cases_occupees)
    else:
        return random.choice(cases_adjacentes)


class Jeu:
    def _init_(self, taille_x, taille_y, nombre_creatures):
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.tour = 0
        self.listeDesCases = [[Case(i, j) for j in range(taille_y)] for i in range(taille_x)]
        self.listeDesCreatures = [Creature(f"Créature {i + 1}", self.listeDesCases[i][j]) for i in
                                  range(nombre_creatures) for j in range(nombre_creatures) if (i + j) % 2 == 0]
        self.actif = self.listeDesCreatures[0]

    def estOccupee(self, case):
        def estOccupee(self, case):
            for creature in self.listeDesCreatures:
                if creature.position == case:
                    return True
            return False

        def deplacer(self, creature, case):
            if case in creature.position.adjacentes(self):
                if self.estOccupee(case):
                    print(f"{creature.nom} a capturé la case occupée par {self.actif.nom} !")
                    return self.actif
                else:
                    creature.position = case
                    self.tour += 1
                    self.actif = self.listeDesCreatures[self.tour % len(self.listeDesCreatures)]
                    return None
            else:
                print("Déplacement non autorisé !")
                return None

        # Création du jeu

    jeu = Jeu(5, 5, 2)

    # Test de déplacement
    print("Position initiale de la créature 1:", jeu.listeDesCreatures[0].position)
    print("Position initiale de la créature 2:", jeu.listeDesCreatures[1].position)
    print("Créature active:", jeu.actif)

    # Déplacement de la créature 1
# Déplacement de la créature 2
case_cible = jeu.listeDesCreatures[1].choisirCible(jeu)
jeu.deplacer(jeu.listeDesCreatures[1], case_cible)

print("Position de la créature 2 après déplacement:", jeu.listeDesCreatures[1].position)
print("Créature active après déplacement:", jeu.actif)