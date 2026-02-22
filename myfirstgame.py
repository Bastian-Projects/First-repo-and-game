import random


def showInstructions():
    print('''
Welcome to my first RPG Game
============================

Get to the Greenery with a key and a potion.
Or get to the Laboratory with the BookOfLife and the Beam-O-Mat.
Avoid the monsters!

Commands: 
	go [south/north/east/west]
	get [item]
	help (shows available directions and monster location)
''')

inventory = []

rooms = \
    {'Hall':{
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Library',
        'item': 'key'
    },
    'Kitchen':{
        'north': 'Hall',
        'south': 'Office',
        'west': 'Storage Room'
    },
    'Dining Room':{
        'west': 'Hall',
        'south': 'Greenery',
        'item': 'potion'
    },
    'Greenery':{
        'north': 'Dining Room',
        'south': 'Laboratory'
    },
    'Library':{
        'east': 'Hall',
        'item': 'BookOfLife',
        'south': 'Storage Room'
    },
    'Office':{
        'north': 'Kitchen',
        'east': 'Laboratory',
        'south': 'Toilet'
    },
    'Laboratory':{
        'west': 'Office',
        'north': 'Greenery',
        'item': 'Beam-O-Mat'
    },
    'Storage Room': {
        'north': 'Library',
        'east': 'Kitchen',
        'item': 'Toiletdoor-Key'
    },
    #a room for the monster to appear without being in the way - IF it appears there
    'Toilet':{
        'north': 'Office',
        'item':'Toiletpaper'
    }
}

currentRoom = 'Hall'
#a cache of rooms in the beginning to reset items when the monster moves around
cachedRooms = \
    {'Hall':{
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Library',
        'item': 'key'
    },
    'Kitchen':{
        'north': 'Hall',
        'south': 'Office',
        'west': 'Storage Room'
    },
    'Dining Room':{
        'west': 'Hall',
        'south': 'Greenery',
        'item': 'potion'
    },
    'Greenery':{
        'north': 'Dining Room',
        'south': 'Laboratory'
    },
    'Library':{
        'east': 'Hall',
        'item': 'BookOfLife',
        'south': 'Storage Room'
    },
    'Office':{
        'north': 'Kitchen',
        'east': 'Laboratory',
        'south': 'Toilet'
    },
    'Laboratory':{
        'west': 'Office',
        'north': 'Greenery',
        'item': 'Beam-O-Mat'
    },
    'Storage Room':{
        'north': 'Library',
        'east': 'Kitchen',
        'item': 'Toiletdoor-Key'
    },
    #a room for the monster to appear without being in the way - IF it appears there
    'Toilet':{
        'north': 'Office',
        'item':'Toiletpaper'
    }
}

#this function sets the monster to a room where the game doesn't begin, so you can at least start playing and
#aren't eaten in the first round
def setMonster():
    roomList = ['Kitchen','Dining Room','Library','Office','Laboratory','Greenery','Toilet']
    j = int(random.randint(0,6))
    print('You hear a monster near the ' + roomList[j])
    rooms[roomList[j]]['item'] = 'monster'


#for a more immersive experience ;)
def moveMonster():
    #search for the monster and delete it first, then set it to a new location so there aren't two monsters
    for singleRoom in rooms:
        if 'item' in rooms[singleRoom] and rooms[singleRoom]['item'] == 'monster':
            del rooms[singleRoom]['item']
            #Problem: when the monster is moved, and there was an item in the room before, the old item now would be deleted
            #so here's a cachedRooms from the beginning and I can set the item of that specific room again.
            if 'item' in cachedRooms[singleRoom]:
                rooms[singleRoom]['item'] = cachedRooms[singleRoom]['item']
    roomList = ['Kitchen','Dining Room','Library','Office','Laboratory','Greenery','Toilet']
    j = int(random.randint(0,6))
    rooms[roomList[j]]['item']='monster'
    print('You heard a monster move around in the mansion. Be careful!')

def showStatus():
    #if a player wants to see the current status of inventory and location for orientation
    print('___________________________')
    print('You are in the '+currentRoom)
    print('Inventory: '+ str(inventory))
    #this also tells the player, what items are available in the room
    if "item" in rooms[currentRoom]:
        print('You see a '+ rooms[currentRoom]['item'])
    print('___________________________')

