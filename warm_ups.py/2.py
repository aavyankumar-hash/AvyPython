class TicTacToe:
    def __init__(self):   
        self.root=tk.Tk()
        self.root.title("Tic - Tac - Toe")
        self.root.configure(bg="black")
        self.root.player1 = "X"
        self.root.player2 = "O"
        self.board  = [""] * 9
        self.buttons = []
        self.create_widgets()
        self.root.mainloop()
    def create_widgets(self):
       """creates the buttons for the tic tac toe board"""

