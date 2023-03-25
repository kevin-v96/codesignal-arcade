from collections import Counter

def solution(votes, k):
    potential_winners = 0
    for i in range(len(votes)):
        new_votes = votes.copy()
        new_votes[i] += k
        new_counts = Counter(new_votes)
        max_votes = max(new_votes)
        if new_votes[i] == max_votes and new_counts[max_votes] < 2:
            potential_winners += 1
            
    return potential_winners