class parrot:


    #class attribute
    speces = "bird
    
    
    # instance attribute
    def _init_(self, name age):
        self.name= name
        self.age = age


        #instantiate the parrot class
        blu= Parrot("Blu", 10)
        woo = Parrot("Woo", 15)


        # acces theclass atributes
        print("Blu is a {}". format(blu.species))
        print("Woo is also a {}".format(woo.species))


        #acces the instance attributes
        print("{} is {} years old". format( blu.name, blu.age))
        print("{} is {} years old". format( woo.name, woo.age))