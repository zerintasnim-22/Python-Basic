#parent class, super class, base class
class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

#child class, sub class, derived class
class Samsung(Phone):
    #call,message
    def photo(self):
        print("You can take photo")

s = Samsung()
s.call()
s.message()
s.photo()

#to check parentclass/superclass and childclass/subclass
print(issubclass(Samsung,Phone))