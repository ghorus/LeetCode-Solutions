from game_finder import find_qualified_games

def test_case_7():
    game_data = [
        {'gameID': 1, 'playerID': 5, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 0, 'fieldGoal2Made': 0, 'fieldGoal3Attempted': 0, 'fieldGoal3Made': 0, 'freeThrowAttempted': 0, 'freeThrowMade': 0},
        {'gameID': 2, 'playerID': 5, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 5, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 2, 'freeThrowMade': 2},
    ]
    qualified_games = find_qualified_games(game_data, 53, 1)
    assert qualified_games == [2]