# Gregory Grabowski
# 12/7/2022
# IT-140
# Prof. Hodg


import random


def main():

    # list of valid movement directions
    DIRECTIONS = ['north', 'south', 'east', 'west']


    # game map defined as a dictionary of dictionaries
    game_map = {
        'library'           : {
            'north' : None,
            'east'  : 'family room',
            'south' : 'office',
            'west'  : None
        },
        'family room'       : {
            'north' : None,
            'east'  : None,
            'south' : 'kitchen',
            'west'  : 'library'
        },
        'office'            : {
            'north' : 'library',
            'east'  : None,
            'south' : 'living room',
            'west'  : None
        },
        'kitchen'           : {
            'north' : 'family room',
            'east'  : 'pantry',
            'south' : 'foyer',
            'west'  : None
        },
        'pantry'    : {
            'north' : None,
            'east'  : None,
            'south' : 'dining room',
            'west'  : 'kitchen'
        },
        'living room'       : {
            'north' : 'office',
            'east'  : 'foyer',
            'south' : None,
            'west'  : None
        },
        'foyer'             : {
            'north' : 'kitchen',
            'east'  : 'dining room',
            'south' : None,
            'west'  : 'living room'
        },
        'dining room'      : {
            'north' : 'pantry',
            'east'  : None,
            'south' : None,
            'west'  : 'foyer'
        }
    }

    item_location = {  # dictonary to store item locations
        'remote' : None,
        'battery': None
    }

    player_inventory = {  # player inventory
        'remote' : False,
        'battery' : False
    }

    # game variables
    roomba_location = 'family room'  # starting room for roomba
    player_location = 'foyer'  # starting room for player
    player_alive = True  # self explanitory... 
    RUNNING = True  # the variable that keeps the game running inside the game loop

    item_location = generate_item_location(item_location)  # generates the random location of the items needed to win

    game_start()  # prints key information before starting gameplay

    while player_alive and RUNNING:  # start of game loop

        # sends all variables related to player actions into the action function and returns updated variables
        player_location, RUNNING, item_location, player_inventory = action(player_location, game_map, RUNNING, item_location, player_inventory)
        
        # allows for roomba actions to occur
        roomba_location = roomba_action(roomba_location, game_map)
        
        # updates player with location of both player and roomba every game tick
        print('You are in the', player_location)
        print('The roomba is in the', roomba_location)
        print('\n' * 2)

        # checks if player and roomba are in the same room and ends game if true
        if roomba_location == player_location:
            print('\n' * 2)
            print('You trip over the roomba and break your neck...')
            print('GAME OVER!')
            print('\n' * 2)
            print('Don\'t let yourself get caught in the same room as the roomba!')
            player_alive = False
        
        # checks if player has both key items and is in the family room, if so, player wins
        if player_location == 'family room' and player_inventory['battery'] == True and player_inventory['remote'] == True:
            print('Congradulations!!! You\'ve won!!!')
            print('\n' * 2)
            RUNNING = False



def action(player_location, game_map, RUNNING, item_location, player_inventory):  # processes text based actions and runs the function corresponding to said action
    player_action = input('Enter your action: ').split()  # forces player action to be a list in case of multi-argument inputs
    print('\n' * 30)
    
    
    if len(player_action) == 0:  # prevents crash if no input is entered
        pass

    elif 'move' == player_action[0]:  # move condition, allows player movement through house
        if len(player_action) < 2:
            print('please enter a second argument \'move [direction]\'')
        elif len(player_action) > 3:
            print('too many arguments for \'move\'')
        else:
            player_location = move_player(player_location, game_map, player_action[1])
    
    elif 'exit' == player_action[0]:  # exit game condition, exits the game
        RUNNING = False
    
    elif 'map' == player_action[0]:  # map condition, displays a map of the house
        print_map()

    elif 'search' == player_action[0]:  # searches the room you are in for items
        player_inventory, item_location = search_room(player_inventory, item_location, player_location)
    
    elif 'inventory' == player_action[0]:
        print_inventory(player_inventory)


    elif 'help' == player_action[0]:  # prints helpful info
        print_help()
    
    else:  # prompts user to type help for list of commands
        print('Invalid command, try typing \'help\' for a list of valid commands')

    return player_location, RUNNING, item_location, player_inventory # returns all update values passed in to function      


def move_player(player_location, game_map, direction):  # handles all things player movement
    if game_map[player_location][direction] != None:  # checks that the attempted move direction is valid
        print('New room is', game_map[player_location][direction])
        print('\n' * 2)
        return game_map[player_location][direction]
    else:  # user prompt for when there is no room in the direction being tried
        print('There is no room that way...')
        print('\n' * 2)
        return player_location


def generate_item_location(item_location):  # generates where the items needed are in the house
    room_list = ['library', 'family room', 'office', 'kitchen', 'pantry', 'living room', 'foyer', 'dining room']
    x = random.randint(0, len(room_list) - 1)
    item_location['remote'] = room_list[x]
    del room_list[x]
    x = random.randint(0, len(room_list) - 1)
    item_location['battery'] = room_list[x]
    return item_location


def print_map():  # prints map to screen
    print('**************************************************')
    print('*_____________    _____________                  *')
    print('*|            |__|             |                 *')
    print('*|  library    __  Family Room |                 *')
    print('*|____    ____|  |_____    ____|                 *')
    print('* ____|  |____    _____|  |____    _____________ *')
    print('*|            |  |             |__|             |*')
    print('*|   Office   |  |   Kitchen    __    Pantry    |*')
    print('*|____    ____|  |_____    ____|  |____    _____|*')
    print('* ____|  |____    _____|  |____    ____|  |_____ *')
    print('*|            |__|             |__|             |*')
    print('*| Living Room __     Foyer     __  Dining Room |*')
    print('*|____________|  |_____________|  |_____________|*')
    print('*                                                *')
    print('**************************************************')


def search_room(player_inventory, item_location, player_location):  # searches the room the player is in for a key item
    print('You search the', player_location, 'and find')
    if player_location == item_location['remote']:
        item_location['remote'] = None
        player_inventory['remote'] = True
        print('the remote!')
    elif player_location == item_location['battery']:
        item_location['battery'] = None
        player_inventory['battery'] = True
        print('the battery!')
    else:
        print('nothing...')
    print('\n' * 2)
    return player_inventory, item_location


def print_help():  # prints a list of all commands and what they do
    print('*************************************************')
    print('exit : Exits the game')
    print('inventory : check the items in your inventory')
    print('move [direction] : moves in the direction entered')
    print('map : displays a layout of the house')
    print('search : search the current room for items')
    print('*************************************************')


def print_inventory(player_inventory):  # prints player inventory
    print('You have found the following items:')
    if player_inventory['remote'] == True:
        print('-Remote')
    if player_inventory['battery'] == True:
        print('-Battery')
    print('\n' * 2)


def roomba_action(roomba_location, game_map):  # allows the roomba to move
    directions = ['north', 'south', 'east', 'west']
    move = directions[random.randint(0, 3)]
    
    if game_map[roomba_location][move] != None:
        roomba_location = game_map[roomba_location][move]

    return roomba_location


def game_start():  # prints key information
    print('hello player!')
    print('You must search the rooms of your house for')
    print('your TV remote and the battery for it.')
    print('once you have found both, make your way')
    print('to the Family Room to sit down for an episode')
    print('of your favorite show, and to beat this game!')
    print('type \'help\' for a list of all commands')
    a = input('press ENTER to continue and play the game!')


if __name__ == '__main__':
    main()
    print('Exiting game, Thank you for playing!')