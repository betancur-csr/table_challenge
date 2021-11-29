# The Table challenge

## Installation
Developed `Python 3.9.7`. There is no further installation required for this project. Run the script with `python table_board.py`.

## Implementation

To run the program is required to introduce 4 comma-separated integers. However, it does not check whether those values are valid or not. Therefore if it gets invalid values (see below) the program still will run but with a failed simulation from the beginning. The following cases are possible:

* Either width, height or both are equal or less than zero 
* The initial position of the object is out of the table range

Once the object has fallen (simulation fails) from the table it cannot be recovered therefore the program does not stop the execution but neither carries out more operations, it just waits until the 0 command (quit simulation) is introduced.

Once the simulation has started, the user can introduce successive instructions either one by one or together in a comma-separated string at once, for example, `1,4,1,3,2,3,0,4,1,0`. In this case, the simulation runs the commands `1,4,1,3,2,3` and quits the simulation therefore the remaining commands after the first `0` are not processed.

### Error handling
There is a brief logic to handle errors when reading the initialization of the simulation. Basically, it asks for another "header" entry until the given format is correct. Note that as is mentioned before it does not check the given values allowing to run already failed simulation

On the other hand, there is no check on the commands introduced. This way introducing wrong commands does not have any effect on the simulation since they are simply ignored. For example the commands `1,4,1,3,2,7,3,2,k,4,1,command1,0` will result in `[0,1]`

## Improvements
The project has been developed using Object-Oriented and modular programming practices in order to make it easy to add future improvements. For example changing the input to a JSON file or object can be carried out with minimum changes in the main function

``header = json_file['header'].split(',')`` 

instead of 

``header = input().split(',')`` 

Other possible easy to implement changes are:
* Add more commands: by simple adding the logic in a method of the class Table and mapping it with a number on the `execute_commands()` function
* Allow the object to recover after falling: using the class method `simulation_fails()` only at the end of the simulation and not every time after the object moves
* Make several simulations on the same or even different Table instances
