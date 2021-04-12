from copy import deepcopy
class Stack:
    def __init__(self,arraylengte=10): # Maakt een stack met specifieke arraylengte.
        """
        Maakt een stack
        :param arraylengte: De lengte van de array(stack).

        Preconditie:Geen
        Postconditie: Er is een lege stack gemaakt met size arraylengte.
        """
        self.stack=[]
        self.size=arraylengte
    def isEmpty(self):
        """
        Kijkt of de gegeven stack empty is
        :return:(Leeg=True of Niet Leeg=False)

        Preconditie:Er moet een stack gegeven zijn
        Postconditie: Er is gecontroleerd of de stack empty is of niet
        """
        if len(self.stack)==0:
            return True
        else:
            return False
    def push(self,element):
        """
        Voegt een element toe aan de stack
        :param element: Gekozen element om toe te voegen
        :return: (True of False)

        Preconditie: Er is een bestaande stack.
        Postconditie: Het nieuwe element wordt aan het einde van de lijst toegevoegd en wordt bij de pop als eerst verwijderd
        """
        if len(self.stack)==self.size:
            return False
        self.stack.append(element)
        return True
    def pop(self):
        """
        Verwijdert het item bovenaan de stack
        :return: (Lijst(len(lijst)-1),True of False)

        Preconditie:/
        Postconditie: Het item aan het einde van de lijst is geretrieved en verwijderd.
        """
        Copy=deepcopy(self.stack)
        if len(self.stack)==0:
            return None,False
        self.stack.remove(self.stack[len(self.stack)-1])
        return (Copy[len(Copy)-1],True)
    def getTop(self):
        """
        Geeft de top van de stack terug
        :return: (self.stack[len(self.stack)-1],True of false)

        Preconditie: We zeggen dat er minstens 1 item moet zitten in de stack voordat deze methode uitgevoerd kan worden
        Postconditie: Het element bovenaan de stack wordt weergeven.
        """
        if (len(self.stack)==0):
            return None,False
        return ((self.stack[len(self.stack)-1]), True)
    def save(self):
        """
        Slaat de huidige stack op in lijst formaat.
        :return: De huidige stack in een lijst.

        Precondities:/
        Postcondities: Huidige stack is als lijst afgedrukt.
        """
        S=[]
        for i in self.stack:
            S.append(i)
        return S
    def load(self,list):
        """
        Load een gegeven stack/lijst in de huidige stack/lijst.
        :param list: De stack die we moeten inladen.
        :return: /

        Precondities:/
        Postcondities: De huidige stack is vervangen door de ingeladen stack.
        """
        self.stack=list
        self.size=len(list)

    def getLength(self):
        return len(self.stack)

class Table:
    def __init__(self):
        """
        constructor: object van Stack()
        """
        self.stack = Stack()

    def tableGetLength(self):
        return self.stack.getLength()

    def tableIsEmpty(self):
        """
        verwijst naar isEmpty() in Stack
        :return: True als hij leeg is anders False
        """
        return self.stack.isEmpty()

    def tableInsert(self, newItem):
        """
        verwijst naar insert() in Stack
        :param newItem: de value van de nieuwe item
        :return: True als het toevoegen is gelukt anders False
        """
        return self.stack.push(newItem)

    def tableGetFront(self):
        """
        Geeft de eerste item in de Stack
        :return: de eerste item
        """
        return self.stack.getTop()

    def save(self):
        """
        verwijst naar save() in Stack
        :return: een list die onze ketting weergeeft
        """
        return self.stack.save()

    def load(self, list):
        """
        verwijst naar load() in Stack
        :param list: list: de list die we willen toevoegen
        :return: niets
        """
        return self.stack.load(list)

    def tableDelete(self):
        """
        verwijst naar delete() in Stack
        Men verwijdert de laatste item dus geen parameters
        :return: returnt de waarde en een boolean
        """
        return self.stack.pop()

