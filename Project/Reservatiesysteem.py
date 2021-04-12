#Datastructuren
from .Denis.BST import Table as Filmdatabase
from .Menua.Chain import Table as ZaalData
from .Denis.Chain import Table as Gebruikerdatabase
from .Menua.BST import Table as Vertoningdatabase
from .Denis.Chain import Table as Reservatiedatabase
from .Menua.Queue import Table as VertoningQueue

#Klassen
from .Film import *
from .Zaal import *
from .Vertoning import *
from .Reservatie import *
from .Gebruiker import *
from .Ticket import *

#ReservatieSysteem
#**********************************
class ReservatieSysteem:
    def __init__(self):
        """
        Maakt een reservatiesysteem aan.

        Precondities: Als de chain gebruikt gaat worden voor eender welk gegevenstype dan moeten de id's van dat type beginnen van 1 en telkens +1 gaan. Alle ID's moeten integers zijn.
        """
        self.filmData = Filmdatabase() # ADT die films opslaat
        self.zaalData = ZaalData() # ADT die zalen opslaat
        self.gebruikersData = Gebruikerdatabase() # ADT die gebruikers opslaat
        self.vertoningData = Vertoningdatabase() # ADT die Vertoningen opslaat
        self.reservatieData = Reservatiedatabase() # ADT die Reservaties opslaat
        self.vertoningQueue = VertoningQueue(100) # ADT die ook Vertoningen opslaat
        self.reservatie_id = 0



#Film
#Gemaakt door: Menua
#**********************************

    def addFilm(self,pfilm_id,pfilm_titel,pfilm_rating):
        """
        Voegt een film toe aan zijn toegewezen ADT
        :param pfilm_id: id van de film
        :param pfilm_titel: titel van de film
        :param pfilm_rating: rating van de film
        :return: True of False
        """
        return self.filmData.tableInsert(pfilm_id,Film(pfilm_id,pfilm_titel,self.checkRating(pfilm_rating))) # Insert film in toegewezen datatype

    def checkRating(self,pfilm_rating):
        """
        Controleert of de gegeven rating geldig is
        :param pfilm_rating: De rating van film
        :return: rating
        """
        rating = 0.0
        if not isinstance(pfilm_rating, float): # Als de rating geen float is dan maakt het een float ervan
            rating = 0.0
        if pfilm_rating > 5.00: # Als er een rating gegeven wordt die groter is dan 5.00 dan wordt die automatisch op 5.00 gezet
            rating = 5.00
        if pfilm_rating == None: # Als er geen rating gegeven wordt dan wordt de rating op 0.00 gezet
            rating = 0.00
        if pfilm_rating <= 5.00: # Als de rating kleiner of gelijk aan 5.00 dan is onze rating gelijk aan de ingegeven rating afgerond op 2 getallen na de komma.
            rating = round(pfilm_rating,2)
        return rating

    """
    def deleteFilm(self,pfilm_id):
        if self.filmData.tableRetrieve(pfilm_id)[1]:
            self.filmData.tableDelete(pfilm_id)
            ##!!verwijderen in Reservatie !!##
            return True
        return False

    def retrieveFilm(self,pfilm_id):
        return self.filmData.tableRetrieve(pfilm_id)

    def modifyFilm(self,pfilm_id, pfilm_titel, pfilm_rating):
        if self.filmData.tableRetrieve(pfilm_id)[1]:
            f = self.retrieveFilm(pfilm_id)[0]
            if pfilm_titel == None:
                pfilm_titel = f.film_titel
            if pfilm_rating == None:
                pfilm_rating = f.film_rating
            f.film_titel = pfilm_titel
            f.film_rating = self.checkRating(pfilm_rating)

            ##!! moet ook aanpassen in Reservatie!!##
            return True

        return False
    """

