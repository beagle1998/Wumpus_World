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


class MyAI ( Agent ):
    '''Agent.Action.TURN_LEFT,
    Agent.Action.TURN_RIGHT,
    Agent.Action.FORWARD,
    Agent.Action.CLIMB,
    Agent.Action.SHOOT,
    Agent.Action.GRAB'''


    def __init__ ( self ):

        self.dict1 = dict()  # map of the world {[position];[breeze/glitter/etc}
        self.direction = 0  #0=up, 1= right, 2 = left, 3 = down, turn right = +1
        self.position = [0, 0]#begining position
        self.x_max = 4 # minimum x and y
        self.y_max = 4
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        #if encounter danger, go back and try another route.
        self.backtrackNum = 2
        self.backtrack = [
                          Agent.Action.TURN_RIGHT,
                          Agent.Action.Forward]


        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        #put in the dict, position and the sensor?

        self.direction = self.direction % 4 #resets it if too big

        if glitter:  # initiate escape
            pass

        if 2 < self.backtrackNum > 0: # back tracking, result is at previous spot facing opp direction
            self.backtrackNum+=1
            return self.backtrack[self.backtrackNum]


        elif stench or breeze:  #if trouble, move back keep looking
            #s=stench, b= breeze, e= empty
            if stench:#add to danger
                self.dict1[self.position] = "s"
                print(self.dict1)

            if breeze: #add to danger
                if stench:
                    self.dict1[self.position] = "sb"
                self.dict1[self.position] = "b"
                print(self.dict1)
            #backtrack
            self.backtrackNum = 0
            self.direction + 2
            return Agent.Action.TURN_RIGHT

        else:  #if spot is empty, move forward, check positon and map, move to place unknown,
            self.dict1[self.position] = "e"
            print(self.dict1)

            return Agent.Action.forward



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

    blacklist = []
    route_found = False

    while not route_found:  # just finds a route to spot

        print(pos_route)
        if (start[0] == final[0]) and (start[1] == final[1]):
            route_found = True
            self.current_route = pos_route

        # move closer returns a pos_route, trying to move a node closer/in direction of final node
        # pos_route1 is just to see if after using the move_closer and just_move functions if movement is possible/no backtracking needed.
        else:
            pos_route1 = pos_route

            pos_route = self.move_closer(start, final, pos_route, blacklist)

            if len(
                    pos_route) == route_len:  # just_move will instead just search all possible directions to see if it can move at all
                # no change, then check other ways
                pos_route1 = self.just_move(start, pos_route, blacklist)

                if pos_route == pos_route1:  # if no difference, then nothing possible, will blacklist

                    blacklist.append(pos_route[-1])  # blacklist last one?
                    pos_route = pos_route[:-1]  # get rid of last one
                    start = pos_route[:-1]
            else:
                pos_route = pos_route1
