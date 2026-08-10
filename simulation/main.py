from simulation.graph import CommunicationGraph
from simulation.propagation import Propagation
#from simulation.VLMpropagation import VLMPropagation
from stories import get_story
from csvEditor import set_Framing


def main():

    for story_id in range(7, 11):
        for framing in ["left", "centre", "right"]:
            print(f"\n\n=== Running simulation for story {story_id} with framing '{framing}' ===\n")
            run_simulation(story_id, framing, "negative", "text")

def run_simulation(story_id, framing, role_selection, input_type):
    #share framing data to csv writer 
    set_Framing(framing, story_id, role_selection, input_type)

    #create the network with a given number of agents, neighbours
    network = CommunicationGraph(
            num_agents=100,
            nearest_neighbours=4,
            rewiring_probability=0.2
        )
    
    network.summary()
    
    network.assign_initial_message(
        0,
        get_story(story_id, framing)["headline"],
        "neutral"
    )
    
    simulation = Propagation(network)
    
    simulation.run()

if __name__ == "__main__":
    main()