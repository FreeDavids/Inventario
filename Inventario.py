bag = {
    "Pan": 200,
    "Agua": 100,
    "Salchichon": 100,
    "Queso": 100,
    "Sobrasada": 150,
}

def travel_in_time(hours):
    for x in bag:
        print(bag[x] - (50*hours))       
        

travel_in_time(1)
