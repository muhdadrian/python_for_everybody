class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

print("Type", type(an))
print("Dir ", dir(an))

# We can use dir() to find the "capabilities" of our newly created class.