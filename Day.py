class car:
   
   def __init__(self,brand,model,color,year):
      self.brand=brand
      self.model=model
      self.color=color
      self.year=year
   def display(self):
      print("car brand:",self.brand)
      print("car model:",self.model)
      print("car color:",self.color)
      print("car year:",self.year)  
car1="bmw"
color="red"
model="x5"
year=2020
print("car,brand,model,color,year")       
