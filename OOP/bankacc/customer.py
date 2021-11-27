class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def get_info(self):
        return f"{self.name}, {self.date_of_birth}, {self.email}, {self.phone}"  