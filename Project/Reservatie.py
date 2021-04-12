#Reservatie
#Gemaakt door: Menua
#Getest door: Denis
#**********************************
class Reservatie:
    def __init__(self, preservatie_id, preservatie_gebruiker_id, preservatie_vertoning_id, preservatie_timerstamp, preservatie_aantal):
        """
        maakt een object reservatie aan
        :param preservatie_id: de reservatie id van de object
        :param preservatie_gebruiker_id: de gebruiker id van de object
        :param preservatie_vertoning_id: de vertoning id van de object
        :param preservatie_timerstamp: de timerstamp van de object
        :param preservatie_aantal: de reservatie aantal van de object
        """
        self.reservatie_id = preservatie_id
        self.reservatie_gebruiker_id = preservatie_gebruiker_id
        self.reservatie_vertoning_id = preservatie_vertoning_id
        self.reservatie_timerstamp = preservatie_timerstamp
        self.reservatie_aantal = preservatie_aantal


    def getReservatieId(self):
        """
        We vragen de id van de reservatie op bij deze functie
        :return: we geven de id van de reservatie als return
        """
        return self.reservatie_id

    def setReservatieId(self, nreservatie_id):
        """
        we geven de reservatie een id bij deze functie
        :param nreservatie_id: de nieuwe id van de reservatie
        :return: \
        """
        self.reservatie_id = nreservatie_id


    def getReservatieGebruikerId(self):
        """
        We vragen de gebruiker id van de reservatie op bij deze functie
        :return: we geven de gebruiker id van de reservatie als return
        """
        return self.reservatie_gebruiker_id

    def setReservatieGebruikerId(self, nreservatie_gebruiker_id):
        """
        we geven de reservatie een gebruiker id bij deze functie
        :param nreservatie_gebruiker_id:de nieuwe gebruiker id van de reservatie
        :return:\
        """
        self.reservatie_gebruiker_id = nreservatie_gebruiker_id


    def getReservatieVertoningId(self):
        """
        We vragen de vertoning id van de reservatie op bij deze functie
        :return:we geven de vertoning id van de reservatie als return
        """
        return self.reservatie_vertoning_id

    def setReservatieVertoningId(self, nreservatie_vertoning_id):
        """
        we geven de reservatie een vertoning id bij deze functie
        :param nreservatie_vertoning_id: de nieuwe vertoning id van de reservatie
        :return:\
        """
        self.reservatie_vertoning_id = nreservatie_vertoning_id


    def getReservatieTimerstamp(self):
        """
        We vragen de timerstamp van de reservatie op bij deze functie
        :return:we geven de timerstamp van de reservatie als return
        """
        return self.reservatie_timerstamp

    def setReservatieTimerstamp(self, nreservatie_timerstamp):
        """
        we geven de reservatie een  timerrstamp bij deze functie
        :param nreservatie_timerstamp: de nieuwe timerstamp van de reservatie
        :return: \
        """
        self.reservatie_timerstamp = nreservatie_timerstamp


    def getReservatieAantal(self):
        """
        We vragen de aantal van de reservatie op bij deze functie
        :return:we geven de aantal van de reservatie als return
        """
        return self.reservatie_timerstamp

    def setReservatieAantal(self, nreservatie_aantal):
        """
        we geven de reservatie een  aantal bij deze functie
        :param nreservatie_aantal:de nieuwe aantal van de reservatie
        :return:\
        """
        self.reservatie_aantal = nreservatie_aantal


