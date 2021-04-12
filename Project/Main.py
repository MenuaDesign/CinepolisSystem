#Klassen
import Project.Reservatiesysteem as reservatiesystem
#Main
#**********************************
class Main:
    def __init__(self,input):
        """
        Object main aanmaken
        :param input: de input txt
        """
        self.input = input
        self.listid = 0
        self.list = []
        self.login = []
        self.file = "Interface/templatefile"
        self.head = ""
        self.tmplist = ""
        self.gridId = 0

        self.system = reservatiesystem.ReservatieSysteem()

#Maken van alle objecten
#Gemaakt door: Denis
#**********************************
    def maakReservatie(self,preservatie_gebruiker_id, preservatie_vertoning_id, preservatie_timerstamp, preservatie_aantal):
        """
        een object aanmaken reservatie
        :param preservatie_gebruiker_id: de gebruiker id van de object
        :param preservatie_vertoning_id: de vertoning id van de object
        :param preservatie_timerstamp: de timerstamp van de object
        :param preservatie_aantal: de aantal van de object
        :return: een functie in de reservatiesysteem die reservatie aanmaakt in de database
        """
        return self.system.addReservatie(preservatie_gebruiker_id,preservatie_vertoning_id,preservatie_timerstamp,preservatie_aantal)

    def maakGebruiker(self,gebruiker_id,gebruiker_name,gebruiker_surname,gebruiker_email):
        """
        een object aanmaken gebruiker
        :param gebruiker_id: de gebruiker id
        :param gebruiker_name: de gebruiker naam
        :param gebruiker_surname: de gebruiker achternaam
        :param gebruiker_email: de gebruiker mail
        :return: een functie in de reservatiesysteem die gebuiker aanmaakt in de database
        """
        return self.system.addGebruiker(gebruiker_id,gebruiker_name,gebruiker_surname,gebruiker_email)

    def maakZaal(self,pzaal_id,pzaal_plaats):
        """
        een object aanmaken zaal
        :param pzaal_id: de zaal id
        :param pzaal_plaats: de zaal plaats
        :return: een functie in de reservatiesysteem die zaal aanmaakt in de database
        """
        return self.system.addZaal(pzaal_id,pzaal_plaats)

    def maakFilm(self,pfilm_id,pfilm_titel,pfilm_rating):
        """
        een object aanmaken film
        :param pfilm_id: de film id
        :param pfilm_titel: de film titel
        :param pfilm_rating: de film rating
        :return: een functie in de reservatiesysteem die film aanmaakt in de database
        """
        return self.system.addFilm(pfilm_id,pfilm_titel,pfilm_rating)

    def maakVertoning(self,pvertoning_id,pvertoning_zaal_id,pvertoning_slot,pvertoning_datum,pvertoning_film_id,pvertoning_plaats):
        """
        een object aanmaken vertoning
        :param pvertoning_id:  de vertoning id
        :param pvertoning_zaal_id: de vertoning zaal id
        :param pvertoning_slot: de vertoning slot
        :param pvertoning_datum:  de vertoning datum
        :param pvertoning_film_id: de vertoning film id
        :param pvertoning_plaats: de vertoning plaats
        :return: een functie in de reservatiesysteem die film aanmaakt in de database
        """
        return self.system.addVertoning(pvertoning_id,pvertoning_zaal_id,pvertoning_slot,pvertoning_datum,pvertoning_film_id,pvertoning_plaats)

