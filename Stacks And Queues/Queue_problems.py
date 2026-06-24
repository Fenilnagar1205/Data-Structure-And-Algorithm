# Example 3 — Print Queue Simulation
# Problem: Simulate a printer queue. Jobs are processed in the order they arrive.

from collections import deque

def printer_queue(jobs):
    queue = deque()

    # Add all jobs to queue
    for job in jobs:
        queue.append(job)
        print(f"Added to queue: {job}")

    print("\nProcessing:")
    while len(queue) > 0:
        current = queue.popleft()    # first job gets processed first
        print(f"Printing: {current}")

printer_queue(["doc1", "photo", "report"])