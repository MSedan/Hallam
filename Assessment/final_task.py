#Final assessment of the module Fundamentals of Computing
import tkinter as tk
from tkinter import *

#Data for the planets
#Mass is in kilograms

class Planet:
       def __init__(self, name, mass, distance_from_sun, number_of_moons, names_of_moons):
              self.name = name
              self.mass = mass
              self.distance_from_sun = distance_from_sun
              self.number_of_moons = number_of_moons
              self.names_of_moons = names_of_moons
              
       def get_name(self):
              return self.name
       def get_mass(self):
              return self.mass
       def get_distance_from_sun(self):
              return self.distance_from_sun
       def get_number_of_moons(self):
              return self.number_of_moons
       def get_names_of_moons(self):      
              return self.names_of_moons

mercury = Planet("Mercury", 3.3011*10**23, 46000000, 0, [])
venus = Planet("Venus", 4.8675*10**24, 108000000, 0, [])
earth = Planet("Earth", 5.972168*10**24, 149600000, 1, ["Moon"])
mars = Planet("Mars", 6.4171*10**23, 230000000, 2, ["Phobos", "Deimos"])
jupiter = Planet("Jupiter", 1.8982*10**27, 778000000, 97, ["Io", "Europa", "Ganymede", "Callisto", "Themisto"])
saturn = Planet("Saturn", 5.6834*10**26, 1434000000, 274, ["Titan", "Rhea", "Pandora", "Prometheus", "Enceladus"])
uranus = Planet("Uranus", 8.6810*10**25, 2000000000, 29, ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"])
neptune = Planet("Neptune", 1.02409*10**26, 4500000000, 16, ["Triton", "Nereid", "Proteus", "Naiad", "Thalassa"])

planets = [mercury.get_name(), venus.get_name(), earth.get_name(), mars.get_name(), jupiter.get_name(),saturn.get_name(), uranus.get_name(), neptune.get_name()]


#Function for user input
def get_entry(entry):
       planet = entry.get().lower().capitalize()
       return planet

#Function to check the input
def check_if_planet(planet):
       if planet in planets:
              show_frame2()
       elif planet == "":
              empty_label = tk.Label(frame1, text="Please enter a planet name.")
              empty_label.pack()
       else:
              wrong_planet = tk.Label(frame1, text= planet + " is not a planet or you have made a typo. Please try again.")
              wrong_planet.pack()

#Functions to switch between frames
def show_frame2():
       frame1.pack_forget()
       frame2.pack()

def return_to_frame1():
       frame2.pack_forget()
       frame1.pack()


#Used this page to help with Tkinter https://www.geeksforgeeks.org/python/python-tkinter-tutorial/
#Creating the main window
window = Tk()
window.title("Solar system planets")
window.geometry("500x500")

#First frame
frame1 = tk.Frame(window)
frame1.pack()
label_main_text = tk.Label(frame1, text = "Please type a planet you would like to learn about:", font="50")
label_main_text.pack(pady=20)
entry = tk.Entry(frame1, width = 40)
entry.pack(pady=10)
check_button = tk.Button(frame1, text = "Submit", command=lambda: check_if_planet(get_entry(entry)),
                         cursor = "hand2")
check_button.pack(pady=10)

#Second frame
frame2 = tk.Frame(window)
button_all_information = tk.Button(frame2, text = "Tell me everything you know",
                         cursor = "hand2"
                     )
button_all_information.pack(pady=10)

button_mass = tk.Button(frame2, text = "Mass",
                         cursor = "hand2")
button_mass.pack(pady=10)

button_distance = tk.Button(frame2, text = "Distance from the sun",
                         cursor = "hand2")
button_distance.pack(pady=10)

button_number_moons = tk.Button(frame2, text = "Number of moons",
                            cursor = "hand2")
button_number_moons.pack(pady=10)

button_names_moons = tk.Button(frame2, text = "Name of moons",
                          cursor = "hand2")
button_names_moons.pack(pady=10)

button_new_planet = tk.Button(frame2, text = "Choose a new planet",
                          cursor = "hand2", command= return_to_frame1)
button_new_planet.pack(pady=10)

button_exit = tk.Button(frame2, text = "Exit",
                          cursor = "hand2", command=window.quit)
button_exit.pack(pady=10)

window.mainloop()