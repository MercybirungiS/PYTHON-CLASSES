class Dog():
    def __init__(self,dog_Name,dog_breed,dog_weight):
        self.dog_Name=dog_Name
        self.dog_breed=dog_breed
        self.dog_weight=dog_weight
    def name(self):
        return f"My dog is called {self.dog_Name}.!"
    def breed(self):
        return f"My dog is a {self.dog_breed}"
     