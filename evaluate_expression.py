import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Use a priority queue to store the end times of meetings currently being scheduled
    meeting_rooms = []

    # Schedule the first meeting
    heapq.heappush(meeting_rooms, intervals[0][1])

    for i in range(1, len(intervals)):
        # Check if the current meeting starts after the earliest ending meeting
        if intervals[i][0] >= meeting_rooms[0]:
            heapq.heappop(meeting_rooms)

        # Schedule the current meeting (either in the same room or a new room)
        heapq.heappush(meeting_rooms, intervals[i][1])

    return len(meeting_rooms)

# Test cases
print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # Output: 2
print(min_meeting_rooms([[7, 10], [2, 4]]))  # Output: 1
