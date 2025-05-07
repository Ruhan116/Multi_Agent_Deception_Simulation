from model.GameState import GameState

class GameStateController:
    def __init__(self):
        self.current_state = GameState.MENU
        self.previous_state = None
        
    def change_state(self, new_state):
        self.previous_state = self.current_state
        self.current_state = new_state
        
    def return_to_previous_state(self):
        if self.previous_state is not None:
            self.current_state, self.previous_state = self.previous_state, self.current_state
            
    def is_state(self, state):
        return self.current_state == state