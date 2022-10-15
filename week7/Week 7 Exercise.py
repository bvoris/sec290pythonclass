#
# SEC290.12780.B1.Online
# Brad Voris
# 10/10/2022
# week 7 Exercise
class golfteam:
    count = 0
    def __init__(self, name):
        self.team_name = name
        self.players = []
        golfteam.count += 1
    def add_player(self, name):
        self.players.append(name)
    def show_team(self):
        print (f'Team {self.team_name}')
        for player in self.players:
            print(f'     {player}')
print(f'Number of teams: {golfteam.count}')
team_woods = golfteam("Woods")
print(f'Number of teams: golfteam.count')
team_woods.add_player("Woods")
team_woods.add_player("Johnson")
team_rahm = golfteam("Rahm")
print(f'Number of team: {golfteam.count}')
team_rahm.add_player("Rahm")
team_rahm.add_player("Finau")
team_woods.show_team()
team_rahm.show_team()