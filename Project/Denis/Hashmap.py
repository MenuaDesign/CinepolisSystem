class Node:
    def __init__(self,ID,data,next=None,prev=None):
        """
        Klasse Node met ID,data,nextpointer,previouspointer.
        :param ID: ID van de huidige node.
        :param data: Data van de huidige node.
        :param next: Pointer naar de volgende node.
        :param prev: Pointer naar de vorige node.
        """
        self.ID=ID
        self.data=data
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

    def insert(self,ID,data):
        """
        Insert een node in de chain.
        :param ID: ID van de node.
        :param data: Data in de node.
        :return: True of False
        Precondities:/
        Postcondities:Voegt node toe op de juist plaats in de chain.
        """
        node = Node(ID, data) # Maakt een node aan met id en data.
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

    def retrieve(self,ID):
        """
        Haalt een item met een gezochte id op.
        :param ID: de gevraagde id.
        :return: (data/none, True/False)

        precondities:/
        postcondities: Value van gezochte item wordt teruggegeven.
        """
        if self.head==None: # Bij een lege chain geeft het none terug met bool false.
            return None,False
        else: # Anders zoekt het de item met de gevraage id. Als die niet gevonden is geeft de functie none terug met bool false. Anders geeft het de value met bool true.
            for i in range(self.getLength()):
                if self.head.ID==ID:
                    return self.head.data,True
                self.head=self.head.next
            return None,False

    def save(self):
        """
        Slaat de chain op in lijst vorm.
        :return: (List)

        precondities:/
        postcondities: Geeft de chain terug in lijst vorm.
        """
        zoom=[]
        if self.head==None:
            return []
        elif (self.getLength() == 1):
            zoom.append(self.head.data)
            return zoom
        else:
            for i in range(self.getLength()):
                zoom.append(self.head.data)
                self.head=self.head.next
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

def createTableItem(key,val):
    return TableItem(key,val)


class TableItem:
    def __init__(self,key,value):
        self.key=key
        self.value=value
