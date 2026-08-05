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

            # Summary header for this sender and its recipients
            print(f"\n=== Agent {current} ({current_agent.role}) sending ===")

            # List recipients once to avoid repeated prints
            recipients = list(self.network.graph.neighbors(current))
            if recipients:
                print(f"Recipients: {', '.join(str(r) for r in recipients)}")
            else:
                print("Recipients: (none)")

            # Show the sender's message once
            print(f"Message:\n{current_agent.message}")

            #testing image generation with the working current version 
            #createImageTest(current, current_agent.message)
            #describeImage(current, current_agent.role)

            for neighbour in recipients:
                neighbour_agent = self.network.agents[neighbour]

                if not neighbour_agent.has_received:
                    neighbour_agent.receive_message(
                        alterMessage(current_agent.message, current_agent.role)
                    )

                    # Clear, labeled block for each recipient's altered response
                    print(f"\n--- To Agent {neighbour} ({neighbour_agent.role}) ---")
                    print(f"Altered response:\n{neighbour_agent.message}")

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

            # Summary header for this sender and its recipients
            print(f"\n=== Agent {current} ({current_agent.role}) sending ===")

            # List recipients once to avoid repeated prints
            recipients = list(self.network.graph.neighbors(current))
            if recipients:
                print(f"Recipients: {', '.join(str(r) for r in recipients)}")
            else:
                print("Recipients: (none)")

            # Show the sender's message once
            print(f"Message:\n{current_agent.message}")

            for neighbour in recipients:
                neighbour_agent = self.network.agents[neighbour]

                if not neighbour_agent.has_received:

                    neighbour_agent.receive_message(
                        current_agent.message
                    )

                    # Clear, labeled block for each recipient's received/altered message
                    print(f"\n--- To Agent {neighbour} ({neighbour_agent.role}) ---")
                    print(f"Received message:\n{neighbour_agent.message}")

                    queue.append(neighbour)