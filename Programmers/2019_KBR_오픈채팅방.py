def solution(record):
    answer = []
    reform = []
    uid_username = {}
    for rec in record:
        reform.append(rec.split())
    
    for rec in reform:
        if rec[0] == "Enter":
            uid_username[rec[1]] = rec[2]
        elif rec[0] == "Change":
            uid_username[rec[1]] = rec[2]
    
    for rec in reform:
        if rec[0] == "Enter":
            answer.append(f"{uid_username[rec[1]]}님이 들어왔습니다.")
        elif rec[0] == "Leave":
            answer.append(f"{uid_username[rec[1]]}님이 나갔습니다.")

    return answer

# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# print(solution(record))