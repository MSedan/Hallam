#Final assessment of the module
import tkinter as tk
from tkinter import *

#Data for the planets
#Mass is in kilograms
mass ={"Mercury": 3.3011*10**23,
       "Venus": 4.8675*10**24,
       "Earth": 5.972168*10**24,
       "Mars": 6.4171*10**23,
       "Jupiter": 1.8982*10**27,
       "Saturn": 5.6834*10**26,
       "Uranus": 8.6810*10**25,
       "Neptune": 1.02409*10**26
       }

#Distance from the sun is in kilometers
distance_from_sun = {"Mercury": 46000000,
                     "Venus": 108000000,
                     "Earth": 149600000,
                     "Mars": 230000000,
                     "Jupiter": 778000000,
                     "Saturn": 1434000000,
                     "Uranus": 2000000000,
                     "Neptune": 4500000000
                     }

#Moons
number_of_moons = {"Mercury": 0,
         "Venus": 0,
         "Earth": 1,
         "Mars": 2,
         "Jupiter": 97,
         "Saturn": 274,
         "Uranus": 29,
         "Neptune": 16
         }

#Names of moons
earth_moons = ["Moon"]
mars_moons = ["Phobos", "Deimos"]
jupiter_moons = ["Io", "Europa", "Ganymede", "Callisto", "Themisto"]
saturn_moons = ["Titan", "Rhea", "Pandora", "Prometheus", "Enceladus"]
uranus_moons = ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"] 
neptune_moons = ["Triton", "Nereid", "Proteus", "Naiad", "Thalassa"]

#List of valid planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]


def check_if_planet():
    planet = entry.get().lower().capitalize()
    if planet in planets:
        show_frame2()
    else:
       wrong_planet = tk.Label(frame1, text = planet + " is not a planet or you have made a typo", font="20", fg="red")
       wrong_planet.pack(pady=10)
       
       
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

#First window frame
frame1 = tk.Frame(window)
frame1.pack()
label_main_text = tk.Label(frame1, text = "Please type a planet you would like to learn about:", font="50")
label_main_text.pack(pady=20)
entry = tk.Entry(frame1, width = 40)
entry.pack(pady=10)
check_button = tk.Button(frame1, text = "Submit", command=check_if_planet)
check_button.pack(pady=10)

#Second window frame
frame2 = tk.Frame(window)
label2 = tk.Label(frame2, text = f"You have picked {entry.get()}", font="50")
label2.pack(pady=20)




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