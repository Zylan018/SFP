import streamlit as st
import random

# Initialize session state
if "pacman_pos" not in st.session_state:
    st.session_state.pacman_pos = [1, 1]
if "dots" not in st.session_state:
    st.session_state.dots = [[1, 3], [2, 2], [3, 1], [3, 3], [4,2], [5,3]]
if "score" not in st.session_state:
    st.session_state.score = 0

# Game grid
grid_size = 10
walls = [[0, 2], [2, 0], [4, 2]]  # Static walls

# Layout
st.title("🟡 Mini Pac-Man (Streamlit Edition)")

# Movement logic
def move(dx, dy):
    new_x = st.session_state.pacman_pos[0] + dx
    new_y = st.session_state.pacman_pos[1] + dy
    if 0 <= new_x < grid_size and 0 <= new_y < grid_size and [new_x, new_y] not in walls:
        st.session_state.pacman_pos = [new_x, new_y]
        if [new_x, new_y] in st.session_state.dots:
            st.session_state.dots.remove([new_x, new_y])
            st.session_state.score += 10

# Control buttons
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬆️"):
        move(-1, 0)
with col1:
    if st.button("⬅️"):
        move(0, -1)
with col3:
    if st.button("➡️"):
        move(0, 1)
with col2:
    if st.button("⬇️"):
        move(1, 0)

# Draw the grid
for i in range(grid_size):
    row = ""
    for j in range(grid_size):
        if [i, j] == st.session_state.pacman_pos:
            row += "🟡 "
        elif [i, j] in walls:
            row += "🟥 "
        elif [i, j] in st.session_state.dots:
            row += "• "
        else:
            row += "⬛ "
    st.markdown(row)

# Score display
st.success(f"Score: {st.session_state.score}")

# Reset button
if st.button("Restart Game"):
    st.session_state.pacman_pos = [1, 1]
    st.session_state.dots = [[1, 3], [2, 2], [3, 1], [3, 3]]
    st.session_state.score = 0
