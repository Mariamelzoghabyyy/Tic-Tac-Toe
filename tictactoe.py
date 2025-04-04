import random
from collections import deque

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize a 3x3 board
        self.current_player = 'X'  # X is the user, O is the computer

    def print_board(self):
        print("\n")
        for i in range(3):
            print("|".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("-----")
        print("\n")

    def check_winner(self):
        # Winning combinations
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_full(self):
        return ' ' not in self.board

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position, player):
        self.board[position] = player

    def undo_move(self, position):
        self.board[position] = ' '

    def depth_first_search(self):
        for move in self.get_available_moves():
            self.make_move(move, 'O')
            if self.check_winner() == 'O':
                self.undo_move(move)
                return move
            self.undo_move(move)

        for move in self.get_available_moves():
            self.make_move(move, 'X')
            if self.check_winner() == 'X':
                self.undo_move(move)
                return move
            self.undo_move(move)

        return random.choice(self.get_available_moves())

    def breadth_first_search(self):
        queue = deque()
        queue.append(self.board[:])

        while queue:
            current_board = queue.popleft()
            available_moves = [i for i, spot in enumerate(current_board) if spot == ' ']

            for move in available_moves:
                next_board = current_board[:]
                next_board[move] = 'O'
                if self.check_winner() == 'O':
                    return move
                queue.append(next_board)

        return random.choice(available_moves)

    def uniform_cost_search(self):
        return self.depth_first_search()

    def iterative_deepening_search(self):
        depth = 0
        while True:
            result = self.dls(depth)
            if result is not None:
                return result
            depth += 1

    def dls(self, depth):
        stack = [(self.board[:], depth)]

        while stack:
            current_board, depth = stack.pop()
            available_moves = [i for i, spot in enumerate(current_board) if spot == ' ']

            for move in available_moves:
                next_board = current_board[:]
                next_board[move] = 'O'
                if self.check_winner() == 'O':
                    return move
                if depth > 0:
                    stack.append((next_board, depth - 1))

        return None

    def computer_move(self):
        move = self.depth_first_search()  # Change this to switch algorithms
        self.make_move(move, 'O')

    def play(self):
        while True:
            self.print_board()
            user_move = input("Enter your move (0-8): ")
            if user_move.isdigit() and 0 <= int(user_move) <= 8:
                user_move = int(user_move)
                if self.board[user_move] == ' ':
                    self.make_move(user_move, 'X')
                    if self.check_winner() == 'X':
                        self.print_board()
                        print("You win!")
                        break
                    if self.is_full():
                        self.print_board()
                        print("It's a draw!")
                        break
                    self.computer_move()
                    if self.check_winner() == 'O':
                        self.print_board()
                        print("Computer wins!")
                        break
                    if self.is_full():
                        self.print_board()
                        print("It's a draw!")
                        break
                else:
                    print("Position already taken, try again.")
            else:
                print("Invalid input, please enter a number between 0 and 8.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()