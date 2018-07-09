from pitanja import *

class Loader():
    def __init__(self):
        self.pitanja = ListaPitanja()

    def load(self, vrsta = 1):
        pitanje_1 = ""
        odgovor_1 = ""
        opcija_1 = ""
        opcija_2 = ""
        opcija_3 = ""
        opcija_4 = ""

        if vrsta == 1:
            pitanja_filmovi = self.pitanja.get_pitanja_filmovi()
            pitanje_1 = pitanja_filmovi.pitanje
            odgovor_1 = pitanja_filmovi.odgovor
            opcija_1 = pitanja_filmovi.odgovor
            opcija_2 = pitanja_filmovi.opcija2
            opcija_3 = pitanja_filmovi.opcija3
            opcija_4 = pitanja_filmovi.opcija4
        elif vrsta == 2:
                pitanja_muzika = self.pitanja.get_pitanja_muzika()
                pitanje_1 = pitanja_muzika.pitanje
                odgovor_1 = pitanja_muzika.odgovor
                opcija_1 = pitanja_muzika.odgovor
                opcija_2 = pitanja_muzika.opcija2
                opcija_3 = pitanja_muzika.opcija3
                opcija_4 = pitanja_muzika.opcija4
        elif vrsta == 3:
                pitanja_igrice = self.pitanja.get_pitanja_igrice()
                pitanje_1 = pitanja_igrice.pitanje
                odgovor_1 = pitanja_igrice.odgovor
                opcija_1 = pitanja_igrice.odgovor
                opcija_2 = pitanja_igrice.opcija2
                opcija_3 = pitanja_igrice.opcija3
                opcija_4 = pitanja_igrice.opcija4

        elif vrsta == 4:
                pitanja_sport = self.pitanja.get_pitanja_sport()
                pitanje_1 = pitanja_sport.pitanje
                odgovor_1 = pitanja_sport.odgovor
                opcija_1 = pitanja_sport.odgovor
                opcija_2 = pitanja_sport.opcija2
                opcija_3 = pitanja_sport.opcija3
                opcija_4 = pitanja_sport.opcija4

        operacijaProveri = [pitanje_1, odgovor_1]
        odgovori = [opcija_1, opcija_2, opcija_3, opcija_4]
        random.shuffle(odgovori)
        load = operacijaProveri + odgovori
        return load
