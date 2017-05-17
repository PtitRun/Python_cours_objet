import json
import math

class Agent:
    
    # Constructeurs
    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)
        
    #Dire bonjour
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + "!"

class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.longitude_degrees = longitude_degrees
        self.latitude_degrees = latitude_degrees
    
    def __degrees_to_radial(self, degrees):
        return degrees * math.pi /180
    
    @property    
    def longitude(self):
        return self.__degrees_to_radial(self.longitude_degrees)
    
    @property
    def latitude(self):
        return self.__degrees_to_radial(self.latitude_degrees)

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        print("My position is Latitude({}) and longitude({})".format(agent.position.latitude, agent.position.longitude))
        

main()