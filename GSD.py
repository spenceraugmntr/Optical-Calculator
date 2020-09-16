import matplotlib.pyplot as plt
import numpy as np
import math

#input variables for calculating gsd
Altitude = float(input("What is your altitude in meters?"))
effective_imaging_element_size = float(input("What is your effective imaging element size in micrometers?"))
focal_length = float(input("What is your focal length in (mm)?"))

#converting variable to meters
effective_imaging_element_size = effective_imaging_element_size*.000001
focal_length = focal_length*.001

#equations
IFOV = math.atan2(effective_imaging_element_size, focal_length)
GSD = Altitude*math.tan(IFOV)
print("Your GSD is", GSD)

#Hypotenuse 
plt.plot([0,GSD],[0,Altitude])
#Horizontal
plt.plot([0,GSD],[0,0])
#Vertical
plt.plot([GSD,GSD],[0,Altitude])

#Add title and axis names
plt.title('GSD VS Altitude')
plt.xlabel('GSD(m)')
plt.ylabel('Altitude(m)')

#Add Angle IFOV Label
plt.text(GSD, Altitude, "Theta=IFOV")

#Save Graph as .png
plt.savefig("GSD.png")

plt.show()

