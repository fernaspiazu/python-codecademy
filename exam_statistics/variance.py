__author__ = 'fumandito'

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(_grades):
    for grade in _grades:
        print grade


def grades_sum(_grades):
    total = 0
    for grade in _grades:
        total += grade
    return total


def grades_average(_grades):
    sum_of_grades = grades_sum(_grades)
    average = sum_of_grades / float(len(_grades))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2

    return variance / len(scores)


def grades_std_deviation(variance):
    return variance ** 0.5


print grades_std_deviation(grades_variance(grades))
