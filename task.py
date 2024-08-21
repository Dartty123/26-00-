class MeClass:
     def __init__(self):
         self.public_attribute = "Публічнa атрибутика"
         self._protected_attribute = "Протестдна атибутика"
         self.__private_attribute = "Приватна атрибутика"

     def public_method(self):
            print("Ви використували публічний метод")

     def _protected_method(self):
            print("Ви використували протестдний метод")

     def __private_method(self):
           print("Ви використували приватний метод")


obj = MeClass()

print(obj.public_attribute)
obj.public_method()

print(obj._protected_attribute)
obj._protected_method()

print(obj.__private_attribute)
obj.__private_method()  