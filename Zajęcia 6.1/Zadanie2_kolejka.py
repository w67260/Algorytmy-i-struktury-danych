from collections import deque

def hot_potato_game(players, num_operations):
    queue = deque(players)
    while len(queue) > 1:
        for _ in range(num_operations):
            player = queue.popleft()
            queue.append(player)
        eliminated_player = queue.popleft()
        print(f"Player {eliminated_player} has been eliminated.")
    winner = queue[0]
    print(f"The winner is: {winner}")


players = ['Konrad', 'Wojciech', 'Barbara', 'Kasia', 'Ewa', 'Franek']
num_operations = 3
hot_potato_game(players, num_operations)