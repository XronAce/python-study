def solution(info, query):
    answer = []
    infolist = []
    querylist = []
    for i in info:
        infolist.append(i.split())
    for q in query:
        querylist.append(q.split())
    info = infolist
    query = querylist

    for q in query:
        count = 0
        for i in info:
            if int(i[4]) >= int(q[7]):
                if q[0] == i[0] or q[0] == "-":
                    if q[2] == i[1] or q[2] == "-":
                        if q[4] == i[2] or q[4] == "-":
                            if q[6] == i[3] or q[6] == "-":
                                count += 1
        answer.append(count)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))