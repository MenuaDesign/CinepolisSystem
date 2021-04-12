def createTreeItem(key,value):
    """
    Een functie die key en valueue omzet in een object die compatibel is met onze boom
    :param key: Een searchkey die de valueue indexeert in onze boom
    :param value: De valueue die we in onze boom willen toevoegen
    :return: Hij returnt n en n is een object van bst waarvan zijn root gelijk is aan value en zijn searchkey aan key
    """
    n = BST() #aanmaken object
    n.root = value
    n.searchkey = key
    return n

class BST:
    def __init__(self):
        """
        Onze constructor die een root,left,right,searchkey en een parent heeft, we initialseren onze variabelen hier
        """
        self.root=None
        self.left=None
        self.right=None
        self.searchkey = None
        self.parent = None

    def isEmpty(self):
        """
        Een functie die kijkt dat onze boom leeg is
        :return: True als hij leeg is anders True
        """
        if self.root is None:
            return True
        else:
            return False

    def searchTreeInsert(self,newItem):
        """
        Een functie die een item in onze boom insert
        :param newItem: Onze item die we willen inserten in onze boom
        :return: True als inserten is gelukt anders False
        """
        if self.isEmpty(): #kijkt na of onze boom leeg is
            self.root = newItem.root # stelt onze root gelijk aan de root van de nieuweitem
            self.searchkey = newItem.searchkey#ook de searchkey
            return True
        else:
            if self.searchkey > newItem.searchkey: #eerste variatie, als de searchkey groter is dan moet hij links van de boom inserten
                if self.left is None: #hij kijkt na of de linker kind leeg is zoja insert hij, anders gaat hij recursief telkens naar links zodat hij leeg is
                    self.left = newItem
                    self.left.parent = self
                    return True
                else:
                    self.left.searchTreeInsert(newItem) #onze recusrieve functie
            elif self.searchkey < newItem.searchkey: #tweede variatie, als de searchkey kleiner is dan moet hij naar rechts van de boom inserten
                if self.right is None: #hij kijkt na of de rechter kind leeg is zoja insert hij, anders gaat hij recursief telkens naar rechts zodat hij leeg is
                    self.right = newItem
                    self.right.parent = self
                    return True
                else:
                    self.right.searchTreeInsert(newItem)

    def searchTreeRetrieve(self, item):
        """
        deze functie neemt een key als input en returnt de item
        :param item: key waarvan we de item willen krijgen
        :return: We return een tupel als hij de item heeft gevonden de waarde,True anders None,False
        """
        if self.isEmpty():#kijkt na of het leeg is
            return None,False
        else:
            if self.searchkey == item: #als de searchkey gelijk is aan de key dan heeft hij die gevonden
                return self.root,True
            elif item < self.searchkey: #als de key kleiner is dan de huidige key dan gaat hij links
                if self.left is None: #maar als links leeg is dan returnt hij false
                    return None,False
                else:
                    return self.left.searchTreeRetrieve(item) #anders werkt hij recursief op links verder
            elif item > self.searchkey:#als de key kleiner is dan de huidige key dan gaat hij rechts
                if self.right is None:#maar als rechts leeg is dan returnt hij false
                    return None,False
                else:
                    return self.right.searchTreeRetrieve(item)#anders werkt hij recursief op rechts verder
    def inorderTraverse(self,func):
        """
        Functie die onze boom in inorder traversed, Hij gaat over elke node op een inorder volgorde
        :param func: func een print functie
        :return: niets
        """
        if self.left:
            self.left.inorderTraverse(func) #als hij een left heeft gaat hijlinks
        func(self.root) #hij print de waarde
        if self.right: #als hij rechts heeft gaat hij rechts
            self.right.inorderTraverse(func)

    def inorderSuccesor(self,bool=True):
        """
        Deze functie zoekt naar zijn inorder succesor
        :param bool: Deze is handig voor enkele berekeningen te vergemakkelijken
        :return: return de inordersuccesor van een node, hij returnt ook een node
        """
        if bool: #als bool waar is;  de bewerkingen worden eenmalig uitgevoerd omdat we recusrief de functie met een bool False werken
            return self.right.inorderSuccesor(False)
        elif self.left:
            return self.left.inorderSuccesor(False)
        return self

    def searchTreeDelete(self,key):
        """
        Een functie die een item in onze boom verwijdert
        :param key: de searchkey van de item die we willen verwijderen
        :return: True als het deleten is gelukt anders False
        """
        if self.isEmpty() is False:#kijkt na of het leeg is
            if key == self.searchkey: #als de key gelijk is aan de searchkey kijkt hij naar de verschillende variaties
                if self.left is None and self.right is None: #ten eerste kijkt hij na of hij kinderen heeft zo niet dan
                    if self.parent.left is self:#als hij op links zit dan zet hij die op None anders zit hij op rechts en zet hij die op None
                        self.parent.left = None
                    elif self.parent.right is self:
                        self.parent.right = None
                elif self.right is None:#als we geen rechter kind hebben maar wel een linker
                    if self == self.parent.left: #dan moet onze self gelijk zijn aan de left van onze parent zoja dan is de left ervan self.left
                        self.parent.left = self.left
                    else:
                        self.parent.right = self.left
                elif self.left is None: #hetzelfde maar dan voor de rechter zijden
                    if self == self.parent.right:
                        self.parent.right = self.right
                    else:
                        self.parent.left = self.right
                else:#anders heeft gaat hij zoeken naar zijn inordersucceror en ze ruilen van plaats en dan gaan we recursief te werk
                    node = self.inorderSuccesor()
                    self.root = node.root
                    self.searchkey = node.searchkey
                    node.searchkey = key
                    return node.searchTreeDelete(key)
                return True

            elif key < self.searchkey: #als key kleiner is dan gaat hij links
                if self.left:
                    return self.left.searchTreeDelete(key) #recursief opschuiven naar links
                else:
                    return False
            elif key > self.searchkey: #als hij groter is dan gaat hij naar rechts
                if self.right:
                    return self.right.searchTreeDelete(key) #recursief opschuiven naar rechts
                else:
                    return False
        else:
            return False

    def save(self):
        """
        Een functie die onze boom saved en print
        :return: Onze boom in een dictionary vorm
        """
        if self.left is None and self.right is None: #als link en rechts leeg zijn
            return {'root':self.root} #returnt hij de root
        elif self.left and self.right is None:#als hij enkel links heeft
            return {'root':self.root,'children':[self.left.save(),None]} #returnt hij recursief ook de root en de kind left
        elif self.right and self.left is None: #als hij enkel rechts heeft
            return {'root':self.root,'children':[None,self.right.save()]} #returnt hij recursief ook de root en de kind right
        else:
            return {'root':self.root,'children':[self.left.save(),self.right.save()]} #als hij beiden heeft dan returnt hij ze beide met een recursie

    def load(self,dict,bool=True):
        """
        een functie load die een dictionary omzet in een boom
        :param dict: De dictionary die we willen omzetten in een boom
        :param bool: Handig voor enkele bewerkingen
        :return: Niets
        """
        if bool: #als Bool waar is dan maken we onze boom volledig leeg
            self.root = None
            self.searchkey = None
            self.searchkey = None
            self.parent = None

        self.root = dict['root'] #de root is 'root'
        self.searchkey = self.root
        if 'children' in dict: #als hij kinderen heeft
            if dict['children'][0]: #kijkt hij of hij links een kind heeft
                self.left = BST() #een object boom(node)
                self.left.parent = self
                self.left.load(dict['children'][0],False) #recursief met False om onze boom niet meer leeg te maken
            if dict['children'][1]:#kijkt hij of hij rechts een kind heeft
                self.right = BST() #een object boom (node)
                self.right.parent = self
                self.right.load(dict['children'][1],False) #recursief met False om onze niet meer leeg te maken


