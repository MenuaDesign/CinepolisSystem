class Node:
    def __init__(self, id,value, next=None, prev=None):
        """
        Een class node met enkele parameters id,value,next en prev
        :param id: deze is uniek en indexeert de value in onze ketting
        :param value: hier in bewaren we de value die we willen opslaan
        :param next: deze wijst naar de next node
        :param prev: deze wijst naat
        """
        self.value = value
        self.next = next
        self.prev = prev
        self.id = id

class LinkedChain:
    def __init__(self):
        """
        Constructor heeft een head die wijst naar de current node en een count die de lengte mee houdt
        """
        self.head = None
        self.count = 0

    def isEmpty(self):
        """
        Een functie die nakijkt dat onze ketting lees is
        :return: True als hij leeg is anders False
        """
        if self.count == 0: #kijkt na of da count 0 is zoja return True
            return True
        else:
            return False

    def getLength(self):
        """
        Een functie die de lengte van de ketting geeft
        :return: Self.count
        """
        return self.count

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

    def insert(self,key,val):
        """
        Een functie om een item toe te voegen in onze ketting
        :param key: de searchkey van de nieuwe item
        :param val: de value van de nieuwe item
        :return: True als het toevoegen is gelukt anders False
        """
        bool = True
        if key >(self.getLength()+1): #als de key groter is dan lengte +1 dan return False
            bool = False
        if bool:
            node = Node(key, val) #nieuwe object node
            if key == 1: #als key 1 is
                if self.isEmpty(): #als node leeg is
                    self.head = node #stellen we onze head an node
                    node.next = node #de node next ook aan de node
                    node.prev = node #en de node prev ook aan de node
                    self.count += 1 #we adden 1 bij de count omdat we 1 item hebben toegevoegd
                    return True
                else:
                    curr = self.head #als hij niet 1 is dan gaan we een var maken cuur en die zetten we gelijk aan self.head
                    prev=self.head.prev #ook een prev die self.head.prev is
                    self.head=node #verder zeggen we dat onze self.head onze node is
                    curr.prev = self.head #verder de current previous is ook de self.head
                    self.head.next=curr #en de next is de curr
                    self.head.prev=prev#en de prev is gewoon ed prev
                    prev.next = self.head #verder is onze prev.next de self.head
                    curr = self.head #en onze cuur de self.head
                    while curr.next != self.head: #zolang de curr.next niet gelijk is aan de self.head dan gaat hij verder en voegt 1 bij de ids
                        curr = curr.next
                        curr.id += 1
                    self.count += 1 #we voegen een nieuwe item toe dus we moete de grootte met 1 aanpassen
                    return True

            if key == (self.getLength() + 1):#als de searchkey gelijk is aan de
                tmp = 1
                curr = self.head
                while tmp != self.getLength(): #zolang de tmp niet gelijk is aan de waarde van de lengte dan gaat curr naar next en voegt hij 1 bij de temp
                    curr = curr.next
                    tmp += 1
                curr.next = node #vervolgens is de curr next ozne node
                node.prev=curr #en de node.prev ook
                node.next=self.head #de node.next is onze self.head
                self.head.prev = node #ook onze self.head.prev is onze node
                self.count += 1 #we voegen 1 bij de count
                return True
            elif key > 1 and key <=(self.getLength()+1): #als de key groter is dan 1 en kleiner of gelijk aande lengte +1
                if self.getLength() == 1: #als de lengte 1 is
                    curr = self.head #we maken curr
                    curr.next = node #onze cuur next is de node
                    curr.next.next = self.head #de next next can de curr is onze self.head
                    curr.prev = node #de prev van de curr is node
                    curr.prev.prev = self.head #de prev prev van de curr is self.head
                    self.count += 1 #we voegen 1 bij de count
                    return True
                else:
                    tmp = 1
                    curr = self.head #cuur is head
                    prev = self.head.prev #prev is prev van head
                    while tmp != key: #zolang tmp niet gelijk is aan de key
                        curr = curr.next #curr springt naar next
                        prev = curr.prev #prev spirnt naar prev van de curr
                        tmp += 1
                    prev.next = node #prev next zetten we op node
                    prev.next.next = curr #en de prev next next op curr
                    prev.next.prev = prev #de prev next prev is de prev
                    curr.prev=node #en de prev van de cuur is onze node
                    curr = node #ten slotte is onze curr de node
                    while curr.next!=self.head: #zolang de curr.next niet gelijk is aan de self.head
                        curr=curr.next #ga curr verder
                        curr.id +=1 #voeg 1 to bij id
                    self.count += 1
                    return True
        else:
            return False


    def save(self):
        """
        Een functie die onze ketting saved en print
        :return: een list die onze ketting weergeeft
        """
        chain = []
        curr = self.head
        if self.isEmpty(): #checkt voor empty
            return chain
        if self.count == 1: #als de lengte 1 is dan
            chain.append(curr.value) #voeg de items toe
            return chain
        else: #anders
            while curr.next!= self.head: #zolang de curr.next niet geljk is aan de head
                chain.append(curr.value) #voeg toe en gaa curr 1 verder
                curr = curr.next
            if curr.next == self.head: #als curr next gelijk is aan de head
                chain.append(curr.value) #voeg de chain toe
        return chain #return de list chain

    def load(self,list):
        """
        Een functie load om van een list te importen in onze ketting
        :param list: de list die we willen toevoegen
        :return: niets
        """
        self.head = None
        self.count = 0
        for i in reversed(list): #omgekeerd invoegen
            self.insert(1,i)

    def delete(self, key):
        """
        een functie delete om een item te verwijderen in onze ketting
        :param key: de searchkey die indexeert naar de item die we willen verwijderen
        :return: returnt de waarde en een boolean
        """
        item = self.retrieve(key) #item is retrieve met als parameter de key
        if self.isEmpty(): #check voor empty
            return None,False
        if key >(self.getLength()+1): #als de key groter is dan is ze false
            return None,False
        curr = self.head

        if key == 1: # als de key 1 is dan verwijderen we op de 1 ste plek
            curr = self.head.next
            prev = self.head.prev
            curr.prev = prev
            prev.next = curr
            self.head = curr
            curr = self.head
            for i in range(1,self.getLength()): #we gaan steeds verder om alle id recht te zetten
                curr.id -= 1
                curr = curr.next
            self.count -= 1
            return item[0],True

        for i in range(1,key): #we gaan verder om op de juiste plaats te komen
            curr = curr.next

        if key == self.getLength(): #als de key gelijk is aan de lengte wilt da zeggen verwijderen op de laatste plek
            curr.prev.next = curr.next
            self.head.prev = curr.prev
            self.count -= 1
            return item[0],True

        if curr.id == key: #als de key gelijk de id dan wilt da zeggen verwijderen tussen 1 en de laatste
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            while curr.next != self.head: #we gaan verder totdat hij gelijk is aan self.head
                curr = curr.next
                curr.id -=1
            self.count -=1
            return item[0],True

        else:
            return None,False

