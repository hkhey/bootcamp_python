
class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        self.first_name=first_name
        self.is_alive=is_alive
class Stark(GotCharacter):
    """A class representing the Stark family. Or when ad things happen to good people"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name="Stark"
        self.house_words="Winter is coming"
    def print_house_words(x):
        print(x.house_words)
    def die(x):
        x.is_alive=False        
    
arya=Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__doc__)