#leesinput
#Gemaakt door: Menua
#**********************************
#lezen van input en omzetten in list
    def leesinput(self):
        """
        een functie die de txt bestand omzet in een list
        :return: de resulterende list
        """
        tmp = ""
        file = []
        #loop over de input file en kkijk na voor spaties
        for line in open(self.input).read():
            if line != "\n": #als er geen enter is voeg te char in tmp
                tmp += line

            elif line == "\n": #als er wel een enter is dan voeg je de tmp in de list en zet je tmp terug op leeg
                file.append(tmp)
                tmp = ""

        if "log" in tmp:
            file.append(tmp)
            tmp = ""

        length = len(file) #lengte van de list file
        t = []
        for i in range(length): #loopt tot de lengte
            if not "#" in file[i]: #als de waarde in file geen # bevat voeg ze toe in list t
                t.append(file[i])
        e = 0 #2de iterator
        length = len(t) #lengte van list t
        while(e<length): #zolang e kleiner is dan de lengte
            if t[e] == "":#als de waarde leeg is verwijder het en neem 1 af van de lengte
                t.remove(t[e])
                length = length - 1
                continue
            e += 1
        #deze stukje code lijnen zal el voor zorgen dat elke lijn in de input in een list wordt gezet
        tmp = [] #een temporary list
        for element in t: #loopt over de elementen in t verwijdert de , en voegt ze toe in een andere list sub
            sub = element.split(', ')
            tmp.append(sub)
        file = []
        file.extend(tmp)

        #omdat nu alle items in een list zitten moeten we sommige items samen zetten in 1 list
        file1= []
        for line in file: #we loopen nu over de lijnen in de list, dus hiermee bedoel ik de root listen
            bool = False
            word=""
            it = 0
            file2 = []
            file3 = []
            for items in line:#nu loopen we over de items in die list
                for char in items:#en nu over de character van die items
                    it += 1
                    if bool: #als bool true is dan wilt het zeggen dat hij " heeft gevonden
                        if char != '"': #als het geen " is dan voegt hij ze toe in word string
                            word += char
                        else: #als het wel een " voegt hij ze toe en zet bool op false
                            word += char
                            bool = False
                    elif char =='"': #als de char een " zet bool op true en voeg de char in word
                        bool = True
                        word += char
                    else:
                        if char != " ": #anders als de char geen spatie is voeg het toe aan de word
                            word += char
                        if char == " ": #als het wel een spatie is voeg het toe in file2, en voeg file 2 in file3 en zet file2 en worde op none
                            file2.append(word)
                            file3.append(file2)
                            file2 = []
                            word = ""
                        if it == len(items): #als de it gelijk is aan de lengte wilt het zeggen dat hij einde van woord heeft gehaald
                            if file3 != []: #als file3 niet leeg is dan voegt hij die toe aan file1
                                file2.append(word)
                                file3.append(file2)
                                file1.append(file3)
                            else:
                                file2.append(word) #anders voegt hij enkel file2 in file1
                                file1.append(file2)
        return file1

#strToint
#Gemaakt door: Menua/Denis
#**********************************
#van String naar int omzetten
    def strToint(self,pslot):
        """
        convert string naar int
        :param pslot: paramter slot
        :return: een int
        """
        tmp = ""
        for i in pslot:
            if i != ":":
                tmp += i

        return int(tmp)


    def reverseSlot(self,tijd):
        """
        we reversen terug van tijd naar slot
        :param tijd: de tijd die we willen reversen
        :return: de slot nummer van de tijd
        """
        vertoning_slot = 0
        if tijd == "14:30":
            vertoning_slot = 1
        if tijd == "17:00":
            vertoning_slot = 2
        if tijd == "20:00":
            vertoning_slot = 3
        if tijd == "22:30":
            vertoning_slot = 4
        return vertoning_slot


#aantalVertoning
#Gemaakt door: Menua/Denis
#**********************************
#Geeft de aantal vertoning per zaal_id
    def aantalVertoning(self,datum):
        """
        de aantalvertoning per zaalid
        :param datum: de datum van de log
        :return: een list met de vertoning van die dag in die zaal
        """
        var_a = 0
        tmp = []
        vertoning = self.system.vertoningQueue.save()
        vertoning.reverse()
        for i in vertoning:
            if i.vertoning_datum == datum:
                if not i.vertoning_zaal_id in tmp:
                    tmp.append(i.vertoning_zaal_id)
        return tmp

