

class TransitionError(Exception):

    """Raised when an operation attempts state transitions that's not allowd

    Attributes:
        previous -- state at the beginning of transition
        next_state -- state at the end of transition
        message -- explanation why specific transtion is not allowed
    """

    def __init__(self, previous, next_state, message):
        self.previous = previous
        self.next_state = next_state
        self.message = message
    
    