class Table:
    def __init__(self):
        """
        constructor Object van BST
        """
        self.tree = BST()

    def tableIsEmpty(self):
        """
        verwijst naar isEmpty() in BST
        :return: True als hij leeg is anders False
        """
        return self.tree.isEmpty()

    def tableInsert(self,key,newItem):
        """
        verwijst naar searchTreeInsert() in BST
        :param newItem: Onze item die we willen inserten in onze boom
        :return: True als inserten is gelukt anders False
        """
        return self.tree.searchTreeInsert(createTreeItem(key,newItem))

    def tableRetrieve(self,item):
        """
        verwijst naar searchTreeRetrieve() in BST
        :param item: key waarvan we de item willen krijgen
        :return: We return een tupel als hij de item heeft gevonden de waarde,True anders None,False
        """
        return self.tree.searchTreeRetrieve(item)

    def traverseTable(self,func):
        """
        verwijst naar inorderTraverse() in BST
        :param func: een print functie
        :return: niets
        """
        return self.tree.inorderTraverse(func)

    def save(self):
        """
        verwijst naar save() in BST
        :return: Onze boom in een dictionary vorm
        """
        return self.tree.save()

    def load(self,dict):
        """
        verwijst naar load() in BST
        :param dict: De dictionary die we willen omzetten in een boom
        :return: Handig voor enkele bewerkingen
        """
        return self.tree.load(dict)

    def tableDelete(self,key):
        """
        verwijst naar searchTreeDelete() in BST
        :param key: de searchkey van de item die we willen verwijderen
        :return: True als het deleten is gelukt anders False
        """
        return self.tree.searchTreeDelete(key)
