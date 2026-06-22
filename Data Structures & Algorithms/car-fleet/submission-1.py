class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        stack = []
        pairs = sorted(pairs, key=lambda x:x[0], reverse=True)
        # pairs has cars closer to target at start of array
        for pos, speed in pairs:
            current_arrival = float(target - pos) / speed
            stack.append(current_arrival)
            if len(stack) >= 2:
                # see if we collide
                car_ahead_arrival = stack[-2]
                if current_arrival <= car_ahead_arrival:
                    # we have a collision! keep the lower arrival time in stack! remove the faster car (current)
                    stack.pop() # removes the just added current_arrival
                
        return len(stack) # we only kept the slow ass fleets
