from collections import deque
from textualAlteration import alterMessage

from textSimilarity import semantic_similarity, sentiment_analysis
from csvEditor import addToCSV, createCSV


#breadth first search
class Propagation:
    def __init__(self, network):
        #init - set all starting values to 0 and start the network with agent[0]
        self.network = network
        self.frontier = deque([0])
        self.original_message =network.agents[0].message
        self.final_message = None
        self.finished = False
        self.depth = {0: 0}


    def step(self):

        if not self.frontier:

            self.finished = True
            return False
        next_frontier = deque()

        while self.frontier:

            current = self.frontier.popleft()

            current_agent = self.network.agents[current]

            #print the current sending agent and their roll 
            print(f"\n=== Agent {current} ({current_agent.role}) sending ===")

            #print a list of agents reciving the message from current
            recipients = list(self.network.graph.neighbors(current))
            if recipients:
                print(f"Recipients: {', '.join(str(r) for r in recipients)}")
            else:
                print("Recipients: (none)")

            #show the senders message
            print(f"Message:\n{current_agent.message}")

            for neighbour in recipients:
                neighbour_agent = self.network.agents[neighbour]

                #make sure the agent being passed to has not already received a message
                if not neighbour_agent.has_received:
                    #pass the current agents message to the neighbour, alter, and save the altered message 
                    neighbour_agent.receive_message(
                        alterMessage(current_agent.message, current_agent.role)
                    )

                    #prints to make the output readable
                    print(f"\n--- To Agent {neighbour} ({neighbour_agent.role}) ---")

                    #show the original message, received message, and altered message for each run
                    print(f"Original Message:{self.original_message}")
                    print(f"Recieved Message:\n{current_agent.message}")
                    print(f"Altered response:\n{neighbour_agent.message}")

                    #print the semantic similarity and sentiement anaylsis score for each message as its recorded
                    print(f"Semantic similarity score between recieved and altered message: {semantic_similarity(current_agent.message, neighbour_agent.message)}")
                    print(f"Sentiment anaylsis of altered message: {sentiment_analysis(neighbour_agent.message)}")

                    #increase the depth for saving / analysis
                    self.depth[neighbour] = self.depth[current] + 1
                    print (f"Propagation depth: {self.depth[neighbour]}")

                    #add the info to the CSV for every step of the simulation for analysis.
                    addToCSV(
                        neighbour,
                        current,
                        neighbour_agent.role,
                        self.original_message,
                        neighbour_agent.message,
                        semantic_similarity(current_agent.message, neighbour_agent.message),
                        semantic_similarity(self.original_message, neighbour_agent.message),
                        sentiment_analysis(neighbour_agent.message),
                        self.depth[neighbour]
                    )

                    self.final_message = neighbour_agent.message

                    
                    next_frontier.append(neighbour)

        self.frontier = next_frontier

        return True
    

    def run(self):
        import matplotlib.pyplot as plt

        createCSV()

        plt.figure(figsize=(8,8))

        #reset the step count to 0 for when the simulation is ran more than once without restarting
        step = 0

        self.network.display()

        while self.step():
            step += 1

            print(f"\n========= step {step} ========")

            self.network.display()

        print("\nPropagation complete")

        #print original, final, and semantic score at the end of each run
        print(f"Original message: {self.original_message}")
        print(f"Final message: {self.final_message}")
        print(f"Semantic similarity score between recieved and altered message: {semantic_similarity(self.original_message, self.final_message)}")

        #show the network at the end of the run for a few seconds before closing 
        plt.show(block = False)
        plt.pause(5)
        plt.close()