#setList
#Gemaakt door: Menua
#**********************************
#De data pakken en sorteren in een list
    def setList(self):
        """
        een functie die de data van de datastructuren haalt en zet met de nodige normen in een list
        :return: de resulterende list
        """
        uur = self.login[0] #uur van de log
        datum = self.login[1] #datum van de log
        film = self.system.filmData #datastructuur van film
        vertoning = self.system.vertoningQueue.save() #een list van de queue vertoningen
        vertoning.reverse() #reverse de queue zodanig dat de eerste vanboven komt
        tmplist=[]
        aantal = self.aantalVertoning(datum) #zet aantalvertoning in aantal door de functie aantalVertoningen te gebruiken
        slist = []
        string =""
        bool = True #een bool om een toepassingn eenmalig te uitvoeren
        index = 0
        plist = [None,None,None,None] #een standaard list met none
        flist = []
        listI = 0

        for i in vertoning: #we loopen over de queue
            if i.vertoning_datum == datum: # we kijken na of de datum klopt zo ja voeg aan list tmplist
                tmplist.append(i)
        tmplist = []
        for e in range(len(aantal)): #we loopen aantal keren dat er een vertoning is
            for k in vertoning: #we loopen over de films
                if k.vertoning_zaal_id == aantal[e]: #als ze overeen komen met de zaalid dan voeg toe aan tmplist
                    tmplist.append(k)
            self.listid += 1 #we houden een ingebouwde id van de grid bij
            slist.append(self.listid) #we voegen de id aan de slist
            slist.append(datum) #we voegen de log datum aan list omdat deze datum toch overeen komt met de film maakt het opzich niet uit
            for n in tmplist: #we gaan loopen over de object in de tmplist dit zijn alle vertoning op die datum
                listI = listI +1

                if n.vertoning_datum == datum: #als de datum overeen komt ga verder anders niet
                    if bool: #de eenmalige bewerking
                        slist.append(film.tableRetrieve(tmplist[listI].vertoning_film_id)[0].film_titel) #we boegen de filmtitel aan de slist
                        bool = False #we zetten de bool op false zodat we hier niet meer in komen

                    if self.strToint(n.vertoning_slot) <= self.strToint(uur): # we kijken na of de timestamp kleiner of gelijk is aan de uut
                        if n.vertoning_tickets.tableIsEmpty(): #als ze leeg is de stack
                            string = "F: " + str(n.vertoning_status_tickets) #dan is het F met de aantal tickets
                            plist[self.reverseSlot(n.vertoning_slot)-1] = string
                        else:
                            string = "W: " + str(n.vertoning_tickets.tableGetLength()) #als niet leeg is dan is het W + de lengte
                            plist[self.reverseSlot(n.vertoning_slot)-1] = string
                    elif self.strToint(n.vertoning_slot) >self.strToint(uur): #als de tijd groter is of anders, dan is het G met ook de lengte van de stack
                        string = "G: " + str(n.vertoning_tickets.tableGetLength())
                        plist[self.reverseSlot(n.vertoning_slot)-1] = string
            #we zetten vervolgens alles terug op nul
            index = 0
            tmplist = []
            bool = True
            listI = 0
            flist.append(slist+plist)
            plist = [None,None,None,None]
            slist = []
            string =""
        return flist


#popTicket
#Gemaakt door: Denis
#**********************************
#Haalt ticket uit de stack
    def popTicket(self,pvertoning_id,pvertoning_aantal):
        """
        een functie die tickets popt van de stack
        :param pvertoning_id: de vertoning id
        :param pvertoning_aantal: de vertoning aantal
        :return: geen return
        """
        stack = self.system.vertoningData.tableRetrieve(pvertoning_id)[0].vertoning_tickets
        for i in range(pvertoning_aantal):
            stack.tableDelete()

