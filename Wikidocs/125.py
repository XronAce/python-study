comm = {"SKT": "011", "KT": "016", "LGU": "019", "알수없음":"010"}
commswap = dict(zip(comm.values(), comm.keys()))
temp = input("Enter your phone number\(ex. 010-1234-5678\): ")

print(f"당신은 {commswap[temp[:3]]} 사용자 입니다.")