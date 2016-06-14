
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
# For iPython Notebook Only:
get_ipython().magic('matplotlib inline')

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
    
    def getTotal_costs(self):
        return self.Total_costs
        


# In[8]:

# Output Begins Here
print("Welcome to (INSERT PROGRAM NAME HERE)!")

# Option which is changed to navigate in menu
menu_option = 1

# List which will store vehicles input into the program
inventory = list()

# Bool to determine what information needs to be gathered
gather_info = True

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
                if inventory[i].getFuel() == "Electricity":
                    print ("\t" + str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel()))
                    print ("\t\tType: " + str(inventory[i].getVehicle_type()) + "\n\t\tPrice: $" +  str("{0:.2f}".format(inventory[i].getPrice()))                           + "\n\t\tFuel Type: " + str(inventory[i].getFuel()) + "\n\t\tFuel Economy: " + str("{0:.2f}".format(inventory[i].getMPG()*100))                           + " kWh/100miles")
                else: 
                    print ("\t" + str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel()))
                    print ("\t\tType: " + str(inventory[i].getVehicle_type()) + "\n\t\tPrice: $" +  str("{0:.2f}".format(inventory[i].getPrice()))                           + "\n\t\tFuel Type: " + str(inventory[i].getFuel()) + "\n\t\tFuel Economy: " + str("{0:.2f}".format(inventory[i].getMPG()))                           + " miles/gallon")
            
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
        
        if fuel_type == "Gas" or fuel_type == "Diesel" or fuel_type == "Gas & Electricity":
            mpg = input("\tWhat is the fuel economy of the car in miles per gallon?: ")
            valid = False
            while valid == False:   # Confirm that input is entered as a number
                try:
                    mpg = float(mpg)
                    valid = True
                except:
                    print ("\tError. Please enter the fuel economy using numbers.")
                    mpg = input("\tWhat is the fuel economy of the car in miles per gallon?: ")
        elif fuel_type == "Electricity":
            mpg = input("\tWhat is the fuel economy of the car in kiloWatts per 100 miles?: ")
            valid = False
            while valid == False:   # Confirm that input is entered as a number
                try:
                    mpg = float(mpg)
                    valid = True
                except:
                    print ("\tError. Please enter the fuel economy using numbers.")
                    mpg = input("\tWhat is the fuel economy of the car in kiloWatts per 100 miles?: ")
            mpg = mpg / 100 # convert to kWh / mile
        
        
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
        
        # Gather More Info
        if gather_info == False:
            gather_again = input("\tWould you like to input new gas prices, miles per year, and current year? Enter 'yes' or 'no': ")
            valid = False
            while valid == False:
                valid = True
                if gather_again == 'yes' or gather_again == 'Yes' or gather_again == 'y':
                    gather_info = True
                elif gather_again != 'no' and gather_again and 'No' and gather_again != 'n':
                    print ("\tINVALID INPUT.")
                    gather_again = input("\tWould you like to input new gas prices, miles per year, and current year? Enter 'yes' or 'no'.")
                    valid = False
                    
        if gather_info == True: # This is true by default when the program compiles, but prevents unneccesary reprompt for info later
            current_year = input("\tWhat is the year of purchasing each car? (This should not occur before the year of the newest car in the inventory): ")
            valid = False
            while valid == False:   # Confirm that input is entered as a number
                try:
                    current_year = int(current_year)
                    valid = True
                except:
                    print ("\tError. Please enter the current year using numbers.")
                    current_year = input("\tWhat is the year of purchasing each car? (This should not occur before the year of the newest car in the inventory): ")
                for i in range(0,len(inventory)):
                    largest_year = 0
                    if int(inventory[i].getYear()) >= largest_year:
                        largest_year = int(inventory[i].getYear())
                if largest_year > current_year:
                    print ("\tError. Must enter at least " + str(largest_year) + " as the year of purchase.")
                    valid = False
                    current_year = input("\tWhat is the year of purchasing each car? (This should not occur before the year of the newest car in the inventory): ")
            gas_price = input("\tWhat is the expected average cost of gas per gallon over the next several years?: $")
            valid = False
            while valid == False:   # Confirm that input is entered as a number
                try:
                    gas_price = float(gas_price)
                    valid = True
                except:
                    print ("\tError. Please enter the price using numbers.")
                    gas_price = input("\tWhat is the expected average cost of gas per gallon over the next several years?: $")
            diesel_price = input("\tWhat is the expected average cost of diesel per gallon over the next several years?: $")
            valid = False
            while valid == False:   # Confirm that input is entered as a number
                try:
                    diesel_price = float(diesel_price)
                    valid = True
                except:
                    print ("\tError. Please enter the price using numbers.")
                    diesel_price = input("\tWhat is the expected average cost of diesel per gallon over the next several years?: $")
            miles_per_year = input("\tHow many miles are you expected to drive each year on average?: ")
            valid = False
            while valid == False:   # Confirm that input is entered as a number
                try:
                    miles_per_year = float(miles_per_year)
                    valid = True
                except:
                    print ("\tError. Please enter the price using numbers.")
                    miles_per_year = input("\tHow many miles are you expected to drive each year on average?: ")
            gather_info = False
                    
        # Prompt the user as to which time period they would like to compare costs over 
        time_span = input("\tWould you like to compare costs over 5, 10, 15, or 20 years? Enter the number: ")
        valid = False
        while valid == False:   # Confirm that input is entered as a number
            try:
                time_span = int(time_span)
                valid = True
            except:
                print ("\tError. Please enter the time span using integers.")
                time_span = input("\tWould you like to compare costs over 5, 10, 15, or 20 years? Enter the number: ")
        
        
        # Create Time (Years) Array 
        valid = False
        while valid == False: # Confirm that valid input is entered
            # 20 Year Time Span
            if time_span == 20:
                valid = True
                T = np.zeros(21)
                for i in range (0,21):
                    T[i] = i

            # 15 Year Time Span    
            elif time_span == 15:
                valid = True
                T = np.zeros(16)
                for i in range (0,16):
                    T[i] = i

            # 10 Year Time Span
            elif time_span == 10:
                valid = True
                T = np.zeros(11)
                for i in range (0,11):
                    T[i] = i

            # 5 Year Time Span
            elif time_span == 5:
                valid = True
                T = np.zeros(6)
                for i in range (0,6):
                    T[i] = i
                    
            else:
                print ("\tError. Please enter one of the available options.")
                time_span = input("\tWould you like to compare costs over 5, 10, 15, or 20 years? Enter the number: ")
                
    
        
        # Make Calculation For Each Car:
        electricity_price = 0.12 # dollars per kWh, average U.S. price
        for i in range(0,len(inventory)):
            # Calculate and Display the Cost of Gas
            if inventory[i].getFuel() == "Gas":
                fuel_cost_per_year=(miles_per_year/inventory[i].getMPG())*gas_price
                print ("\n\t" + str(i+1) + ". " + str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel()) + ":")
                print ("\t\tYou will spend about $" + str("{0:.2f}".format(fuel_cost_per_year)) + " per year on gas." )
            elif inventory[i].getFuel() == "Diesel":
                fuel_cost_per_year=(miles_per_year/inventory[i].getMPG())*diesel_price
                print ("\n\t" + str(i+1) + ". " + str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel()) + ":")
                print ("\t\tYou will spend about $" + str("{0:.2f}".format(fuel_cost_per_year)) + " per year on diesel." )
            elif inventory[i].getFuel() == "Gas & Electricity":
                fuel_cost_per_year=(miles_per_year/inventory[i].getMPG())*gas_price
                print ("\n\t" + str(i+1) + ". " + str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel()) + ":")
                print ("\t\tYou will spend about $" + str("{0:.2f}".format(fuel_cost_per_year)) + " per year on gas." )
            elif inventory[i].getFuel() == "Electricity":
                fuel_cost_per_year=miles_per_year*inventory[i].getMPG()*electricity_price # miles per year * kWh per mile * $ per kWh = $ / year
                print ("\n\t" + str(i+1) + ". " + str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel()) + ":")
                print ("\t\tYou will spend about $" + str("{0:.2f}".format(fuel_cost_per_year)) + " per year on electricity." )
              
            
                
                
            
            # Calculate and Display Deprecitation
            priceDepreciationValues=[.91,.81,.69,.58,.49,.40,.34,.27,.22,.18,.10]
                #New 100%
                #Right off the lot sellback price 91%
                #1 year 81%
                #2 years 69%
                #3 years 58%
                #4 years 49%
                #5 years 40%
                #On average lose 60% of inital car value in five years
                #6 years 34%
                #7 years 27%
                #8 years 22%
                #9 years 18%
                #By year 10 depreciation is negligable, average sellback price is 10%
            
            # Create a list based off of the depreciation value each year in T
            Depreciation_Values = np.zeros(len(T))                             
            for j in range(0,len(T)):
                sellback = inventory[i].getPrice() * priceDepreciationValues[min(current_year + j - int(inventory[i].getYear()),(len(priceDepreciationValues))-1)]
                dep_val = inventory[i].getPrice() - sellback
                Depreciation_Values[j] = dep_val
            print ("\t\tThis vehicle will depreciate by about:"  )
            print ("\t\t\t$" + str("{0:.2f}".format(Depreciation_Values[5])) + " in 5 years")
            if time_span != 5:
                print ("\t\t\t$" + str("{0:.2f}".format(Depreciation_Values[10])) + " in 10 years" )
            
            # Calculate Maintenance Per Mile
            maint_per_mile = 440/15000 # maintenance per year / miles per year = maintenance per mile
            
            # Create a list based off of the total cost each year in T (used j because this is within a for loop with i as the variable)
            Total_Costs = np.zeros(len(T)) 
            for j in range(0,len(T)):
                total_cost = (fuel_cost_per_year * j) + Depreciation_Values[j] + (maint_per_mile * miles_per_year * j)
                Total_Costs[j] = total_cost
                
            # Save the list to the vehicle object (use getTotal_costs() to obtain it later)
            inventory[i].Total_costs = Total_Costs
            
        # Plot the Results
        for i in range(0,len(inventory)):
            plt.plot(T,inventory[i].getTotal_costs(), label = (str(inventory[i].getYear()) + " " + str(inventory[i].getMake()) + " " + str(inventory[i].getModel())))
            plt.legend(loc='upper left', bbox_to_anchor=(1,1))
            plt.xlabel("Years")
            plt.ylabel("Total Cost $")
            plt.title("Total Cost of Owning a Car Over " + str(time_span) + " Years")
        plt.show()
            
    # Exit While Loop
    elif menu_option == 0:
        print ("\n\nGoodbye!")
    
    # For testing purposes. Instantly Add several cars to the inventory
    elif menu_option == 99:
        new_vehicle = vehicle("2016", "Subaru", "Legacy", "Car", 30000, "Gas", 32)
        new_vehicle1 = vehicle("2016", "Chevy", "Camero", "Car", 80000, "Gas", 17)
        new_vehicle2 = vehicle("2016", "Subaru", "Outback", "Car", 35000, "Gas", 27)
        new_vehicle3 = vehicle("2016", "Toyota", "Carrola", "Car", 17000, "Gas", 30)
        new_vehicle4 = vehicle("2016", "Ford", "F-150", "Truck", 40000, "Diesel", 17)
        new_vehicle5 = vehicle("2016", "Honda", "Civic", "Car", 20000, "Gas", 34)
        new_vehicle6 = vehicle("2016", "Toyota", "Prius", "Hybrid", 60000, "Gas & Electricity", 45)
        new_vehicle7 = vehicle("2016", "Nissan", "Leaf", "Electric", 65000, "Electricity", 30/100)
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


# In[3]:

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
        
    def getTotal_costs(self):
        return self.Total_Costs

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
    Total_Costs:
        list of total cost to own car per year (corresponds to time list T)

"""


# In[4]:

import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
menStd = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (25, 32, 34, 20, 25)
womenStd = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

# add some text for labels, title and axes ticks
ax.set_ylabel('Cost $')
ax.set_title('Total Cost After __ Years')
ax.set_xticks(ind + width)
ax.set_xticklabels(( '1', '2', '3', '4', '5'))

ax.legend((rects1[0], rects2[0]), ('Total Cost', 'Fuel Cost'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()


# In[ ]:




# In[ ]:




# In[ ]:



