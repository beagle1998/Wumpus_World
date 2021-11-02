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
        # ======================================================================
        # YOUR CODE BEGINS
        self.map1 = dict()  # map of the world {[position];[Tile type[breeze, empty, unkown],danger level(PD,D, Safe?}

        #7x7 empty nodes
        for i in range(7):
            for k in range (7):
                self.map1[(i,k)] = [["unknown"],""]



        self.x_max = 7  # minimum x and y
        self.y_max = 7

        self.direction = "right"
        self.position = (0, 0)  # begining position

        self.current_route=[]
        self.leave = False #when we want to leave/climb set this to true

        self.limiter1 = 0


        # ======================================================================
        # if encounter danger, go back and try another route.

        #move to spot


        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def check_pos(self,next1,route,blacklist):
        #print()
        #print("CHECK POS HERE")
        #print(next1)
        #print()
        if (0 <= next1[0] < self.x_max) and (0 <= next1[1] < self.y_max):
         #   print(self.map1[next1][1])
        #    print(next1)
        #    print(route)
            if (self.map1[next1][1] == "safe") and (next1 not in blacklist) and (next1 not in route):
         #       print("get here?")
         #       print(self.map1[next1][1])
         #       print(blacklist)
                #if len(route) > 0:
                #    if next1 != route[-1]:
                #        return True
               # print("safe--"+str(next1))
                return True
        return False


    def move_closer(self, current, final, route, blacklist):
        xdif = final[0] - current[0]
        ydif = final[1] - current[1]
        '''
        print()
        print("move_closer:")
        print("current:"+str(current))
        print("final:"+str(final))
        print()
        '''
        next1 = ()

        if xdif > 0:#make it so that route in move spot function is affected?
            next1 = (current[0]+1,current[1])
            if self.check_pos(next1, route, blacklist):
                route.append(next1)
                return next1

        elif xdif < 0:
            next1 = (current[0] - 1, current[1])
            if self.check_pos(next1, route, blacklist):
                route.append(next1)
                return next1

        #checking if a y difference is possible
        if ydif > 0:

            next1 = (current[0],current[1] + 1)
            if self.check_pos(next1, route, blacklist):
                route.append(next1)
                return next1


        elif ydif < 0:
            next1 = (current[0], current[1] - 1)
            if self.check_pos(next1, route, blacklist):
                route.append(next1)
                return next1
        return ()



    def just_move(self,current,route, blacklist):#this will check all four directions, if movmenent possible will return different route.
        '''
        print()
        print("just move")
        print()
        '''
        next_list=[(current[0]+1,current[1]),(current[0]-1, current[1]),(current[0], current[1]+1),(current[0], current[1]-1)]
        for i in next_list:
            if self.check_pos(i, route, blacklist):
                route.append(i)
                #print("is this 1,3?"+str(i))
                return i
        #gets to here, if no possible direction, will return empty
        return ()



    def find_route(self,start,final):#should it be move bidirectionally? or move little by little
        #finds a route from all the way to.
        #sets self.current_route to possible route to end point

        if start == final:
            return

        pos_route = []
        route_len = len(pos_route)
        blacklist = []
        route_found = False
        limiter = 0
        start1 = ()


        while not route_found:#just finds a route to spot
            '''
            print()
            print("a route not found yet?")
            print("start:"+str(start))
            print("final:"+str(final))
            print("pos_route:"+str(pos_route))
            print("blacklist"+str(blacklist))
            print()
            '''
            if (start[0] == final[0]) and (start[1] == final[1]):
                '''
                print()
                print("should get here to equal final")
                print(pos_route)
                print()
                '''
                route_found = True
                self.current_route = pos_route

            #move closer returns a pos_route, trying to move a node closer/in direction of final node
            #pos_route1 is just to see if after using the move_closer and just_move functions if movement is possible/no backtracking needed.
            else:


                start1 = self.move_closer(start,final,pos_route, blacklist)
                '''
                print()
                print("check here")
                print("pos_route:"+str(pos_route))
                print("route_len:"+str(route_len))
                print(start1)
                print()
                '''
                if start1 == ():#just_move will instead just search all possible directions to see if it can move at all
                    #no change, then check other ways
                    start1 = self.just_move(start, pos_route, blacklist)

                    if start1 == (): #if no difference, then nothing possible, will blacklist
                        '''
                        print()
                        print("blacklist/backtracking")
                        print(start)
                        print(start1)
                        print(pos_route)
                        print(blacklist)
                        '''
                        blacklist.append(pos_route[-1])  # blacklist last one?
                        pos_route = pos_route[:-1]  # get rid of last one
                        start = pos_route[-1]
             #           print(start)
              #          print(pos_route)
              #          print(blacklist)
              #          print()
                    else:
                        '''
                        print()
                        print("did it add here? This spot is for just move")
                        print(start)
                        print(start1)
                        print()
                        '''
                        start = pos_route[-1]
                        route_len += 1

                else:
                    '''
                    print()
                    print("did it add here?")
                    print(start)
                    print(start1)
                    print()
                    '''
                    start = pos_route[-1]
                    route_len += 1

            #if limiter >= 5:
            #    route_found=True
            #    self.current_route = pos_route
            #limiter +=1
        ''' print()
            print("End stuff?")
            print(start)
            print(final)
            print()
            route_found = True
            self.current_route = pos_route   '''


    def vector_dir(self, vector):#turns a vector into a direction left, right, etc
        if vector[0] == 1:
            return "right"
        elif vector[0] == -1:
            return "left"
        elif vector[1] == 1:
            return "up"
        elif vector[1] == -1:
            return "down"

    def dir_vect(self, direction):  # turns a vector into a direction left, right, etc
        if direction == "right":
            return [1, 0]
        if direction == "left":
            return [-1, 0]
        if direction == "up":
            return [0, 1]
        if direction == "down":
            return [0, -1]

    def turn_self(self, turn): #returns direction after rturning.
        dir = ["up", "right", "down", "left"]
        pos = dir.index(self.direction)

        if turn == "right":
            if pos+1 > 3:
                return dir[0]
            return dir[pos+1]

        elif turn == "left":
            return dir[pos-1]

    def get_safe_unknowns(self):
        safe_unknowns = []
        for k, v in self.map1.items():
            if 0 <= k[0] < self.x_max and 0 <= k[1] < self.y_max:
                if v[0] == ["unknown"] and v[1] == "safe":
                    safe_unknowns.append(k)
        return safe_unknowns

    def explored_all_safe_unknowns(self):
        safe_unknowns = self.get_safe_unknowns()
        if len(safe_unknowns) == 0:
            return True
        return False


    def getAction(self, stench, breeze, glitter, bump, scream):
        # ======================================================================
        # YOUR CODE BEGINS
        # put in the dict, position and the sensor?
        #self.limiter1 +=1
        #if self.limiter1 > 5:
        #    exit()
        '''
        print()
        print("AN ACTION STARTS HERE")
        print(self.position)
        print(self.direction)
        print(self.current_route)
        if stench:
           print("stench")
        elif breeze:
           print("breeze")
        elif glitter:
            print(glitter)
        elif bump:
            print("bump")
        else:
            print("empty")
        print()
        '''




        if self.leave and self.position == (0,0):
            return Agent.Action.CLIMB


        if glitter:
            self.find_route(self.position,(0,0))
            self.leave = True
            return Agent.Action.GRAB
            #pickup gold
            #move to 0,0 and climb

        if bump:
            #only positve checks(up, right, since 0,0 never go negative, use self.check
            wall_pos = (self.dir_vect(self.direction)[0] + self.position[0], self.dir_vect(self.direction) [1]) #get the position of the wall bumped into
            if self.dir_vect(self.direction)[0] == 1:
                #right wall
                self.x_max = self.position[0]
                self.position = (self.position[0]-1, self.position[1])
            if self.dir_vect(self.direction)[1] == 1:#if upper wall
                self.y_max = self.position[1]
                self.position = (self.position[0], self.position[1]-1)
            #wall_pos= position + direciton , if 0,0 + up = 0,1



