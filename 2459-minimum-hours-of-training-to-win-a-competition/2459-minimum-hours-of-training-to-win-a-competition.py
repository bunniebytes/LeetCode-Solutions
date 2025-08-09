class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energy_hours = xp_hours = 0
        player_xp = initialExperience
        opponent_energy = sum(energy)
        if initialEnergy <= opponent_energy:
            energy_hours = (opponent_energy + 1) - initialEnergy
        for xp in experience:
            if player_xp <= xp:
                xp_hours += ((xp + 1) - player_xp)
                player_xp += (((xp + 1) - player_xp) + xp)
            else:
                player_xp += xp
        print(energy_hours, xp_hours)
        return energy_hours + xp_hours