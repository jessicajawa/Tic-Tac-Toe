import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def init(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x300")
        self.player_turn = True
        self.game_mode = "PvP"  # or "PvAI"
        self.score = {"X": 0, "O": 0, "draw": 0}
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.mode_label = tk.Label(self.window, text="Player vs Player")
        self.mode_label.grid(row=3, column=0, columnspan=3)

        self.score_label = tk.Label(self.window, text="Score: X - 0, O - 0, Draw - 0")
        self.score_label.grid(row=4, column=0, columnspan=3)

        self.restart_button = tk.Button(self.window, text="Restart", command=self.restart)
        self.restart_button.grid(row=5, column=0)

        self.exit_button = tk.Button(self.window, text="Exit", command=self.window.destroy)
        self.exit_button.grid(row=5, column=2)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            if self.player_turn:
                self.buttons[row][column]['text'] = "X"
                if self.check_win("X"):
                    self.score["X"] += 1
                    self.score_label['text'] = f"Score: X - {self.score['X']}, O - {self.score['O']}, Draw - {self.score['draw']}"
                    messagebox.showinfo("Game Over", "X wins!")
                    self.restart()
                elif self.check_draw():
                    self.score["draw"] += 1
                    self.score_label['text'] = f"Score: X - {self.score['X']}, O - {self.score['O']}, Draw - {self.score['draw']}"
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.restart()
                else:
                    self.player_turn = False
                    if self.game_mode == "PvAI":
                        self.ai_move()
            else:
                self.buttons[row][column]['text'] = "O"
                if self.check_win("O"):
                    self.score["O"] += 1
                    self.score_label['text'] = f"Score: X - {self.score['X']}, O - {self.score['O']}, Draw - {self.score['draw']}"
                    messagebox.showinfo("Game Over", "O wins!")
                    self.restart()
                elif self.check_draw():
                    self.score["draw"] += 1
                    self.score_label['text'] = f"Score: X - {self.score['X']}, O - {self.score['O']}, Draw - {self.score['draw']}"
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.restart()
                else:
                    self.player_turn = True

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    self.buttons[i][j]['text'] = "O"
                    score = self.minimax(0, False)
                    self.buttons[i][j]['text'] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        self.buttons[best_move[0]][best_move[1]]['text'] = "O"
        if self.check_win("O"):
            self.score["O"] += 1
            self.score_label['text'] = f"Score: X - {self.score['X']}, O - {self.score['O']}, Draw - {self.score['draw']}"
            messagebox.showinfo("Game Over", "O wins!")
            self.restart()
        elif self.check_draw():
            self.score["draw"] += 1
            self.score_label['text'] = f"Score: X - {self.score['X']}, O - {self.score['O']}, Draw - {self.score['draw']}"
            messagebox.showinfo("Game Over", "It's a draw!")
            self.restart()
        else:
            self.player_turn = True