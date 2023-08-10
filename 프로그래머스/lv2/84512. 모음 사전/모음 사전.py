def solution(word):
    answer = 0
    dic = 'AEIOU'
    wordList = []
    
    def dfs(cnt, temp):
        if cnt == 5:
            return
        for i in range(len(dic)):
            wordList.append(temp + dic[i])
            dfs(cnt + 1, temp+dic[i])
    
    dfs(0, '')
    
    return wordList.index(word)+1