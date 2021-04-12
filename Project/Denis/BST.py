def createTreeItem(key, value):
    """
    Maakt een nieuwe BST item aan met self.key=key en self.Root=value
    :param key: De zoeksleutel van het item.
    :param value: De waarde van het item.
    :return: Geeft de gemaakte BST terug.
    """
    Tree = BST()
    Tree.key = key
    Tree.Root = value
    return Tree


class BST:
    def __init__(self):  # Maakt een lege boom aan.
        """
        Maakt een boomklasse aan
        Preconditie:/
        Postconditie: Boomklasse gemaakt
        """
        self.Root = None
        self.left = None
        self.right = None
        self.key = None
        self.parent = None

    def isEmpty(self):  # Controleert of de boom leeg is, Zo ja geeft het True terug. Anders geeft het false terug.
        if self.Root == None:
            return True
        return False

    def searchTreeInsert(self, TreeItem):  # Insert een treeitem in de boom.
        """
        Insert een node
        :param TreeItem: De nieuweTreeitem
        :return: True of False afhankelijk of de node er al in zit of niet.

        Preconditie: Je kan geen node toevoegen met een key die al in de boom zit.
        Postconditie: Node is toegevoegd.
        """
        if BST.isEmpty(self):  # Als de boom leeg, is het nieuwe item de root.
            self.Root = TreeItem.Root
            self.key = TreeItem.key
            return True
        if BST.searchTreeRetrieve(self, TreeItem.key)[1]:  # Als er een item gevonden kan worden met dezelfde searchkey, dan kan je deze node niet toevoegen aan de boom.
            return False
        if self.key > TreeItem.key:  # Als  de key van het nieuwe item kleiner is controleren we of er een linkerkind is of niet. Zo ja, dan gaan we recursief tot we een plek vinden voor het nieuwe item. Zo nee, is het nieuwe item het linkerkind. En de ouder van het nieuwe item is de tree zelf.
            if self.left:
                return BST.searchTreeInsert(self.left, TreeItem)
            else:
                self.left = TreeItem
                self.left.parent = self
                return True
        else:
            if self.right:  # Als  de key van het nieuwe item groter is controleren we of er een rechterkind is of niet. Zo ja, dan gaan we recursief tot we een plek vinden voor het nieuwe item. Zo nee, is het nieuwe item het rechterkind. En de ouder van het nieuwe item is de tree zelf.
                return BST.searchTreeInsert(self.right, TreeItem)
            else:
                self.right = TreeItem
                self.right.parent = self
                return True

    def searchTreeRetrieve(self, key):
        """
        Zoekt een key in de tree en geeft de value terug.
        :param key: De searchkey van het item dat gevonden moet worden.
        :return:(value),True/False

        Precondities: Er mogen geen items in de boom zijn met eenzelfde zoeksleutel.
        Precondities: Geeft de value van de gezochte zoeksleutel terug.
        """
        if BST.isEmpty(self):  # Als de boom leeg is geeft het none terug als value en false als bool.
            return None, False
        if self.key == key:  # Als de huidige root dezelfde zoeksleutel heeft als de gezochte, wordt de waarde van de root samen met True teruggegeven.
            return self.Root, True
        if self.key > key:  # Als de key kleiner is dan de key van de huidige root, kijken we of er een linkerdeelboom is. Stel van wel, dan gaan we recursief op zoek naar ons item. Anders geven we None terug met bool false.
            if self.left:
                return BST.searchTreeRetrieve(self.left, key)
            return None, False
        if self.key < key:  # Als de key groter is dan de key van de huidige root, kijken we of er een rechterdeelboom is. Stel van wel, dan gaan we recursief op zoek naar ons item. Anders geven we None terug met bool false.
            if self.right:
                return BST.searchTreeRetrieve(self.right, key)
            return None, False

    def inorderTraverse(self, Functie=None,Traversed=[]):
        """
        Traversed de boom op inorder wijze. En afhankelijk van de functie doet het iets met die waarde.
        :param Functie: Wat er met de inorder waarden moet gebeuren. Print/Return/....., Als het niet ingevoerd wordt neemt de functie automatisch aan dat het een return is. Bij een return geven we de waarden gelijst terug, bij een print geven we ze gewoon afgedrukt terug.
        :param Traversed: Deze parameter wordt alleen maar gebruikt bij de return.
        :return:(Compleet afhankelijk van functie)

        Precondities:/
        Postcondities: Functie wordt uitgevoerd op de inorder items.
        """
        if (Functie!=None):
            if self.left != None:
                BST.inorderTraverse(self.left, Functie)
            Functie(self.key)
            if self.right != None:
                BST.inorderTraverse(self.right, Functie)
        else:
            if self.left != None:
                BST.inorderTraverse(self.left)
            Traversed.append(self.key)
            if self.right != None:
                BST.inorderTraverse(self.right)
        return Traversed

    def inorderSuccesor(self, Succ=True):
        if Succ:
            return BST.inorderSuccesor(self.right, False)  # Gaat recursief rechts af en kijkt bij de volgende recursie of er een node links is.
        if self.left:  # Zo ja recurseert hij over de linkse node anders geeft hij gewoon de current node terug.
            return BST.inorderSuccesor(self.left, False)
        return self
    def searchTreeDelete(self, item):
        """
        Delete een node uit een boom
        :param item: De te verwijderen node
        :return: (value/None,True/False)

        Preconditie: Als de root de enige node is mag je ze niet verwijderen
        Postconditie: Node is verwijdert
        """
        if not self.isEmpty():  # Kijkt of de boom leeg is of niet. Als die wel leeg is geeft hij gewoon false terug anders gaat hij verder.
            if item == self.key:  # Kijkt of de item gelijk is aan de huidige node zijn key.
                if self.left == None and self.right == None:  # Zo ja, controleert het of het een rechter kind of linker kind heeft,beiden of geen een.
                    if self.parent.left == self:
                        self.parent.left = None
                    elif self.parent.right == self:
                        self.parent.right = None
                elif self.right == None:  # Bij Als het linkerkind bestaat wisselt de methodie die van plaats met de parent en verwijderen we het item dat nu in een blad zit.
                    if self == self.parent.left:
                        self.parent.left = self.left
                    else:
                        self.parent.right = self.left
                elif self.left == None:  # Bij Als het rechterkind bestaat wisselt de methodie die van plaats met de parent en verwijderen we het item dat nu in een blad zit.
                    if self.parent:
                        if self == self.parent.right:
                            self.parent.right = self.right
                        else:
                            self.parent.left = self.right
                    else:
                        Succ = self.inorderSuccesor()
                        self.Root = Succ.Root
                        self.key = Succ.key
                        Succ.key = item
                        return Succ.searchTreeDelete(item)
                else:  # Vindt de inordersuccesor en wisselt die om met het te verwijderen item. Verwijder dan het item wanneer het een blad is. Dit is als er 2 kinderen zijn.
                    Succ = self.inorderSuccesor()
                    self.Root = Succ.Root
                    self.key = Succ.key
                    Succ.key = item
                    return Succ.searchTreeDelete(item)
                return True
            if item < self.key:  # Als item niet overeenkomt met self.key controleren we of deze groter of kleiner is dan de key en voeren we een recursief uit afhankelijk of het groter of kleiner is en of het linker of rechterkind bestaat.
                if self.left:
                    return BST.searchTreeDelete(self.left, item)
                return False
            if item > self.key:
                if self.right:
                    return BST.searchTreeDelete(self.right, item)
                return False
        return False

    def save(self):
        """
        Slaat de huidige boom op in een dict.
        :return: (Dict)

        Precondities:/
        Postcondities: Geeft de dictionary terug die van de boom is opgesteld.
        """
        Boompje = {"Root": None, "Children": []}  # Maakt een lege boomdict aan.
        if self.Root != None:  # Als de root in die boomdict leeg is wordt de root gelijkgesteld aan self.root.
            Boompje["Root"] = self.key
        if self.left != None:  # Als het linkerkind niet none is kijken we of het rechterkind none is. Zo ja voegen we een none waarde toe op de positie van het rechterkind. Anders niet
            if self.right == None:
                Boompje["Children"].append(self.left.save())
                Boompje["Children"].append(None)
            else:
                Boompje["Children"].append(self.left.save())
        if self.right != None:  # Exact hetzelfde als hierboven alleen omgedraaide volgorde.
            if self.left == None:
                Boompje["Children"].append(None)
                Boompje["Children"].append(self.right.save())
            else:
                Boompje["Children"].append(self.right.save())
        if len(Boompje["Children"]) == 0:  # Als de boom geen kinderen heeft wordt gewoon de onderstaande dict teruggegeven.
            return {"Root": self.key}
        if self == None:
            return {}
        return Boompje

    def emptyTree(self):  # Maakt de boom leeg.
        """
        Maakt de boom leeg voor het geval dat wij een nieuwe willen loaden.
        :return: /

        Precondities:/
        Postcondities: Maakt de boom leeg.
        """
        self.left=None
        self.right=None
        self.Root=None
        self.key=None

    def load(self, dict, NotEmpty=True):
        """
        Maakt de boom leeg en load een nieuwe daar in plaats.
        :param dict: De boom die moet worden ingeladen.
        :param Empty: Controleert of het leeg moet worden gemaakt of niet.
        :return:/

        Precondities:/
        Postcondities:Maakt de boom leeg en laad een nieuwe boom..
        """
        if NotEmpty:  # Als de boom niet leeg is wordt die leeggemaakt.
            BST.emptyTree(self)
        if len(dict) == 0 or dict=={}:  # Als de dict leeg is geeft het een lege boom terug.
            return BST.emptyTree(self)
        self.Root = dict["root"]  # Stelt de root gelijk aan de root van de dict.
        self.key = self.Root  # Stelt de key gelijk aan de root.
        if "children" in dict:  # Kijkt of het kinderen heeft.
            if dict['children'][
                0]:  # Als er een linkerkind is wordt self.left een bst klasse met parent de huidige root en worden de waarden recursief ingeladen.
                self.left = BST()
                self.left.parent = self
                self.left.load(dict['children'][0], False)
            if dict['children'][
                1]:  # Als er een rechterkind is wordt self.right een bst klasse met parent de huidige root en worden de waarden recursief ingeladen.
                self.right = BST()
                self.right.parent = self
                self.right.load(dict['children'][1], False)

class Table:
    def __init__(self):
        self.tree=BST()
    def tableIsEmpty(self):
        return self.tree.isEmpty()
    def tableInsert(self,key,Treeitem):
        return self.tree.searchTreeInsert(createTreeItem(key,Treeitem))
    def tableRetrieve(self,key):
        return self.tree.searchTreeRetrieve(key)
    def traverseTable(self,Func=None):
        return self.tree.inorderTraverse(Func)
    def load(self,NewTabel):
        return self.tree.load(NewTabel)
    def save(self):
        return self.tree.save()
    def tableDelete(self,key):
        return self.tree.searchTreeDelete(key)

