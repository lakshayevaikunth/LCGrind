import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # First, sort meetings based on their start times to process them in chronological order.
        meetings.sort()

        # Initialize a list of all available rooms. Each room is initially available.
        available = [i for i in range(n)]

        # Priority queue (min-heap) for rooms that are currently in use.
        # It stores tuples (end time of the meeting, room index).
        used = []

        # Array to count the number of times each room is booked.
        count = [0] * n

        # Process each meeting one by one.
        for start, end in meetings:
            # Free up rooms that have finished their meetings before the current meeting starts.
            while used and start >= used[0][0]:
                # Pop rooms from the heap that are now free.
                _, room = heapq.heappop(used)
                # Add the room back to the list of available rooms.
                heapq.heappush(available, room)

            # If no rooms are available, wait for the next room to free up.
            if not available:
                # Pop the room that will free up the soonest.
                end_time, room = heapq.heappop(used)
                # Adjust the current meeting's end time by adding the duration of the meeting.
                end = end_time + (end - start)
                # Since this room becomes available again, reinsert it into the available heap.
                heapq.heappush(available, room)

            # Allocate the next available room (the smallest index room, thanks to the nature of heaps).
            room = heapq.heappop(available)
            # Book the room and schedule its next free time.
            heapq.heappush(used, (end, room))
            # Increment the count for this particular room as it gets used one more time.
            count[room] += 1

        # Return the index of the room that was booked the most times.
        # max(count) finds the highest booking count, index() finds the first room with this count.
        return count.index(max(count))
