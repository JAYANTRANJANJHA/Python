from collections import deque

def water_jug_bfs(jug1, jug2, target):
    # Queue for BFS, storing state and path
    queue = deque([(0, 0, [])])
    visited = set()
    
    print("Steps to reach the solution:")
    
    while queue:
        x, y, path = queue.popleft()
        
        # If state already visited, skip
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        current_path = path + [(x, y)]
        
        print(f"Jug1: {x} | Jug2: {y}")
        
        # If target is reached
        if x == target or y == target:
            print("\nReached the target!")
            print("Path to solution:")
            for step, state in enumerate(current_path):
                print(f"Step {step+1}: Jug1 = {state[0]}, Jug2 = {state[1]}")
            return True

        # Generate all possible next states
        # 1. Fill Jug1
        if (jug1, y) not in visited:
            queue.append((jug1, y, current_path))
            
        # 2. Fill Jug2
        if (x, jug2) not in visited:
            queue.append((x, jug2, current_path))
            
        # 3. Empty Jug1
        if (0, y) not in visited:
            queue.append((0, y, current_path))
            
        # 4. Empty Jug2
        if (x, 0) not in visited:
            queue.append((x, 0, current_path))
            
        # 5. Pour Jug1 → Jug2
        pour = min(x, jug2 - y)
        if (x - pour, y + pour) not in visited:
            queue.append((x - pour, y + pour, current_path))
            
        # 6. Pour Jug2 → Jug1
        pour = min(y, jug1 - x)
        if (x + pour, y - pour) not in visited:
            queue.append((x + pour, y - pour, current_path))
            
    print("No solution possible.")
    return False

# Example: Jug1 = 4L, Jug2 = 3L, Target = 2L
water_jug_bfs(4, 3, 2)
