#Zaal
#Gemaakt door: Menua
#Getest door: Denis
#**********************************
class Zaal:
    def __init__(self, pzaal_id, pzaal_plaats):
        """
        Maakt een object Zaal aan
        :param pzaal_id: de id nummer van de zaal
        :param pzaal_plaats: de aantal zitplaatsen in een zaal
        """
        self.zaal_id = pzaal_id
        self.zaal_plaats = pzaal_plaats


    def getZaalId(self):
        """
        We vragen de id van de zaal op bij deze functie
        :return: we geven de id van de zaal als return
        """
        return self.zaal_id

    def setZaalId(self, nzaal_id):
        """
        we geven de zaal een id bij deze functie
        :param nzaal_id: de nieuwe id van de zaal
        :return:\
        """
        self.zaal_id = nzaal_id


    def getZaalPlaats(self):
        """
        We vragen de aantal zitplaatsen van de zaal op bij deze functie
        :return: we geven de aantal zitplaatsen als return
        """
        return self.zaal_plaats

    def setZaalPlaats(self, nzaal_plaats):
        """
        we geven de aantal zitplaats bij deze functie
        :param nzaal_plaats: de nieuwe aantal zitplaatsen van de zaal
        :return: \
        """
        self.zaal_plaats = nzaal_plaats