class Table:
    def __init__(self):
        """
        constructor: object van LinkedChain
        """
        self.chain = LinkedChain()

    def tableIsEmpty(self):
        """
        verwijst naar isEmpty() in LinkedChain
        :return: True als hij leeg is anders False
        """
        return self.chain.isEmpty()

    def tableInsert(self,key,newItem):
        """
        verwijst naar insert() in LinkedChain
        :param key: de searchkey van de nieuwe item
        :param newItem: de value van de nieuwe item
        :return: True als het toevoegen is gelukt anders False
        """
        return self.chain.insert(key,newItem)

    def tableLength(self):
        """
        verwijst naar de getLength in LinkedChain
        :return: Self.count
        """
        return self.chain.getLength()

    def tableRetrieve(self,key):
        """
        verwijst naar retrieve() in LinkedChain
        :param key: searchkey wordt gebruikt om de value te vinden
        :return: een tupel Waarde, boolean-> Als hij true is dan waarde,True anders None,False
        """
        return self.chain.retrieve(key)

    def save(self):
        """
        verwijst naar save() in LinkedChain
        :return: een list die onze ketting weergeeft
        """
        return self.chain.save()

    def load(self,list):
        """
        verwijst naar load() in LinkedChain
        :param list: list: de list die we willen toevoegen
        :return: niets
        """
        return self.chain.load(list)

    def tableDelete(self,key):
        """
        verwijst naar delete() in LinkedChain
        :param key: de searchkey die indexeert naar de item die we willen verwijderen
        :return: returnt de waarde en een boolean
        """
        return self.chain.delete(key)



if __name__ == "__main__":
    system = Table()
    system.tableInsert(1,"he")
    print(system.save())

