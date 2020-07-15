#!/usr/bin/env python3 

from random import shuffle

"""
Scrabble Game
Classes:
Tile - keeps track of the tile letter and value
Rack - keeps track of the tiles in a player's letter rack
Bag - keeps track of the remaining tiles in the bag
Word - checks the validity of a word and its placement
Board - keeps track of the tiles' location on the board
"""
#Keeps track of the score-worth of each letter-tile.
LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,
                 "#": 0}

class Tile:
    """
    Class that allows for the creation of a tile. Initializes using an uppercase string of one letter,
    and an integer representing that letter's score.
    """
    def __init__(self, letter, letter_values):
        #Initializes the tile class. Takes the letter as a string, and the dictionary of letter values as arguments.
        self.letter = letter.upper()
        if self.letter in letter_values:
            self.score = letter_values[self.letter]
        else:
            self.score = 0

    def get_letter(self):
        #Returns the tile's letter (string).
        return self.letter

    def get_score(self):
        #Returns the tile's score value.
        return self.score

def test_Tile():
    t = Tile("A", LETTER_VALUES)
    assert type(t).__name__ == 'Tile'
    assert t.get_letter() == 'A'
    #assert type(t) == lib.scrabble.Tile 

class Bag:
    """
    Creates the bag of all tiles that will be available during the game. Contains 98 letters and two blank tiles.
    Takes no arguments to initialize.
    """
    def __init__(self):
        #Creates the bag full of game tiles, and calls the initialize_bag() method, which adds the default 100 tiles to the bag.
        #Takes no arguments.
        self.bag = []
        self.initialize_bag()

    def add_to_bag(self, tile, quantity):
        #Adds a certain quantity of a certain tile to the bag. Takes a tile and an integer quantity as arguments.
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        #Adds the intiial 100 tiles to the bag.
        global LETTER_VALUES
        self.add_to_bag(Tile("A", LETTER_VALUES), 9)
        self.add_to_bag(Tile("B", LETTER_VALUES), 2)
        self.add_to_bag(Tile("C", LETTER_VALUES), 2)
        self.add_to_bag(Tile("D", LETTER_VALUES), 4)
        self.add_to_bag(Tile("E", LETTER_VALUES), 12)
        self.add_to_bag(Tile("F", LETTER_VALUES), 2)
        self.add_to_bag(Tile("G", LETTER_VALUES), 3)
        self.add_to_bag(Tile("H", LETTER_VALUES), 2)
        self.add_to_bag(Tile("I", LETTER_VALUES), 9)
        self.add_to_bag(Tile("J", LETTER_VALUES), 9)
        self.add_to_bag(Tile("K", LETTER_VALUES), 1)
        self.add_to_bag(Tile("L", LETTER_VALUES), 4)
        self.add_to_bag(Tile("M", LETTER_VALUES), 2)
        self.add_to_bag(Tile("N", LETTER_VALUES), 6)
        self.add_to_bag(Tile("O", LETTER_VALUES), 8)
        self.add_to_bag(Tile("P", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Q", LETTER_VALUES), 1)
        self.add_to_bag(Tile("R", LETTER_VALUES), 6)
        self.add_to_bag(Tile("S", LETTER_VALUES), 4)
        self.add_to_bag(Tile("T", LETTER_VALUES), 6)
        self.add_to_bag(Tile("U", LETTER_VALUES), 4)
        self.add_to_bag(Tile("V", LETTER_VALUES), 2)
        self.add_to_bag(Tile("W", LETTER_VALUES), 2)
        self.add_to_bag(Tile("X", LETTER_VALUES), 1)
        self.add_to_bag(Tile("Y", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Z", LETTER_VALUES), 1)
        self.add_to_bag(Tile("#", LETTER_VALUES), 2)
        shuffle(self.bag)

    def take_from_bag(self):
        #Removes a tile from the bag and returns it to the user. This is used for replenishing the rack.
        return self.bag.pop()

    def get_remaining_tiles(self):
        #Returns the number of tiles left in the bag.
        return len(self.bag)

class Rack:
    """
    Creates each player's 'dock', or 'hand'. Allows players to add, remove and replenish the number of tiles in their hand.
    """
    def __init__(self, bag):
        #Initializes the player's rack/hand. Takes the bag from which the racks tiles will come as an argument.
        self.rack = []
        self.bag = bag
        self.initialize()

    def add_to_rack(self):
        #Takes a tile from the bag and adds it to the player's rack.
        self.rack.append(self.bag.take_from_bag())

    def initialize(self):
        #Adds the initial 7 tiles to the player's hand.
        for i in range(7):
            self.add_to_rack()

    def get_rack_str(self):
        #Displays the user's rack in string form.
        return ", ".join(str(item.get_letter()) for item in self.rack)

    def get_rack_arr(self):
        #Returns the rack as an array of tile instances
        return self.rack

    def remove_from_rack(self, tile):
        #Removes a tile from the rack (for example, when a tile is being played).
        self.rack.remove(tile)

    def get_rack_length(self):
        #Returns the number of tiles left in the rack.
        return len(self.rack)

    def replenish_rack(self):
        #Adds tiles to the rack after a turn such that the rack will have 7 tiles (assuming a proper number of tiles in the bag).
        while self.get_rack_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_rack()

class Player:
    """
    Creates an instance of a player. Initializes the player's rack, and allows you to set/get a player name.
    """
    def __init__(self, bag):
        #Intializes a player instance. Creates the player's rack by creating an instance of that class.
        #Takes the bag as an argument, in order to create the rack.
        self.name = ""
        self.rack = Rack(bag)
        self.score = 0

    def set_name(self, name):
        #Sets the player's name.
        self.name = name

    def get_name(self):
        #Gets the player's name.
        return self.name

    def get_rack_str(self):
        #Returns the player's rack.
        return self.rack.get_rack_str()

    def get_rack_arr(self):
        #Returns the player's rack in the form of an array.
        return self.rack.get_rack_arr()

    def increase_score(self, increase):
        #Increases the player's score by a certain amount. Takes the increase (int) as an argument and adds it to the score.
        self.score += increase

    def get_score(self):
        #Returns the player's score
        return self.score

class Board:
    """
    Creates the scrabble board.
    """
    def __init__(self):
        #Creates a 2-dimensional array that will serve as the board, as well as adds in the premium squares.
        self.board = [["   " for i in range(15)] for j in range(15)]
        self.add_premium_squares()
        self.board[7][7] = " * "

    def get_board(self):
        #Returns the board in string form.
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.board)
        for i in range(len(board)):
            if i < 10:
                board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    def add_premium_squares(self):
        #Adds all of the premium squares that influence the word's score.
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TRIPLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TWS"
        for coordinate in TRIPLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TLS"
        for coordinate in DOUBLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DWS"
        for coordinate in DOUBLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DLS"

    def place_word(self, word, location, direction, player):
        #Allows you to play words, assuming that they have already been confirmed as valid.
        global premium_spots
        premium_spots = []
        direction = direction.lower()
        word = word.upper()

        #Places the word going rightwards
        if direction.lower() == "right":
            for i in range(len(word)):
                if self.board[location[0]][location[1]+i] != "   ":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                self.board[location[0]][location[1]+i] = " " + word[i] + " "

        #Places the word going downwards
        elif direction.lower() == "down":
            for i in range(len(word)):
                if self.board[location[0]][location[1]+i] != "   ":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                self.board[location[0]+i][location[1]] = " " + word[i] + " "

        #Removes tiles from player's rack and replaces them with tiles from the bag.
        for letter in word:
            for tile in player.get_rack_arr():
                if tile.get_letter() == letter:
                    player.rack.remove_from_rack(tile)
        player.rack.replenish_rack()

    def board_array(self):
        #Returns the 2-dimensional board array.
        return self.board

class Word:
    def __init__(self, word, location, player, direction, board):
        self.word = word.upper()
        self.location = location
        self.player = player
        self.direction = direction.lower()
        self.board = board

    def check_word(self):
        #Checks the word to make sure that it is in the dictionary, and that the location falls within bounds.
        #Also controls the overlapping of words.
        global round_number, players
        word_score = 0
        global dictionary 
        if "dictionary" not in globals():
            dictionary = open("dic.txt").read().splitlines()

        current_board_ltr = ""
        needed_tiles = ""
        blank_tile_val = ""

        #Assuming that the player is not skipping the turn:
        if self.word != "":

            #Allows for players to declare the value of a blank tile.
            if "#" in self.word:
                while len(blank_tile_val) != 1:
                    blank_tile_val = get_response("Please enter the letter value of the blank tile: ")
                self.word = self.word[:word.index("#")] + blank_tile_val.upper() + self.word[(word.index("#")+1):]

            #Reads in the board's current values under where the word that is being played will go. Raises an error if the direction is not valid.
            if self.direction == "right":
                for i in range(len(self.word)):
                    if self.board[self.location[0]][self.location[1]+i][1] == " " or self.board[self.location[0]][self.location[1]+i] == "TLS" or self.board[self.location[0]][self.location[1]+i] == "TWS" or self.board[self.location[0]][self.location[1]+i] == "DLS" or self.board[self.location[0]][self.location[1]+i] == "DWS" or self.board[self.location[0]][self.location[1]+i][1] == "*":
                        current_board_ltr += " "
                    else:
                        current_board_ltr += self.board[self.location[0]][self.location[1]+i][1]
            elif self.direction == "down":
                for i in range(len(self.word)):
                    if self.board[self.location[0]+i][self.location[1]] == "   " or self.board[self.location[0]+i][self.location[1]] == "TLS" or self.board[self.location[0]+i][self.location[1]] == "TWS" or self.board[self.location[0]+i][self.location[1]] == "DLS" or self.board[self.location[0]+i][self.location[1]] == "DWS" or self.board[self.location[0]+i][self.location[1]] == " * ":
                        current_board_ltr += " "
                    else:
                        current_board_ltr += self.board[self.location[0]+i][self.location[1]][1]
            else:
                return "Error: please enter a valid direction."

            #Raises an error if the word being played is not in the official scrabble dictionary (dic.txt).
            if self.word not in dictionary:
                return "Please enter a valid dictionary word.\n"

            #Ensures that the words overlap correctly. If there are conflicting letters between the current board and the word being played, raises an error.
            for i in range(len(self.word)):
                if current_board_ltr[i] == " ":
                    needed_tiles += self.word[i]
                elif current_board_ltr[i] != self.word[i]:
                    display("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                    return "The letters do not overlap correctly, please choose another word."

            #If there is a blank tile, remove it's given value from the tiles needed to play the word.
            if blank_tile_val != "":
                needed_tiles = needed_tiles[needed_tiles.index(blank_tile_val):] + needed_tiles[:needed_tiles.index(blank_tile_val)]

            #Ensures that the word will be connected to other words on the playing board.
            if (round_number != 1 or (round_number == 1 and players[0] != self.player)) and current_board_ltr == " " * len(self.word):
                display("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                return "Please connect the word to a previously played letter."

            #Raises an error if the player does not have the correct tiles to play the word.
            for letter in needed_tiles:
                if letter not in self.player.get_rack_str() or self.player.get_rack_str().count(letter) < needed_tiles.count(letter):
                    return "You do not have the tiles for this word\n"

            #Raises an error if the location of the word will be out of bounds.
            if self.location[0] > 14 or self.location[1] > 14 or self.location[0] < 0 or self.location[1] < 0 or (self.direction == "down" and (self.location[0]+len(self.word)-1) > 14) or (self.direction == "right" and (self.location[1]+len(self.word)-1) > 14):
                return "Location out of bounds.\n"

            #Ensures that first turn of the game will have the word placed at (7,7).
            if round_number == 1 and players[0] == self.player and self.location != [7,7]:
                return "The first turn must begin at location (7, 7).\n"
            return True

        #If the user IS skipping the turn, confirm. If the user replies with "Y", skip the player's turn. Otherwise, allow the user to enter another word.
        else:
            if get_response("Are you sure you would like to skip your turn? (y/n)").upper() == "Y":
                if round_number == 1 and players[0] == self.player:
                    return "Please do not skip the first turn. Please enter a word."
                return True
            else:
                return "Please enter a word."

    def calculate_word_score(self):
        #Calculates the score of a word, allowing for the impact by premium squares.
        global LETTER_VALUES, premium_spots
        word_score = 0
        for letter in self.word:
            for spot in premium_spots:
                if letter == spot[0]:
                    if spot[1] == "TLS":
                        word_score += LETTER_VALUES[letter] * 2
                    elif spot[1] == "DLS":
                        word_score += LETTER_VALUES[letter]
            word_score += LETTER_VALUES[letter]
        for spot in premium_spots:
            if spot[1] == "TWS":
                word_score *= 3
            elif spot[1] == "DWS":
                word_score *= 2
        self.player.increase_score(word_score)

    def set_word(self, word):
        self.word = word.upper()

    def set_location(self, location):
        self.location = location

    def set_direction(self, direction):
        self.direction = direction

    def get_word(self):
        return self.word

def turn(player, board, bag):
    #Begins a turn, by displaying the current board, getting the information to play a turn, and creates a recursive loop to allow the next person to play.
    global round_number, players, skipped_turns

    #If the number of skipped turns is less than 6 and a row, and there are either tiles in the bag, or no players have run out of tiles, play the turn.
    #Otherwise, end the game.
    if (skipped_turns < 6) or (player.rack.get_rack_length() == 0 and bag.get_remaining_tiles() == 0):

        #Displays whose turn it is, the current board, and the player's rack.
        status = "\nRound " + str(round_number) + ": " + player.get_name() + "'s turn \n"
        status += board.get_board()
        status += "\n" + player.get_name() + "'s Letter Rack: " + player.get_rack_str()
        display(status)
        #Gets information in order to play a word.
        # !! ?? bunch up for gui
        word_to_play, col, row, direction = get_response("Word to play: ", \
                "Column number: ", \
                "Row number: ", "Direction of word (right or down): " )
        location = []
        if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
            location = [-1, -1]
        else:
            location = [int(row), int(col)]

        word = Word(word_to_play, location, player, direction, board.board_array())

        #If the first word throws an error, creates a recursive loop until the information is given correctly.
        checked_result = word.check_word()
        while checked_result != True:
            display(checked_result)
            #!! ??conditional here, based on ui value, i.e. bunch up req/resp if GUI
            word_to_play, col, row, direction = get_response("Word to play: ", \
                "Column number: ", \
                "Row number: ", "Direction of word (right or down): " )
            word.set_word(word_to_play)
            location = []
            if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                location = [-1, -1]
            else:
                word.set_location([int(row), int(col)])
                location = [int(row), int(col)]
            word.set_direction(direction)
            checked = word.check_word()

        #If the user has confirmed that they would like to skip their turn, skip it.
        #Otherwise, plays the correct word and prints the board.
        if word.get_word() == "":
            display("Your turn has been skipped.")
            skipped_turns += 1
        else:
            board.place_word(word_to_play, location, direction, player)
            word.calculate_word_score()
            skipped_turns = 0

        #Prints the current player's score
        display("\n" + player.get_name() + "'s score is: " + str(player.get_score()))

        #Gets the next player.
        if players.index(player) != (len(players)-1):
            player = players[players.index(player)+1]
        else:
            player = players[0]
            round_number += 1

        #Recursively calls the function in order to play the next turn.
        turn(player, board, bag)

    #If the number of skipped turns is over 6 or the bag has both run out of tiles and a player is out of tiles, end the game.
    else:
        end_game()
# IN: text to display - can be string or tuple
#     if input is needed - can be string or tuple; if tuple, index matches with text typle
# OUT: values that user inputted; string if single value, list if not
#
# If type of data is string
#   show_response
# Elif type of data is list or tuple
#   iterate through each entry
#   
def get_response(*text_strings):
    ret_vals = []
    for text in text_strings:
        if type(text) is str: 
            if ( ui == "tui" ):
                retval = None
                while retval is None:
                    retval = str(input(text)) 
            elif ( ui == "gui" ):
                pass
            ret_vals.append(retval)
        else:
            print("ERROR: display value " + str(text) + " is not text")
    if len(ret_vals) == 1:
        return ret_vals[0]
    else:
        return ret_vals

# IN: text to display,
#     if input is required
# OUT: response (string)
def display(text):
    if ( ui == "tui" ):
        print(text)
    elif ( ui == "gui" ):
        txt_no_resp += text

def start_game(mode):
    #Begins the game and calls the turn function.
    global round_number, players, skipped_turns, ui, txt_no_resp # text_no_resp if no respnse from user needed
    ui = mode 
    board = Board()
    bag = Bag()

    #Welcomes players to the game and allows players to choose their name.
    num_of_players=4  #Initially assume max number of players
    num_of_players_min=2
    display("\nWelcome to Scrabble! A minimum of 2 and a maximum of 4 players are needed.")
    players = []
    i = 0
    while i < num_of_players:
        name_taken = False
        player_name = get_response( "Please enter player " + str(i+1) + "'s name. Enter a blank name if there are no more players (need at least 2 players, maximum 4 players). ")
        #print ("Got " + str(player_name))
        if player_name is not None and len(player_name) != 0:    
            if i > 0:
                for j in range(i): # Check if requested name already used
                    #print(" j " + str(j) + ", name " + str(players[j].get_name() ) )
                    if ( player_name == players[j].get_name() ):
                         display("Name " + str(player_name) + " already taken.  Please choose another name.")
                         name_taken = True
            if name_taken is True:  # If taken, repeat while loop, i.e. is i not incremented
                continue
            players.append(Player(bag))  # If all conditions OK, set up user with bag
            players[i].set_name(player_name)
            i = i+1
        else:  
            if i < num_of_players_min:
                display("Not enough players.")
            else:
                break  #stop collecting info if player name is blank, i.e. no more players.

    #Sets the default value of global variables.
    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    #Forces the game to end when the bag runs out of tiles.
    global players
    highest_score = 0
    winning_player = ""
    for player in players:
        if player.get_score > highest_score:
            highest_score = player.get_score()
            winning_player = player.get_name()
    display("The game is over! " + winning_player + ", you have won!")

    response = get_response("\nWould you like to play again? (y/n)")
    if response.upper() == "Y":
        start_game(ui)

#start_game()
