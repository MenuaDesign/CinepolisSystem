class Stack: #Onze klasse Stack
    def __init__(self,lengte=10): #constructor van de klasse stack, deze initialiseert de parameters.deze gaat een python list aanpassen
        """
        Dit is de contstructor, we declareren hier een lege list items. waar onze stack zal geimplenteert worden.
        """
        self.items =[]#Hier zetten we items gelijk aan een lege list
        self.lengte = lengte #de lengte van de stack die wordt meegegeven
        self.size = 0 #de size van de stack die word bijgehouden


    def getLength(self):
        return len(self.items)

    def save(self):
        """
        Hier slagen we de stack op en printen die.
        :param geen
        :return: de stack in een list
        """
        stack = []
        if self.isEmpty() == True:
            return stack
        else:
            stack.extend(self.items)
            return stack

    def isEmpty(self): #bepaalt of een stack leeg is.
        """
        Hier gaan we nakijken of de stack leeg is.
        :return: een boolean true or false.
        """
        if self.size == 0: #als de size 0 is dan is ze empty anders niet
            return True
        else:
            return False

    def push(self, newItem):#voegt een element toe aan de stack.
        """
        Hier hebben we een parameter newItem deze bevat een item, we gaan deze toevoegen in onze stack, deze zal altijd van bove de stack komen.
        :param item: Deze zal de waarde zijn die wel willen toevoegen in onze stack
        :return: We returnen hier True als het is gelukt anders False.
        """
        if self.isFull() == True: #Kijkt na of de stack vol is
            return False
        else:
            self.items.append(newItem) #voegt de item toe in de stack
            self.size += 1 #voegt 1 bij size
            return True

    def isFull(self): #een functie om na tekijken of de stack vol is
        """

        :return: True als hij vol is anders False
        """
        if self.isEmpty()== True: #kijkt of de stack leeg is
            return False
        elif self.size >= self.lengte: #vergelijkt de grootte met de lengte als size groter of gelijk dan is hij vol
            return True
        else:
            return False


    def pop(self): #verwijdert het laatst toegevoegde element uit de stack.
        """
        Bij de methode pop gaan we de bovenste item verwijderen
        :return: Hier returnen we de nieuwe list waarvan de bovenste item is verwijderd en een boodschgp succescvol verwijderd.
        """
        curr = 0
        if self.isEmpty() == True: #checkt of het leeg is
            return False,False
        else:
            curr = self.getTop()[0]
            self.items.pop() #Het is zeer handig want python heeft een functie pop waarvan de eerste item in list wordt verwijderd
            self.size -= 1
            return curr,True

    def getTop(self): #vraagt het laatst toegevoegde element uit de stack op.
        """
        In deze functie kijken we eerst na of het niet leeg is, als het niet leeg is dan zoeken we naar items-1
        :return: we returnen de bovenste item en een boodschap dat het is gelukt
        """
        if not self.isEmpty():
            return self.items[-1], True
        else:
            return None,False

    def load(self,list): #functie om in te laden
        """
        Een functie om een list toetevoegen in onze stack
        :param list: input list
        :return: voegt de input list in self.items
        """
        self.items=[] #items leeg maken
        self.lengte = len(list) #lengte op de lengte van de list zetten
        self.size = len(list) #size is de grootte van de list
        self.items.extend(list)

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

    def tableIsFull(self):
        """
        Kijkt na of de Stack vol is
        :return: returnt True or False
        """

        return self.stack.isFull()

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