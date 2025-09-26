# Stack helper + the two practical scenarios (complete code)
class Stack:
    def __init__(self):
        self._data = []
    def push(self, item):
        self._data.append(item)
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()
    def top(self):
        return self._data[-1] if self._data else None
    def contents(self):
        return list(self._data)  # shallow copy
    def __repr__(self):
        return f"Stack({self._data})"

# Scenario 1: MoMo pushes ["Enter PIN", "Choose Service", "Confirm"]. Undo twice.
momo_stack = Stack()
momo_actions = ["Enter PIN", "Choose Service", "Confirm"]
for a in momo_actions:
    momo_stack.push(a)

# Undo twice (two pops)
undo1 = momo_stack.pop()  # removes "Confirm"
undo2 = momo_stack.pop()  # removes "Choose Service"
momo_remaining = momo_stack.contents()
momo_top = momo_stack.top()

# Scenario 2: UR student pushes ["Revise1", "Revise2", "Revise3"]. Pop one.
ur_stack = Stack()
ur_actions = ["Revise1", "Revise2", "Revise3"]
for a in ur_actions:
    ur_stack.push(a)

popped = ur_stack.pop()  # removes "Revise3"
ur_remaining = ur_stack.contents()
ur_top = ur_stack.top()

# Print results (this is what I included in the screenshot)
print("Scenario 1 - MoMo remaining:", momo_remaining, "Top:", momo_top)
print("Scenario 2 - UR remaining:", ur_remaining, "Top:", ur_top)
def reverse_with_stack(s):
    stack = []                       # Step 1: empty stack
    for ch in s:
        stack.append(ch)             # Step 2: push each character onto stack
    reversed_chars = []              # Step 3: buffer for popped chars
    while stack:
        reversed_chars.append(stack.pop())  # Step 4: pop => gets characters in reverse
    return ''.join(reversed_chars)   # Step 5: join into final reversed string

# Example:
print(reverse_with_stack("RWANDA"))  # => "ADNAWR"
from collections import deque

def simulate_voter_queue(arrivals, serve_count):
    q = deque()                     # Step 1: initialize queue
    # Step 2: enqueue arrivals
    for voter in arrivals:
        q.append(voter)             # enqueue (arrive -> back of queue)
    served = []
    # Step 3: serve by dequeuing from front
    for _ in range(min(serve_count, len(q))):
        current = q.popleft()       # dequeue front -> serve this voter
        served.append(current)
    # After serving, 'served' holds served in order, 'q' holds remaining queue
    return served, list(q)

# Example:
arrivals = ["Voter1","Voter2","Voter3","Voter4"]
served, remaining = simulate_voter_queue(arrivals, 2)
# served => ["Voter1","Voter2"]  (order preserved), remaining => ["Voter3","Voter4"]
