def tictactoe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    winningcombos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choosenumber()
        if board[n] == "x" or board[n] == "o":
            print("\nyou can't go there. please try again")
            p1()
        else:
            board[n] = "x"

    def p2():
        n = choosenumber()
        if board[n] == "x" or board[n] == "o":
            print("\nyou can't go there. please try again")
            p2()
        else:
            board[n] = "o"

    def choosenumber():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nthat's not on the board. please try again")
                        continue
                except ValueError:
                   print("\nnot a number. please try again")
                   continue

    def checkboard():
        count = 0
        for a in winningcombos:
            if board[a[0]] == board[a[1]] == board[a[2]] == "x":
                print("player 1 wins!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "o":
                print("player 2 wins!\n")
                return True
        for a in range(9):
            if board[a] == "x" or board[a] == "o":
                count += 1
            if count == 9:
                print("it's a tie\n")
                return True

    while not end:
        draw()
        end = checkboard()
        if end == True:
            break
        print("player 1 choose where to place a x")
        p1()
        print()
        draw()
        end = checkboard()
        if end == True:
            break
        print("player 2 choose where to place an o")
        p2()
        print()

    if input("play again? (yes/no)\n") == "yes":
        print()
        tictactoe()

tictactoe()