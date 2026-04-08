class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for pos, speed in cars:
            time = (target - pos)/speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #time of the previous one is shorter
                stack.pop() #decrease car fleet
        
        return len(stack)

