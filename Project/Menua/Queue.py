class Queue: #Onze klasse Queue
    def __init__(self,lengte=10):
        """
        onze constructor bevat items lengte en size gelikaardig als onze stack
        :param lengte: een basis lengte van de queue
        """
        self.items = []
        self.lengte = lengte #het meegegeven lengte van de queue
        self.size = 0 #houd de size van de queue bij, bij het verwijderen en toevoegen van items

    def isFull(self):
        """
        Deze functie kijkt of het vol is onze queue
        :return: True als hij vol zit anders False
        """
        if self.isEmpty() == True: #kijkt of hij leeg is
            return False
        elif self.size >= self.lengte: #vergelijkt de lengte met de size, als size groter is of gelijk dan is hij vol
            return True
        else:
            return False

    def getFront(self):
        """
        Een functie om de bovenste waarde op te halen
        :return: een tupel (waarde, True or False)
        """
        if not self.isEmpty(): #kijkt of hij leeg is
            return self.items[len(self.items)-1], True #hij returned de bovenste item
        else:
            return None,False

    def dequeue(self):
        """
        Een dunctie om een item te dequeuen
        :return: een tupel (waarde dat je hebt verwijdert, True or False)
        """
        curr = 0
        if self.isEmpty() == True:
            return False, False
        else:
            #als de Queue niet leeg is dan verwijdert hij de getfront item
            curr = self.getFront()[0]
            self.items.remove(curr)
            self.size -= 1
            return curr, True

    def enqueue(self, newItem):
        """
        Een functie om items te pushen of enqueue in een Queue
        :param newItem: Deze is de item die we willen enqueue of pushen
        :return: True als het enqueue is gelukt anders False
        """
        if self.isFull() == True:#kijkt na of het vol is
            return False
        else:
            self.items.insert(0,newItem) #anders voegt hij op de 1ste plek de item toe
            self.size += 1
            return True

    def isEmpty(self):
        """
        functie om te kijken of de queue leeg is
        :return: True als hij leeg is anders False
        """
        if self.size == 0: #als size 0 is dan is hij leeg
            return True
        else:
            return False

    def save(self):
        """
        Een functie om een queue te saven(printen)
        :return: een list die de queue weergeeft
        """
        stack = [] #een lege list
        if self.isEmpty() == True: #als hij leeg is return de lege list
            return stack
        else:
            stack.extend(self.items) #we voegen onze self.items in de list stack
            return stack

    def load(self,list):
        """
        een functie om items te loaden vanuit een list naar onze queue
        :param list: de list die we als input willen gebruiken om ze te zetten in onze queue
        :return: Niets
        """
        self.items=[] #items leeg maken
        self.lengte = len(list) #lengte op de lengte van de list zetten
        self.size = len(list) #size is de grootte van de list
        self.items.extend(list)

class Table:
    def __init__(self,arraylengte):
        """
        constructor: object van Queue()
        """
        self.queue = Queue(arraylengte)

    def tableIsEmpty(self):
        """
        verwijst naar isEmpty() in Queue
        :return: True als hij leeg is anders False
        """
        return self.queue.isEmpty()

    def tableInsert(self, newItem):
        """
        verwijst naar insert() in Queue
        :param newItem: de value van de nieuwe item
        :return: True als het toevoegen is gelukt anders False
        """
        return self.queue.enqueue(newItem)

    def tableGetFront(self):
        """
        Geeft de eerste item in de Queue
        :return: de eerste item
        """
        return self.queue.getFront()

    def save(self):
        """
        verwijst naar save() in Queue
        :return: een list die onze ketting weergeeft
        """
        return self.queue.save()

    def load(self, list):
        """
        verwijst naar load() in Queue
        :param list: list: de list die we willen toevoegen
        :return: niets
        """
        return self.queue.load(list)

    def tableDelete(self):
        """
        verwijst naar delete() in Queue
        Men verwijdert de laatste item dus geen parameters
        :return: returnt de waarde en een boolean
        """
        return self.queue.dequeue()