# Finding which of two entered rectangles has the larger area
# asking for rectangle width and height
r1h = float(input('Input the height of the first rectangle: '))
r1w = float(input('Input the width of the first rectangle: '))

r2h = float(input('Input the height of the second rectangle: '))
r2w = float(input('Input the width of the second rectangle: '))

r1area = r1h * r1w
r2area = r2h * r2w


if r1area > r2area:
    print('Rectangle 1 has the greater area.')
elif r1area < r2area:
    print('Rectangle 2 has the greater area.')
else:
    print('Both rectangles have the same area.')

    

