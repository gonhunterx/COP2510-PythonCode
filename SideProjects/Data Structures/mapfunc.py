def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num


x = [551, 641, 257, 241, 444, 246, 223, 556, 240]
# map will create a map object so you have to turn it into a list.
y = list(map(make_even, x))
# what map basically does is applies a function to a variable like a for loop.
# this would be like for num in x: y.append(make_event(num))


print(y)
