from .Player import Player
import Pyro4
def create_response(message="empty", data=None, code=None):
    return dict(message="Response--" + message + "--End of response", data=data, code=code)

@Pyro4.behavior(instance_mode="single")
class Grid:
    def __init__(self):
        self.grid = [[0 for x in range(3)] for y in range(3)]
        self.turn_flag = 0
        self.running = False
        self.winner = "Draw"
        self.spectators = []
        self.players = []
        self.currentmv ='O'


    def is_player_full(self):
        return len(self.players) >= 2

    def get_board(self):
        return create_response("Success", self.grid)

    def remove_client(self, name: str, role: str):
        if role == "1":
            _player_index = self.get_player_index(name)
            self.players.pop(_player_index)
            self.clear_grid()
        self.spectators.remove(name)

    def register_client(self, name: str, role: str):
        if name in self.spectators:
            name = name + "_alter"
        self.spectators.append(name)
        _message = "Connected successfully"
        if role == "1":
            if not self.is_player_full():
                if len(self.players) == 0:
                    _symbol = "O"
                    _player = Player(name, _symbol)
                    self.players.append(_player)
                    _message = _message + "--Register Success"
                    _message = _message + "--You get to move first"
                    self.currentmv = _symbol
                elif len(self.players) == 1:
                    _symbol = "X"
                    _player = Player(name, _symbol)
                    self.players.append(_player)
                    _message = _message + "--Registered as 'Player' successfully"
                    _message = _message + "--You get to move second"
                _code = "101"
                return create_response(_message, None, _code)
            else:
                _code = "102"
                _message = _message + "--Registered as 'Spectator' successfully"
        return create_response(_message, None, _code)

    def player_role(self, name):
        return len([x for x in self.players if x.name == name])

    def get_player_index(self, name):
        return next((i for i, item in enumerate(self.players) if item.name == name), -1)

    def start_game(self, name):
        if not self.player_role(name):
            return create_response("You are not a 'Player'!")
        if not self.is_player_full():
            return create_response("Not enough 'Player'!")
        if self.running:
            return create_response("Game is already started!")

        self.running = True
        self.winner = "Draw"
        return create_response("Game started, 'Player' who connects first may make their first move")

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def is_grid_full(self):
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False
        return True

    def clear_grid(self):
        for y in range(len(self.grid)):
            for x in range (len(self.grid[y])):
                self.set_cell_value(x, y, 0)
        self.running = False

    def available(self, x, y):
        if(self.get_cell_value(x,y) != 0):
            return False
        else:
            return True

    def equal3(self, a, b, c):
        if (a==b and b==c and a!=0):
            return True

    def checkWinner(self):
        for j in range(3):
            if(self.equal3(self.grid[j][0],self.grid[j][1],self.grid[j][2])):
                self.winner = self.grid[j][0]
        for i in range(3):
            if (self.equal3(self.grid[0][i],self.grid[1][i],self.grid[2][i])):
                self.winner = self.grid[0][i]
        if (self.equal3(self.grid[0][0],self.grid[1][1],self.grid[2][2])):
            self.winner = self.grid[1][1]

        if (self.equal3(self.grid[0][2],self.grid[1][1],self.grid[2][0])):
            self.winner = self.grid[1][1]
        return self.winner


    def set_grid(self, x, y, player):
            if player == "X":
                self.set_cell_value(x, y, "X")
            elif player == "O":
                self.set_cell_value(x, y, "O")

    def nextmv(self):
        if (self.currentmv == 'X'):
            self.currentmv = 'O'
        else:
            self.currentmv = 'X'

    def fill_board(self, name: str, y: int, x: int):
        if not self.player_role(name):
            return create_response("You are not a 'Player'!")
        if not self.running:
            return create_response("Game hasn't started yet!")
        _player_index = self.get_player_index(name)
        if (self.currentmv != self.players[_player_index].symbol):
            return create_response("It is not your turn yet!")
        if not self.available(x, y):
            return create_response("The spot is already taken!")
        self.set_cell_value(x,y,self.players[_player_index].symbol)
        self.nextmv()
        if self.checkWinner() == self.players[_player_index].symbol:
            self.clear_grid()
            self.winner = name
            _code = "201"
            return create_response("{} won the game!--Game ended".format(name), self.winner, _code)

        if self.is_grid_full():
            self.clear_grid()
            _code = "202"
            return create_response("Board is already full!--It's a draw!--Game ended")

        return create_response("Made move successfully", self.grid)
