import random
from terminaltables import AsciiTable, SingleTable

def make_game():
    goats = random.randint(0,3)
    doors = [True for _ in range(0,goats)] + [False for _ in range(0, 3 - goats)]
    random.shuffle(doors)
    return doors

def run(maxruns):
    result = { 'switchtowin' : 0,
               'keeptowin' : 0,
               'alwayslose' : 0,
               'alwayswin' : 0,
               'nomonty_switchtowin' : 0,
               'nomonty_alwayswin' : 0}
    for x in range(0,maxruns):
        game = make_game(maxdoors)
        possdoors = [x for x in range(0,maxdoors)]
        ipick = random.randint(0,maxdoors-1)
        yourdoor = game[ipick]
        possdoors.remove(ipick)
        can_monty_pick = False
        for door in possdoors:
            if game[door]:
                can_monty_pick = True
                montypick = door
                possdoors.remove(montypick)
                otherdoor = game[possdoors[0]]
                break
        if can_monty_pick:
            if yourdoor and otherdoor:
                result['alwayslose'] += 1
            elif otherdoor and not yourdoor:
                result['keeptowin'] += 1
            elif yourdoor and not otherdoor:
                result['switchtowin'] += 1
            else:
                result['alwayswin'] += 1
        else:
            if yourdoor:
                result['nomonty_switchtowin'] += 1
            else:
                result['nomonty_alwayswin'] += 1
    table_data = [[v, result[v], str(round(100*(result[v] / maxruns), 4)) + '%'] for k,v in enumerate(result)]
    table = SingleTable(table_data)
    table.inner_heading_row_border = False
    print(table.table)
