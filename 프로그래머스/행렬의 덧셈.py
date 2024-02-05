def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        answer = []
        for j in range(len(arr1[0])):
            answer.append(arr1[i][j] + arr2[i][j])
        ans.append(answer)
    return ans