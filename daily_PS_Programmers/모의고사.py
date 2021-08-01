def solution(answers):
    answer = []
    answer_temp = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == arr1[i % len(arr1)]:
            cnt1 += 1
        if answers[i] == arr2[i % len(arr2)]:
            cnt2 += 1
        if answers[i] == arr3[i % len(arr3)]:
            cnt3 += 1
    answer_temp = [cnt1, cnt2, cnt3]
    for person, score in enumerate(answer_temp):
        if score == max(answer_temp):
            answer.append(person + 1)

    return answer