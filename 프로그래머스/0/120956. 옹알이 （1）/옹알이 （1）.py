def solution(babbling):
    answer = 0
    check_list = ["aya", "ye", "woo", "ma"] 
    
    for babb in babbling:
        finded = 0
        for i in range(4):
            if babb.find(check_list[i]) !=-1:
                finded+= len(check_list[i])
        if finded == len(babb):
            answer +=1

    return answer