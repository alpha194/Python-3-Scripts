class Car(object):
    
    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self):
        self.speed += 5
        return self.speed
    
    def brake(self):
        if self.speed >= 1:
            self.speed -= 5
        return self.speed
        
    def honk_horn(self):
        print(self.model + " goes 'beep beep'")
        
    def __str__(self):
        return (self.model + " (" + str(self.year) + ")" 
                + ", moving at " + str(self.speed) + " km/h")
        
    