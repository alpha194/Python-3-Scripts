class Person(object):
    """Defines a Person class, suitable for use in a gym context.
    Data attributes: name of type str, age of type int, weight (kg) and
    height (meters) of type float.
    Methods: bmi()
    """
    def __init__(self, name, age, weight, height):
        """ Creates a new Person object with the specified name, age, 
        weight and height"""
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def bmi(self):
        """ Returns body mass index of a person"""
        return self.weight / (self.height * self.height)
    
    def status(self):
        """ Returns a status if the bmi is Underweight, Overweight etc"""
        bmi_value = int(self.bmi())
        if 18.5 > bmi_value: 
            return "Underweight"
        if  18.5 <= bmi_value and 25 > bmi_value:
            return "Normal"
        if 25 <= bmi_value and 30 > bmi_value:
            return "Overweight"
        if 30 <= bmi_value:
            return "Obese"
        

