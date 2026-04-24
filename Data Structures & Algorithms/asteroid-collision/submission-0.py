class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroid_stack = []

        for asteroid_size in asteroids:
            while asteroid_stack and asteroid_size < 0 and asteroid_stack[-1] > 0:
                size = asteroid_size + asteroid_stack[-1]

                if size < 0: #smaller one will explode
                    asteroid_stack.pop()
                elif size > 0:  #discord current asteroid
                    asteroid_size = 0
                else: #both are equal, so pop both
                    asteroid_size = 0
                    asteroid_stack.pop()
            if asteroid_size != 0:
                asteroid_stack.append(asteroid_size)
        return asteroid_stack
