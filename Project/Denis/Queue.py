from copy import deepcopy
class Queue:
    def __init__(self,arraylengte):
        """
        Maakt een queue
        :param arraylengte: De lengte van de array van de queue.

        Preconditie:Geen
        Postconditie: Er is een lege lijst gemaakt met size arraylengte.
        """
        self.queue=[]
        self.size=arraylengte
    def isEmpty(self):
        """
        Kijkt of gegeven queue leeg is
        :return:(Leeg=True of Niet Leeg =False)

        Preconditie: Er moet een queue gegeven zijn
        Postconditie: Kijkt of de queue leeg is of niet
        """
        if len(self.queue)==0:
            return True
        return False

    def enqueue(self,element):
        """
        Voegt een gekozen element toe aan de queue
        :param element: Gekozen element dat je wilt toevoegen aan de queue
        :return: True of False afhankelijk van succes.

        Preconditie: Er moet een queue zijn waarin dit element kan geplaatst worden
        Postcondities: Element toegevoegd aan queue
        """
        if (len(self.queue)==self.size):
            return False
        self.queue.append(element)
        return True
    def dequeue(self):
        """
        Verwijdert een element uit de queue
        :return: (Queue[0],True of False)

        Precondities:/
        Postcondities: Het element is geretrieved en verwijdert uit de queue en al zijn opvolgers schuiven met een positie naar links. Er wordt ook true of false teruggegeven afhankelijk of het item is verwijdert of niet.
        """
        Copy=deepcopy(self.queue)
        if len(self.queue)==0:
            return None,False
        self.queue.remove(self.queue[0])
        return (Copy[0],True)
    def getFront(self):
        """
        Zoekt naar het voorwerp dat op de eerste postie in de queue staat
        :return: (self.queue[0],True of False)

        Precondities: We zeggen dat er minstens 1 item moet zitten in de queue voordat deze methode uitgevoerd kan worden
        Postcondities: Het element vooraan de queue wordt gegeven
        """
        if len(self.queue)==0:
            return None,False
        return ((self.queue[0]),True)
    def save(self):
        """
        Slaat de huidige queue op in een lijst en drukt het af.
        :return: (Lijst)

        Precondities:/
        Postcondities: Geeft de queue terug in lijst vorm.
        """
        Q=[]
        for i in reversed(self.queue):
            Q.append(i)
        return Q
    def load(self,list):
        """
        Laad een queue in.
        :param list: De queue die wordt ingeladen.
        :return: /

        Precondities:/
        Postcondities: De huidige queue is vervangen door de ingeladen queue.
        """
        B=[]
        for i in reversed(list):
            B.append(i)
        self.queue=B
        self.size=len(B)

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