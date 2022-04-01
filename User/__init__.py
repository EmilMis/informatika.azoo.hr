import requests
from User.Color import format_c
from User.Error import error_message


class User:
    def __init__(self, number):

        self.error_message = error_message
        self.important_message_color = "BLUE"

        self.url = f"https://informatika.azoo.hr/korisnik/{number}"
        self.content = requests.get(self.url).text
        self.name = self.get_name()
        self.reg_date = self.get_reg_date()
        self.description = self.get_description()

    def get_name(self):
        try:
            ind = self.content.index('<div class="name">') + 20
            ind_end = self.content.index('</div>', ind) - 1
            return self.content[ind:ind_end]
        except:
            return self.error_message

    def get_reg_date(self):
        try:
            ind = self.content.index('<div class="label">Registriran:</div>') + 87
            ind_end = self.content.index('</span>', ind)
            return self.content[ind:ind_end]
        except:
            return self.error_message

    def get_description(self):
        try:
            ind = self.content.index('<p class="description">') + 24
            ind_end = self.content.index('</p>', ind) - 1
            return self.content[ind:ind_end]
        except:
            return self.error_message

    def info(self):
        print(f"Name: {format_c(self.name, self.important_message_color)}")
        print(f"Date Registered: {format_c(self.reg_date, self.important_message_color)}")
        print(f"Description: {format_c(self.description, self.important_message_color)}")
        print(f"Link: {self.url}")
