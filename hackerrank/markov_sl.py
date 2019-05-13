import random

T = int(input())
movements = [i for i in range(1,7)]

# print(dices)
def roll_dice(dices):
    return random.choices(movements,weights=dices,k=1)

def simulation():

    inputs = input().split(',')
    dices = [float(i) for i in inputs]

    snakes_and_ladders = input().split(',')

    ladder_count = int(snakes_and_ladders[0])
    snake_count = int(snakes_and_ladders[1])

    ladders_datas = input().split()
    splitted = [data.split(',') for data in ladders_datas]
    ladders_start = [(int(x)) for x,_ in splitted]
    ladders_end = [(int(y)) for _,y in splitted]


    snakes_datas = input().split()
    splitted = [data.split(',') for data in snakes_datas]
    snakes_start = [(int(x)) for x,_ in splitted]
    snakes_end = [(int(y)) for _,y in splitted]

    cur = 1
    round_array = []
    for i in range(5000):
        dice_count = 0
        while(dice_count <= 1000):
            movements = roll_dice(dices)
            dice_count+=1
            orig_cur = cur
            cur+=movements[0]
            if(cur in ladders_start):
                cur = ladders_end[ladders_start.index(cur)]
            if(cur in snakes_start):
                cur = snakes_end[snakes_start.index(cur)]

            if(cur==100):
                break
            elif(cur>100):
                cur=orig_cur
        # print('sibar',dice_count)
        cur = 1
        round_array.append(dice_count)
    # print(round_array)

    return sum(round_array)/len(round_array)
    # print(ladders)
    # print(snakes)

for i in range(T):
    print(int(simulation()))
