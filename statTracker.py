# Creating classes to account for all Roster members
class RosterMember:
    def __init__(self, player_id, name, jersey_number, position):
        self.player_id = player_id
        self.name = name
        self.jersey_number = jersey_number
        self.position = position

    def display_stats(self):
        print(self.name, self.jersey_number, self.position)        

# Creating a Batter class to keep track of all batter stats
class Batter(RosterMember):
    def __init__(self, player_id, name, jersey_number, position, at_bats, singles, doubles, triples, home_runs, strikeouts, walks, hbp, sac_flies, sb_attempts, sb_successes):
        super().__init__(player_id, name, jersey_number, position)
        self.at_bats = at_bats
        self.singles = singles
        self.doubles = doubles
        self.triples = triples
        self.home_runs = home_runs
        self.strikeouts = strikeouts
        self.walks = walks
        self.hbp = hbp
        self.sac_flies = sac_flies
        self.sb_attempts = sb_attempts
        self.sb_successes = sb_successes
    
    def batting_average(self):
        hits = self.singles + self.doubles + self.triples + self.home_runs
        if self.at_bats == 0:
            return 0.0
        return hits / self.at_bats
    
    def on_base_percentage(self):
        numerator = self.singles + self.doubles + self.triples + self.home_runs + self.walks + self.hbp
        denominator = self.at_bats + self.walks + self.hbp + self.sac_flies
        if denominator == 0:
            return 0.0
        return numerator / denominator
    
    def stolen_base_percentage(self):
        if self.sb_attempts == 0:
            return 0.0
        return self.sb_successes / self.sb_attempts
    
    def display_stats(self):
        super().display_stats()
        print("AVG:", self.batting_average())
        print("WHIP:", self.on_base_percentage())
        print("SB%:", self.stolen_base_percentage())
        print("Strikeouts:", self.strikeouts())


# Creating a Pitcher class to keep track of all pitcher stats
class Pitcher(RosterMember):
    def __init__(self, player_id, name, jersey_number, position, pitch_count, earned_runs, unearned_runs, hits_allowed, strikes, balls, strikeouts, walks, innings_pitched, win, lose):
        super().__init__(player_id, name, jersey_number, position)
        self.pitch_count = pitch_count
        self.earned_runs = earned_runs
        self.unearned_runs = unearned_runs
        self.hits_allowed = hits_allowed
        self.strikes = strikes
        self.balls = balls
        self.strikeouts = strikeouts
        self.walks = walks
        self.innings_pitched = innings_pitched
        self.win = win
        self.lose = lose

    def innings_to_decimal(self):
        remainder = self.innings_pitched % 1
        whole_innings = int(self.innings_pitched // 1)
        partial = round(remainder * 10)

        if partial == 0:
            fractional_inning = 0.0
        elif partial == 1:
            fractional_inning = 1 / 3
        elif partial == 2:
            fractional_inning = 2 / 3
        
        return whole_innings + fractional_inning
        
    def era(self):
        innings = self.innings_to_decimal()
        if innings == 0:
            return 0.0
        return (self.earned_runs * 9) / innings
    
    def whip(self):
        innings = self.innings_to_decimal()
        if innings == 0:
            return 0.0
        return (self.walks + self.hits_allowed) / innings
    
    def k_per_9(self):
        innings = self.innings_to_decimal()
        if innings == 0:
            return 0.0
        return (self.strikeouts * 9) / innings
    
    def display_stats(self):
        super().display_stats()
        print("ERA:", self.era())
        print("WHIP:", self.whip())
        print("K/9:", self.k_per_9())
        print("W-L:", self.win, "-", self.lose)