from collections import defaultdict

def solution(survey, choices):
    n = len(survey)
    scores = defaultdict(int)

    for i in range(n):
        if choices[i] <= 4:
            scores[survey[i][0]] += 4 - choices[i]
        else:
            scores[survey[i][1]] += choices[i] - 4

    answer = ''
    # RT
    if scores['R'] >= scores['T']:
        answer += 'R'
    else:
        answer += 'T'
    # CF
    if scores['C'] >= scores['F']:
        answer += 'C'
    else:
        answer += 'F'
    # JM
    if scores['J'] >= scores['M']:
        answer += 'J'
    else:
        answer += 'M'
    # AN
    if scores['A'] >= scores['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer