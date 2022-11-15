# инкапсуляция
# private
import uuid


# class Product:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def get_info(self):
#         print(f"{self.name} - {self.price}")
#
# potato = Product("potato", 25)
# potato.get_info()

# ####
# import uuid
# class Bank:
#     def __init__(self, name: str):
#         self.name = name
#         self.__generate_account()
#
#     def __generate_account(self):
#         self.__account = str(uuid.uuid4())
#     @property
#     def account(self):
#         print(f"ваш аккаунт {self.__account}")
#     @account.setter
#     def account(self, key_word: str):
#         self.__account = str(uuid.uuid4()) + key_word
#
#
# sman = Bank("sman")
# sman.account
# sman.account = "no_name"
# sman.account



username_list = ["sman", "smandarkness"]
email_tail_list = ["@gmail.com", "@outlook.com" "@mail.ru"]

username_list = ["Sman", ]
email_tail_list = ["@gmail.com", "@outlook.com", "@mail.ru"]


class Registrtion:

    def __init__(self, username: str, password: str, email: str):
        self.save(username, password, email)

    def __validate_username(self, username):
        if username not in username_list:
            return True
        raise Exception("пользователь уже существует!!!")

    def __validate_password(self, password):
        if len(password) < 8 or password.isalpha() or password.isdigit() or password[0].islower():
            raise Exception("Пароль должен содержать не менее 8 символов включая символы и числа")
        return True

    def __validate_email(self, email: str):
        for i in email_tail_list:
            if email.endswith(i):
                return True
            raise Exception(" error email")

    def save(self, username, password, email):
        if (self.__validate_email(email) and
                self.__validate_password(password) and
                self.__validate_username(username)):
            self.username = username
            username_list.append(username)
            self.password = password
            self.email = email


nazgul = Registrtion("Nazgul", "K,dfjvblf23", "t@gmail.com")
print(nazgul.username)
print(username_list)