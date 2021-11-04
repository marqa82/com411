import tui

COL_MEDAL = 14
COL_TEAM = 6
COL_YEAR = 9


def list_years(data):
    tui.started("Listing years")
    years = set()
    for record in data:
        year = record[COL_YEAR]
        years.add(year)
    tui.display_years(years)
    tui.completed()


def tally_medals(data):
    tui.started("Tallying medals")
    medal_tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for record in data:
        medal = record[COL_MEDAL]
        if medal in ("Gold", "Silver", "Bronze"):
            medal_tally[medal] += 1
    tui.display_medal_tally(medal_tally)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying medals for each team")
    medal_tally = {}
    for record in data:
        team = record[COL_TEAM]
        medal = record[COL_MEDAL]

        if medal not in ("Gold", "Silver", "Bronze"):
            continue

        if team in medal_tally:
            medal_tally[team][medal] += 1
        else:
            medal_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medal_tally[team][medal] += 1

    tui.display_team_medal_tally(medal_tally)
    tui.completed()

LINE_WIDTH = 85


def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")


def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")


def error(msg):
    print(f"Error! {msg}\n")


def menu():
    print(f"""Please select one of the following options:
     {"[years]":<10} List unique years
     {"[tally]":<10} Tally up medals
     {"[team]":<10} Tally up medals for each team
     {"[exit]":<10} Exit the program
     """)
    selection = input("Your selection: ")
    return selection.strip().lower()


def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)