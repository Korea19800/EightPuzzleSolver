from board import Board
from astar import AStar
from bfs import BFS
import sys

class InvalidFileException(Exception):
    pass

# function to print 1D list to 2D list
def print2D(list):
      for x in range(9):
          print(str(list
                    [x]) + ' ',end='')
          if( x == 2 or x == 5 or x == 8):
              print()
      print()
  
def main():
    print("Welcome\nThis program will sove eight-puzzle problem\n")
    print("Enter a file name: ")
 
    # read a file and check errors
    fname = input()  
    try:
        file = open(fname, 'r')    
        s = file.read()
        file.close()   
        fileList = s.split()  #splice text in file before ' '

        # check if there is an non numeric character in the file
        for i in fileList:
            if not i.isdigit() : 
                raise ValueError
              
        # check if there are more than 9 chars in the file
        if len(fileList) != 9: 
            raise InvalidFileException
          
    except FileNotFoundError:
        print("Cannot find the file. Ending the program")
        sys.exit(1)
        
    except InvalidFileException:
        print("The file should have only 9 numbers. Ending the program")
        sys.exit(1)
      
    except ValueError:
        print("Only numbers between 1 to 9 should be in the file. Ending the program")
        sys.exit(1)
      
    else:
        print("Successfuly load the file")
    
    #convert string list to int list
    eightList = list(map(int, fileList))  
   
    # use eightList list to make a Board instance
    p = Board(eightList)
    # print initial state
    print("\nInitial State:")
    print2D(eightList)

    print("Select which algorithm you wish to run on this puzzle.")
    print("To choose BFS, type bfs. To choose A*, type astar")
    choice = input()
  
    if choice == 'bfs':
        s = BFS(p)
    elif choice == 'astar':
        s = AStar(p)
    else:
        print("Not available answer, calculating with A* search")
        s = AStar(p)
      
    s.solve()

    print('\n')
  
    # printing path to goal
    print("Path to Goal\n")
    print("Initial State:")
    print2D(eightList)         # printing eightList in 2d form

    # printing path using s.path list.
    for i in s.path:
        if i == 'Up':
          for j in eightList:
            if eightList[j] == 0:
              eightList[j], eightList[j-3] = eightList[j-3],eightList[j]
              break
        elif i == 'Down':
          for j in eightList:
            if eightList[j] == 0:
              eightList[j], eightList[j+3] = eightList[j+3],eightList[j]
              break
        elif i == 'Right':
          for j in eightList:
            if eightList[j] == 0:
              eightList[j], eightList[j+1] = eightList[j+1],eightList[j]
              break
        elif i == 'Left':
          for j in eightList:
            if eightList[j] == 0:
              eightList[j], eightList[j-1] = eightList[j-1],eightList[j]
              break
        print2D(eightList)  # printing eightList in 2d form
        
    print('\n')
    print('The number of moves: ' + str(len(s.path)) + '\n')
    print('nodes_expanded: ' + str(s.nodes_expanded) + '\n')

if __name__ == "__main__":
    main()