#Zaal
#Gemaakt door: Menua
#**********************************

    def addZaal(self,pzaal_id,pzaal_plaats):
        """
        Voegt een zaal toe aan zijn toegewezen ADT
        :param pzaal_id: id van de zaal
        :param pzaal_plaats: aantal plaatsen van de zaal
        :return: True of False
        """
        return self.zaalData.tableInsert(pzaal_id,Zaal(pzaal_id,pzaal_plaats)) # Insert zaal in toegewezen datatype

    """
    def deleteZaal(self,pzaal_id):
        if self.zaalData.tableRetrieve(pzaal_id)[1]:
            self.zaalData.tableDelete(pzaal_id)
            ##!!verwijdert ook alles dat ermee is gelinkt, dus een reservatie een vertoning!!##
            return True
        return False

    def retrieveZaal(self,pzaal_id):
        return self.zaalData.tableRetrieve(pzaal_id)

    def modifyZaal(self,pzaal_id,pzaal_plaats):
        if self.retrieveZaal(pzaal_id)[1]:
            f = self.retrieveZaal(pzaal_id)[0]
            ##Elke aanpassing moet ook angepast worden in vertoning en reservatie##
            f.zaal_plaats = pzaal_plaats
            return True
        return False
    """

#Gebruiker
#Gemaakt door: Yasmine
#Getest door: Denis
#**********************************

    def addGebruiker(self,pgebruiker_id,pgebruiker_voornaam,pgebruiker_naam,pgebruiker_email):
        """
        Voegt een gebruiker toe aan zijn toegewezen datatype
        :param pgebruiker_id: id van gebruiker
        :param pgebruiker_voornaam: voornaam van de gebruiker
        :param pgebruiker_naam: achternaam van de gebruiker
        :param pgebruiker_email: email van de gebruiker
        :return: True of False

        Precondities: Alles buiten de ID moet een string zijn
        """
        user = Gebruiker(pgebruiker_id,pgebruiker_voornaam,pgebruiker_naam,pgebruiker_email)
        return self.gebruikersData.tableInsert(pgebruiker_id, user) # Insert Gebruiker in toegewezen datatype

    """
    def deleteGebruiker(self,pgebruiker_id):
        if self.gebruikersData.tableIsEmpty():
            return False
        user = self.vertoningData.tableRetrieve(pgebruiker_id)
        if user[1] == False:
            return False
        return self.gebruikersData.tableDelete(pgebruiker_id)

        # AANPASSEN***********************************

    def retrieveGebruiker(self,pgebruiker_id):
        if self.gebruikersData.tableIsEmpty() or self.gebruikersData.tableRetrieve(pgebruiker_id) == False:
            return False
        else:
            return vars(self.gebruikersData.tableRetrieve(pgebruiker_id)[0])

    def modifyGebruiker(self,pgebruiker_id,pgebruiker_voornaam,pgebruiker_naam,pgebruiker_email):
        if self.retrieveGebruiker(pgebruiker_id)[1]:
            f = self.retrieveGebruiker(pgebruiker_id)[0]
            if pgebruiker_naam == None:
                pgebruiker_naam = f.gebruiker_naam
            if pgebruiker_voornaam == None:
                pgebruiker_voornaam = f.gebruiker_voornaam
            if pgebruiker_email == None:
                pgebruiker_email = f.gebruiker_email

            f.gebruiker_voornaam = pgebruiker_voornaam
            f.gebruiker_naam  = pgebruiker_naam
            f.gebruiker_email = pgebruiker_email
            return True
        return False
    """