class Hashmap:
    def __init__(self,type,n):
        """
        type is een van "lin","quad","sep"
        n is de grootte van de hashmap
        """
        self.map=[None]*n
        self.type=type
        self.size=n
    def isEmpty(self): # Kijkt of de boom bestaat uit alleen None waardes. Zo ja? True anders False.
        SizeCheck = []
        for i in self.map:
            if i != None:
                SizeCheck.append(i)
        if len(SizeCheck) == 0:
            return True
        return False
    def tableInsert(self,Tableitem): #Insert op basis van self.type.
        if self.type=="lin": #Index verhoogt telkens met 1
                SizeCheck = [] # Mag niet groter zijn dan self.size
                for i in self.map:
                    if i != None:
                        SizeCheck.append(i)
                    if len(SizeCheck) == self.size:
                        return False
                placed=False
                index = Tableitem.key % self.size
                while not placed:
                    if self.map[index]==None:
                        self.map[index]=Tableitem
                        return True
                    index += 1
                    if index==self.size:
                        index=0
        if self.type=="quad": # Items worden toegevoegd door de index + x^2 te doen als de index bezet is.
            if self.tableRetrieve(Tableitem.key)[1]:
                return False
            SizeCheck = []
            for i in self.map:
                if i != None:
                    SizeCheck.append(i)
                if len(SizeCheck) == self.size:
                    return False
            index=Tableitem.key%self.size
            if self.map[index]==None:
                self.map[index]=Tableitem
                return True
            else:
                placed=False
                indices = []
                x = 1
                while not placed:
                    index=Tableitem.key%self.size+(x**2)
                    if index>=self.size:
                        index=index%self.size
                    if self.map[index]==None:
                        self.map[index]=Tableitem
                        return True
                    else:
                        if index in indices:
                            return False
                        else:
                            indices.append(index)
                        x+=1
        if self.type=="sep": # Items worden toegevoegd aan een ketting op een positie.
            index=Tableitem.key%self.size
            i=self.map[index]
            if i!=None:
                if isinstance(i,LinkedChain):
                    i.insert(1,Tableitem)
                    return True
            else:
                j=LinkedChain()
                j.insert(1, Tableitem)
                self.map[index]=j
                return True
    def tableRetrieve(self,key):
        if self.type=="lin": #Gaat heel de table af tot het item gevonden is.
            In = False # Kijkt eerst natuurlijk of het er zelfs inzit.
            for i in self.map:
                if i != None:
                    if i.key == key:
                        In = True
            if In == False:
                return None, False
            index = key%self.size
            found=False
            indices = []
            while not found:
                if index in indices:
                    return None,False
                indices.append(index)
                if index==self.size:
                    index=0
                if self.map[index]!=None:
                    if self.map[index].key==key:
                        return self.map[index].value,True
                    index+=1
                else:
                    index+=1
            return None,False
        if self.type=="quad": # Zelfde als erboven alleen met minder clusters.
            In = False
            for i in self.map:
                if i != None:
                    if i.key == key:
                        In = True
            if In == False:
                return None, False
            index = key % self.size
            if self.map[index].key == key:
                return self.map[index].value,True
            else:
                found = False
                indices = []
                x = 1
                while not found:
                    index = key % self.size + (x ** 2)
                    if index >= self.size:
                        index = index % self.size
                    if self.map[index].key == key:
                        return self.map[index].value,True
                    else:
                        if index in indices:
                            return None,False
                        else:
                            indices.append(index)
                        x += 1
            return None,False
        if self.type=="sep": # Zoekt het item op de huidige index in de linkedchain.
            index=key%self.size
            i=self.map[index]
            if i==None:
                return False
            else:
                if isinstance(i,LinkedChain):
                    curr = i.head
                    while curr.next != i.head and curr.next != None:
                        if curr.data.key==key:
                            return curr.data.value,True
                        curr = curr.next
                    if curr.next == i.head or curr.next==None:
                        if curr.data.key == key:
                            return curr.data.value, True
                    return None,False
    def save(self): # Slaat de huidige hashmap op.
        S = {'type': self.type, 'items': []}
        if self.type=="sep":
            for i in self.map:
                if i==None:
                    S['items'].append(None)
                else:
                    Chainlist=[]
                    if isinstance(i,LinkedChain):
                        curr=i.head
                        while curr.next!=i.head and curr.next!=None:
                            Chainlist.append(curr.data.key)
                            curr=curr.next
                        if curr.next==i.head or curr.next==None:
                            Chainlist.append(curr.data.key)
                    S['items'].append(Chainlist)
            return S
        for i in range(len(self.map)):
            if self.map[i]:
                S['items'].append(self.map[i].key)
            else:
                S['items'].append(None)
        return S
    def load(self,dict): # Laad een hashmap in .
        if dict['type']=="sep":
            self.map=[]
            self.size=len(dict['items'])
            self.type="sep"
            for i in dict['items']:
                if i==None:
                    self.map.append(None)
                else:
                    self.map.append(LinkedChain())
                    for k in reversed(i):
                        self.map[len(self.map)-1].insert(1,TableItem(k,k))
        else:
            self.map=[]
            self.size=len(dict['items'])
            self.type=dict['type']
            for i in dict['items']:
                if i is not None:
                    self.map.append(createTableItem(i,i))
                else:
                    self.map.append(None)
    def tableDelete(self,key): # Verwijdert een item adhv een gegeven zoeksleutel.
        if self.type=="lin":
            if not self.tableRetrieve(key)[1]:
                return False
            index = key % self.size
            startindex=key % self.size
            found = False
            while not found:
                if self.map[index]!=None:
                    if self.map[index].key==key:
                        item=self.map[index]
                        self.map[index] = None
                        return True
                    else:
                        index += 1
                        if index == self.size:
                            index = 0
                        if index==startindex:
                            found=True
                else:
                    index += 1
                    if index == self.size:
                        index = 0
                    if index == startindex:
                        found = True
            return False
        if self.type=="quad":
            if not self.tableRetrieve(key)[1]:
                return False
            index = key % self.size
            if self.tableRetrieve(key):
                if self.map[index].key == key:
                    self.map[index] = None
                    return True
                else:
                    placed = False
                    indices = []
                    x = 1
                    while not placed:
                        index = key % self.size + (x ** 2)
                        if index >= self.size:
                            index = index % self.size
                        if self.map[index].key == key:
                            self.map[index] = None
                            return True
                        else:
                            if index in indices:
                                return False
                            else:
                                indices.append(index)
                            x += 1
            return False
        if self.type=="sep":
            index = key % self.size
            i = self.map[index]
            if i == None:
                return False
            else:
                if isinstance(i, LinkedChain):
                    curr = i.head
                    while curr.next != i.head and curr.next != None:
                        if curr.data.key == key:
                            i.delete(curr.ID)
                            if i.getLength() == 0:
                                self.map[index] = None
                            return True
                        curr = curr.next
                    if curr.next == i.head or curr.next == None:
                        if curr.data.key == key:
                            i.delete(curr.ID)
                            if i.getLength() == 0:
                                self.map[index] = None
                            return True
            return False
class Table:
    def __init__(self,type,size):
        self.hash=Hashmap(type,size)
    def tableIsEmpty(self):
        """
        Kijk of table empty is
        :return: (True/False)
        """
        return self.hash.isEmpty()
    def tableInsert(self,key,item):
        """
        Insert item
        :param item: Het item om te inserten
        :return: (True/False)
        """
        return self.hash.tableInsert(createTableItem(key,item))
    def tableRetrieve(self,key):
        """
        Retrieve een item uit een table adhv een zoeksleutel.
        :param key: zoeksleuten
        :return: (item.value,True/None,False)
        """
        return self.hash.tableRetrieve(key)
    def save(self):
        """
        Save huidige table
        :return: (Huidige Table)
        """
        return self.hash.save()
    def load(self,dict):
        """
        Laad een hashmaptable in.
        :param dict: De hashmaptable die ingeladen moet worden
        :return: /
        """
        self.hash.load(dict)
    def tableDelete(self,key):
        """
        Delete de item met de ingegeven key uit de tabel.
        :param key: De te verwijderen item
        :return: (True/False)
        """
        return self.hash.tableDelete(key)
