#Gebruiker
#Gemaakt door: Yasmine
#Getest door: Menua
#Aangepast door: Menua
#**********************************
class Gebruiker:
    def __init__(self, pgebruiker_id, pgebruiker_voornaam, pgebruiker_naam, pgebruiker_email):
        """
        Maakt een object Gebruiker aan
        :param pgebruiker_id: de id nummer van de gebruiker
        :param pgebruiker_voornaam: de voornaam van de gebruiker
        :param pgebruiker_naam: de naam van de gebruiker
        :param pgebruiker_email: de email van de gebruiker
        """
        self.gebruiker_id = pgebruiker_id
        self.gebruiker_voornaam = pgebruiker_voornaam
        self.gebruiker_naam = pgebruiker_naam
        self.gebruiker_email = pgebruiker_email


    def getGebruikerId(self):
        """
        We vragen de id van de gebruiker op bij deze functie
        :return: we geven de id van de gebruiker als return
        """
        return self.gebruiker_id

    def setGebruikerId(self, ngebruiker_id):
        """
        We geven de gebruiker een id bij de functie
        :param ngebruiker_id: De nieuwe id van de gebruiker
        :return:\
        """
        self.gebruiker_id = ngebruiker_id


    def getGebruikerVoornaam(self):
        """
        We vragen de voornaam van de gebruiker op bij deze functie
        :return: we geven de voornaam van de gebruiker als return
        """
        return self.gebruiker_voornaam

    def setGebruikerVoornaam(self, ngebruiker_voornaam):
        """
        We geven de gebruiker een voornaam bij de functie
        :param ngebruiker_voornaam: De nieuwe voornaam van de gebruiker
        :return: \
        """
        self.gebruiker_voornaam = ngebruiker_voornaam


    def getGebruikerNaam(self):
        """
        We vragen de naam van de gebruiker op bij deze functie
        :return: we geven de naam van de gebruiker als return
        """
        return self.gebruiker_naam

    def setGebruikerNaam(self, ngebruiker_naam):
        """
        We geven de gebruiker een naam bij de functie
        :param ngebruiker_naam: De nieuwe naam van de gebruiker
        :return: \
        """
        self.gebruiker_naam = ngebruiker_naam


    def getGebruikerEmail(self):
        """
        We vragen de email van de gebruiker op bij deze functie
        :return: we geven de email van de gebruiker als return
        """
        return self.gebruiker_email

    def setGebruikerEmail(self, ngebruiker_email):
        """
        We geven de gebruiker een email bij de functie
        :param ngebruiker_email:De nieuwe email van de gebruiker
        :return:\
        """
        if self.checkEmail(ngebruiker_email):
            self.gebruiker_email = ngebruiker_email


    def checkEmail(self,ngebruiker_email):
        """
        Bij deze functie berekenen we of de email geldig is
        :param ngebruiker_email: de email die we gaan valideren
        :return: True als het geldig is anders False
        """
        mail = []
        mail.extend(ngebruiker_email)
        if "@" not in mail:
            return False
        else:
            return True


