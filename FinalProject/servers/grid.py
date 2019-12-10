from .Player import Player
import Pyro4
def create_response(message="empty", data=None, code=None):
    return dict(message="Rep:" + message + "!", data=data, code=code)

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
        _message = "Connected successfully"
        if role == "1":
            if not self.is_player_full():
                if len(self.players) == 0:
                    print("tol")
                    name = "_plx"+name
                    _symbol = "O"
                    _player = Player(name, _symbol)
                    self.players.append(_player)
                    _message = _message + "--Register Success"
                    _message = _message + "--You get first turn"
                    print(self.get_player_names())
                elif len(self.players) == 1:
                    print("tolol")
                    name = "_plo"+name
                    _symbol = "X"
                    _player = Player(name, _symbol)
                    self.players.append(_player)
                    _message = _message + "--Register Success"
                    _message = _message + "--You get second turn"
                _code = "101"
                return create_response(_message, name, _code)
            else:
                if name in self.spectators:
                    name = name + "_spec"
                self.spectators.append(name)
                _code = "102"
                _message = _message + "--Registered as 'Spectator' successfully"
                return create_response(_message, name, _code)

    def player_role(self, name):
        return len([x for x in self.players if x.name == name])

    def get_player_index(self, name):
        return next((i for i, item in enumerate(self.players) if item.name == name), -1)

    def get_player_names(self):
        return [x.name for i,x in enumerate(self.players)]

    def get_symbol(self,index):
        return self.players[index].symbol

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

    def get_cell_value(self, y, x):
        return self.grid[y][x]

    def get_grid(self,y,x):
        if(self.get_cell_value(y,x)==0):
            return create_response("Success", '')
        else:
            return create_response("Success", self.get_cell_value(y,x))

    def set_cell_value(self, y, x, value):
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

    def available(self, y, x):
        if(self.get_cell_value(y,x) != 0):
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

    def get_currentmv(self):
        return self.currentmv

    def nextmv(self):
        if (self.currentmv == 'X'):
            self.currentmv = 'O'
        elif(self.currentmv == 'O'):
            self.currentmv = 'X'

    def fill_board(self, name: str, y: int, x: int):
        _player_index = self.get_player_index(name)
        print(self.players[_player_index].symbol)
        print(self.get_player_names())
        print(self.player_role)
        if not self.player_role(name):
            return create_response("You are not a 'Player'!")
        if not self.running:
            return create_response("Game hasn't started yet!")
        if (self.currentmv != self.players[_player_index].symbol):
            return create_response("It is not your turn! -- "+self.currentmv+"-"+self.players[_player_index].symbol)
        if not self.available(y, x):
          return create_response("The spot is not available!")
        self.set_cell_value(y,x,self.players[_player_index].symbol)
        self.nextmv()
        self.print_grid()
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

    def print_grid(self):
        for row in self.grid:
            print(row)