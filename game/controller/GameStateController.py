from model.GameState import GameState
from controller.MenuState import MenuState
from controller.PlayingState import PlayingState

class GameStateController:
    def __init__(self):
        self.running = True
        self.state = None
        self.states = {
            GameState.MENU: MenuState(self),
            GameState.PLAYING: PlayingState(self)
        }
        self.change_state(GameState.MENU)

    def change_state(self, new_state):
        self.state = self.states[new_state]

    def get_state(self):
        return self.state
