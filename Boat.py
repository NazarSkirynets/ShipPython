MAX_NAME_SIZE = 50

class Boat:
    SEARCH_CRITERIA = {'1': 'Name', '2': 'Port', '3': 'Tonnage'}
    def __init__(self, name: str='', port: str='', tonnage: float=1.):
        try:
            self.__name = name
            self.__port = port
            self.__tonnage = float(tonnage)
            
        except:
            print('Type casting error. Tonnage value should be float')
        
    @property
    def Name(self) -> str:
        return self.__name
    
    @Name.setter
    def Name(self, name : str):
        try:
            if len(name) < MAX_NAME_SIZE:
                self.__name = name
            else:
                raise ValueError
            
        except ValueError:
                print("Oops! This name is too big")
    
    @property
    def Port(self) -> str:
        return self.__port
    
    @Port.setter
    def Port(self, port : str):
        self.__port = port
    
    @property
    def Tonnage(self) -> float:
        return self.__tonnage
    
    @Tonnage.setter
    def Tonnage(self, tonnage : float):
        try:
            self.__tonnage = float(tonnage)
        except:
            print('Type casting error. Tonnage value should be float')
        
    def __str__(self):
        return 'Boat {0} from port {1} with tonnage {2}'.format(self.Name, self.Port, self.Tonnage)
    
    def __repr__(self):
        return self.__str__()
    
    def ReadFromConsole(self):
        self.Name, self.Port, self.Tonnage = input().split(' ')
    
    def ReadFromFile(self, fileName: str):
        with open(fileName, 'r') as file:
            self.Name, self.Port, self.Tonnage = file.readline().split(' ')
            

        
        
    
    
    