#first time starting would start here.

        if stench or breeze:# if there are safe unkown spaces, can still move there
            if stench:
                self.map1[self.position][0] = ["stench"]
                self.map1[self.position][1] = "safe"
                if breeze:
                    self.map1[self.position][0].append("breeze")
            elif breeze:
                self.map1[self.position][0] = ["breeze"]
                self.map1[self.position][1] = "safe"

            adj_list = [(self.position[0] + 1, self.position[1]),
                        (self.position[0] - 1, self.position[1]),
                        (self.position[0], self.position[1] + 1),
                        (self.position[0], self.position[1] - 1)]


            for i in adj_list:
                if (0 <= i[0] < self.x_max) and (0 <= i[1] < self.y_max) and (self.map1[i][1] == ""):
                    self.map1[i][1] = "pd"

            #here add to make surrounding tiles possible danger
            #continue to next two if statements, to determine course of action

        else:#if this spot is empty

            self.map1[self.position][0] = ["empty"]
            self.map1[self.position][1] = "safe"

            adj_list = [(self.position[0] + 1, self.position[1]),
                        (self.position[0] - 1, self.position[1]),
                        (self.position[0], self.position[1] + 1),
                        (self.position[0], self.position[1] - 1)]


            for i in adj_list:
                if 0 <= i[0] < self.x_max and 0 <= i[1] < self.y_max:
                    self.map1[i][1] = "safe"

        if len(self.current_route) > 0:  # high priority to move to a spot., only moves on nodes known?
            # route direction is the vector to the next node.[1,0]
            r_direction = [self.current_route[0][0] - self.position[0], self.current_route[0][1] - self.position[1]]
            if self.direction == self.vector_dir(
                    r_direction):  # if current direction ex left is equal to route direction

                self.position = self.current_route[0]
                if len(self.current_route) == 1:
                    self.current_route = []
                else:
                    self.current_route = self.current_route[1:]  # take of the first node since moving there
                return Agent.Action.FORWARD
            else:  # optimize HERERE ONLY TURNING RIGHT TO GET TO RIGHT DIRECTION< MAYBE FASTER WAY??????
                self.direction = self.turn_self("right")
                return Agent.Action.TURN_RIGHT
                # change direction towards current_route[0]
            # either way, an action is returned, so will start from top either way.



        #these are if current position is safe
        #if there is a safe unkown, move to closest one:
        if self.explored_all_safe_unknowns():
            self.leave = True
            #print(self.map1)
            self.find_route(self.position, (0, 0))
        else:
            #print("before first move")
            #print(self.map1)
            #print(self.get_safe_unknowns())
            if(len(self.get_safe_unknowns()) != 1):
                self.find_route(self.position, self.get_safe_unknowns()[-1])
            else:
                self.find_route(self.position, self.get_safe_unknowns()[0])
            #print("first move soon")

        #arbitrary action
        self.direction = self.turn_self("right")
        #print("direction after?")
        #print(self.direction)
        #print(self.current_route)
        return Agent.Action.TURN_RIGHT





    # ======================================================================
        #should never get to here

        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================

    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================