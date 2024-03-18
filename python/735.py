from typing import List


class Solution(object):
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
       :type asteroids: List[int]
       :rtype: List[int]
       """

        crashed_asteroids = []
        len_asteroids = len(asteroids)
        for index, asteroid in enumerate(asteroids):
            if index == len_asteroids - 1:
                next_asteroid = 0
            else:
                next_asteroid = asteroids[index + 1]

            if index == 0:
                prev_asteroid = 0
            else:
                prev_asteroid = asteroids[index - 1]

            if asteroid > 0:
                if next_asteroid > 0:
                    crashed_asteroids.append(asteroid)
                elif next_asteroid < 0:
                    if asteroid + next_asteroid == 0:
                        continue
                    elif asteroid + next_asteroid < 0:
                        crashed_asteroids.append(next_asteroid)
                        crashed_asteroids = self.asteroidCollision(crashed_asteroids)
                    elif asteroid + next_asteroid > 0:
                        crashed_asteroids.append(asteroid)
                        continue
                elif next_asteroid == 0:
                    crashed_asteroids.append(asteroid)

            elif asteroid < 0:
                if prev_asteroid == 0:
                    crashed_asteroids.append(asteroid)
                elif prev_asteroid < 0:
                    if crashed_asteroids and crashed_asteroids[-1] > 0:
                        crashed_asteroids.append(asteroid)
                        crashed_asteroids = self.asteroidCollision(crashed_asteroids)
                    else:
                        crashed_asteroids.append(asteroid)

        return crashed_asteroids


solution = Solution()
multi_asteroids = [
    [-2, -1, 1, 2],  # [-2, -1, 1, 2]
    [5, 10, -5],  # [5, 10]
    [-2, -1, -1, -2],  # [-2, -1, -1, -2]
    [-2, -2, -2, 1],  # [-2, -2, -2, 1]
    [-2, 1, -2, -2],  # [-2, -2, -2]
    [10, 2, -5],  # [10]
    [-2, 2, -1, -2],  # [-2]
    [1, 1, -2, -2],  # [-2,-2]
    [2, -1, 1, -2],  # []
]
for asteroids in multi_asteroids:
    print(f"start: {asteroids}")
    crashed_asteroids = solution.asteroidCollision(asteroids)
    print(f"result: {crashed_asteroids}")
