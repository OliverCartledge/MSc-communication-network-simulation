from simulation.graph import CommunicationGraph
from simulation.propagation import Propagation


def main():

    network = CommunicationGraph(
        num_agents=12,
        nearest_neighbours=4,
        rewiring_probability=0.2
    )

    network.summary()

    network.assign_initial_message(
        0,
        "The protest remained peaceful",
        "neutral"
    )

    simulation = Propagation(network)

    # simulation.propagate()

    # network.display()

    simulation.run()


if __name__ == "__main__":
    main()