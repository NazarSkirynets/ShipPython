from Boat import Boat
from utils import ReadBoatsFromFile, SearchBoat

if __name__ == '__main__':
    fileName = 'Boats.txt'
    boatList = []
    opt = 0
    while opt != -1:
        print('-----This is console interface for Boat program-----\n')
        print('--To exit enter -1--\n')
        print('--To read new Boat from console enter 1--\n')
        print('--To read Boats from file enter 2--\n')
        print('--To search Boats with particular criterion enter 3--\n')
        print('--To sort Boats with particular criterion enter 4--\n')
        print('--To print Boats enter 5--\n')
        opt = input('Your option:')
        try:
            if int(opt) == -1:
                break
            elif int(opt) == 1:
                newBoat = Boat()
                newBoat.ReadFromConsole()
                print(newBoat)
                boatList.append(newBoat)
                print('Boat is added to list\n')
            elif int(opt) == 2:
                tmpConsoleInput = input('Write file name(default=Boats.txt Press Enter for default)') 
                fileName = tmpConsoleInput if '.txt' in tmpConsoleInput else fileName
                print(ReadBoatsFromFile(fileName))
                boatList.extend(ReadBoatsFromFile(fileName))
                
                print('Boats added to list\n')
            elif int(opt) == 3:
                try:
                    print('--To search Boats with Name enter 1--\n')
                    print('--To search Boats with Port enter 2--\n')
                    print('--To search Boats with Tonnage enter 3--\n')
                    searchOpt = input('Your option:')
                    value = input('Value to search with:')
                    
                    if searchOpt in Boat.SEARCH_CRITERIA.keys():
                        matchedBoats = SearchBoat(boatList, value, searchOpt)
                        print('Mathced boats:\n')
                        for boat in matchedBoats:
                            print(boat)
                    else:
                        raise ValueError
                except:
                    print('Wrong input!')
                    continue
            elif int(opt) == 4:
                try:
                    print('--To sort Boats with Name enter 1--\n')
                    print('--To sort Boats with Port enter 2--\n')
                    print('--To sort Boats with Tonnage enter 3--\n')
                    sortOpt = input('Your option:')
                   
                    if sortOpt in Boat.SEARCH_CRITERIA.keys():
                        criterion = Boat.SEARCH_CRITERIA.get(sortOpt, 'Name')
                        boatList = sorted(boatList, key=lambda boat: getattr(boat, criterion), reverse=False) 
                        print('Sorted boats:\n')
                        for boat in boatList:
                            print(boat)
                    else:
                        raise ValueError
                except:
                    print('Wrong input!')
                    continue
            elif int(opt) == 5:
                print('All boats:\n')
                
                for boat in boatList:
                    print(boat)
            else:
                raise ValueError
        except:
            print('Wrong input! Try again\n')
            continue
