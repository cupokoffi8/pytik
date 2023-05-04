import streamlit as st
import random 

#Setup page title 
st.set_page_config(page_title="PyTik", page_icon="🎟")

# Initialize the board
board = ['-'] * 9

# Define the layout of the board
board_layout = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Define the players
players = ['X', 'O']

# Define the initial player
current_player = players[0]

# Define the function to draw the board
def draw_board():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button(board[0], key="button"+str(random.random()), on_click=lambda: update_board(0))
    with col2:
        st.button(board[1], key="button"+str(random.random()), on_click=lambda: update_board(1))
    with col3:
        st.button(board[2], key="button"+str(random.random()), on_click=lambda: update_board(2))
    with col1:
        st.button(board[3], key="button"+str(random.random()), on_click=lambda: update_board(3))
    with col2:
        st.button(board[4], key="button"+str(random.random()), on_click=lambda: update_board(4))
    with col3:
        st.button(board[5], key="button"+str(random.random()), on_click=lambda: update_board(5))
    with col1:
        st.button(board[6], key="button"+str(random.random()), on_click=lambda: update_board(6))
    with col2:
        st.button(board[7], key="button"+str(random.random()), on_click=lambda: update_board(7))
    with col3:
        st.button(board[8], key="button"+str(random.random()), on_click=lambda: update_board(8))
 

def check_game_over():
    # check for horizontal wins
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    # check for vertical wins
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    # check for diagonal wins
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    # check for a tie
    if " " not in board:
        return "TIE"
    # if there is no winner and the game is not a tie, return False
    return False 

# Define the function to update the board
def update_board(button_id): 
    global board, current_player

    st.title("Tic Tac Toe")
    st.header("Continue playing on the top board")

    # check if the button has already been clicked
    if board[button_id] != "-":
        st.warning("This cell has already been filled!")
        return 

    # update the board with the current player's symbol
    board[button_id] = current_player

    # switch to the other player
    current_player = "X" if current_player == "O" else "O"

    # check for a win or a tie
    game_over = check_game_over()

    # redraw the board
    draw_board()

    # display a message if the game is over
    if game_over:
        st.write("Current Player: ", current_player)
        if game_over == "TIE":
            st.warning("The game is a tie!")
        else:
            st.success(f"Player {game_over} wins!")
        # disable all the buttons
        for i in range(9):
            st.session_state[f"button_{i}_disabled"] = True

    # Large <br /> element
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")


def main():

    st.title("Tic Tac Toe")
    # Display the current player
    st.write("Current Player: ", current_player)

    # Initialize the session state variables for the buttons
    for i in range(9):
        st.session_state[f"button_{i}_disabled"] = False

    # Draw the board
    draw_board() 


if __name__ == "__main__":
    main()

