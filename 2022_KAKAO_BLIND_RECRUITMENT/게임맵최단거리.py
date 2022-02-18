# This code is not completed. Need to fix some errors as well as running time.

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    mvrec = [(0, 0)] # 이동한 좌표 기록
    for map in maps:
        map.append(0)
    maps.append([0]*(n+1))

    for map in maps:
        print(map)
    
    if (maps[n-2][m-1] == 0) and (maps[n-1][m-2] == 0):
        answer = -1
    else:
        bpos = () # 1회 직전의 캐릭터의 위치
        cpos = (0, 0) # 현재 캐릭터의 위치. 초기값 좌표 (0, 0)
        mvrec.append(cpos)
        print(mvrec)
        count = 0
        flagd = 1
        flagr = 1
        flagl = 1
        flagu = 1

        while cpos != (n-1, m-1):
        #while count != 15:
            if maps[cpos[1]+1][cpos[0]] == 1 and flagd == 1: # 캐릭터 아래칸이 벽이 없는 자리일 경우
                print("Move down")
                count += 1 
                if mvrec[-2] == (cpos[0], cpos[1]+1):
                    flagd = 0
                    continue
                else:
                    mvrec.append((cpos[0], cpos[1]+1))
                    print(mvrec)
                    cpos = (cpos[0], cpos[1]+1)
                    flagd = 1
                    flagr = 1
                    flagu = 1
                    flagl = 1
            elif maps[cpos[1]][cpos[0]+1] == 1 and flagr == 1: # 캐릭터 오른쪽칸이 벽이 없는 자리일 경우
                print("Move right")
                count += 1 
                if mvrec[-2] == (cpos[0]+1, cpos[1]):
                    flagr = 0
                    continue
                else:
                    mvrec.append((cpos[0]+1, cpos[1]))
                    print(mvrec)
                    cpos = (cpos[0]+1, cpos[1])
                    flagd = 1
                    flagr = 1
                    flagu = 1
                    flagl = 1
            elif maps[cpos[1]-1][cpos[0]] == 1 and flagu == 1: # 캐릭터 윗칸이 벽이 없는 자리일 경우
                print("Move up")
                count += 1 
                if mvrec[-2] == (cpos[0], cpos[1]-1):
                    flagu = 0
                    continue
                else:
                    mvrec.append((cpos[0], cpos[1]-1))
                    print(mvrec)
                    cpos = (cpos[0], cpos[1]-1)
                    flagd = 1
                    flagr = 1
                    flagu = 1
                    flagl = 1
            elif maps[cpos[1]][cpos[0]-1] == 1 and flagl == 1: # 캐릭터 왼쪽칸이 벽이 없는 자리일 경우
                print("Move left")
                count += 1 
                if mvrec[-2] == (cpos[0]-1, cpos[1]):
                    flagl = 0
                    continue
                else:
                    mvrec.append((cpos[0]-1, cpos[1]))
                    print(mvrec)
                    cpos = (cpos[0]-1, cpos[1])
                    flagd = 1
                    flagr = 1
                    flagu = 1
                    flagl = 1
            else:
                mvrec.pop()
                maps[cpos[0]][cpos[1]] = 0
                cpos = mvrec[-1]
                print("Popped")
                print(mvrec)
                flagd = 1
                flagr = 1
                flagu = 1
                flagl = 1
        answer = len(mvrec)-1

    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
#maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
#maps =[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(solution(maps))

"""
[1,0,1,1,1],
[1,0,1,0,1],
[1,0,1,1,1],
[1,1,1,0,1],
[0,0,0,0,1]
"""

"""
maps[y, x] = position (x, y)
"""