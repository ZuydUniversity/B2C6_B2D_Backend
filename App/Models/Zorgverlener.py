

class Zorgverlener:
    
    def CreateZorgverlener(self, _id: int, _name: str, _lastname: str, _email: str, _password: str):
        self.id = _id
        self.name = _name
        self.lastname = _lastname
        self.email = _email
        self.password = _password

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password   