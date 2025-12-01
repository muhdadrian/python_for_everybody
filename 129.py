class PartyAnimal:
    x = 0 # Each PartyAnimal object has a bit of data

    def party(self): #This is a method as it is inside a class
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal() # construct a PartyAnimal object and store in an

#Tell the an object to run the party() code within it.
an.party() #PartyAnimal.party(an)
an.party()
an.party()