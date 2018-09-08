def handle_keys(user_input):
    key_char = user_input.char

    # Movement keys
    if user_input.key == 'UP' or key_char == 'k':
        return {'move': (0, -1)}
    elif user_input.key == 'DOWN' or key_char == 'k':
        return {'move': (0, 1)}
    elif user_input.key == 'LEFT' or key_char == 'h':
        return {'move': (-1, 0)}
    elif user_input.key == 'RIGHT' or key_char == 'l':
        return {'move': (1, 0)}
    elif key_char == 'y' or (user_input.key == 'UP' and user_input.key == 'LEFT'):
        return {'move': (-1, -1)}
    elif key_char == 'u' or (user_input.key == 'UP' and user_input.key == 'RIGHT'):
        return {'move': (1, -1)}
    elif key_char == 'b' or (user_input.key == 'DOWN' and user_input.key == 'LEFT'):
        return {'move': (-1, 1)}
    elif key_char == 'n' or (user_input.key == 'DOWN' and user_input.key == 'RIGHT'):
        return {'move': (1, 1)}

    if user_input.key == 'ENTER' and user_input.alt:
        # ALt+Enter: toggle full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exits the game
        return {'exit': True}
    
    #No key was pressed
    return {}