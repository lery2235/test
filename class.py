
class Person:
    def greeting(self):
        print('Hello')
    def hello(self):
        self.greeting()

james = Person()

print(james.greeting())
print(james.hello())
