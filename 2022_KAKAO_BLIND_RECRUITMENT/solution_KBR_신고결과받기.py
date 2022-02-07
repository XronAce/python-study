def solution(id_list, report, k):
    reported = {} # {id: How many times id got reported}
    reportedWho = {} # {reporter id: reported id list}
    emailCount = {} # {id: How many times id gets report email(=answer)}
    jail = [] # id who got limited access.
    for id in id_list:
        reported[id] = 0 #Initializing reported dict.
        reportedWho[id] = [] #Initializing reportedWho dict.
        emailCount[id] = 0 #Initializing emailCount dict.
    answer = []

    for case in report:
        repFrom, repTo = case.split(" ")
        if repFrom == repTo:
            continue
        if repTo not in reportedWho[repFrom]:
            reportedWho[repFrom].append(repTo)

    for value in reportedWho.values():
        for id in value:
            reported[id] += 1
    
    for item in reported.items():
        if item[1] >= k:
            jail.append(item[0])

    for item in reportedWho.items():
        for id in jail:
            if id in item[1]:
                emailCount[item[0]] += 1

    answer = list(emailCount.values())
            
    return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# print(solution(id_list, report, 2))

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# print(solution(id_list, report, 3))

"""
Commentary after the solution:
1. Troublemaker: Code efficiency. Use less for-loops for faster code run, and save up some requisite elements on seperate data types (cf. report parameter can be really long)
2. What should I do next?: Try to make code more compact. My code seems a bit long and wasteful compared with others' codes.
"""