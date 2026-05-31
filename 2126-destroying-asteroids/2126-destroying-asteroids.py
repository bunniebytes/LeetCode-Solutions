class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # sort asteroids
        asteroids.sort()
        total = mass
        for num in asteroids:
            if total >= num:
                total += num
            else:
                return False
        return True