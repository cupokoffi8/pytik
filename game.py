import streamlit as st

# Initialize the board with empty cells
board = [''] * 9

# Define the players
players = ['Red', 'Blue']

# Initialize the player index and turn counter
player_idx = 0
turn = 0

# Define the function to update the board when a button is clicked
def update_board(idx):
    global player_idx, turn
    board[idx] = players[player_idx]
    button_labels[idx] = players[player_idx]
    player_idx = (player_idx + 1) % 2
    turn += 1

# Define the button labels
button_labels = [''] * 9

# Create the buttons and display the board
col1, col2, col3 = st.columns(3)
for i in range(3):
    with col1:
        button_labels[i] = st.button('', key=f'button_{i}')
    with col2:
        button_labels[i+3] = st.button('', key=f'button_{i+3}')
    with col3:
        button_labels[i+6] = st.button('', key=f'button_{i+6}')

# Wait for a button to be clicked and update the board
while turn < 9:
    clicked = False
    for i in range(9):
        if button_labels[i]:
            update_board(i)
            clicked = True
            break
    if clicked:
        break

# Display the final board
col1, col2, col3 = st.columns(3)
for i in range(3):
    with col1:
        st.button(button_labels[i], key=f'button_{i}')
    with col2:
        st.button(button_labels[i+3], key=f'button_{i+3}')
    with col3:
        st.button(button_labels[i+6], key=f'button_{i+6}')
