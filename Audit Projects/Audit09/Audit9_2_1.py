from abc import ABC, abstractmethod

class Spy(ABC):
    @abstractmethod
    def visitGeneralStaff(self, militaryObject):
        pass

    @abstractmethod
    def visitMilitaryBase(self, militaryObject):
        pass

class MilitaryObject(ABC):
    @abstractmethod
    def accept(self, visitor: Spy):
        pass

class GeneralStaff(MilitaryObject):
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def accept(self, visitor: Spy):
        visitor.visitGeneralStaff(self)

    def __str__(self):
        return f"GeneralStaff: У генеральному штабі є {self.generals} генералів та {self.secretPaper} секретних паперів."

class MilitaryBase(MilitaryObject):
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def accept(self, visitor: Spy):
        visitor.visitMilitaryBase(self)

    def __str__(self):
        return f"MilitaryBase: На військовій базі є {self.officers} офіцерів, {self.soldiers} солдатів, {self.jeeps} джипів та {self.tanks} танків."

class SecretAgent(Spy):
    def __init__(self):
        self.stoleninformation = ""

    def visitGeneralStaff(self, militaryObject):
        gen = militaryObject.generals
        sp = militaryObject.secretPaper
        self.stoleninformation = f"В генеральному штабі є {gen} генералів та {sp} секретних паперів"
        militaryObject.secretPaper = 0

    def visitMilitaryBase(self, militaryObject):
        of = militaryObject.officers
        sol = militaryObject.soldiers
        tn = militaryObject.tanks
        dj = militaryObject.jeeps
        self.stoleninformation = f"На військовій базі є {of} офіцерів, {sol} солдатів, {tn} танків, {dj} джипів"

    def __str__(self):
        return self.stoleninformation

class Saboteur(Spy):

    def visitMilitaryBase(self, militaryObject):
        militaryObject.jeeps = 0
        militaryObject.tanks = 0
        militaryObject.officers = 0
        militaryObject.soldiers = 0

    def visitGeneralStaff(self, militaryObject):
        militaryObject.generals = 0
        militaryObject.secretPaper = 0

    def __str__(self):
        return "Всі ворожі об'єкти знищено!"


if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100)
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20)
    print(militaryBase)

    print("==SPY==")
    secretAgent = SecretAgent()
    saboteur = Saboteur()

    generalStaff.accept(secretAgent)

    print("secret agent", secretAgent)
    print("GEN STAFF", generalStaff)
    print("=========")

    militaryBase.accept(secretAgent)
    print("secr agent on military base", secretAgent)
    print("military base", militaryBase)

    print("Sabouteur")
    militaryBase.accept(saboteur)
    print("saboteur", saboteur)
    print("general staff", generalStaff)

    print("=========")
    militaryBase.accept(saboteur)
    print("saboteur", saboteur)
    print("MILITARY BASE", militaryBase)