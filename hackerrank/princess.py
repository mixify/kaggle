#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    # print(n)
    bot_loc = [int(n/2),int(n/2)]
    for i in range(0,m):
        if(grid[i].find('p') != -1):
            princess_loc = [i, grid[i].find('p')]
    # print(bot_loc)
    # print(princess_loc)
    for i in range(bot_loc[0],princess_loc[0]):
        print('DOWN')
    for i in range(princess_loc[0],bot_loc[0]):
        print('UP')
    for i in range(bot_loc[1],princess_loc[1]):
        print('RIGHT')
    for i in range(princess_loc[1],bot_loc[1]):
        print('LEFT')

#print all the moves here

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
