from simulation.graph import CommunicationGraph
from simulation.propagation import Propagation
from simulation.VLMpropagation import VLMPropagation


def main():

    network = CommunicationGraph(
        num_agents=40,
        nearest_neighbours=4,
        rewiring_probability=0.2
    )

    network.summary()

    network.assign_initial_message(
        0,
        #Abbott Baby Formula Plant Halts Production Again : Story
        #Abbott baby formula plant floods in Michigan, halting production for 'weeks' : Right
        #Formula production at Abbott's Michigan plant delayed after flooding from severe storms : Left
        "Chicago Gun Violence Spikes and Increasingly Finds the Youngest Victims",
        "neutral"
    )

    simulation = Propagation(network)

    simulation.run()


if __name__ == "__main__":
    main()