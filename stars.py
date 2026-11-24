class Star:
    """ Klasse für Sterne"""
    def __init__(self, name, mass, radius, temperature):
        self.name = str(name)
        self.mass = float(mass)
        self.radius = float(radius)
        self.temperature = float(temperature)

    def __str__(self):
         return f'{self.name} has mass: {self.mass}, radius: {self.radius} and temperature {self.temperature}'
 
    def print_info(self):
        print(f'{self.name} has mass: {self.mass}, radius: {self.radius} and temperature {self.temperature}')
       
    def is_FGKM(self, t_limit = 7300):
        return (self.temperature < t_limit)

def find_star(stars, name):
    for star in stars:
        if star.name == name:
            return star
        else:
            return f'"{name}" does not exist'

if __name__ == "__main__":
    print("Running stars.py directly")

print('I am ' + __name__)