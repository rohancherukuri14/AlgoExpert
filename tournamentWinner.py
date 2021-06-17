def tournamentWinner(competitions, results):
    teams = {}
    max_wins = 0
    tourney_winner = ""
    for i in range(0, len(competitions)):
        matchup = competitions[i]
        if results[i] == 0:
            winner = matchup[1]
        else:
            winner = matchup[0]
        if winner in teams:
            teams[winner] += 1
        else:
            teams[winner] = 1
        curr_wins = teams[winner]
        if curr_wins > max_wins:
            max_wins = curr_wins
            tourney_winner = winner
    return tourney_winner