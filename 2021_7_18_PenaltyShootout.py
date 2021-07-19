import random

SIMS = 100000

class Shootout():
    def __init__(self, team1, team2, shot_chance):
        self.team1 = team1
        self.team2 = team2
        self.shot_chance = shot_chance

    def shot(self):
        # Simulate a single shot
        outcomes = [0, 1] # 0 if miss, 1 if make
        shot = random.choices([1, 0], cum_weights=[self.shot_chance, 1])
        return shot[0]

    def shootout(self):
        team1_shots = []
        team2_shots = []
        # Simulate first 5 rounds
        for i in range(5):
            # Team 1 takes a shot
            team1_shots.append(self.shot())
            # See if either team has won
            if (sum(team1_shots) + (5 - len(team1_shots))) < sum(team2_shots) or (sum(team2_shots) + (5 - len(team2_shots))) < sum(team1_shots):
                return {
                    self.team1: team1_shots,
                    self.team2: team2_shots,
                    "Goals": sum(team1_shots) + sum(team2_shots),
                    "Shots": len(team1_shots) + len(team2_shots)
                }

            # Team 2 takes a shot
            team2_shots.append(self.shot())
            # See if either team has won
            if sum(team1_shots) + (5 - len(team1_shots)) < sum(team2_shots) or sum(team2_shots) + (5 - len(team2_shots)) < sum(team1_shots):
                return {
                    self.team1: team1_shots,
                    self.team2: team2_shots,
                    "Goals": sum(team1_shots) + sum(team2_shots),
                    "Shots": len(team1_shots) + len(team2_shots)
                }

        # If no winner after 5, keep going until there is a winner
        while True:
            team1_shots.append(self.shot())
            team2_shots.append(self.shot())
            if sum(team1_shots) < sum(team2_shots) or sum(team1_shots) > sum(team2_shots):
                return {
                    self.team1: team1_shots,
                    self.team2: team2_shots,
                    "Goals": sum(team1_shots) + sum(team2_shots),
                    "Shots": len(team1_shots) + len(team2_shots)
                }

def main():
    goals = []
    shots = []
    for i in range(SIMS):
        shootout = Shootout("Italy", "England", .7)
        result = shootout.shootout()
        goals.append(result["Goals"])
        shots.append(result["Shots"])
    shot_percent = sum(goals)/sum(shots)
    mean_shots = sum(shots)/len(shots)
    print(f"Shot Percent: {shot_percent}")
    print(f"Average Shots per Shootout: {mean_shots}")

if __name__ == "__main__":
    main()




