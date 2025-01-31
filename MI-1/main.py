
import random

class Node:
    id: int
    startingTime: int
    terminationTime: int
    isActive: int
    relations: []
    value: int
    
    def __init__(self, id, startingTime, terminationTime ):
        self.id = id
        self.startingTime = startingTime
        self.terminationTime = terminationTime 
        self.isActive = True
        self.relations = []
        self.value = 100
        print(f"node: {self.id} is created at {self.startingTime} and it will terminate at {self.terminationTime} with value {self.value}")
    
    



class Relation:
    id: int
    startingNode: Node
    terminalNode: Node 
    weight: Node
    
    def __init__(self, id, startingNode, terminalNode):
        self.id = id
        self.startingNode = startingNode
        self.terminalNode = terminalNode
        self.weight = 50
        print(f"relation: {self.id} is created from {self.startingNode.id} to {self.terminalNode.id} and its weight is {self.weight}")
            

class Agent:
    root: Node
    currentId: int
    currentRelationId: int
    nodes: []
    
    
    def __init__(self):
        print("Agent way to creating...")
        terminationTime = random.randint(1,10)
        root = Node(1, 0, terminationTime)
        self.nodes = [root]
        self.currentId = 1
        self.currentRelationId = 1
        
    
    def run(self):
        print("agent is running")
        # created 5 node whose are interconnected
        for _ in range(5):
            terminationTime = random.randint(1,10)
            node = Node(self.currentId, 0, terminationTime)
            self.currentId += 1
            for anotherNode in self.nodes:
                relation = Relation(self.currentRelationId, node, anotherNode)
                self.currentRelationId += 1
                node.relations.append(relation)
            self.nodes.append(node)    
        self.printState()
        self.modifyState(self.getNode(3),5, 2)
        self.printState()
        self.modifyState(self.getNode(3),5, 2)
        self.printState()
        self.modifyState(self.getNode(3),5, 2)
        self.printState()
        



    def printState(self):
        print("------------------------------")
        for node in self.nodes:
            print(f"node: {node.id} :: {node.value}")
            for relation in node.relations:
                print(f"({relation.terminalNode.id}, {relation.weight})", end=" ")
                
            print()
    
    
    
    def modifyState(self, node, value, range):
        if range == 0:
            return 
        for relation in  node.relations:
            nextNode = relation.terminalNode
            nextNode.value -= value
            
    
    def getNode(self, id: int):
        return next((node for node in self.nodes if id == node.id), None)    






if __name__ == "__main__":
    agent = Agent()
    agent.run()








