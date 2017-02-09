#!/usr/bin/env python3

import random

from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['x_min', 'x_max', 'y_min', 'y_max'])


def parse():
    r, _, l, h = map(int, input().split())
    p = [list(map(lambda c: int(c=='M'), input())) for _ in range(r)]
    return p, l, h

def output(d):
    print(len(d))
    for (r1,c1,r2,c2) in d: print(r1, c1, r2, c2)

def score(d):
    return sum(get_area(rect) for rect in d)

def psum(p):
    ps = [[0]*(len(p[0])+1) for _ in range(len(p)+1)]
    for r in range(len(p)):
        for c in range(len(p[0])):
            ps[r+1][c+1] = p[r][c] + ps[r][c+1] + ps[r+1][c] - ps[r][c]
    return ps

def get_area(rect):
    return (abs(rect.x_max - rect.x_min) + 1) * (abs(rect.y_max - rect.y_min) + 1)

def get_zeros_and_ones(rect, pizza):
    ones = pizza[rect.x_max+1][rect.y_max+1] - pizza[rect.x_min][rect.y_max+1] - pizza[rect.x_max+1][rect.y_min] + pizza[rect.x_min][rect.y_min]
    zeros = get_area(rect) - ones
    return zeros, ones

def isvalid(rect, pizza, l, h):
    if get_area(rect) > h:
        return False
    zeros, ones = get_zeros_and_ones(rect, pizza)
    if (zeros < l) or (ones < l):
        return False
    return True

def generate_initial_points(pizza, l, h, rect):
    print(rect)
    if isvalid(rect, pizza, l, h):
        print("Valid")
        return [rect]
    elif get_area(rect) < h:
        print("Invalid")
        return []
    (x_min, x_max, y_min, y_max) = rect
    length = x_max - x_min
    width = y_max - y_min
    vertical_cut = (random.random() > ((width-1)/(width+length-2)))
    if vertical_cut:
        cut_point = random.randint(x_min, x_max-1)
        up_point = Rectangle(x_min, cut_point, y_min, y_max)
        down_point = Rectangle(cut_point+1, x_max, y_min, y_max)
    else:
        cut_point = random.randint(y_min, y_max-1)
        up_point = Rectangle(x_min, x_max, y_min, cut_point)
        down_point = Rectangle(x_min, x_max, cut_point+1, y_max)
    ret = generate_initial_points(pizza, l, h, up_point) + generate_initial_points(pizza, l, h, down_point)
    return ret


def main():
    p, l, h = parse()
    ps = psum(p)
    for i in p:
        print(i)
    print()
    for i in ps:
        print(i)
    print()
    rect = Rectangle(1, 2, 2, 3)
    print(rect, get_area(rect), get_zeros_and_ones(rect, ps), isvalid(rect, ps, l, h))
    points = generate_initial_points(ps, l, h, Rectangle(0, len(p)-1, 0, len(p[0])-1))
    points.sort()
    print()
    for poi in points:
        print(poi)
    #output([((1,2),(3,4))])
    print(sum(get_area(poi) for poi in points))

if __name__ == '__main__': main()
