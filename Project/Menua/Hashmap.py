class Node:
    def __init__(self, id, value, next=None, prev=None):
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
        if self.count == 0:  # kijkt na of da count 0 is zoja return True
            return True
        else:
            return False

    def getLength(self):
        """
        Een functie die de lengte van de ketting geeft
        :return: Self.count
        """
        return self.count

    def retrieve(self, key):
        """
        een functie die doormiddel van een key de value weergeeft op die index
        :param key: searchkey wordt gebruikt om de value te vinden
        :return: een tupel Waarde, boolean-> Als hij true is dan waarde,True anders None,False
        """
        if self.isEmpty():  # kijkt na of hij leeg is
            return None, False
        bool = False
        curr = self.head
        for i in range(1, self.getLength() + 1):  # loopt over de ketting
            if key == i:  # als de key gelijk is aan de index
                bool = True  # bool wordt true
                break
            curr = curr.next
        if bool:  # als bool true is dan returnt hij de waarde,True
            return curr.value, True
        else:
            return None, False

    def insert(self, key, val):
        """
        Een functie om een item toe te voegen in onze ketting
        :param key: de searchkey van de nieuwe item
        :param val: de value van de nieuwe item
        :return: True als het toevoegen is gelukt anders False
        """
        bool = True
        if key > (self.getLength() + 1):  # als de key groter is dan lengte +1 dan return False
            bool = False
        if bool:
            node = Node(key, val)  # nieuwe object node
            if key == 1:  # als key 1 is
                if self.isEmpty():  # als node leeg is
                    self.head = node  # stellen we onze head an node
                    node.next = node  # de node next ook aan de node
                    node.prev = node  # en de node prev ook aan de node
                    self.count += 1  # we adden 1 bij de count omdat we 1 item hebben toegevoegd
                    return True
                else:
                    curr = self.head  # als hij niet 1 is dan gaan we een var maken cuur en die zetten we gelijk aan self.head
                    prev = self.head.prev  # ook een prev die self.head.prev is
                    self.head = node  # verder zeggen we dat onze self.head onze node is
                    curr.prev = self.head  # verder de current previous is ook de self.head
                    self.head.next = curr  # en de next is de curr
                    self.head.prev = prev  # en de prev is gewoon ed prev
                    prev.next = self.head  # verder is onze prev.next de self.head
                    curr = self.head  # en onze cuur de self.head
                    while curr.next != self.head:  # zolang de curr.next niet gelijk is aan de self.head dan gaat hij verder en voegt 1 bij de ids
                        curr = curr.next
                        curr.id += 1
                    self.count += 1  # we voegen een nieuwe item toe dus we moete de grootte met 1 aanpassen
                    return True

            if key == (self.getLength() + 1):  # als de searchkey gelijk is aan de
                tmp = 1
                curr = self.head
                while tmp != self.getLength():  # zolang de tmp niet gelijk is aan de waarde van de lengte dan gaat curr naar next en voegt hij 1 bij de temp
                    curr = curr.next
                    tmp += 1
                curr.next = node  # vervolgens is de curr next ozne node
                node.prev = curr  # en de node.prev ook
                node.next = self.head  # de node.next is onze self.head
                self.head.prev = node  # ook onze self.head.prev is onze node
                self.count += 1  # we voegen 1 bij de count
                return True
            elif key > 1 and key <= (
                    self.getLength() + 1):  # als de key groter is dan 1 en kleiner of gelijk aande lengte +1
                if self.getLength() == 1:  # als de lengte 1 is
                    curr = self.head  # we maken curr
                    curr.next = node  # onze cuur next is de node
                    curr.next.next = self.head  # de next next can de curr is onze self.head
                    curr.prev = node  # de prev van de curr is node
                    curr.prev.prev = self.head  # de prev prev van de curr is self.head
                    self.count += 1  # we voegen 1 bij de count
                    return True
                else:
                    tmp = 1
                    curr = self.head  # cuur is head
                    prev = self.head.prev  # prev is prev van head
                    while tmp != key:  # zolang tmp niet gelijk is aan de key
                        curr = curr.next  # curr springt naar next
                        prev = curr.prev  # prev spirnt naar prev van de curr
                        tmp += 1
                    prev.next = node  # prev next zetten we op node
                    prev.next.next = curr  # en de prev next next op curr
                    prev.next.prev = prev  # de prev next prev is de prev
                    curr.prev = node  # en de prev van de cuur is onze node
                    curr = node  # ten slotte is onze curr de node
                    while curr.next != self.head:  # zolang de curr.next niet gelijk is aan de self.head
                        curr = curr.next  # ga curr verder
                        curr.id += 1  # voeg 1 to bij id
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
        if self.isEmpty():  # checkt voor empty
            return chain
        if self.count == 1:  # als de lengte 1 is dan
            chain.append(curr.value)  # voeg de items toe
            return chain
        else:  # anders
            while curr.next != self.head:  # zolang de curr.next niet geljk is aan de head
                chain.append(curr.value)  # voeg toe en gaa curr 1 verder
                curr = curr.next
            if curr.next == self.head:  # als curr next gelijk is aan de head
                chain.append(curr.value)  # voeg de chain toe
        return chain  # return de list chain

    def load(self, list):
        """
        Een functie load om van een list te importen in onze ketting
        :param list: de list die we willen toevoegen
        :return: niets
        """
        self.head = None
        self.count = 0
        for i in reversed(list):  # omgekeerd invoegen
            self.insert(1, i)

    def delete(self, key):
        """
        een functie delete om een item te verwijderen in onze ketting
        :param key: de searchkey die indexeert naar de item die we willen verwijderen
        :return: returnt de waarde en een boolean
        """
        item = self.retrieve(key)  # item is retrieve met als parameter de key
        if self.isEmpty():  # check voor empty
            return None, False
        if key > (self.getLength() + 1):  # als de key groter is dan is ze false
            return None, False
        curr = self.head

        if key == 1:  # als de key 1 is dan verwijderen we op de 1 ste plek
            curr = self.head.next
            prev = self.head.prev
            curr.prev = prev
            prev.next = curr
            self.head = curr
            curr = self.head
            for i in range(1, self.getLength()):  # we gaan steeds verder om alle id recht te zetten
                curr.id -= 1
                curr = curr.next
            self.count -= 1
            return item[0], True

        for i in range(1, key):  # we gaan verder om op de juiste plaats te komen
            curr = curr.next

        if key == self.getLength():  # als de key gelijk is aan de lengte wilt da zeggen verwijderen op de laatste plek
            curr.prev.next = curr.next
            self.head.prev = curr.prev
            self.count -= 1
            return item[0], True

        if curr.id == key:  # als de key gelijk de id dan wilt da zeggen verwijderen tussen 1 en de laatste
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            while curr.next != self.head:  # we gaan verder totdat hij gelijk is aan self.head
                curr = curr.next
                curr.id -= 1
            self.count -= 1
            return item[0], True

        else:
            return None, False


