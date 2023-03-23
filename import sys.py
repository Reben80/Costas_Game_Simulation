import random

def calculate_slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] != p1[0] else None

def is_within_grid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def is_smart_move(point, current_points, distinct_slopes):
    new_xs = [p[0] for p in current_points + [point]]
    new_ys = [p[1] for p in current_points + [point]]

    if len(set(new_xs)) < len(new_xs) or len(set(new_ys)) < len(new_ys):
        return False

    for p in current_points:
        slope = calculate_slope(p, point)
        if slope in distinct_slopes:
            return False

    return True

def get_next_move(current_points, n, m, distinct_slopes):
    available_points = [(x, y) for x in range(n) for y in range(m) if (x, y) not in current_points]

    if not available_points:
        return None

    smart_points = [point for point in available_points if is_smart_move(point, current_points, distinct_slopes)]

    if smart_points:
        return random.choice(smart_points)
    else:
        return None

def run_simulation(first_move, n, m, num_simulations):
    player1_wins = 0
    player2_wins = 0

    for sim in range(num_simulations):
        distinct_points = [first_move]
        distinct_slopes = []

        while True:
            point = get_next_move(distinct_points, n, m, distinct_slopes)
            if point is None:
                break

            distinct_points.append(point)

            if len(distinct_points) > 1:
                for i in range(len(distinct_points) - 1):
                    slope = calculate_slope(distinct_points[i], point)
                    if slope in distinct_slopes:
                        break
                    distinct_slopes.append(slope)

        if len(distinct_points) % 2 == 1:
            player1_wins += 1
        else:
            player2_wins += 1

    return player1_wins, player2_wins

def main():
    n, m = 4, 4
    num_simulations = 100000
    first_move = (1, 1)

    # Check if the first move is within a specific range of the grid
    if first_move[0] > n//2 or first_move[1] > m//2:
        print("Invalid first move. Please choose a point within the first half of the grid.")
        return

    player1_wins, player2_wins = run_simulation(first_move, n, m, num_simulations)

    player1_percentage = (player1_wins / num_simulations) * 100
    player2_percentage = (player2_wins / num_simulations) * 100

    print(f"Player 1 won {player1_percentage}% of the games.")
    print(f"Player 2 won {player2_percentage}% of the games.")


if __name__ == "__main__":
    main()
