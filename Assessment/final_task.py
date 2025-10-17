#Final assessment of the module
import tkinter as tk
from tkinter import *

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

earth_moons = ["Moon"]
mars_moons = ["Phobos", "Deimos"]
jupiter_moons = ["Io", "Europa", "Ganymede", "Callisto", "Themisto"]
saturn_moons = ["Titan", "Rhea", "Pandora", "Prometheus", "Enceladus"]
uranus_moons = ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"] 
neptune_moons = ["Triton", "Nereid", "Proteus", "Naiad", "Thalassa"]


#Used this page to help with Tkinter https://www.geeksforgeeks.org/python/python-tkinter-tutorial/ 
#Creating the main window
window = Tk()
window.title("Solar system planets")
window.geometry("500x500")
label = tk.Label(window, text = "Select a planet to see its details")
label.pack(pady=20)

button_venus = tk.Button(window, text = "Venus",
                         cursor = "hand2"
                     )
button_venus.pack(pady=10)

button_earth = tk.Button(window, text = "Earth",
                         cursor = "hand2")
button_earth.pack(pady=10)

button_mars = tk.Button(window, text = "Mars",
                         cursor = "hand2")
button_mars.pack(pady=10)

button_jupiter = tk.Button(window, text = "Jupiter",
                            cursor = "hand2")
button_jupiter.pack(pady=10)

button_saturn = tk.Button(window, text = "Saturn",
                          cursor = "hand2")
button_saturn.pack(pady=10)

button_uranus = tk.Button(window, text = "Uranus",
                          cursor = "hand2")
button_uranus.pack(pady=10)

button_neptune = tk.Button(window, text = "Neptune",
                           cursor = "hand2")
button_neptune.pack(pady=10)

window.mainloop()