#predefined variables
rooms = {
    'Courtyard': {'North': 'Castle'},
    'Castle': {'South': 'Courtyard', 'East': 'East Wing', 'West': 'West Wing', 'North': 'North Wing'},
    'East Wing': {'West': 'Castle'},
    'West Wing': {'East': 'Castle'},
    'North Wing': {'South': 'Castle', 'West': 'Tower'},
    'Tower': {},
    '???': {}
}

currentRoom = ''
key_list = list(rooms)
roomname = 0


#inital/print function
def player_start():
    print("-" * 40)
    print("Castle Adventure Game")
    print("Obtain 5 items to access the secret room!")
    print("Move Commands: 'North', 'East', 'South', 'West'")
    print("Add to inventory: 'item ____'")
    print("-" * 40)
    startCmd = input("Enter 'Start' to begin:").lower()
    while startCmd != 'start':
            print("invalid input")
            startCmd = input("Enter 'Start' to begin:").lower()


def roomDesc():
     match roomname:
          case 0 :
               return "This is where you begin your adventure.\nYou see paths leading to the Castle."

def player_room(name):
     print("-" * 40)
     print("You are in the " + key_list[name])
     print(roomDesc())
     print("Available Moves: " + ', '.join(rooms[key_list[name]].keys()))
     print("-" * 40)
     player_move = input("Enter your move:").lower()
     if player_move != valid_move(player_move):
          print("invalid move")

def valid_move(move):
     match roomname:
          case 0 :
               if move == 'north':
                    currentRoom = rooms['Castle']
                    roomname = 1
                    return move
               else:
                    return 'invalid'

     
#main while loop
while currentRoom != 'exit':
    player_room(roomname)


player_start()