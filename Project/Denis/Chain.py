from Gebruiker import Gebruiker
class Node:
    def __init__(self,ID,value,next=None,prev=None):
        """
        Klasse Node met ID,value,nextpointer,previouspointer.
        :param ID: ID van de huidige node.
        :param value: value van de huidige node.
        :param next: Pointer naar de volgende node.
        :param prev: Pointer naar de vorige node.
        """
        self.ID=ID
        self.value=value
        self.next=next
        self.prev=prev

class LinkedChain:
    def __init__(self):
        """
        Klasse chain met head.
        """
        self.head=None

    def getLength(self):
        """
        Telt het aantal nodes in de chain.
        :return: (amountofnodes)

        Precondities:/
        Postcondities: Geeft het aantal nodes terug.
        """
        if self.head==None: # Als er geen head is, is het aantal nodes gelijk aan 0.
            return 0
        amountofnodes=1 # Als self.head niet None is hebben we al een node. We itereren over onze nodes tot de laatste en dan returen wij het aantal nodes.
        currentnode=self.head
        previousnode=self.head.prev
        while currentnode.next!=self.head:
            currentnode=currentnode.next
            previousnode=currentnode.prev
            amountofnodes+=1
        return amountofnodes

    def insert(self,ID,value):
        """
        Insert een node in de chain.
        :param ID: ID van de node.
        :param value: value in de node.
        :return: True of False
        Precondities:/
        Postcondities:Voegt node toe op de juist plaats in de chain.
        """
        node = Node(ID, value) # Maakt een node aan met id en value.
        if (ID==1): # Als de id van de te inserten node 1 is controleren we hoeveel nodes er zijn.
            if(self.getLength()==0): # Als er geen nodes zijn is dat dan de head node.
                self.head=node
                self.head.next=node
                self.head.prev=node
                return True
            currentnode=self.head #Anders is dit de nieuwe eerste node en moeten we alle ID's +1 doen en de verbindingen tussen de nodes herstellen. specifiek de laatste node, de nieuwe head node en de voormalige head node.
            prevnode=self.head.prev
            self.head=node
            currentnode.prev=self.head
            self.head.next=currentnode
            self.head.prev=prevnode
            prevnode.next=self.head
            currentnode = self.head
            previousnode = self.head.prev
            while currentnode.next != self.head:
                previousnode = currentnode
                currentnode = currentnode.next
                currentnode.ID += 1
            return True
        if (ID>(self.getLength() + 1)): # Als de ID niet maximaal 1 groter is dan het aantal nodes, dan kan deze niet geinsert worden.
            return False
        if (ID==self.getLength()+1): # Als de node als laatste node moet worden toegevoegd. Veranderen de ID's niet. Alleen de verbindingen tussen de huidige laatste node, de voormalige laatste node en de head node.
            currentnodeid=1
            currentnode=self.head
            previousnode=self.head.prev
            while(currentnodeid!=self.getLength()):
                currentnode=currentnode.next
                previousnode=currentnode.prev
                currentnodeid += 1
            currentnode.next=node
            node.prev=currentnode
            node.next=self.head
            self.head.prev=node
            return True
        elif (ID>1 and ID<=(self.getLength())): # Als we de node ergens tussenin plaatsen moeten we alle ID's vanaf dat punt met 1 verhogen. En natuurlijk moeten we de verbindingen tussen de nodes waartussen het geplaatst wordt aanpassen.
            currentnodeid = 1
            currentnode = self.head
            previousnode = self.head.prev
            while (currentnodeid != ID):
                currentnode = currentnode.next
                previousnode = currentnode.prev
                currentnodeid += 1
            previousnode.next=node
            previousnode.next.prev=previousnode
            previousnode.next.next=currentnode
            currentnode.prev=node
            currentnode=node
            while (currentnode.next!=self.head):
                currentnode=currentnode.next
                currentnode.ID+=1
            return True

    def isEmpty(self):
        """
        Controleert of de linked chain leeg is.
        :return: True of False

        """
        if self.head==None:
            return True
        return False
    def delete(self, ID):
        """
        Delete een node uit de ketting
        :param ID: ID van de Node
        :return: True of False

        Preconditie:/
        Postconditie: Node met zoeksleutel is verwijderd
        """
        if (ID<1 or ID>self.getLength()): # Als de id onder 1 of boven het aantal nodes is geeft het false terug.
            return False
        if self.head==None: # Als de chain leeg is geeft het false terug.
            return False
        currentnode=self.head
        previousnode=currentnode.prev
        if(ID==1 and not self.getLength() == 1): # Als de eerste node verwijdert moet worden en het hoeveelheid nodes is niet 1. Dan worden de verbindingen herstelt tussen de laatste node en de nieuwe head node. En alle id's worden met 1 verlaagd.
            currentnode=self.head.next
            previousnode=self.head.prev
            currentnode.prev=previousnode
            previousnode.next=currentnode
            self.head=currentnode
            currentnode=self.head
            while (currentnode.next!=self.head):
                currentnode.ID-=1
                currentnode=currentnode.next
            currentnode.ID -= 1
            return True
        elif (ID>1 and ID<(self.getLength())): #Als er in het midden verwijdert wordt dan wordt vanaf dat punt elke node zijn ID met -1 verlaagt. De verbindingen worden ook hersteld.
            currentnodeid = 1
            currentnode = self.head
            previousnode = self.head.prev
            while (currentnodeid != ID):
                currentnode = currentnode.next
                previousnode = currentnode.prev
                currentnodeid += 1
            previousnode.next=currentnode.next
            currentnode.next.prev=previousnode
            while (currentnode.next!=self.head):
                currentnode=currentnode.next
                currentnode.ID-=1
            return True
        if (ID == 1 and self.getLength() == 1):  # Als je het enige item wilt verwijderen.
            self.head = None
            return True
        if(ID==self.getLength()): # Als het laatste item verwijdert wordt veranderen de ID's niet maar moeten de verbinden wel hersteld worden.
            currentnode=self.head
            previousnode=self.head.prev
            while(currentnode.next!=self.head):
                previousnode = currentnode
                currentnode=currentnode.next
            currentnode.prev.next=self.head
            self.head.prev=currentnode.prev
            return True
        return False

    def retrieve(self,key):
        """
        een functie die doormiddel van een key de value weergeeft op die index
        :param key: searchkey wordt gebruikt om de value te vinden
        :return: een tupel Waarde, boolean-> Als hij true is dan waarde,True anders None,False
        """
        if self.isEmpty():#kijkt na of hij leeg is
            return None,False
        bool = False
        curr = self.head
        for i in range(1,self.getLength()+1): #loopt over de ketting
            if key == i: #als de key gelijk is aan de index
                bool = True #bool wordt true
                break
            curr = curr.next
        if bool: #als bool true is dan returnt hij de waarde,True
            return curr.value,True
        else:
            return None, False

    def save(self):
        """
        Slaat de chain op in lijst vorm.
        :return: (List)

        precondities:/
        postcondities: Geeft de chain terug in lijst vorm.
        """
        currentnode = self.head
        zoom=[]
        if self.head==None:
            return []
        elif (self.getLength() == 1):
            zoom.append(self.head.value)
            return zoom
        else:
            for i in range(self.getLength()):
                zoom.append(currentnode.value)
                currentnode=currentnode.next
        return zoom
    def load(self,lijst):
        """
        Laad een chain in.
        :param lijst: De chain die moet worden ingeladen.
        :return: /

        precondities: Geen
        postcondities: Huidige chain wordt leeggemaakt en vervangen door een nieuwe chain.
        """
        self.head=None
        for i in range(len(lijst)):
            LinkedChain.insert(self,(i+1),lijst[i])
    def emptyChain(self):
        self.head=None
        print("De ketting is nu volledig leeg.")
        return True

