#!/usr/bin/env python3

def parse():
    r, _, l, h = map(int, input().split())
    p = [list(map(lambda c: int(c=='M'), input())) for _ in range(r)]
    return p, l, h

def output(d):
    print(len(d))
    for (r1,c1),(r2,c2) in d: print(r1, c1, r2, c2)

def score(d):
    return sum((abs(r2-r1)+1)*(abs(c2-c1)+1) for (r1,c1),(r2,c2) in d)

def psum(p):
    ps = [[0]*(len(p[0])+1) for _ in range(len(p)+1)]
    for r in range(len(p)):
        for c in range(len(p[0])):
            ps[r+1][c+1] = p[r][c] + ps[r][c+1] + ps[r+1][c] - ps[r][c]
    return ps

def valid():
    pass

def main():
    p, l, h = parse()
    ps = psum(p)
    print(p)
    print(ps)
    #output([((1,2),(3,4))])

if __name__ == '__main__': main()
