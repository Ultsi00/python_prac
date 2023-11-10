#Practising inheritance: parent, child, composition

from machine import Machine
import cutter

mach_frame_0 = Machine('Hilderen', 'Germany', 'public')
slicer3000 = cutter.Cutter('Hilderen', 'Germany', 'public', 'electric', 15200)
slicer1000 = cutter.Cutter('Hilderen', 'Germany', 'public', 'coal', 11000)

#slicer3000 details
print(f"slicer3000 manufacturer: {slicer3000.get_manufacturer()}")
print(f"slicer3000 country of origin: {slicer3000.get_country_of_origin()}")
print(f"slicer3000 secrecy level: {slicer3000.get_secrecy_lvl()}")
print(f"slicer3000 energy type: {slicer3000.get_energy_type()}")
print(f"slicer3000 target: {slicer3000.get_target()}")
print(f"slicer3000 cost: {slicer3000.get_cost()}")

#slicer1000 details
print(f"\nslicer1000 manufacturer: {slicer1000.get_manufacturer()}")
print(f"slicer1000 country of origin: {slicer1000.get_country_of_origin()}")
print(f"slicer1000 secrecy level: {slicer1000.get_secrecy_lvl()}")
print(f"slicer1000 energy type: {slicer1000.get_energy_type()}")
print(f"slicer1000 target: {slicer1000.get_target()}")
print(f"slicer1000 cost: {slicer1000.get_cost()}")

#Output:
# >>> slicer3000 manufacturer: Hilderen
# >>> slicer3000 country of origin: Germany
# >>> slicer3000 secrecy level: private
# >>> slicer3000 energy type: electric
# >>> slicer3000 target: sewer network
# >>> slicer3000 cost: 18400
# >>> 
# >>> slicer1000 manufacturer: Hilderen
# >>> slicer1000 country of origin: Germany
# >>> slicer1000 secrecy level: public
# >>> slicer1000 energy type: coal
# >>> slicer1000 target: shoreline projects
# >>> slicer1000 cost: 11500