# creert item met var key en val
def createTableItem(key, val):
    """
    een functie om de te creeren van een item
    :param key: searchey
    :param val: data
    :return: de object item
    """
    return Item(key, val)


# onze classe item die we gaan gebruiken als object
class Item:
    """
    returnt niets een object item
    """

    def __init__(self, key, val):
        self.searchkey = key
        self.value = val


class Hashmap:  # onze class hashmap
    def __init__(self, type, length):
        """
        Constructor initialseren van parameters
        :param type: type van probing
        :param length: lengte die wordt meegegeven
        """

        self.items = []  # de items worden hier opgeslagen
        self.type = type  # hier de type
        self.length = length  # hier de lengte
        self.count = 0
        for i in range(length):  # vullen met Nones
            self.items.append(None)

    def isEmpty(self):  # checkt of het empty is
        """
        een functie die checkt of het leeg is
        :return: true or false
        """

        if self.count == 0:
            return True
        else:
            return False

    def linearProbing(self, val):  # linear probing
        """
        een functie die items toevoegt door mideel van linear probing
        :param val: onze data die we willlen toevoegen
        :return: true or false
        """
        key = val.searchkey  # neemt key van val
        if self.tableRetrieve(key)[1]:  # retrieved de value
            return False
        check = []
        i = key % self.length  # mod van de key op lengte
        while self.items[i] is not None:
            i += 1
            if i == self.length:
                i = 0
            if i in check:
                return False
            else:
                check.append(i)
        new = Item(key, val)  # nieuwe object maken
        new.value = val  # de value is val
        new.searchkey = key  # de searchkey is key
        self.items[i] = val
        self.count += 1
        return True

    def quadraticProbing(self, val):
        """
        een functie die items tovoegt doormiddel van quadratic probing
        :param val: data
        :return:  true or false
        """
        key = val.searchkey  # neemt ket van val
        if self.tableRetrieve(key)[1]:  # retrieved item
            return False
        check = []
        i = key % self.length
        while self.items[i] is not None:  # zolange de items niet none zijn
            i = (i ** 2) + key % self.length  # de formule voor quadratic
            if i >= self.length:
                i = i % self.length
            if self.items[i] == None:  # als ze leeg is
                new = Item(key, val.value)  # maak object
                new.value = val.value  # stel items gelijk
                new.searchkey = key
                self.items[i] = new  # de locatie is onze object
                self.count += 1
                return True
            else:
                if i in check:
                    return False
                else:
                    check.append(i)
                i += 1
        new = Item(key, val.value)  # object maken
        new.value = val.value  # gelijk stellen van data
        new.searchkey = key
        self.items[i] = new
        self.count += 1
        return True

    def separateProbing(self, val):
        """
        een functie die items toevoegt door middel van seprate chaining
        :param val: data
        :return: true or false
        """

        key = val.searchkey % self.length  # gaat naar zijn locatie
        if self.items[key] != None:  # als de loc leeg is dan kijkt hij of hij een instance ervan is
            if isinstance(self.items[key], LinkedChain):
                self.items[key].insert(1, val)  # voegt ze toe in de items
                self.count += 1  # count +1
                return True
        else:
            l = LinkedChain()  # we maken object van linkedchain
            l.insert(1, val)  # we voegen items toe
            self.items[key] = l
            self.count += 1
            return True

    def tableInsert(self, val):
        """
        een functie om items toe te voegen
        :param val: data
        :return: de gevraagde type soort insert
        """

        if self.type == "lin":  # als type lin is
            return self.linearProbing(val)
        elif self.type == "quad":  # als type quad is
            return self.quadraticProbing(val)
        elif self.type == "sep":  # als type sep is
            return self.separateProbing(val)
        else:
            return False

    def save(self):
        """
        een functie om hash te printen
        :return:  de hash in een dictonary
        """
        result = []
        if self.type == "lin" or self.type == "quad":  # allen voor lin en quad
            for i in range(self.length):
                item = self.items[i]
                if item is not None:  # checkt voor none
                    result.insert(i, item.value)
                else:
                    result.insert(i, None)
        if self.type == "lin":
            return {'type': self.type, 'items': result}
        elif self.type == "quad":
            return {'type': self.type, 'items': result}
        elif self.type == "sep":  # sep apate formule
            dict = {'type': self.type, 'items': []}  # stelt een dict aan de gevraagde items
            for i in range(len(self.items)):  # lus die loopt over de lengte
                if self.items[i] is None:
                    dict['items'].append(None)
                else:
                    list = []
                    if isinstance(self.items[i], LinkedChain):  # checkt of het een instance is van linkedchain
                        curr = self.items[i].head
                        while curr.next != self.items[i].head and curr.next != None:
                            list.append(curr.value.searchkey)
                            curr = curr.next
                        if curr.next == self.items[i].head:  # curr next van items head
                            list.append(curr.value.searchkey)
                        if curr.next == None:  # curr is none
                            list.append(curr.value.searchkey)  # append van de item
                    dict['items'].append(list)
            return dict
        else:
            return False

    def tableRetrieve(self, key):
        """
        een funcite die via key een item retrieved
        :param key: ket
        :return: waarde, boolean
        """
        for i in range(self.length):
            if self.items[i] != None:
                if self.items[i].searchkey == key:
                    return self.items[i].value, True
        return None, False

    def getLength(self):
        """
        lengte
        :return: de lengte
        """
        return len(self.items)

    def load(self, dict):
        """
        een load pakt een dict en zet die in onze hash
        :param dict:  data
        :return: niets
        """
        if dict['type'] == 'sep':  # alles leeg stellen
            self.items = []
            self.length = 0
            self.type = ""
            self.count = 0

            for i in dict['items']:  # lus met doorloopen van de items
                if i == None:
                    self.items.append(None)
                    self.length = len(dict['items'])
                    self.type = 'sep'
                    self.count = self.length
                else:
                    self.length = len(dict['items'])  # checkt de lengte en stelt gelijk aan de legte
                    self.type = 'sep'
                    self.count = self.length
                    self.items.append(LinkedChain())
                    for item in reversed(i):  # reversen van de items en toevoegen bij de items list
                        new = Item(item, item)
                        self.items[self.getLength() - 1].insert(1, new)
        else:
            self.items = []  # deze geldt voor de rest dus voor lin en quad
            self.length = 0
            self.type = ""
            self.count = 0
            self.type = dict['type']
            if 'items' in dict:  # gelijkaardeige maar deze kijkt na of items er in zitten
                self.items = dict['items']
                self.length = len(self.items)
                for i in range(self.length):
                    item = self.items[i]
                    if self.items[i] != None:  # als geen none
                        new = Item(item, item)  # maak object van item
                        new.value = item
                        new.searchkey = item
                        self.items[i] = new
                        self.count += 1

    def getObject(self, key):
        """
        get object
        :param key: data
        :return:  waarde ,boolean
        """
        for i in range(self.length):
            if self.items[i] != None:
                if self.items[i].searchkey == key:
                    return self.items[i], True
        return None, False

    def tableDelete(self, key):
        """
        een functie delete die items verwijdert
        :param key: data
        :return: true or false
        """
        if self.type == "lin" or self.type == "quad":  # alleen voor lin en quad
            object = self.getObject(key)[0]
            if object != None:  # object niet gelijk aan none
                i = self.items.index(object)
                self.items[i] = None
                self.count -= 1
                return True
            else:
                return False
        elif self.type == "sep":  # deze is voor de seperate
            val = key % self.length  # modeulo formule
            if self.items[val] is None:
                return False
            else:
                if isinstance(self.items[val], LinkedChain):  # instance checken voor items in linkedchain
                    curr = self.items[val].head
                    while curr.next != self.items[
                        val].head and curr.next != None:  # zolang de curr.next niet gelijk aan de self.items[val].head en de curr.next mag niet none zijn
                        if curr.value.searchkey == key:  # checkt voor de key of ze gelijk is
                            self.items[val].delete(curr.id)
                            self.count -= 1
                            return True
                        curr = curr.next

                    if curr.next == self.items[val].head:  # als ze gelijk is met de head de next curr
                        if curr.value.searchkey == key:  # als de key gelijk is dan voert hij uit
                            self.items[val].delete(curr.id)
                            self.count -= 1
                            return True

                    if curr.next == None:  # als curr next leeg is
                        if curr.value.searchkey == key:  # als de key gelijk is dan voert hij uit
                            self.items[val].delete(curr.id)
                            self.count -= 1
                            return True
                    return False
        else:
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