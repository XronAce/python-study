def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    installPoint = []
    while routes:
        install = routes[0][1]
        installPoint.append(install)
        for i in range(0, len(routes)):
            if routes[i][0] <= install <= routes[i][1]:
                routes[i] = 'X'
        while 'X' in routes:
            routes.remove('X')
    answer = len(installPoint)

    return answer

# routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
# print(solution(routes))

"""
이 고속도로는 양방향인가 단방향인가에 따라 탐욕법을 적용할 수 있냐 없냐가 정해지는 것 같습니다.
이 풀이법은 단방향을 가정했을 때 작성한 풀이법입니다.
즉, routes의 예시로 [-13, -18]과 같은 형태의 routes 는 없다고 가정했습니다.

문제의 조건에 '고속도로는 단방향이다'라고 지문제시가 필요한 것 같습니다.
"""