#Vertoning
#Gemaakt door: Denis
#Getest door Menua
##**********************************

    def addVertoning(self,pvertoning_id,pvertoning_zaal_id,pvertoning_slot,pvertoning_datum,pvertoning_film_id,pvertoning_plaats):
        """
        Maakt een vertoning aan voor zijn toegepaste datatype
        :param pvertoning_id: id van de vertoning
        :param pvertoning_zaal_id: id van de zaal
        :param pvertoning_slot: het tijdsslot
        :param pvertoning_datum: de datum
        :param pvertoning_film_id: id van de film
        :param pvertoning_plaats: aantal plaatsen
        :return: True of False
        
        Precondities : Slot>4 of Slot <1 is niet toegestaan, datum is een string in yyyy-mm-dddd formaat. Zaal en film moeten bestaan voordat vertoning wordt aangemaakt
        """
        if pvertoning_slot > 4 or pvertoning_slot < 1:
            return None
        V = Vertoning(pvertoning_id, pvertoning_zaal_id, self.setSlotVertoing(pvertoning_slot), pvertoning_datum,pvertoning_film_id,pvertoning_plaats)
        self.vertoningQueue.tableInsert(V)
        return self.vertoningData.tableInsert(pvertoning_id, V)

    def setSlotVertoing(self,nvertoning_slot):
        """
        Check welk slot de vertoning heeft
        :param nvertoning_slot: het gegeven slot
        :return: het uur met het gegeven slot gelinkt in string vorm
        """
        vertoning_slot =""
        if nvertoning_slot == 1:
            vertoning_slot = "14:30"
        if nvertoning_slot == 2:
            vertoning_slot = "17:00"
        if nvertoning_slot == 3:
            vertoning_slot = "20:00"
        if nvertoning_slot == 4:
            vertoning_slot = "22:30"
        return vertoning_slot

    """
    def deleteVertoning(self,pvertoning_id):
        if self.vertoningData.tableIsEmpty():
            return False
        Vert = self.vertoningData.tableRetrieve(pvertoning_id)
        if Vert[1] == False:
            return False
        return self.vertoningData.tableDelete(pvertoning_id)
        #AANPASSEN***********************************

    def retrieveVertoning(self,pvertoning_id):
        if self.vertoningData.tableIsEmpty() or self.vertoningData.tableRetrieve(pvertoning_id) == False:
            return False
        else:
            return self.vertoningData.tableRetrieve(pvertoning_id)

    def modifyVertoning(self,pvertoning_id,code, newvalue): #code = welke item je wilt aanpassen en newvalue de waarde.

        v = self.vertoningData.tableRetrieve(pvertoning_id)[0]
        if code < 1 or code > 5:
            return False
        elif code == 1:
            v.vertoning_zaal_id = newvalue
            return True
        elif code == 2:
            v.vertoning_datum = newvalue
            return True
        elif code == 3:
            v.vertoning_film_id = newvalue
            return True
        elif code == 4:
            v.vertoning_slot = self.setSlotVertoing(newvalue)
            return True
        else:
            v.vertoning_plaats = newvalue
            return True
        # AANPASSEN***********************************
    """

#Ticket
#Gemaakt door: Menua
#Getest door: Denis
#**********************************

    def addTicket(self,pticket_vertoning_id, pticket_aantal):
        """
        Maakt een Ticket type aan dat op de stack gepushed gaat worden bij een reservatie
        :param pticket_vertoning_id: id van de vertoning waarop het moet
        :param pticket_aantal: Het aantal bestelde ticketten
        :return: /
        """
        ticket = Ticket(pticket_vertoning_id,pticket_aantal)
        stack = self.vertoningData.tableRetrieve(pticket_vertoning_id)[0].vertoning_tickets
        for i in range(pticket_aantal):
            stack.tableInsert(ticket)


#Reservatie
#Gemaakt door: Menua
#Getest door: Denis
#**********************************

    def addReservatie(self,preservatie_gebruiker_id, preservatie_vertoning_id, preservatie_timerstamp, preservatie_aantal):
        """
        Reservatie wordt aangemaakt voor zijn toebehorend datatype
        :param preservatie_gebruiker_id: id van de gebruiker
        :param preservatie_vertoning_id: id van de vertoning
        :param preservatie_timerstamp: tijdstip
        :param preservatie_aantal: aantal tickets
        :return: true of false
        
        Precondities: Gebruiker en Vertoning moeten bestaan voordat de reservatie wordt gemaakt.
        """
        vertoning = self.vertoningData.tableRetrieve(preservatie_vertoning_id)
        gebruiker = self.gebruikersData.tableRetrieve(preservatie_gebruiker_id)
        if vertoning[1] and gebruiker[1]:
            self.reservatie_id += 1
            self.addTicket(preservatie_vertoning_id,preservatie_aantal)
            self.vertoningData.tableRetrieve(preservatie_vertoning_id)[0].vertoning_status_tickets += preservatie_aantal

            reservatie = Reservatie(self.reservatie_id,preservatie_gebruiker_id,preservatie_vertoning_id,preservatie_timerstamp,preservatie_aantal)
            return self.reservatieData.tableInsert(self.reservatie_id,reservatie)


