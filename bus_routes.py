# BFS with set intersection - Intutive solution 
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        #handle edge case
        if source == target:
            return 0
        #convert every route to set
        routes = [set(route) for route in routes]
        #find all buses with source
        source_buses = {i for i, route in enumerate(routes) if source in route}
       
        #initialize queue with every bus source_buses
        queue = deque([(bus, 1) for bus in source_buses])
        #add every source bus to seen
        seen = set(source_buses)

        #run BFS
        while queue:
            current_bus, num_buses = queue.popleft()
            if target in routes[current_bus]:
                return num_buses

            #check all buses for a transfer
            for next_bus, route in enumerate(routes):
                #if bus not seen and there is an intersection between it and the current bus, add to queue
                if next_bus not in seen and routes[current_bus] & route:
                    seen.add(next_bus)
                    queue.append((next_bus, num_buses + 1))
        return -1


# BFS with hashmap - Efficient

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        # Step 1: Create a mapping of each stop to the buses that stop at it
        stop_to_buses = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus)

        # Step 2: Use BFS to explore the routes
        queue = deque([(source, 0)])  # Initialize the queue with the source stop and the number of buses taken
        visited_stops = set([source])  # Keep track of visited stops
        visited_buses = set()  # Keep track of visited buses

        # Step 3: BFS traversal
        while queue:
            stop, buses_taken = queue.popleft()  # Get the current stop and the number of buses taken
            if stop == target:  # If we reach the target stop, return the number of buses taken
                return buses_taken

            # Explore buses that stop at the current stop
            for bus in stop_to_buses[stop]:
                if bus not in visited_buses:  # If the bus hasn't been visited yet
                    visited_buses.add(bus)  # Mark the bus as visited
                    for next_stop in routes[bus]:  # Explore stops of the current bus
                        if next_stop not in visited_stops:  # If the stop hasn't been visited
                            visited_stops.add(next_stop)  # Mark the stop as visited
                            queue.append((next_stop, buses_taken + 1))  # Add the next stop to the queue with updated number of buses taken

        return -1  # If the target stop is not reachable, return -1


            
        
    
        
