def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start,lesson_end = intervals['lesson']
    pupil_time = intervals['pupil']
    tutor_time = intervals['tutor']

    # Обрезаем интервалы по уроку (чтобы те интервалы, которые вышли за пределы, мы их обрезали до конца и начало урока)
    pupil_time = [max(p, lesson_start) for p in pupil_time]
    pupil_time = [min(p, lesson_end) for p in pupil_time]
    tutor_time = [max(t, lesson_start) for t in tutor_time]
    tutor_time = [min(t, lesson_end) for t in tutor_time]

    # Объединяем интервалы ученика (если не объединять, то может пересечение посчитаться дважды)
    pupil_time_intervals = []
    for i in range(0, len(pupil_time), 2):
        pupil_time_intervals.append((pupil_time[i], pupil_time[i+1]))

    merge_pupil_intervals = []
    for start, end in pupil_time_intervals:
        if not merge_pupil_intervals:
            merge_pupil_intervals.append([start, end])
        else:
            last_start, last_end = merge_pupil_intervals[-1]
            if start <= last_end: # тут если интервалы пересекаются 
                merge_pupil_intervals[-1][1] = max(end, last_end)
            else:
                merge_pupil_intervals.append([start, end])

    # Объединяем интервалы учителя (если не объединять, то может пересечение посчитаться дважды)
    tutor_time_intervals = []
    for i in range(0, len(tutor_time), 2):
        tutor_time_intervals.append((tutor_time[i], tutor_time[i+1]))

    merge_tutor_intervals = []
    for start, end in tutor_time_intervals:
        if not merge_tutor_intervals:
            merge_tutor_intervals.append([start, end])
        else:
            last_start, last_end = merge_tutor_intervals[-1]
            if start <= last_end: # тут если интервалы пересекаются
                merge_tutor_intervals[-1][1] = max(end, last_end)
            else:
                merge_tutor_intervals.append([start, end])

    # Подсчет всех пересечений
    all_presence_time = 0
    for p_start, p_end in merge_pupil_intervals:
        for t_start, t_end in merge_tutor_intervals:
            result_start, result_end = max(p_start, t_start), min(p_end, t_end)
            if result_start < result_end:
                all_presence_time += result_end - result_start

    return all_presence_time

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
        print(test_answer)

