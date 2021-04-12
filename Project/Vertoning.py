#Vertoning
#Gemaakt door: Denis
#Getest door: Menua
#**********************************
from Denis.Stack import Table as Ticketsdatabase

class Vertoning:
    def __init__(self, pvertoning_id, pvertoning_zaal_id,pvertoning_slot, pvertoning_datum,pvertoning_film_id, pvertoning_plaats):
        """
        Maakt een object Vertoning aan
        :param vertoning_id: De unieke id van de vertoning
        :param vertoning_zaal_id: De zaal id van de zaal waarin de vertoning gebeurt
        :param vertoning_film_id: De film id van de film die afgespeeld wordt
        :param vertoning_datum: De datum
        :param vertoning_slot: Het tijdsslot dat de film heeft
        :param vertoning_plaats: Aantal plaatsen in de vertoning
        :param vertoning_status:
        :param vertoning_status_tickets: Deze houd het aantal ticketen per vertoning bij
        :param vertoning_tickets: hierin wordt de stack per vertoning opgeslagen

        Precondities: De vertoning ID zelf is uniek. De andere id's juist niet, die moeten van een bestaand object zijn. De datum is altijd in dd-mm-yyyy formaat. Het slot is een integer tussen 0 en 3 en het aantal plaatsen is nooit negatief.
        Postcondities: Object Vertoning aangemaakt
        """
        self.vertoning_id = pvertoning_id
        self.vertoning_zaal_id = pvertoning_zaal_id
        self.vertoning_datum = pvertoning_datum
        self.vertoning_slot = pvertoning_slot
        self.vertoning_film_id = pvertoning_film_id
        self.vertoning_plaats = pvertoning_plaats
        self.vertoning_status = None
        self.vertoning_status_tickets=0
        self.vertoning_tickets = Ticketsdatabase()


    def getVertoningId(self):
        """
        Geeft de vertoning id terug
        :return: (self.ID)

        Precondities: Geen
        Postcondities: Laat de id zien van de huidige vertoning
        """
        return self.vertoning_id

    def setVertoningId(self, nvertoning_id):
        """
        Zet een nieuwe id op de vertoning
        :param nvertoning_id: Nieuwe Vertoning ID
        :return: \

        Precondities: Mag niet dezelfde ID als een andere voorstelling
        Postcondities: Nieuwe ID voor de vertoning
        """
        self.vertoning_id = nvertoning_id


    def getVertoningZaalId(self):
        """
        Geeft de Zaal id terug
        :return: (self.ZaalID)
        Precondities: Geen
        Postcondities: Laat de id zien van de huidige Zaal
        """
        return self.vertoning_zaal_id

    def setVertoningZaalId(self, nvertoning_zaal_id):
        """
         Zet een nieuwe zaalid op de vertoning
         :param nzaal_id: Nieuwe zaal ID
         :return: \

         Precondities: Mag niet dezelfde ID als de zaal id van een andere vertoning
         Postcondities: Nieuwe ZaalID voor de vertoning
        """
        self.vertoning_zaal_id = nvertoning_zaal_id


    def getVertoningDatum(self):
        """
        Geeft de Datum terug
        :return: (self.Datum)

        Precondities: Geen
        Postcondities: Geeft de datum terug
        """
        return self.vertoning_datum

    def setVertoningDatum(self, nvertoning_datum):
        """
        Zet een nieuwe datum op de vertoning
        :param ndate: Nieuwe datum
        :return: \

        Precondities: Datum moet in dd-mm-yyyy formaat
        Postcondities: Nieuwe datum voor de vertoning
        """
        self.vertoning_datum = nvertoning_datum


    def getVertoningFilmId(self):
        """
        Geeft de FilmID terug
        :return: (self.FilmID)

        Precondities: Geen
        Postcondities: Geeft de FilmID terug
        """
        return self.vertoning_film_id

    def setVertoningFilmId(self, nvertoning_film_id):
        """
        Zet een nieuwe FilmID op de vertoning
        :param nfilm: Nieuwe FilmID
        :return: \

        Precondities: FilmID moet van een bestaande film zijn.
        Postcondities: Nieuwe FilmID vvoor de vertoning
        """
        self.vertoning_film_id = nvertoning_film_id


    def getVertoningSlot(self):
        """
        Geeft het slot terug
        :return: (self.Slot)

        Precondities: Geen
        Postcondities: Geeft het Slot terug
        """
        return self.vertoning_slot

    def setVertoningSlot(self, nvertoning_slot):
        """
        Zet een nieuw Slot op de vertoning
        :param nslot: Nieuw Slot
        :return: \

        Precondities: Slot moet een getal tussen 0 en 3 zijn
        Postcondities: Nieuw Slot voor de vertoning
        """
        if nvertoning_slot == 1:
            self.vertoning_slot = "14:30"
        if nvertoning_slot == 2:
            self.vertoning_slot = "17:00"
        if nvertoning_slot == 3:
            self.vertoning_slot = "20:00"
        if nvertoning_slot == 4:
            self.vertoning_slot = "22:30"

    def getVertoningPlaats(self):
        """
        Geeft het aantal plaatsen terug
        :return: (self.Plaatsen)

        Precondities: Geen
        Postcondities: Geeft het aantal plaatsen terug
        """
        return self.vertoning_plaats

    def setVertoningPlaats(self, nvertoning_plaats):
        """
        Zet een nieuw plaatsaantal op de vertoning
        :param nPlaatsen: nieuw plaatsaantal
        :return: \

        Precondities: nieuw plaatsaantal mag geen negatief getal zijn
        Postcondities: Plaatsaantal is veranderd
        """
        self.vertoning_plaats = nvertoning_plaats
