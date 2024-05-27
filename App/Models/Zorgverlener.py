class Zorgverlener:
    
    def Zorgverlenergegevens(self, _id: int, _naam: str, _achternaam: str, _email: str, _wachtwoord: str):
        self.id = _id
        self.naam = _naam
        self.achternaam = _achternaam
        self.email = _email
        self.wachtwoord = _wachtwoord

    def get_id(self):
        return self.id

    def get_naam(self):
        return self.naam

    def get_achternaam(self):
        return self.achternaam

    def get_email(self):
        return self.email

    def get_wachtwoord(self):
        return self.wachtwoord    