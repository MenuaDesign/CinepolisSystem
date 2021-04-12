#Film
#Gemaakt door: Menua
#Getest door: Denis
#**********************************
class Film:
    def __init__(self, pfilm_id, pfilm_titel, pfilm_rating):
        """
        Maakt een object Film aan
        :param pfilm_id: De id nummer van een film
        :param pfilm_titel: de titel van een film
        :param pfilm_rating: de rating van een film
        """
        self.film_id = pfilm_id
        self.film_titel = pfilm_titel
        self.film_rating = pfilm_rating


    def getFilmId(self):
        """
        We vragen de id van de film op bij deze functie
        :return: we krijgen hier de id van de film als return
        """
        return self.film_id

    def setFilmId(self, nfilm_id):
        """
        We geven de film een id bij deze functie
        :param nfilm_id: de nieuwe film id
        :return: \
        """
        self.film_id = nfilm_id


    def getFilmTitel(self):
        """
        We vragen de titel van de film op bij deze functie
        :return:we krijgen hier de titel van de film als return
        """
        return self.film_titel

    def setFilmTitel(self, nfilm_titel):
        """
        We geven de film een titel bij deze functie
        :param nfilm_titel: de nieuw titel van de film
        :return:\
        """
        self.film_titel = nfilm_titel


    def getFilmRating(self):
        """
        We vragen de titel van de film op bij deze functie
        :return: we krijgen hier de rating van de film als return
        """
        return self.film_rating

    def setFilmRating(self, nfilm_rating):
        """
        We geven de film een rating bij deze functie
        :param nfilm_rating: de nieuwe rating van de film
        :return: \
        """
        if not isinstance(nfilm_rating, float):
            self.film_rating = 0.00
        if nfilm_rating > 5.00:
            self.film_rating = 5.00
        if nfilm_rating == None:
            self.film_rating = 0.00
        if nfilm_rating <= 5.00:
            self.film_rating = round(nfilm_rating,2)

