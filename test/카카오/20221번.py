def solution(id_list, report, k):
    tmp = {}
    reported = {}
    for i in id_list:
        tmp[i] = 0

    for i in report:
        reporter, reportedP = i.split(" ")

        if reportedP not in reported:
            reported[reportedP] = [reporter]
        else:
            if reporter not in reported[reportedP]:
                reported[reportedP].append(reporter)

    for i in reported.keys():
        if len(reported[i]) >= k:
            for j in reported[i]:
                tmp[j] += 1

    answer = [tmp[i] for i in tmp.keys()]

    return answer

#14분 5초

# 신고한 사람
# 신고 당한 사람, 신고당한 횟수


report = ["muzi frodo", "apeach frodo","frodo neo", "muzi neo", "apeach muzi"]
id_list = ["muzi", "frodo", "apeach", "neo"]
k = 2

print(solution(id_list, report, k))
