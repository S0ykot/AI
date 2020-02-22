# #from queuelib import PriorityQueue
# try:
#    import queue as Q
# except ImportError:
#    import Queue as Q
# graph = {
#     "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
#     "Zerind": {"Arad": 75, "Oradea": 71},
#     "Oradea": {"Zerind": 71, "Sibiu": 151},
#     "Timisoara": {"Arad": 118, "Lugoj": 111},
#     "Lugoj": {"Timisoara": 111, "Mehadia":70},
#     "Mehadia": {"Lugoj": 70, "Dobreta": 75},
#     "Dobreta": {"Mehadia":75, "Craiova":120},
#     "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
#     "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
#     "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
#     "Fagaras": {"Sibiu": 99, "Bucharest":211},
#     "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
#     "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
#     "Giurgiu": {"Bucharest": 90},
#     "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
#     "Hirsova": {"Urziceni": 98, "Eforie": 86},
#     "Eforie": {"Hirsova": 86},
#     "Vaslui": {"Urziceni": 142, "Iasi": 92},
#     "Iasi": {"Vaslui": 92, "Neamt": 87},
#     "Neamt": {"Iasi": 87}
# }




# def search(graph, start, end):
#     if start not in graph:
#         #raise TypeError(str(start) + ' not found in graph !')
#         return 
#     if end not in graph:
#         #raise TypeError(str(end) + ' not found in graph !')
#         return
    
#     queue= Q.PriorityQueue()
#     queue.put((0, [start]))
    
#     while not queue.empty():
#         node = queue.get()
#         current = node[1][len(node[1]) - 1]
        
#         if end in node[1]:
#             print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
#             break
        
#         cost = node[0]
#         for neighbor in graph[current]:
#             temp = node[1][:]
#             temp.append(neighbor)
#             queue.put((cost + graph[current][neighbor], temp))
        


# search(graph, 'Arad', 'Bucharest')
import queue as Q

romania = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia":70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia":75, "Craiova":120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest":211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}

class graphProblem:

    def __init__(self,initial,goal,graph):
        self.initial=initial
        self.goal=goal
        self.graph=graph

    def actions(self,state):
        return list(self.graph[state].keys())

    def result(self,state,action):
        return action

    def goal_test(self,state):
        return state == self.goal

    def path_cost(self,cost_so_far,state1,action,state2):
        return cost_so_far + (self.graph[state1][state2])
        

class Node:
    def __init__(self,state,parent=None,action=None,path_cost=0):
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost

    def expand(self,graphProblem):
        return [self.child_node(graphProblem,action)
                for action in graphProblem.actions(self.state)]
        

    def child_node(self,graphProblem,action):
        next_state=graphProblem.result(self.state,action)        
        return Node(next_state,self,action,
                    graphProblem.path_cost(self.path_cost,self.state,action,next_state))

    def path(self):        
        node, path_back = self, []       
        
        while node:            
            path_back.append(node)            
            node = node.parent
            
        
        return list(reversed(path_back))

    def solution(self):
        return [node.action for node in self.path()[1:]]





def graph_search(problem,index=0):
    frontier = Q.PriorityQueue()
    frontier.put(Node(problem.initial))
    explored = set()    

    while frontier:        
        node = frontier.get()
        if problem.goal_test(node.state):return node
        explored.add(node.state)

        frontier.queue.append(child for child in node.expand(problem)
                        if child.state not in explored and child.state not in frontier)
    return None


##def graph_search(problem,index):
##    frontier = []
##    frontier.append(Node(problem.initial))
##    explored = set()    
##
##    while frontier:        
##        node = frontier.pop(index)
##        if problem.goal_test(node.state):return node
##        explored.add(node.state)
##
##        frontier.extend(child for child in node.expand(problem)
##                        if child.state not in explored and child.state not in frontier)
##    return None




def Stack():
    return []


def breath_first_graph_search(problem,index=0):    
    return graph_search(problem,index)

def depth_first_graph_search(problem,index=-1):    
    return graph_search(problem,index)


gp = graphProblem('Arad','Bucharest',romania)
goalNode = breath_first_graph_search(gp)
print(goalNode.solution(),'Path Cost: ',goalNode.path_cost)

gp1 = graphProblem('Arad','Bucharest',romania)
goalNode1 = depth_first_graph_search(gp1)
print(goalNode1.solution(),'Path Cost: ',goalNode1.path_cost)
