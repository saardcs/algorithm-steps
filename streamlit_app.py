import streamlit as st

# Initialize the session state for command list and index
if 'commands' not in st.session_state:
    st.session_state.commands = []
if 'index' not in st.session_state:
    st.session_state.index = 0

# Title and description
st.title('Algorithm Command List')
st.write("Create an algorithm, type in the commands, and volunteers will try to execute them.")

# Command input field
command_input = st.text_input('Enter a command')

# Add command button
if st.button('Add Command'):
    if command_input:
        st.session_state.commands.append(command_input)
        st.session_state.index = 0  # Reset to show the first command
        st.success(f'Command "{command_input}" added to the list!')
    else:
        st.warning('Please enter a valid command.')

# Display the current list of commands
st.subheader('Commands List:')
for idx, command in enumerate(st.session_state.commands):
    st.write(f'{idx + 1}. {command}')

# Show the current command (one by one)
if st.session_state.commands:
    st.subheader('Current Command:')
    st.write(st.session_state.commands[st.session_state.index])

    # Next command button
    if st.button('Next Command') and st.session_state.index < len(st.session_state.commands) - 1:
        st.session_state.index += 1

    # Previous command button
    if st.button('Previous Command') and st.session_state.index > 0:
        st.session_state.index -= 1
else:
    st.write("No commands in the list yet. Add some commands above.")

# Option to clear the command list
if st.button('Clear All Commands'):
    st.session_state.commands.clear()
    st.session_state.index = 0
    st.success('All commands cleared.')

# Option to remove a specific command from the list
command_to_remove = st.selectbox('Select a command to remove', options=st.session_state.commands, index=-1)
if st.button('Remove Selected Command') and command_to_remove:
    st.session_state.commands.remove(command_to_remove)
    st.session_state.index = 0  # Reset to show the first command
    st.success(f'Command "{command_to_remove}" removed from the list.')
