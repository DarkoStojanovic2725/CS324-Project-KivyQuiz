from kivy.clock import Clock
import json
import random
import inspect
import os

class Pitanja():
    def __init__(self, pitanje, odgovor, opcija2, opcija3, opcija4):
        self.pitanje = pitanje
        self.odgovor = odgovor
        self.opcija2 = opcija2
        self.opcija3 = opcija3
        self.opcija4 = opcija4

class ListaPitanja():
    def __init__(self, folderPitanja = "/pitanja"):
        self.folderPitanja = folderPitanja
        self.pitanja_filmovi = []
        self.pitanja_muzika = []
        self.pitanja_igrice = []
        self.pitanja_sport = []
        self.indeks_pitanja_filmovi = []
        self.indeks_pitanja_muzika = []
        self.indeks_pitanja_igrice = []
        self.indeks_pitanja_sport = []
        self.ucitajPitanja()

    def get_pitanja_filmovi(self):
        self.randomPitanje = self.pitanja_filmovi[random.randint(0, len(self.pitanja_filmovi) - 1)]
        print(self.indeks_pitanja_filmovi)
        if self.randomPitanje not in self.indeks_pitanja_filmovi:
            print("Nema u listi, dodavanje...")
            self.indeks_pitanja_filmovi.append(self.randomPitanje)
            return self.randomPitanje
        elif self.randomPitanje in self.indeks_pitanja_filmovi:
            print("Postoji u listi")
            self.randomPitanje = self.pitanja_filmovi[random.randint(0, len(self.pitanja_filmovi) - 1)]
            self.indeks_pitanja_filmovi.append(self.randomPitanje)
            print("dodat u listu")
            print(self.indeks_pitanja_filmovi)
            return self.randomPitanje

    def get_pitanja_muzika(self):
        self.randomPitanje = self.pitanja_muzika[random.randint(0, len(self.pitanja_muzika) - 1)]
        print(self.indeks_pitanja_muzika)
        if self.randomPitanje not in self.indeks_pitanja_muzika:
            print("Nema u listi, dodavanje...")
            self.indeks_pitanja_muzika.append(self.randomPitanje)
            return self.randomPitanje
        elif self.randomPitanje in self.indeks_pitanja_muzika:
            print("Postoji u listi")
            self.randomPitanje = self.pitanja_muzika[random.randint(0, len(self.pitanja_muzika) - 1)]
            self.indeks_pitanja_muzika.append(self.randomPitanje)
            print("dodat u listu")
            print(self.indeks_pitanja_muzika)
            return self.randomPitanje

    def get_pitanja_igrice(self):
        self.randomPitanje = self.pitanja_igrice[random.randint(0, len(self.pitanja_igrice) - 1)]
        print(self.indeks_pitanja_igrice)
        if self.randomPitanje not in self.indeks_pitanja_igrice:
            print("Nema u listi, dodavanje...")
            self.indeks_pitanja_igrice.append(self.randomPitanje)
            return self.randomPitanje
        elif self.randomPitanje in self.indeks_pitanja_igrice:
            print("Postoji u listi")
            self.randomPitanje = self.pitanja_igrice[random.randint(0, len(self.pitanja_igrice) - 1)]
            self.indeks_pitanja_igrice.append(self.randomPitanje)
            print("dodat u listu")
            print(self.indeks_pitanja_igrice)
            return self.randomPitanje

    def get_pitanja_sport(self):
        self.randomPitanje = self.pitanja_sport[random.randint(0, len(self.pitanja_sport) - 1)]
        print(self.indeks_pitanja_sport)
        if self.randomPitanje not in self.indeks_pitanja_sport:
            print("Nema u listi, dodavanje...")
            self.indeks_pitanja_sport.append(self.randomPitanje)
            return self.randomPitanje
        elif self.randomPitanje in self.indeks_pitanja_sport:
            print("Postoji u listi")
            self.randomPitanje = self.pitanja_sport[random.randint(0, len(self.pitanja_sport) - 1)]
            self.indeks_pitanja_sport.append(self.randomPitanje)
            print("dodat u listu")
            print(self.indeks_pitanja_sport)
            return self.randomPitanje
    #za ostale kategorije nakon testiranja za filmove

    def ucitajPitanja(self):
        with open(os.getcwd() + '/pitanja/pitanja.json') as json_fajl:
            json_podaci = json.load(json_fajl)

            for pitanje in json_podaci:
                if(pitanje["kategorija"] == "filmovi"):
                    self.pitanja_filmovi.append(Pitanja(pitanje["pitanje"], pitanje["odgovor"], pitanje["opcija2"], pitanje["opcija3"], pitanje["opcija4"]))
                elif(pitanje["kategorija"] == "muzika"):
                    self.pitanja_muzika.append(Pitanja(pitanje["pitanje"], pitanje["odgovor"], pitanje["opcija2"], pitanje["opcija3"], pitanje["opcija4"]))
                elif (pitanje["kategorija"] == "igrice"):
                    self.pitanja_igrice.append(
                        Pitanja(pitanje["pitanje"], pitanje["odgovor"], pitanje["opcija2"], pitanje["opcija3"],
                                pitanje["opcija4"]))
                elif (pitanje["kategorija"] == "sport"):
                    self.pitanja_sport.append(
                        Pitanja(pitanje["pitanje"], pitanje["odgovor"], pitanje["opcija2"], pitanje["opcija3"],
                                pitanje["opcija4"]))