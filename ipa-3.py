
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

legs = {
    ('a0', 'a1'): {
        'travel_time_mins': 2
    },
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'a3'): {
        'travel_time_mins': 34
    },
    ('a3', 'a4'): {
        'travel_time_mins': 145123
    },
    ('a4', 'a5'): {
        'travel_time_mins': 1239
    },
    ('a5', 'a6'): {
        'travel_time_mins': 1935
    },
    ('a6', 'a7'): {
        'travel_time_mins': 1891345
    },
    ('a7', 'a8'): {
        'travel_time_mins': 789253
    },
    ('a8', 'a9'): {
        'travel_time_mins': 78234
    },
    ('a9', 'a10'): {
        'travel_time_mins': 432678
    },
    ('a10', 'a0'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    total_time = 0

    while current_stop != second_stop:
        next_stop = None
        travel_time = None

        for leg, details in route_map.items():
            if leg[0] == current_stop:
                next_stop = leg[1]
                travel_time = details['travel_time_mins']
                break

        if next_stop is None:
            raise ValueError("No valid route found between the stops.")

        total_time += travel_time

        current_stop = next_stop
    return total_time


