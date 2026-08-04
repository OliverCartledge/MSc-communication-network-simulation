from simulation.graph import CommunicationGraph
from simulation.propagation import Propagation
from simulation.VLMpropagation import VLMPropagation


def main():

    network = CommunicationGraph(
        num_agents=8,
        nearest_neighbours=2,
        rewiring_probability=0.2
    )

    network.summary()

    network.assign_initial_message(
        0,
        """
Dozens of shootings across US mark bloody July 4th weekend
        """,
        "neutral"
    )

    simulation = VLMPropagation(network)

    # simulation.propagate()

    # network.display()

    simulation.run()


if __name__ == "__main__":
    main()