planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

del planet_list[-1]

rocky_planets = planet_list[0:4]

spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

for planet in planet_list:
    if planet == "Saturn":
        for tuple in spacecraft:
            if "Saturn" in tuple:
                print(f'{tuple[1]}: {tuple[0]}')
    elif planet == "Mars":
        for tuple in spacecraft:
            if "Mars" in tuple:
                print(f'{tuple[1]}: {tuple[0]}')
    else:
        print(planet)
    

