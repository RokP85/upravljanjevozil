# -*- coding: utf-8 -*-

class Vozilo(object):
    def __init__(self, znamka, model, kilometri, zadnji_servis):
        self.znamka = znamka
        self.model = model
        self.kilometri = kilometri
        self.zadnji_servis = zadnji_servis
    def podatki_vozila(self):
        print "{0} {1} s prevoženimi {2} kilometri, nazadnje servisiran {3}".format(self.znamka, self.model, self.kilometri, self.zadnji_servis)


seznam_vozil = "vozila.txt"
vozila = []
izpis_vozil = []


def dodaj_vozilo(vozila):
    print "\nDODAJANJE NOVEGA VOZILA"
    novo_vozilo = Vozilo(raw_input("Vnesi model: "), raw_input("Vnesi znamko: "), raw_input("Vnesi prevožene kilometre: "), raw_input("Vnesi datum zadnjega servisa: "))
    #print "Dodal si vozilo ", novo_vozilo.podatki_vozila()
    vozila.append(novo_vozilo)
    shrani(vozila)
    vrnitev_v_meni()


def izpis_seznama(seznam_vozil):
    print "\nSEZNAM VOZIL V LASTI PODJETJA"
    with open(seznam_vozil, "r") as seznam:
        for vrsta in seznam:
            znamka, model, kilometri, zadnji_servis = vrsta.split(",")
            ustvari_vozilo = Vozilo(znamka, model, kilometri, zadnji_servis)
            izpis_vozil.append(ustvari_vozilo)
    for index, vozilo in enumerate(izpis_vozil):
        index += 1
        print "{0}.) ".format(index), vozilo.podatki_vozila()


def urejanje_kilometrov(seznam_vozil):
    print "\nSEZNAM VOZIL V LASTI PODJETJA"
    for index, vozilo in enumerate(izpis_vozil):
        index += 1
        print "{0}.) ".format(index), vozilo.podatki_vozila()
    izbira = int(raw_input("Kateremu vozilu bi rad spremenil kilometre? Vpiši številko vozila: "))
    izbrano_vozilo = izpis_vozil[izbira-1]
    novi_km = raw_input("Koliko kilometrov ima po novem vozilo? Vpiši številko: ")
    izbrano_vozilo.kilometri = int(novi_km)
    print "\nSPREMEMBA: ", izbrano_vozilo.podatki_vozila()
    vrnitev_v_meni()

def urejanje_servisa(seznam_vozil):
    print "\nSEZNAM VOZIL V LASTI PODJETJA"
    for index, vozilo in enumerate(izpis_vozil):
        index += 1
        print "{0}.) ".format(index), vozilo.podatki_vozila()
    izbira = int(raw_input("Kateremu vozilu bi rad spremenil datum servisa? Vpiši številko vozila: "))
    izbrano_vozilo = izpis_vozil[izbira-1]
    nov_servis = raw_input("Vpiši nov datum zadnjega sevisa: ")
    izbrano_vozilo.zadnji_servis = nov_servis
    print "\nSPREMEMBA: ", izbrano_vozilo.podatki_vozila()
    vrnitev_v_meni()


def shrani(vozila):
    with open(seznam_vozil, "a") as seznam:
        for vozilo in vozila:
            seznam.write("%s,%s,%s,%s\n" %(vozilo.znamka, vozilo.model, vozilo.kilometri, vozilo.zadnji_servis))
            print "\nDodal si vozilo ", vozilo.podatki_vozila()

def vrnitev_v_meni():
    vrnitev = raw_input("\nAli se želiš vrniti v meni? ")
    if vrnitev in "DAdaDaJAjaJa":
        print "**********"
        main()
    elif vrnitev in "NEneNe":
        print "\n**********\nNasvidenje!"
    else:
        vrnitev_v_meni()

def main():
    print "Izberi eno izmed možnosti:\na) Dodajanje novega vozila\nb) Izpis seznama vseh vozil pojetja\nc) Urejanje prevoženih kilometrov\nd) Urejanje datuma zadnjega servisa\ne) Izhod"
    izbor = raw_input("Vnesi izbiro: ")
    if izbor in "Aa":
        dodaj_vozilo(vozila)
    elif izbor in "Bb":
        izpis_seznama(seznam_vozil)
        vrnitev_v_meni()
    elif izbor in "Cc":
        urejanje_kilometrov(seznam_vozil)
    elif izbor in "Dd":
        pass
    elif izbor in "Ee":
        print "\n**********\nNasvidenje!"
    else:
        print "Ups, izbral si neobstoječo možnost."
        main()













if __name__ == "__main__":
    "Pozdravljeni v upravitelju službenih vozil!\n"
    main()