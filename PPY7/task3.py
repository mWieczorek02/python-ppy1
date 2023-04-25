class Osoba:
    def __init__(self, imie, nazwisko, plec, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.data_urodzenia = data_urodzenia

    def wyswietl_info(self, typ):
        if typ == 'lista':
            print([self.imie, self.nazwisko, self.plec, self.data_urodzenia])
        elif typ == 'krotka':
            print((self.imie, self.nazwisko, self.plec, self.data_urodzenia))
        elif typ == 'slownik':
            print({'imie': self.imie, 'nazwisko': self.nazwisko, 'plec': self.plec, 'data_urodzenia': self.data_urodzenia})

    @staticmethod
    def wyswietl_osoby(osoby):
        result = []
        for o in osoby:
            result.append({'imie': o.imie, 'nazwisko': o.nazwisko, 'plec': o.plec, 'data_urodzenia': o.data_urodzenia})
        return result
    
class Gracz(Osoba):
    def __init__(self, imie, nazwisko, plec, data_urodzenia, nick, typ, email):
        super().__init__(imie, nazwisko, plec, data_urodzenia)
        self.nick = nick
        self.typ = typ
        self.email = email

    def wyswietl_info(self, typ):
        if typ == 'lista':
            print([self.imie, self.nazwisko, self.plec, self.data_urodzenia, self.nick, self.typ, self.email])
        elif typ == 'krotka':
            print((self.imie, self.nazwisko, self.plec, self.data_urodzenia, self.nick, self.typ, self.email))
        elif typ == 'slownik':
            print({'imie': self.imie, 'nazwisko': self.nazwisko, 'plec': self.plec, 'data_urodzenia': self.data_urodzenia, "nick" :self.nick, "typ": self.typ, "email": self.email})

    @staticmethod
    def wyswietl_graczy(gracze):
        for id_gracz, g in enumerate(gracze):
            print({f"gracz{id_gracz}": {'imie': g.imie, 'nazwisko': g.nazwisko, 'plec': g.plec, 'data_urodzenia': g.data_urodzenia, 
                           'nick': g.nick, 'typ': g.typ, 'email': g.email}})
    

def main():
    gracz = Gracz("Mikołaj", "Wieczorek", "M", "14.03.2002", "mw", "Human", "mwieczorek@email.com")
    gracz.wyswietl_info("slownik")
    gracz.wyswietl_info("lista")
    gracz.wyswietl_info("krotka")

    Gracz.wyswietl_graczy([gracz, Gracz("Baltazar", "Kowalski", "M", "12.12.1212", "bk", "NPC", "BaltKowal@Email.com")])

if (__name__ == "__main__"):
    main()