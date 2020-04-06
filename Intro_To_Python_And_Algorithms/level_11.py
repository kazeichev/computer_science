def MassVote(n, votes):
    max_vote = max(votes)
    vote_index = votes.index(max_vote) + 1

    if votes.count(max_vote) > 1:
        return 'no winner'

    if round(max_vote * 100 / sum(votes), 2) > 50:
        return 'majority winner {}'.format(vote_index)
    else:
        return 'minority winner {}'.format(vote_index)
