import streamlit as st

# Initialize session state for commands and index
if 'commands' not in st.session_state:
    st.session_state.commands = []
if 'index' not in st.session_state:
    st.session_state.index = 0

# Title and instructions
st.title('Algorithm Command List')
st.markdown("""
    Enter algorithm steps in the input box, and volunteers will try to execute each one.
    You can add, remove, and navigate through the list of commands below.
""")

# Command input field
command_input = st.text_input('Enter a new command')

# Add command button
if st.button('Add Command'):
    if command_input:
        st.session_state.commands.append(command_input)
        st.session_state.index = len(st.session_state.commands) - 1  # Go to the last command
        st.success(f'Command "{command_input}" added!')
    else:
        st.warning('Please enter a command.')

# Display the current list of commands
st.subheader('Commands List:')
if st.session_state.commands:
    st.write("\n".join([f"{idx + 1}. {cmd}" for idx, cmd in enumerate(st.session_state.commands)]))
else:
    st.write("No commands yet! Please add some above.")

# Show current command (if any)
if st.session_state.commands:
    st.subheader('Current Command:')
    st.write(st.session_state.commands[st.session_state.index])

    # Buttons for navigation
    col1, col2, col3 = st.columns([1, 2, 1])  # Split the screen into columns for large buttons
    with col1:
        if st.button('Previous Command', key='prev'):
            if st.session_state.index > 0:
                st.session_state.index -= 1
    with col2:
        if st.button('Next Command', key='next'):
            if st.session_state.index < len(st.session_state.commands) - 1:
                st.session_state.index += 1
    with col3:
        if st.button('Clear All Commands', key='clear'):
            st.session_state.commands.clear()
            st.session_state.index = 0
            st.success('All commands cleared.')

    # Command removal (only show if there are commands)
    if len(st.session_state.commands) > 1:
        command_to_remove = st.selectbox('Select a command to remove', st.session_state.commands)
        if st.button('Remove Selected Command'):
            st.session_state.commands.remove(command_to_remove)
            st.session_state.index = min(st.session_state.index, len(st.session_state.commands) - 1)  # Stay within range
            st.success(f'Command "{command_to_remove}" removed.')

else:
    st.write("Add some commands to get started!")
