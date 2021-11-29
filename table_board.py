from itertools import cycle

class Table:

    def __init__(self, width, height, x, y) -> None:
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.orientation_list = cycle(["north", "east", "south", "west"])
        self.orientation = next(self.orientation_list)
        self.has_fallen = False
        self.simulation_fails()

    def rotate_clockwise(self):
        self.orientation = next(self.orientation_list)

    def rotate_counter_clockwise(self):
        for i in range(3):
            self.orientation = next(self.orientation_list)
    
    def simulation_fails(self):
        if self.x < 0 or self.x > self.width - 1 or self.y < 0 or self.y > self.height - 1:
            self.x = -1
            self.y = -1
            self.has_fallen = True

    def move_forward(self,step = 1):
        if self.orientation == "north":
            self.y -= step
        if self.orientation == "south":
            self.y += step
        if self.orientation == "east":
            self.x += step
        if self.orientation == "west":
            self.x -= step

        self.simulation_fails()    

    def move_barckwards(self):
        self.move_forward(-1)

    def print_position(self):
        print('[{},{}]'.format(self.x,self.y))

def execute_commands(commands,table):
    for command in commands:
        if command == '1':
            table.move_forward()
        elif command == '2':
            table.move_barckwards()
        elif command == '3':
            table.rotate_clockwise()
        elif command == '4':
            table.rotate_counter_clockwise()
        
# read and execute commands from stdin until the simulations is finished
def simulate(table):
    while True:
        commands = input().split(',')
        if '0' not in commands:
            if not table.has_fallen:
                execute_commands(commands,table)
        else:
            execute_commands(commands[0:commands.index('0')], table)
            table.print_position()
            break

def main():
    # read table size and position from stdin
    while True:
        header = input().split(',')
        try:
            width,height,x,y = [int(i) for i in header]
            break
        except:
            print("input must be 4 comma separated integer values: width,height,x,y")

    # create table with the given values
    my_table = Table(width, height, x, y)

    # read and execute commands from stdin until the simulations is finished
    simulate(my_table)
  
if __name__== "__main__" :
    main()        
