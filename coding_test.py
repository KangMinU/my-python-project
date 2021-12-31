# 코딩테스트

"""
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
"""

def solution(new_id):
    answer = ''
    Sol = ''
    use_list = '-_.'
    # 1단계 소문자로 변형   self.lower() -> 문자열을 소문자로 변환해 반환하는 메소드 (이 때 원형을 바꾸는 것이 아님을 주의)
    answer = new_id.lower()
    print('1단계 결과 : ', answer)
    # 2단계

    for Value in answer:
        if Value in use_list :
            Sol += Value
        
        elif Value.islower() or Value.isdigit() :
            Sol += Value
        
        '''
        elif Value.isdigit():
            Sol += Value
        '''

    print('2단계 결과 : ', Sol)
    
    #3단계
    while '..' in Sol:
        Sol = Sol.replace('..','.')
    
    print('3단계 결과 : ', Sol)

    #4단계 처음 혹은 끝이 .으로 시작하면 삭제
    if Sol == '':
        pass
    
    if Sol[0] == '.' :
        Sol = Sol[1:]

    if Sol[-1] == '.' :
        Sol = Sol[:-1]

    print('4단계 결과 : ', Sol)

    # 5단계
    Sol = 'a' if Sol == '' else Sol 

    print('5단계 결과 : ', Sol)

    # 6단계
    if len(Sol) > 15 :
        answer = Sol[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]
    else :
        answer = Sol

    print('6단계 결과 : ', answer)

    # 7단계
    while len(answer) < 3 :
        answer += answer[-1]

    print('최종 : ', answer)
    #return answer

    
    #return answer
id = ".sfgsgsg."

solution(id)
#print('inp : ', id)
#print('outp : ', solution(id))




def solution(new_id):
    answer = ''
    Sol = ''
    use_list = '-_.'
    # 1단계 소문자로 변형   self.lower() -> 문자열을 소문자로 변환해 반환하는 메소드 (이 때 원형을 바꾸는 것이 아님을 주의)
    answer = new_id.lower()
    # 2단계
    for Value in answer:
        if Value == '.' or Value == '-' or Value == '_' or Value.islower() or Value.isdigit():
            Sol += Value
    
    #3단계
    while '..' in Sol:
        Sol = Sol.replace('..','.')

    #4단계 처음 혹은 끝이 .으로 시작하면 삭제
    if Sol == '' :
        pass
    
    if Sol[0] == '.' :
        Sol = Sol[1:]

    if Sol[-1] == '.' :
        Sol = Sol[:-1]

    # 5단계
    Sol = 'a' if Sol == '' else Sol 

    # 6단계
    if len(Sol) > 15 :
        answer = Sol[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]
    else :
        answer = Sol

    # 7단계
    if len(answer) < 3 :
        i = answer[-1]
        while len(answer) < 3 :
            answer += i
    
    return answer