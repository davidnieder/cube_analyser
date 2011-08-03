import Image
import config

def analyse( image ):
    areas = []
    colors = []
    for box in config.boxes:
        areas.append( image.crop(box) )

    # calc arithmetic mean of all pixels for each box
    mean = []
    for area in areas:
        sum = [0,0,0]

        for pixel in area.getdata():
            sum[0] += pixel[0]
            sum[1] += pixel[1]
            sum[2] += pixel[2]
        sum[0] = sum[0] / len(area.getdata())
        sum[1] = sum[1] / len(area.getdata())
        sum[2] = sum[2] / len(area.getdata())

        mean.append(sum)

    # fill in colors list
    for el in mean:
        colors.append( compare_colors(el) )

    return colors

def compare_colors( rgbtuple ):
    red = rgbtuple[0] - config.red[0], rgbtuple[1] - config.red[1], rgbtuple[2] - config.red[2]
    red = abs( red[0] ) + abs( red[1] ) + abs( red[2] )

    blue = rgbtuple[0] - config.blue[0], rgbtuple[1] - config.blue[1], rgbtuple[2] - config.blue[2]
    blue = abs( blue[0] ) + abs( blue[1] ) + abs( blue[2] )

    yellow = rgbtuple[0] - config.yellow[0], rgbtuple[1] - config.yellow[1], rgbtuple[2] - config.yellow[2]
    yellow = abs( yellow[0] ) + abs( yellow[1] ) + abs( yellow[2] )

    green = rgbtuple[0] - config.green[0], rgbtuple[1] - config.green[1], rgbtuple[2] - config.green[2]
    green = abs( green[0] ) + abs( green[1] ) + abs( green[2] )

    orange = rgbtuple[0] - config.orange[0], rgbtuple[1] - config.orange[1], rgbtuple[2] - config.orange[2]
    orange = abs( orange[0] ) + abs( orange[1] ) + abs( orange[2] )

    white = rgbtuple[0] - config.white[0], rgbtuple[1] - config.white[1], rgbtuple[2] - config.white[2]
    white = abs( white[0] ) + abs( white[1] ) + abs( white[2] )

    colorlist = [ red, blue, yellow, green, orange, white ]
    minimum = colorlist[0]
    for color in colorlist:
        if color < minimum:
            minimum = color

    if red == minimum:
        return 'red'
    elif blue == minimum:
        return 'blue'
    elif yellow == minimum:
        return 'yellow'
    elif green == minimum:
        return 'green'
    elif orange == minimum:
        return 'orange'
    elif white == minimum:
        return 'white'

# Debug funtion
def debug(el):
    print el,
    print compare_colors(el)