class Table:
    def __init__(self):
        self.chain=LinkedChain()
    def tableIsEmpty(self):
        """
        Kijkt of de LinkedChainTable leeg is.
        :return: (True/False)

        Precondties:/
        Postcondities: Geeft true of false afhankelijk of de tabel leeg is of niet.
        """
        return self.chain.isEmpty()

    def tableInsert(self,ID,Value):
        """
        Voegt een item toe aan de tabel
        :param ID: De ID van het toe te voegen item.
        :param Value: De value van het toe te voegen item.
        :return: True of False afhankelijk of het gelukt is of niet

        Preconditie:/
        Postcondities: Item toegevoegd aan de de tabel.
        """
        return self.chain.insert(ID,Value)

    def tableRetrieve(self,ID):
        """
        Retrieved een item
        :param ID: ID van het gezochte item.
        :return: (value/None,True/False)

        Precondities:\
        Postcondities: Geeft de value van het gezochte item terug.
        """
        return self.chain.retrieve(ID)

    def tableLength(self):
        """
        Kijkt hoelang de tabel is.
        :return: (self.chain.getLength())

        Preconditie:\
        Postcondite: Geeft de lengte van de tabel terug.
        """
        return self.chain.getLength()

    def load(self,dict):
        """
        Load een tabel in.
        :param dict: De tabel die moet worden ingeladen.
        :return: (self.chain.load(dict))

        Preconditie:\
        Postconditie:Tabel is ingeladen
        """
        return self.chain.load(dict)

    def save(self):
        """
        Slaat de huidige tabel op in een lijst
        :return: (self.chain.save())

        Precondities:\
        Postcondities: Tabel is opgeslagen
        """
        return self.chain.save()
    def tableDelete(self,Item):
        """
        Verwijdert een item uit de tabel.
        :param Item: Het item dat verwijdert moet worden
        :return: (value/None,True/False)

        Precondities:/
        Postcondities:Item is verwijderd uit de tabel en true of false wordt teruggegeven.
        """
        return self.chain.delete(Item)
