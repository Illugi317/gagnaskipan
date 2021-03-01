import unittest

class TestHolder(unittest.TestCase):
    def test_add_pizza(self):
        holder = PizzaHolder()
        self.assertEqual(0,holder.addPizza())

class Pizza:
    ID = 0
    def __init__(self):
        self.ID = Pizza.ID
        Pizza.ID += 1
        self.served = False
        self.toppings = []

    def add_topping(self, topp:list):
        for topping in topp:
            self.toppings.append(topping)

    def __str__(self):
        return f"Pizza ID: {self.ID}\nToppings: {self.toppings}"

class PizzaHolder:
    def __init__(self):
        self.pizza_list = [] #pizza list

    def add_pizza(self, toppings:list):
        p = Pizza()
        p.add_topping(toppings)  
        self.pizza_list.append(p)

    def serve_pizza(self, pizza_id):
        for pizza in self.pizza_list:
            if pizza.ID == pizza_id:
                pizza.served = True
    
    def remove_all_served_pizzas(self):
        for pizza in self.pizza_list:
            if pizza.served == True:
                self.pizza_list.remove(pizza)

    def __str__(self):
        return_str = ""
        for pizza in self.pizza_list:
            return_str += str(pizza) +"\n"
        return return_str

#pizza testing goes on here

#create pizza
pizza = Pizza()
pizza.add_topping(["Cheese","Heroin"])
assert ["Cheese","Heroin"] == pizza.toppings #check toppings

#check ID
assert pizza.ID == 0

#check served_status
assert pizza.served == False

#check string
assert str(pizza) == "Pizza ID: 0\nToppings: ['Cheese', 'Heroin']"

#pizza holder tests

holder = PizzaHolder()

holder.add_pizza(["Cheese","Paprika","Socks"])
assert str(holder.pizza_list[0]) == "Pizza ID: 1\nToppings: ['Cheese', 'Paprika', 'Socks']"

#add more pizzas
holder.add_pizza(["Cheese","Rabbabari","Pants"])
holder.add_pizza(["Cheese","Math","Meth"])
holder.add_pizza(["Cheese","Computer","PCB"])

#serve pizza ID 3
assert holder.serve_pizza(3) is None 
assert holder.pizza_list[2].served is True

#print all pizzas
print(holder)

#removed
assert holder.remove_all_served_pizzas() is None
for pizza in holder.pizza_list:
    if pizza.served is True:
        raise AssertionError

print(holder)

class Street:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Street Name: {self.name}"

class Neighborhoods:
    def __init__(self, name):
        self.name = name
        self.streets = []


class City:
    def __init__(self):
        self.neighborhoods = []
    
    def new_street(self, name, neighborhood):
        s = Street(name)
        neighborhood.streets.append(s)
        return s
    
    def get_streets(self, neighborhood_name):
        n = None
        for neighborhood in self.neighborhoods:
            if neighborhood_name == neighborhood.name:
                n = neighborhood
                break
        if n:
            string = ""
            for street in n.streets:
                string += str(street) + "\n"
            return string

    def get_neighborhood(self, street_name):
        for neighborhood in self.neighborhood:
            for street in neighborhood.streets:
                if street.name == street_name:
                    return neighborhood.name

#city testing goes on here

class CityTesting(unittest.TestCase):
    def test_neighborhood(self):
        n = Neighborhoods

#log shit here

#log testing goes on here