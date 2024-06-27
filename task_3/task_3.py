def correct_list(intervals, lesson_start, lesson_end):
    correct_intervals_list = []
    for index in range(0, len(intervals), 2):

        if intervals[index] > lesson_end:
            break

        if intervals[index + 1] < lesson_start:
            continue

        current_interval_start = max(intervals[index], lesson_start)

        if correct_intervals_list:
            current_interval_start = max(current_interval_start, correct_intervals_list[-1])

        current_interval_end = min(intervals[index + 1], lesson_end)

        if current_interval_start < current_interval_end:
            correct_intervals_list.extend([current_interval_start, current_interval_end])

    return correct_intervals_list


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']
    correct_pupil_intervals = correct_list(pupil_intervals, lesson_start, lesson_end)
    correct_tutor_intervals = correct_list(tutor_intervals, lesson_start, lesson_end)

    index_pupil = 0
    index_tutor = 0
    total_time = 0

    len_pupil = len(correct_pupil_intervals)
    len_tutor = len(correct_tutor_intervals)

    while index_pupil < len_pupil and index_tutor < len_tutor:

        cur_pupil_start = correct_pupil_intervals[index_pupil]
        cur_pupil_end = correct_pupil_intervals[index_pupil + 1]
        cur_tutor_start = correct_tutor_intervals[index_tutor]
        cur_tutor_end = correct_tutor_intervals[index_tutor + 1]

        if cur_pupil_start > cur_tutor_end:
            index_tutor += 2
            continue
        elif cur_tutor_start > cur_pupil_end:
            index_pupil += 2
            continue

        current_start = max(cur_pupil_start, cur_tutor_start)
        current_end = min(cur_pupil_end, cur_tutor_end)

        total_time += current_end - current_start

        if cur_pupil_end > cur_tutor_end:
            index_tutor += 2
        elif cur_tutor_end > cur_pupil_end:
            index_pupil += 2
        else:
            index_pupil += 2
            index_tutor += 2
    return total_time
