import networkx as nx
import matplotlib.pyplot as plt

from simulation.agent import Agent

class CommunicationGraph:

    def __init__(
            self, 
            num_agents = 50, 
            nearest_neighbours = 4, 
            rewiring_probability = 0.2
        ):
        
        self.num_agents = num_agents

        self.graph = nx.watts_strogatz_graph(
            n = num_agents,
            k=nearest_neighbours,
            p=rewiring_probability,
            #seed = 42
        )

        self.agents = {}

        self.create_agents()

    def create_agents(self):
        for node in self.graph.nodes:
            self.agents[node] = Agent(node)

    def assign_initial_message(self, agent_id, message, role):
        self.agents[agent_id].receive_message(message)
        self.agents[agent_id].assign_role(role)
        

    def display(self):

        plt.clf()

        colours = []

        for node in self.graph.nodes:
            if self.agents[node].has_received:
                colours.append("red")
            else:
                colours.append("lightblue")
        
        pos = nx.spring_layout(self.graph, seed = 42)

        nx.draw_networkx(
            self.graph,
            pos,
            node_color=colours,
            with_labels=True,
            node_size=450,
            font_size=8
        )

        plt.title("Communication network")

        plt.pause(0.75)

    def summary(self):
          
          print(f"Agents: {self.graph.number_of_nodes()}")

          print(f"Conections: {self.graph.number_of_edges()}")