
#predefined variables
rooms = {
    'Courtyard': {},
    'Castle': {},
    'East Wing': {},
    'West Wing': {},
    'North Wing': {},
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
               return ""
    



def player_room(name):
     print("-" * 40)
     print("You are in the " + key_list[name])
     print(roomDesc())
     input3 = input("ppo")


     
#main while loop
while currentRoom != 'exit':
    player_room(roomname)


player_start()