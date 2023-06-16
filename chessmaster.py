class ChessPro:

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def check_color(self):
        letter = self.coordinates[0]
        number = int(self.coordinates[1])
        if letter in ['a', 'c', 'e', 'g']:
            column_color = 'black'
        else:
            column_color = 'white'
 
        if (number % 2 == 0 and column_color == 'black') or (number % 2 != 0 and column_color == 'white'):
            cell_color = 'white'
        else:
            cell_color = 'black'

        return f"{self.coordinates} - {cell_color}"


c = ChessPro("d3")
print(c.check_color())
