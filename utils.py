from Boat import Boat

def ReadBoatsFromFile(fileName : str) -> list:
    boatList = []

    with open(fileName, 'r') as file:
        for line in file:
        
            newBoat = Boat()
            newBoat.Name, newBoat.Port, newBoat.Tonnage = line.split(' ')
            
            boatList.append(newBoat)
            
    return boatList


def SearchBoat(boatList : list, value : str,  criterion : str) -> list:
    criterion = Boat.SEARCH_CRITERIA.get(criterion, 'Name')
    matchedBoats = []
    for boat in boatList:
        if value.lower() in str(getattr(boat, criterion)).lower():
            matchedBoats.append(boat)
    return matchedBoats