def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def divisions(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def min_perimeter(area):
    heights = divisions(area)
    print(heights)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    
    return min(perimeters)

print(min_perimeter(10))