__author__ = 'fumandito'


# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if "fizz" == item:
            count += 1

    return count


print fizz_count(["fizz", "cat", "fizz"])
