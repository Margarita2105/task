def appearance(intervals):
    z = min(intervals['lesson'][-1], intervals['pupil'][-1], intervals['tutor'][-1])
    people = []
    j = 0
    i = 2
    man = 'pupil'
    while i <= len(intervals[man]):
        x2 = intervals[man][j:i]
        people.append(x2)
        j += 2
        i += 2
        if i > len(intervals[man]) and man == 'pupil':
            man = 'tutor'
            people1 = people
            people = []
            j = 0
            i = 2
    people.sort()
    people1.sort()
    i1 = 0
    k = 0
    while i1 < len(people):
        if people[i1][0] > z:
            people = people[:i1]
            if not k: 
                people2 = people
                people = people1
                k = 1
                i1 = 0
                continue
            else:
                break
        elif people[i1][1] >= z:
            people[i1][1] = z
            people = people[:i1+1]
            if not k: 
                people2 = people
                people = people1
                k = 1
                i1 = 0
                continue
            else:
                break
        if i1 == 0:
            people[0][0] = max(intervals['lesson'][0], intervals['pupil'][0], intervals['tutor'][0])
        if people[i1][1] < people[0][0]:
            people.pop(i1)
            i1 -= 1
        if i1 > 0:
            if people[i1][1] < people[i1-1][1]:
                people.pop(i1)
                i1 -= 1
            elif people[i1][0] < people[i1-1][1]:
                people[i1-1][1] = people[i1][1]
                people.pop(i1)
                i1 -= 1
        i1 += 1
    s = 0
    while people and people2:
        a = max(people[0][0], people2[0][0])
        b = min(people[0][1], people2[0][1])
        s += b - a
        if b == people[0][1]:
            people2[0][0] = b
            people.pop(0)
        else:
            people[0][0] = b
            people2.pop(0)
    return s

tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
