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
from queue import Queue


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

    def getAdjacencyList(self, current):
        adj_list = [(current[0] + 1, current[1]),
                    (current[0] - 1, current[1]),
                    (current[0], current[1] + 1),
                    (current[0], current[1] - 1)]
        return adj_list

    def BFS(self, queue, visited, parent):
        current = queue.get()
        adj = self.getAdjacencyList(current)
        for i in adj:
            if (i in self.map1.keys() and self.map1[i][1] == "safe"):
                if (not visited[i]):
                    visited[i] = True
                    # print(parent)
                    parent[i] = current
                    # print(parent)
                    queue.put(i)
                pass

    def isIntersecting(self, s_visited, t_visited):
        intersecting_nodes = []
        for i in self.map1.keys():
            if (s_visited[i] and t_visited[i]):
                intersecting_nodes.append(i)
                # return i
        if (intersecting_nodes != []):
            # print(intersecting_nodes)
            middle = int((len(intersecting_nodes) / 2))
            return intersecting_nodes[middle]
        return -1

    def getPath(self, s_parent, t_parent, s, t, intersectNode):
        # print(s_parent,t_parent)
        # print(intersectNode)
        path = []
        path.append(intersectNode)
        i = intersectNode
        # print(intersectNode)
        while (i != s):
            path.append(s_parent[i])
            i = s_parent[i]
        path.reverse()
        i = intersectNode
        # print(i)
        while (i != t):
            path.append(t_parent[i])
            # print(t_parent[i])
            i = t_parent[i]
        if (path != [] and path[0] == self.position):
            path.pop(0)
        return path

    def find_route(self,s,t):#should it be move bidirectionally? or move little by little
        s_visited = dict()
        t_visited = dict()
        s_parent = dict()
        t_parent = dict()
        s_queue = Queue(maxsize=49)
        t_queue = Queue(maxsize=49)
        for i in range(7):
            for j in range(7):
                s_visited[(i, j)] = False
                t_visited[(i, j)] = False
        s_queue.put(s)
        s_visited[s] = True
        s_parent[s] = -1
        t_queue.put(t)
        t_visited[t] = True
        t_parent[t] = -1
        while (not s_queue.empty() and not t_queue.empty()):
            self.BFS(s_queue, s_visited, s_parent)  # try breadth first from source and goal
            self.BFS(t_queue, t_visited, t_parent)
            intersectNode = self.isIntersecting(s_visited, t_visited)
            if (intersectNode != -1):
                self.current_route = self.getPath(s_parent, t_parent, s, t, intersectNode)
                pass
            pass

        return []  # could not find a path so return empty list

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

    def turn_self1(self,r_direction):  #returns agent.action.turn and sets direction to new direction

        #turn right then check if new direction is correct one
        dir = ["up", "right", "down", "left"]
        pos = dir.index(self.direction)
        #checking a turn right
        if(pos+1 > 3):
            pos = 0
        else:
            pos+=1

        if(dir[pos] == self.dir_vect(r_direction)):
            self.direction = dir[pos]
            return Agent.Action.TURN_RIGHT
        else: #if direction not right, then if left or opposite side it is optimal to go left ok
            if(pos == 0):
                pos = -1
            else:
                pos -= 1
            self.direction = dir[pos-1]
            return Agent.Action.TURN_LEFT



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
            if self.direction == self.vector_dir(r_direction):  # if current direction ex left is equal to route direction
                self.position = self.current_route[0]
                if len(self.current_route) == 1:
                    self.current_route = []
                else:
                    self.current_route = self.current_route[1:]  # take of the first node since moving there
                return Agent.Action.FORWARD
            else:  # optimize HERERE ONLY TURNING RIGHT TO GET TO RIGHT DIRECTION< MAYBE FASTER WAY?????? here is where agent must change direction, then it can go "forward"

                #self.turn_self(next node,r_direction)
                return self.turn_self1(r_direction)
                #return Agent.Action.TURN_RIGHT
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
            else:  # optimize HERERE ONLY TURNING RIGHT TO GET TO RIGHT DIRECTION< MAYBE FASTER WAY?????? here is where agent must change direction, then it can go "forward"

                # self.turn_self(next node,r_direction)
                return self.turn_self1(r_direction)
        #arbitrary action
        #return self.turn_self1("right")
        #print("direction after?")
        #print(self.direction)
        #print(self.current_route)
        #return Agent.Action.TURN_RIGHT





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