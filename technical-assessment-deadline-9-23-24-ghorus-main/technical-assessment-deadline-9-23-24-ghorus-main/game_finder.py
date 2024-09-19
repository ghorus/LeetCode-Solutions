"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, 
but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, 
fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, 
ordered from most to least recent game.
"""

from datetime import datetime

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	"""
	Output: Returns a list of qualified gameIDs where <player_count> of players have greater than or equal to the <true_shooting_cutoff>
	"""

	#return empty list if data is empty
	if not game_data:
		return []
	
	#store qualified games and by qualified true shooting
	qualified_games = []
	qualified_by_true_shooting = {}

	# calculate each player's true shooting and add to a qual by shooting if qualified, with dates for future sorting
	for game in game_data:
		attempts = game["fieldGoal2Attempted"] + game["fieldGoal3Attempted"] + game["freeThrowAttempted"]
		mades = game["fieldGoal2Made"] + game["fieldGoal3Made"] + game["freeThrowMade"]

		#handle division by zero
		if attempts == 0:
			calculated_true_shooting_perc = 0
		else:
			calculated_true_shooting_perc = (mades/attempts) * 100

		if calculated_true_shooting_perc >= true_shooting_cutoff:
			curr_date = datetime.strptime(game["gameDate"], '%m/%d/%Y')
			if game["gameID"] not in qualified_by_true_shooting: 
				qualified_by_true_shooting[game["gameID"]] = [curr_date]
			else:
				qualified_by_true_shooting[game["gameID"]].append(curr_date)

	#sort games by most recent date first
	qualified_by_true_shooting = dict(sorted(qualified_by_true_shooting.items(), key=lambda item: max(item[1]),reverse=True))

	# add to qualified games list for games that at least have <player_count> players with qualified true shooting
	for quals in qualified_by_true_shooting:
		if len(qualified_by_true_shooting[quals]) >= player_count:
			qualified_games.append(quals) 

	return qualified_games
		
		




