#Ticket
#Gemaakt door: Menua
#Getest door: Denis
#**********************************
class Ticket:
    def __init__(self,pticket_vertoning_id,pticket_aantal):
        """
        De maakt een object Ticket aan
        :param pticket_vertoning_id: De vertoning_id van de ticket
        :param pticket_aantal: de aantal tickets
        """
        self.ticket_vertoning_id = pticket_vertoning_id
        self.ticket_aantal = pticket_aantal
