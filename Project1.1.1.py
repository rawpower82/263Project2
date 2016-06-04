
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

class vehicle:  # Definition of vehicle class, which is used to store different vehicles which are input
    
    def __init__(self, year, make, model, vehicle_type, price, fuel_type, mpg):
        self.year = year
        self.make = make
        self.model = model
        self.vehicle_type = vehicle_type
        self.price = price
        self.fuel = fuel_type
        self.mpg = mpg
        
    def getYear(self):
        return self.year
    
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getVehicle_type(self):
        return self.vehicle_type
    
    def getPrice(self):
        return self.price
    
    def getFuel(self):
        return self.fuel
    
    def getMPG(self):
        return self.mpg
        


# In[5]:

# Output Begins Here
print("Welcome to (INSERT PROGRAM NAME HERE)!")

# Option which is changed to navigate in menu
menu_option = 1

# List which will store vehicles input into the program
inventory = list()

# Tests, feel free to ignore
# del inventory[1]

# Main Menu
while menu_option != 0:
    print ("\n\nMAIN MENU:\n\t1. View Vehicle Inventory\n\t2. Add a Vehicle to the Inventory")
    print ("\t3. Remove a Vehicle from the Inventory\n\t4. Compare Costs\n\t0. Exit Program\n ")
    menu_option = input("Please select an option: ")
    # Confirm that input is entered as a number
    try:
        menu_option = int(menu_option)
    except:
        menu_option = 999
    
    # View Vehicle Inventory
    if menu_option == 1:
        print ("\n\nView Vehicle Inventory:\n")
        if len(inventory) == 0:
            print ("\tThe inventory is empty.")
        else:
            for i in range(0,len(inventory)):
                print ("\t" + str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel()))
                print ("\t\tType: " + str(inventory[i].getVehicle_type()) + "\n\t\tPrice: $" +  str("{0:.2f}".format(inventory[i].getPrice()))                       + "\n\t\tFuel Type: " + str(inventory[i].getFuel()) + "\n\t\tFuel Economy: " + str("{0:.2f}".format(inventory[i].getMPG()))                       + " miles/gallon")
            
    # Add a Vehicle to the Inventory
    elif menu_option == 2:
        print ("\n\nAdd a Vehicle to the Inventory:\n")
        
        # Input Information About the Car
        year = input("\tWhat is the year of the car?: ")
        
        make = input("\tWhat is the make (Subaru, Ford, Honda, etc.) of the car?:")
        
        model = input("\tWhat is the model (Legacy, Mustang, Accord, etc.) of the car?: ")
        
        print("\tWhat type of vehicle is this? Enter the corresponding number:              \n\t\t1. Car\n\t\t2. Truck\n\t\t3. Hybrid\n\t\t4. Electric\n")
        vehicle_type = input("\t\t(Wagons, sedans and hatchbacks are defined as cars. \n\t\tTrucks, SUV's and mini-vans qualify as trucks): ")
        car = '1'
        truck = '2'
        hybrid = '3'
        electric = '4'
        valid = False
        while valid == False:     # Confirm that a correct choice was made
            if vehicle_type == car:
                valid = True
                vehicle_type = "Car"
            elif vehicle_type == truck:
                valid = True
                vehicle_type = "Truck"
            elif vehicle_type == hybrid:
                valid = True
                vehicle_type = "Hybrid"
            elif vehicle_type == electric:
                valid = True
                vehicle_type = "Electric"
            else:
                vehicle_type = input("\t\tInvalid Input. Please enter the corresponding number: ")
        
        price = input("\n\tWhat is the purchase price of the vehicle?: ")
        valid = False
        while valid == False:   # Confirm that input is entered as a number
            try:
                price = float(price)
                valid = True
            except:
                print ("\tError. Please enter the price using numbers.")
                price = input("\tWhat is the purchase price of the vehicle?: ")
                
        print("\tWhat type of fuel does the vehicle use? Enter the corresponding number:              \n\t\t1. Gas\n\t\t2. Diesel\n\t\t3. Electricity\n\t\t4. Hybrid (Gas and Electricity)")
        fuel_type = input("\t\t")
        gas = '1'
        diesel = '2'
        electricity = '3'
        hybrid = '4'
        valid = False
        while valid == False:     # Confirm that a correct choice was made
            if fuel_type == gas:
                valid = True
                fuel_type = "Gas"
            elif fuel_type == diesel:
                valid = True
                fuel_type = "Diesel"
            elif fuel_type == electricity:
                valid = True
                fuel_type = "Electricity"
            elif fuel_type == hybrid:
                valid = True
                fuel_type = "Gas & Electricity"
            else:
                fuel_type = input("\t\tInvalid Input. Please enter the corresponding number: ")
        
        
        mpg = input("\tWhat is the fuel economy of the car in miles per gallon?: ")
        valid = False
        while valid == False:   # Confirm that input is entered as a number
            try:
                mpg = float(mpg)
                valid = True
            except:
                print ("\tError. Please enter the price using numbers.")
                mpg = input("\tWhat is the fuel economy of the car in miles per gallon?: ")
        
        
        # Create a New Vehicle and add it to the Inventory
        new_vehicle = vehicle(year, make, model, vehicle_type, price, fuel_type, mpg)
        inventory.append(new_vehicle)
    
    
    # Remove a Vehicle from the Inventory
    elif menu_option == 3:
        print ("\n\nRemove a Vehicle from the Inventory:\n")
        if len(inventory) == 0:
            print ("\tThe inventory is empty.")
        else:
            for i in range(0,len(inventory)):
                print ("\t" + str(i+1) + ". " + str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel()))
                print ("\t\tPrice: $" +  str("{0:.2f}".format(inventory[i].getPrice())))
            remove_option = input("\n\tWhich vehicle would you like to remove from the inventory? Please enter the corresponding number: ")
            valid = False
            while valid == False:    # Confirm that a correct choice is entered
                try:
                    inventory[int(remove_option) - 1].getMake()
                    if int(remove_option) > 0:
                        valid = True
                except:
                    remove_option = input("\t\tInvalid Input. Please enter the corresponding number: ")

            # Delete the Unwanted Vehicle
            inventory_copy = list()
            for i in range (0,int(remove_option)-1):
                inventory_copy.append(inventory[i])
            for i in range (int(remove_option),len(inventory)):
                inventory_copy.append(inventory[i])
            inventory = inventory_copy
            del inventory_copy
        
    # Compare Costs, View Plots, Etc.
    elif menu_option == 4:
        print ("\n\nCompare Costs:\n")
        gas_price = input("\tWhat is the expected average cost of gas per gallon over the next five years?: $")
        valid = False
        while valid == False:   # Confirm that input is entered as a number
            try:
                gas_price = float(gas_price)
                valid = True
            except:
                print ("\tError. Please enter the price using numbers.")
                gas_price = input("\tWhat is the expected average cost of gas per gallon over the next five years?: $")
        miles_per_year = input("\tHow many miles are you expected to drive each year on average ?: ")
        valid = False
        while valid == False:   # Confirm that input is entered as a number
            try:
                miles_per_year = float(miles_per_year)
                valid = True
            except:
                print ("\tError. Please enter the price using numbers.")
                miles_per_year = input("\tHow many miles are you expected to drive each year on average ?: ")
    
    
    # Exit While Loop
    elif menu_option == 0:
        print ("\n\nGoodbye!")
    
    # For testing purposes. Instantly Add several cars to the inventory
    elif menu_option == 99:
        new_vehicle = vehicle("2016", "Subaru", "Legacy", "Car", 30000, "Gas", 32)
        new_vehicle1 = vehicle("2016", "Chevy", "Camero", "Car", 80000, "Gas", 17)
        new_vehicle2 = vehicle("2016", "Subaru", "Outback", "Car", 35000, "Gas", 27)
        new_vehicle3 = vehicle("2016", "Toyota", "Carrola", "Car", 17000, "Gas", 30)
        new_vehicle4 = vehicle("2016", "Ford", "F-150", "Truck", 40000, "Diesel", 20)
        new_vehicle5 = vehicle("2016", "Honda", "Civic", "Car", 20000, "Gas", 34)
        new_vehicle6 = vehicle("2016", "Toyota", "Prius", "Hybrid", 60000, "Gas & Electricity", 32)
        new_vehicle7 = vehicle("2016", "Nissan", "Leaf", "Electric", 65000, "Electricity", 1000000000000)
        inventory.append(new_vehicle)
        inventory.append(new_vehicle1)
        inventory.append(new_vehicle2)
        inventory.append(new_vehicle3)
        inventory.append(new_vehicle4)
        inventory.append(new_vehicle5)
        inventory.append(new_vehicle6)
        inventory.append(new_vehicle7)
    
    # Invalid Entries
    else:
        print ("\n\nInvalid Entry.")
        

# End of Program


# In[ ]:


"""
if vehicle_type==truck:
  maintenance=
elif vehicle)type==car:
  maintenance=
total_cost_5year=cost*.6+(miles_per_year*5*gas_price/mpg)+maintenance
"""


"""
***********************************************LEGEND***********************************************
The important things for you guys to know are: 

menu_option:
    Allows the user to navigate through the menu
miles_per_year:
    number of miles that the driver plans to drive on average per year
gas_price:
    estimate for average gas price over the next five years (we may change this to be calculated for a range later on)
class functions:
    def getYear(self):
        return self.year
    
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getVehicle_type(self):
        return self.vehicle_type
    
    def getPrice(self):
        return self.price
    
    def getFuel(self):
        return self.fuel
    
    def getMPG(self):
        return self.mpg

    year:
        Year of the car
    make:
        Brand of the car (Toyota, Chevy, Ford, Honda, etc.)
    model:
        Specific car type (Sequoia, Silverado, Mustang, Accord, etc.)
    vehicle_type:
        type of car (car, hybrid, electric, truck, etc.)
    price: 
        purchase price of the car
    fuel:
        fuel type used by the car
    mpg:
        miles per gallon

"""


# In[ ]:




# In[ ]:



