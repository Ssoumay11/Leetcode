class Solution:
    def carFleet(self, target, position, speed):
        
        cars = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))

        # Closest to target first
        cars.sort(reverse=True)

        stack = []

        for pos, time in cars:

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)