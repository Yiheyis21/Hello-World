class Person:
    def __inint__(self, name):
        self.name = name
    def talk(self):
        print(f"hi,i am {self.name}")


John = Person('John Smith')
John.talk()
