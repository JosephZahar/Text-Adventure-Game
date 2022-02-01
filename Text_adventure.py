import time
from datetime import datetime

inventory = ['ID']

def lost(score):
    print("You just lost! you reached level ", score, "! Do you want to play again and reach a higher level this time?"
    "\n -------------------------------------------------yes or no-------------------------------------------------" )
    score = 'game over'
    log('lost', score)
    answer = input()
    time.sleep(2)
    if answer.lower() == "yes":
        log('play again', score)
        bedroom()
    else:
        print('Thanks for playing! We hope you enjoyed the game!')

def bedroom():
    score = 1
    print("""WELCOME TO GROUP 5 ADVENTURE GAME!
        And... ACTION! ☆-🎬-☆

        You are in your bedroom. You just woke up and need to get ready for school. 
        On the table next to your bed there is a covid mask. You can go right, left, forward, or pick up the mask;
        there is a door to the right.
        \n What now?
    """)
    answer = input()
    time.sleep(2)
    if answer.lower() == 'pick up the mask':
        log('pick up mask', score)
        inventory.append('mask')
        print('\n You can go right, left, forward. \n What now?')
        answer = input()
        time.sleep(2)
        if answer.lower() == 'right':
            log('move right', score)
            living_room()
        else:
            lost(score)
    else:
        lost(score)


def living_room():
    print('\n You enter the living room. There is a big TV in the center of the room and your ID is on a table. '
          'You can go right, left, forwards, or pick up the ID.  There is a door in front of you.'
          '\n What now?')
    score = 2
    answer = input()
    time.sleep(2)
    if answer.lower() == 'pick up the id':
        log('pick up id', score)
        print('\n You can go right, left, forward. \n What now?')
        answer = input()
        time.sleep(2)
        if answer.lower() == 'forward':
            log('move forward', score)
            kitchen()
        else:
            lost(score)
    else:
        lost(score)


def kitchen():
    print('\n You enter the kitchen. The lights are off and you can not see anything but you feel a lightswitch to '
          'your right. You can go right, left forwards, or turn on the lightswitch. There is a door on the left.'
          '\n What now?')
    score = 3
    answer = input()
    time.sleep(2)
    if answer.lower() == 'turn on the lightswitch':
        log('turn on the lightswitch', score)
        print('\n Now you are able to see. You see the stove and dishwasher to the left and a pair of car keys hanging on '
              'the wall next to it. The apartment door is on the left. You can go right, left or forwards or get the keys.'
              ' There is a door on the left. '
              '\n What now?')
        answer = input()
        time.sleep(2)
        if answer.lower() == 'get the keys':
            log('get the keys', score)
            print('\n You can go right, left, forward. \n What now?')
            inventory.append('keys')
            answer = input()
            time.sleep(2)
            if answer.lower() == 'left':
                log('move left', score)
                downstairs()
            else:
                lost(score)
        else:
            lost(score)
    else:
        print('You bumped into something!')
        lost(score)


def downstairs():
    print('\n You open the house door. You see a sign that says be safe from the covid pandemic. '
          'You see your car parked down the street to the right. You can go right, left or forwards, or view inventory.'
          '\n What now?')
    score = 4
    answer = input()
    time.sleep(2)
    if answer.lower() == 'view inventory':
        log('view inventory', score)
        print('What would you like to use?')
        for i in range(len(inventory)):
            print(str(i+1)+') ', inventory[i])
        print('What now?')
        answer = input()
        time.sleep(2)
        if 'mask' in answer.lower():
            log('put mask on', score)
            inventory.remove('mask')
            print('\n You can go right, left, forward. \n What now?')
            answer = input()
            time.sleep(2)
            if answer.lower() == 'right':
                log('move right', score)
                car()
            else:
                lost(score)
        else:
            lost(score)
    else:
        lost(score)


def car():
    print('\n You sit down in the driver seat and put your seatbelt on. '
          'You can go right, left, forwards, or view inventory. '
          '\n Now what?')
    score = 5
    answer = input()
    time.sleep(2)
    if answer.lower() == 'view inventory':
        log('view inventory', score)
        print('What would you like to use?')
        for i in range(len(inventory)):
            print(str(i+1)+') ', inventory[i])
        print('What now?')
        answer = input()
        time.sleep(2)
        if 'keys' in answer.lower():
            log('use the keys to start the car', score)
            inventory.remove('keys')
            print('\n The car turns on and you drive to uni')
            university()
        else:
            lost(score)
    else:
        lost(score)


def university():
    print('\n You walk into the university, the security guard and the turnstile are in front of you. '
          'You can go right, left, forwards or view inventory')
    score = 6
    answer = input()
    time.sleep(2)
    if answer.lower() == 'view inventory':
        log('view inventory', score)
        print('What would you like to use?')
        for i in range(len(inventory)):
            print(str(i+1)+') ', inventory[i])
        print('What now?')
        answer = input()
        time.sleep(2)
        if 'id' in answer.lower():
            log('show id to the security', score)
            inventory.remove('ID')
            print('\n You can go right, left, forward. \n What now?')
            answer = input()
            time.sleep(2)
            if answer.lower() == 'forward':
                log('move forward', score)
                classsroom()
            else:
                lost(score)
        else:
            lost(score)
    else:
        lost(score)


def classsroom():
    print('\n You walk past the turnstile. There is a hallway with 3 classrooms. '
          'You can’t remember what class you are in. You have to pick which classroom to enter.')
    score = 7
    answer = input()
    time.sleep(2)
    if answer.lower() == '2':
        log('go to class number 2', score)
        print('YOU WIN THE GAME!')
        log('WON THE GAME', score)
    else:
        print('GAME OVER')
        lost(score)

def log(message, score):
    timestamp_format = '%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("user_actions.txt","a") as f:
        f.write(timestamp + ',' + ' Level ' + str(score) + ' : ' + message + '\n')

bedroom()