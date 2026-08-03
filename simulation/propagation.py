from collections import deque
from ollamaTest import alterMessage

from imageGeneration import createImageTest
from photoAnalysis import describeImage

#breadth first search
class Propagation:
    def __init__(self, network):
        self.network = network

        self.frontier = deque([0])

        self.finished = False

    def step(self):

        if not self.frontier:

            self.finished = True
            return False
        next_frontier = deque()

        while self.frontier:

            current = self.frontier.popleft()

            current_agent = self.network.agents[current]

            print(f"\nAgent {current} {current_agent.role} communicating...")

            print(f"\nMy message is: {current_agent.message}")

            #testing image generation with the working current version 
            #createImageTest(current, current_agent.message)
            #describeImage(current, current_agent.role)

            for neighbour in self.network.graph.neighbors(current):
                neighbour_agent = self.network.agents[neighbour]

                if not neighbour_agent.has_received:
                    neighbour_agent.receive_message(
                        alterMessage(current_agent.message, current_agent.role)
                    )
                    print(f"Neighbours altered message: {neighbour_agent.message}")
                    print(
                        f"Agent {current} -> Agent {neighbour}"
                    )

                    next_frontier.append(neighbour)

        self.frontier = next_frontier

        return True
    

    def run(self):
        import matplotlib.pyplot as plt

        plt.figure(figsize=(8,8))

        step = 0

        self.network.display()

        while self.step():
            step += 1

            print(f"\n========= step {step} ========")

            self.network.display()

        print("\nPropagation complete")

        plt.show()


    #done in an instant. may be good for debugging later? 
    def propagate(self):
        queue = deque()

        queue.append(0)

        while queue:
            current = queue.popleft()

            current_agent = self.network.agents[current]

            print(f"\nAgent {current} is communicating...")

            for neighbour in self.network.graph.neighbors(current):
                neighbour_agent = self.network.agents[neighbour]

                if not neighbour_agent.has_received:

                    neighbour_agent.receive_message(
                        current_agent.message
                    )

                    print(
                        f"Agent {current} "
                        f"-> "
                        f"Agent {neighbour}"
                    )

                    queue.append(neighbour)