valid_chs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
             't','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-','_','.']

def remove_c(new_id):
    temp = ''
    for c in new_id:
        if c in valid_chs:
            temp += c
    return temp    

def transform_one(new_id):
    if not new_id : return ''
    
    temp = ''
    cnt=0
    for c in new_id:
        if c == '.':
            cnt += 1
            if cnt == 2:
                cnt = 1
                continue
        else:
            cnt = 0
        temp += c
    return temp

def remove_fstend_point(new_id):
    if not new_id or (len(new_id)==1 and new_id[0] == '.'):
        return ''

    temp = list(new_id)
    if new_id[0] == '.':
        del temp[0]
    if new_id[-1] == '.':
        del temp[-1]

    return ''.join(temp) 


def solution(new_id):
    answer = ''
    #1단계 소문자 치환
    new_id=new_id.lower()
    #2단계 불필요 문자 삭제
    new_id = remove_c(new_id)
    #3단계 연속된 . 은 한개로 치환
    new_id = transform_one(new_id)
    #4단계 처음에 . 이면 제거 
    new_id = remove_fstend_point(new_id)
    #5단계 빈 문자열이면  a 대입 
    if '' == new_id: new_id='a'
    #6단계 길이 16자 이상 15개제외 제거, 제거 후 마침표 . 이면  . 도 제거 
    if len(new_id) > 15: new_id = new_id[:15]
    if new_id[-1] == '.': new_id = new_id[:14]
    print("1번째 - ",new_id )
    #7단계 길이 2자 이하면 마지막문자 길이 3될때까지 반복해서 붙이기 
    if len(new_id) < 3:
        for vv in range(len(new_id), 3):
            new_id += new_id[-1]
            
    
    
    
    answer = new_id
    return answer