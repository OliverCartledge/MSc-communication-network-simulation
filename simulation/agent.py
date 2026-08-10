import random

ACTOR_TYPES = [
    "neutral",
    "positive",
    "negative"
]


class Agent:
    def __init__(self, agent_id):
        self.id = agent_id
        self.message = None
        self.similarity = 1.0

        #if the roles are randomized
        self.role = "negative"
        #self.role = random.choice(ACTOR_TYPES)
        
        #checks to make sure info isnt repassed to the same node
        self.has_received = False

    def receive_message(self, message):
        self.message = message

        #checks to make sure info isnt repassed to the same node
        self.has_received = True

    def receive_image(self, imageDescription):
        self.message = imageDescription
        
        self.has_received = True

    def assign_role(self, role):
        self.role = role

    def __repr__(self):
        return f"Agent({self.id})"