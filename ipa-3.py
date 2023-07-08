
def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph.get(from_member, {}).get("following", []):
        if from_member in social_graph.get(to_member, {}).get("following", []):
            return "friends"
        else:
            return "follower"
    elif from_member in social_graph.get(to_member, {}).get("following", []):
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    # Check rows
    for row in board:
        if all(cell == row[0] and cell for cell in row):
            return row[0]

    # Check columns
    for col in range(len(board)):
        if all(board[row][col] == board[0][col] and board[row][col] for row in range(len(board))):
            return board[0][col]

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] for i in range(len(board))):
        return board[0][0]

    if all(board[i][len(board) - 1 - i] == board[0][len(board) - 1] and board[i][len(board) - 1 - i] for i in range(len(board))):
        return board[0][len(board) - 1]

    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    # Check if the first_stop and second_stop are in the route_map
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]['travel_time_mins']

    # Iterate over each leg in the route_map
    for leg in route_map:
        # Check if the first_stop matches the starting point of the leg
        if leg[0] == first_stop:
            # Check if the second_stop matches the ending point of the leg
            if leg[1] == second_stop:
                return route_map[leg]['travel_time_mins']

    # If no direct leg is found, return -1 to indicate an invalid route
    return "INVALID"
