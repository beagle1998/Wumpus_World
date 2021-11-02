# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent


class MyAI(Agent):
    '''Agent.Action.TURN_LEFT,
    Agent.Action.TURN_RIGHT,
    Agent.Action.FORWARD,
    Agent.Action.CLIMB,
    Agent.Action.SHOOT,
    Agent.Action.GRAB'''

    def __init__(self):

        self.map1 = dict()  # map of the world {[position];[breeze/glitter/etc}
        self.x_max = 7  # minimum x and y
        self.y_max = 7

        self.direction = 0  # 0=up, 1= right, 2 = left, 3 = down, turn right = +1
        self.position = [0, 0]  # begining position

        self.current_route=[]
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        # if encounter danger, go back and try another route.

        #move to spot


        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    def move_spot(self,fromx,fromy,Tox,Toy):#should it be move bidirectionally? or move little by little
        #finds a route from all the way to.
        pos_route = []
        blacklist = []
        route_found = False
        1fromx=fromx
        1fromy=fromy
        while not route_found:#just finds a route to spot
            if 1fromx == tox and 1fromy == toy:
                pos_route equals a route that can get to final spot!

            if 1fromx-Tox >= 1:# if to the right
                check right node if ok, add to list of pos routes and update 1fromx
                if ok= not blacklist, has a safe marking in maps.

            elif 1fromx-tox < 0:
                check left node, if ok addd to pos_route
            etc
            etc

            else:#if not possible to continue/no possible route
                blacklist.append(pos_route[-1])#blacklist last one?
                pos_route=pos_route[:-1]#get rid of last one

        self.current_route = pos_route

























def calcMap

    def get_direction(self):
        if self.direction == 0:
            return "up"
        if self.direction == 1:
            return "right"
        if self.direction == 2:
            return "down"
        if self.direction == 3:
            return "left"

    def getAction(self, stench, breeze, glitter, bump, scream):
        # ======================================================================
        # YOUR CODE BEGINS
        # put in the dict, position and the sensor?
        if glitter:
            #pickup gold
            #move to 0,0 and climb
            pass
        if bump:
            # add to y/x max turn right
            pass




        if len(self.current_route) > 0: #high priority to move to a spot., only moves on nodes known?
            if direction towards current_route[0]:
                current_route=current_route[1:]
                action forward
            else:
                change direction towards current_route[0]

               return left/right


        if stench or breeze:# if there are safe unkown spaces, can still move there
           # add to map
           # go back, search for safe,
            pass
        #these are if current position is safe
        if there is a safe unkown, move to closest one
            #action set to direciton change or move towards current route
            pass

        if no more safe unkown:
            #calc map to find safe spaces even if stench or breeze
            #set route to there
            pass



        # ======================================================================

        return Agent.Action.CLIMB
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================

    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================

# first try moving in a direction closer to object, if not possible then move in any direction just not backwards.
elif tox - curr1[0] >= 1:  # if to the left, move right
if self.check_pos([curr1 + 1, curr1[1]], pos_route, blacklist):
    curr1[0] += 1
    pos_route.append([curr1[0], curr1[1]])

elif tox - curr1[0] <= -1:  # if to the right, move left
if self.check_pos([curr1[0] - 1, curr1[1]], pos_route, blacklist):
    curr1[0] -= 1
    pos_route.append([curr1[0], curr1[1]])

elif toy - curr1[1] >= 1:  # if below final, move up
    if self.check_pos([curr1[0], curr1[1] + 1], pos_route, blacklist):
        curr1[1] += 1
        pos_route.append([curr1[0], curr1[1]])

    elif toy - curr1[1] <= -1:  # if above, move down
    if self.check_pos([curr1[0], curr1[1] - 1], pos_route, blacklist):
        curr1[1] -= 1
        pos_route.append([curr1[0], curr1[1] - 1])

    elif self.check_pos([curr1 + 1, curr1[1]], pos_route, blacklist):
    curr1[0] += 1
pos_route.append([curr1[0], curr1[1]])





for i, k in self.map1:
    if "unkown" in k[0] and k[1] == "safe":
        self.find_route(self.position, [i])
        self.turn_self("right")
        return Agent.Action.TURN_RIGHT
    else:
        self.leave = True
        self.find_route(self.positon, [0, 0])
        self.turn_self("right")
        return Agent.Action.TURN_RIGHT