#create
#Gemaakt door: Denis
#**********************************
#Leest input en maakt objecten uit de txt
    def create(self):
        """
        een functie die na kijkt welke bewerking hij moet doen
        :return: geen return
        """
        list = self.leesinput() #hij zet de list gelijk aan list
        bool1 = False
        bool2 = False
        for i in list:

            if bool1: #als bool waar is dan moet je kijken naar de lists zijn waarde, als het gelijk komt aan de string, voer zijn bewerking dan uit
                if i[0][0] == "zaal":
                    self.maakZaal(int(i[1][0]), int((i[2][0])))
                if i[0][0] == "vertoning":
                    self.maakVertoning(int(i[1][0]), int(i[2][0]), int(i[3][0]), i[4][0], int(i[5][0]), int(i[6][0]))
                if i[0][0] == "gebruiker":
                    self.maakGebruiker(int(i[1][0]), i[2][0], i[3][0], i[4][0])
                if i[0][0] == "film":
                    self.maakFilm(int(i[1][0]), i[2][0], float(i[3][0]))

            if i[0] =="init": #als de item gelijk is aan init dan is de eerste bool op true en we kunnen beginnnen initailiseren anders niet
                bool1 = True

            if bool2 is True: #idem
                if i[2][0] == "reserveer":
                    timestamp = i[0][0] + " "+ i[1][0]
                    self.maakReservatie(int(i[3][0]),int(i[4][0]),timestamp,int(i[5][0]))

                if i[2][0] == "ticket":
                    self.popTicket(int(i[3][0]),int(i[4][0]))

                if i[2][0] == "log":
                    self.login.append(i[1][0])
                    self.login.append(i[0][0])


            if i[0] == "start":
                bool2 = True

#updateHtml
#Gemaakt door: Menua
#**********************************
#Hierin wordt de html bestand aangepast de nodige informatie wordt toegevoegd
    def updateHtml(self,list):
        """
        We maken een functie die de html bestand aanmaakt en aanpast
        :param list: de nodige input list met data
        :return:niets
        """
        items = "<td>{}</td>" #we maken de item tabel
        row =""
        headitem = "<th scope='row'>{}</th>" #de head dus de indexeren in dit geval
        date = "<h3>Log op <span>{}</span></h3>" #de aanpasing van de log tijd
        datum = self.login[1] +" " +self.login[0]
        if self.head == "": #functie die de template file opent en zet in tmplist
            with open(self.file) as file:
                self.tmplist = file.readlines()
                file.close()
            self.head = self.tmplist[0].strip() #we zetten de waarde0 in de head, deze items moeten niet worden aangepast
            self.head += date.format(str(datum)) #nu zetten we de datum wanneer we zijn ingelogde in de head
            self.head += self.tmplist[1].strip() #en nu zetten we nog een gedeelte dat niet moet worden aangepast
        #we loopen nu over de aantal lengte van de vertoning
        for i in range(len(self.aantalVertoning(self.login[1]))):
            row = "<tr>"
            self.gridId += 1 #een algemene gridview index
            row += headitem.format(str(self.gridId))
            #we loopen over de list zijn aantal en voegen de items er in toe aan de rows
            for e in range(1,len(list[i])):
                it = list[i][e]
                if it == None:
                    it =""
                row += items.format(str(it))

            row += "</tr>"
            self.head += row

#createHtml
#Gemaakt door: Menua
#**********************************
#Hier wordt het omgezet in een html
    def createHtml(self):
        """
        een functie die een html bestand aanmaakt
        :return: niks
        """
        full = self.head + self.tmplist[2]
        html = "Interface/log.html"
        log = open(html,"w")
        log.write(full)
        log.close()

#Start
#Gemaakt door: Menua
#**********************************
#hier wordt het systeem opgestart
    def Start(self,interface=False):
        """
        een functie die heel het systeem start
        :param interface:
        :return: niets
        """
        self.create()
        list = self.setList()
        if interface:
            m.updateHtml(list)
            m.createHtml()
        else:
            print(list)

if __name__ == "__main__":
    m = Main("input.txt")
    m.Start(True)