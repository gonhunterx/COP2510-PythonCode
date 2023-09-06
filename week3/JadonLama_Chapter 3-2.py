# Ask for both rectangles width and height
rectangleHeight1 = float(input('what is the first rectangles height'))
rectangleWidth1 = float(input('what is the first rectangles width'))
rectangleHeight2 = float(input('what is the first rectangles height'))
rectangleWidth2 = float(input('what is the first rectangles width'))

# calculate the area of the rectangles
area1 = rectangleHeight1 * rectangleWidth1
area2 = rectangleHeight2 * rectangleWidth2


if(area1 > area2):
    print('Rectangle 1 has the greater area')
elif(area2 > area1):
    print('Rectangle 2 has the greater area')
else:
    print('Both rectangles have the same area.')
    
