from collections import deque

from imageGeneration import createImageTest
from photoAnalysis import describeImage

from textSimilarity import semantic_similarity, sentiment_analysis
from csvEditor import addToVisualCSV, createVisualCSV

#breadth first search
class VLMPropagation:
    def __init__(self, network):
        self.network = network

        self.propLayer = deque([0])

        self.original_message =network.agents[0].message

        self.finished = False

        self.depth = {0: 0}

    def step(self):

        if not self.propLayer:

            self.finished = True
            return False
        next_propLayer = deque()

        while self.propLayer:

            current = self.propLayer.popleft()

            current_agent = self.network.agents[current]

            print(f"\nAgent {current} {current_agent.role} communicating...")

            print(f"\nMy message is: {current_agent.message}")

            if current == 0:
                print(f"Start agent is {current}")
                createImageTest(current, current_agent.message)

            for neighbour in self.network.graph.neighbors(current):
                neighbour_agent = self.network.agents[neighbour]

                if not neighbour_agent.has_received:
                    neighbour_agent.receive_image(
                        describeImage(current, current_agent.role)
                    )
                    print(f"Neighbours altered message image saved from this description: \n{neighbour_agent.message}")
                    createImageTest(
                        neighbour, neighbour_agent.message
                        )

                    print(f"\n--- To Agent {neighbour} ({neighbour_agent.role}) ---")

                    next_propLayer.append(neighbour)

                    #print the semantic similarity and sentiement anaylsis score for each message as its recorded
                    print(f"Semantic similarity score between recieved and altered message: {semantic_similarity(current_agent.message, neighbour_agent.message)}")
                    print(f"Sentiment anaylsis of altered message: {sentiment_analysis(neighbour_agent.message)}")

                    #increase the depth for saving / analysis
                    self.depth[neighbour] = self.depth[current] + 1
                    print (f"Propagation depth: {self.depth[neighbour]}")

                    #add the info to the CSV for every step of the simulation for analysis.
                    addToVisualCSV(
                        neighbour,
                        current,
                        neighbour_agent.role,
                        self.original_message,
                        current_agent.message,
                        f"generateTesting{neighbour}.png",
                        neighbour_agent.message,
                        semantic_similarity(current_agent.message, neighbour_agent.message),
                        semantic_similarity(self.original_message, neighbour_agent.message),
                        sentiment_analysis(neighbour_agent.message),
                        self.depth[neighbour]
                    )

        self.propLayer = next_propLayer

        return True
    
    def run(self):
        import matplotlib.pyplot as plt

        createVisualCSV()
    
        plt.figure(figsize=(8,8))

        step = 0

        self.network.display()

        while self.step():
            step += 1

            print(f"\n========= step {step} ========")

            self.network.display()

        print("\nPropagation complete")

        plt.show()