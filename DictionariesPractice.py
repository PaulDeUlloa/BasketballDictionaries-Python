class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    def __str__(self):
        # return f"Name:{self.name}"
        return f"|Name:{self.name} Age:{self.age}|"

    def __repr__(self):
        # return f"Name:{self.name}"
        return f"|Name:{self.name} Age:{self.age}|"


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets",
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics",
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets",
}
damien = {
    "name": "Damian Lillard",
    "age": 33,
    "position": "Point Guard",
    "team": "Portland Trailblazers",
}
joel = {
    "name": "Joel Embiid",
    "age": 32,
    "position": "Power Foward",
    "team": "Philidelphia 76ers",
}
deMar = {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls",
}

player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position)

player_jason = Player(jason["name"], jason["age"], jason["position"], jason["team"])
print(player_jason.position)

player_kyrie = Player(kyrie["name"], kyrie["age"], kyrie["position"], kyrie["team"])
print(player_kyrie.position)

player_damien = Player(
    damien["name"], damien["age"], damien["position"], damien["team"]
)
print(player_damien.position)

player_joel = Player(joel["name"], joel["age"], joel["position"], joel["team"])
print(player_joel.position)

player_deMar = Player(deMar["name"], deMar["age"], deMar["position"], deMar["team"])
print(player_deMar.position)


players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls",
    },
]
new_team = []


def create_team():
    for player in players:
        new_player = Player(
            player["name"], player["age"], player["position"], player["team"]
        )
        new_team.append(new_player)


create_team()
print(new_team)

# create a new player by calling the constructor function of the Player class and passing in the required arguments
# Append the new player to the new team list
