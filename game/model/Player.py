class Player:
    def __init__(self, name, position, color="red", is_impostor=False):
        self.name = name
        self.position = list(position) 
        self.color = color
        self.is_impostor = is_impostor
        self.alive = True
        self.velocity = 100
        self.size = (15, 20)
    def move(self, dx, dy):
        if self.alive:
            self.position[0] += dx * self.velocity 
            self.position[1] += dy * self.velocity

    def kill(self, other_player):
        if self.is_impostor and other_player.alive:
            other_player.alive = False
            return True
        return False

    def report(self):
        return f"{self.name} reported a body."

    def __repr__(self):
        status = "Alive" if self.alive else "Dead"
        role = "Impostor" if self.is_impostor else "Crewmate"
        return f"<Player {self.name} | {role} | {status} at {self.position}>"
