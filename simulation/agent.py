class Agent:
    def __init__(self, agent_id):
        self.id = agent_id
        self.message = None
        
        #checks to make sure info isnt repassed to the same node
        self.has_received = False

    def receive_message(self, message):
        self.message = message

        #checks to make sure info isnt repassed to the same node
        self.has_received = True

    def __repr__(self):
        return f"Agent({self.id})"