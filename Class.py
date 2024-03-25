# [count, __init__, greet, get_fullname, add_one]
class User:

    count = 0

    def __init__(self, name, lname):
        self.name = name.lower()
        self.lname = lname
        self._ban = False
        self.add_one()

    def greet(self):
        print(f'Hello, {self.name} {self.lname}')

    @classmethod
    def add_one(cls):
        cls.count += 1

    def get_fullname(self):
        return f'{self.name}, {self.lname}'

    def __str__(self):
        return self.get_fullname()

    @staticmethod
    def function(age):
        return age > 18

user1 = User('John', 'Smith')
user2 = User('Ivan', "Larin")
print(user1.name,user1.lname,'\n',user2.name,user2.lname)
user1.greet()
print(user2.get_fullname())
print(user1)
print(User.count)
print(user1.function(34))

# Наследование
class PremiumUser(User): # Наследует все атрибуты и методы родительскоwedwfго класса

    def __init__(self, name, lname, desk):
        super().__init__(name, lname)
        self.desk = desk

    def greet(self):
        print(f'***Hello, {self.name} {self.lname}***') # Переписали из родительского класса


pr_user = PremiumUser('Mike', 'Novel', 'jjjjj')
pr_user.greet()
print(pr_user.desk)

print('Hello, world')

# Comment