#trying to get the item and remove it from the room so it can't be picked up twice and will instead appear in own inventory
def getItem(pickedItem):
    if 'item' in rooms[currentRoom]:
        #in case the monster moved and suddenly is in your room
        if rooms[currentRoom]['item'] == 'monster' and move[1] == 'monster':
            print('You can\'t catch the monster.')
            return
        # special case "Upper Case word":
        if move[1] == 'beam-o-mat':
            if 'Beam-O-Mat' in rooms[currentRoom]['item']:
                inventory.append(rooms[currentRoom]['item'])
                print('Got item Beam-O-Mat')
                del rooms[currentRoom]['item']
                return
        # second special case "Upper Case word":
        if move[1] == 'bookoflife':
            if 'BookOfLife' in rooms[currentRoom]['item']:
                inventory.append(rooms[currentRoom]['item'])
                print('Got item BookOfLife')
                del rooms[currentRoom]['item']
                return
        if move[1] == 'toiletdoor-key':
            if 'Toiletdoor-Key' in rooms[currentRoom]['item']:
                inventory.append(rooms[currentRoom]['item'])
                print('Got item Toiletdoor-Key')
                del rooms[currentRoom]['item']
                return
        if move[1] == 'toiletpaper':
            if 'Toiletpaper' in rooms[currentRoom]['item']:
                inventory.append(rooms[currentRoom]['item'])
                print('Got item Toiletpaper')
                del rooms[currentRoom]['item']
                return
        if move[1] == rooms[currentRoom]['item']:
            inventory.append(rooms[currentRoom]['item'])
            print('Got item ' + move[1])
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')


showInstructions()
setMonster()
#set i to 1, so the text when you go to a monster-room, without doing anything else in the first round, is right.
i = 1
while True:
    showStatus()
    if i == 2:
        moveMonster()
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split()
    if move[0] == 'exit':
        break
    if move[0] == "help":
        for direction in rooms[currentRoom]:
            if direction != 'item':
                print('You can go ' + direction)
        for room in rooms:
            if 'item' in rooms[room] and rooms[room]['item'] == 'monster':
                print('The monster is in the ' + room)
            if i == 2:
                i = 0
        continue
    if move[0] == 'go':
        if len(move) > 1 and move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')
    elif move[0] == 'get':
        if len(move) > 1:
            getItem(move[1])
        else:
            print('Can\'t get item')
    if 'potion' in inventory and 'key' in inventory:
        if currentRoom == 'Greenery':
            print('''As you open the door, you see a light shining bright and warm. You can feel grass beneath your feet
After a while your eyes got accustomed to the light and you can see that you\'re in the Greenery
You\'ve got a potion and a key in your inventory so you can open the huge entrance to the mansion
Finally it is time. These creepy scratching noises you heard for so long are about to be gone, you can escape!
Congratulations! You got to the exit of the creepy mansion and WIN!''')
            print()
            input('Press enter to exit the game')
            break
    if 'BookOfLife' in inventory and 'Beam-O-Mat' in inventory:
        if currentRoom == 'Laboratory':
            print('You feel the power of the \'Beam-O-Mat\', and by reading the BookOfLife, you learned how to use it!')
            print('Those items enable you to beam the monster away, and to finally live in peace inside this mansion')
            print('Congratulations! You are now able to defeat the monster and WIN!')
            print()
            input('Press enter to exit the game')
            break
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and i == 0:
        print('You stayed too long in the ' + currentRoom + ', and you hear something entering the room.')
        print('With growing horror you see a humanoid monster at the door... you are trapped!')
        print('You desperately search for a way out, but the hungry monster already jumped and caught you.')
        print('A starved monster has got you... GAME OVER!')
        print()
        input('Press enter to exit the game')
        break
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('As you cautiously enter the ' + currentRoom + ', you hear scratching sounds, as if someone was searching something.')
        print('you look around but don\'t see anything. You close the door and turn around to take a few steps.')
        print('Suddenly, you jump back as a strange, humanoid monster appears. It\'s drooling and appears to be very hungry...')
        print('You desperately turn around and run, but the monster already jumped and caught you.')
        print('A starved monster has got you... GAME OVER!')
        print()
        input('Press enter to exit the game')
        break
    if i == 2:
        #the monster now moves around every second round so it's more difficult to escape
        i = 0
    else:
        i += 1


