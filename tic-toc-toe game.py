#making tic-tac toe game for learning python3.7.1

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def win(current_game):
        #logical part of the game
        #cheaking the horaizontal part of the game
        for row in game:
            if row.count(row[0]) == len(row) and row[0] != 0:
                print(f"player {row[0]} is the winner horizontally !!!")
                return True

        #logical part of the game
        #cheaking the diagonal part of the game
        diags = []
        for col,row in enumerate(reversed(range(len(game)))):
                diags.append(game[row][col])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
                print(f"player {diags[0]} is the winner diagonally (/) !!!")
                return True

        diags = []
        for ix in range(len(game)):
                diags.append(game[ix][ix])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
                print(f"player {diags[0]} is the winner diagonally (\\) !!!")
                return True

 
        #logical part of the game
        #cheaking the vertical part of the game
        for col in range(len(game)):
            cheak = []
            for row in game:
                cheak.append(row[col])

            if cheak.count(cheak[0]) == len(cheak) and cheak[0] != 0:
                print(f"player {diags[0]} is the winner vertically (|) !!!")
                return True

        #finishing of logical part

def game_board(game_map,player = 0,row = 0,column = 0,just_display = False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: did you input row/column as 0, 1 or 2?", e)

    except Exception as e:
        print("Something went very wrong!",e)


import itertools
play = True
players = [1, 2]
while play:
        game = [[0,0,0],
                [0,0,0],
                [0,0,0]]

        game_won = False
        game = game_board(game,just_display=True)
        player_choice = itertools.cycle([1,2])
        while not game_won:
                current_player = next(player_choice)
                print(f"current player: {current_player}")
                column_choice = int(input("what column do you want to play? (0,1,2): "))
                row_choice = int(input("what row do you want to play? (0,1,2): "))
                game = game_board(game,current_player,row_choice,column_choice)
                is_won = win(game)
                if is_won:
                        game_won = True