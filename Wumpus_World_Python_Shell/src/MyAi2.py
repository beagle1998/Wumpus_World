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
        self.direction = 0  # 0=up, 1= right, 2 = left, 3 = down, turn right = +1
        self.position = [0, 0]  # begining position
        self.x_max = 7  # minimum x and y
        self.y_max = 7

        self.move1=0
        self.move_set=[]
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        # if encounter danger, go back and try another route.

        #move to spot


        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    def move_spot(self,fromx,fromy,Tox,Toy):#should it be move bidirectionally? or move little by little
        pass

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
        if self.move1 > 1:
            pass

        if bump:
            if self.direction == 0:
                self.y_max = self.position[1]+1
            else:
                self.x_max = self.position[0] + 1

        possible_action = [["right",[self.position[0]+1,self.position[1]]],   #right
                             ["up",[self.position[0],self.position[1]+1]], #up
                            ["left",[self.position[0]-1,self.position[1]]],  #left
                           ["down",[self.position[0],self.position[1]-1]]]   #down
        for k,i in possible_action:
            if 0 < i[0] <= self.x_max and 0 < i[1] <= self.y_max: # if action does not hit wall
                #check map
                if [i[0],i[1]] not in self.map1 or self.map1[[i[0],i[1]]] == "e": #if an action gets to a safe spot do it
                    self.move1=1
                    if self.get_direction() == k:
                        self.position[1] += 1
                        return Agent.Action.FORWARD
                    else:   #basically just navigates safe stuff
                        self.direction += 1
                        return Agent.Action.TURN_RIGHT






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