working = True # 작동 시작


sample = [] # 표본집단/모집단
sample_processed = {} # {관찰값: 개수} 딕셔너리

# 입력값 타입 분석
exist_str = False # 문자열 존재 여부

# 분석 함수
def mean(list): # 평균 
    return sum(list)/len(list)
def sigma_squared(list): # 모분산 
    m = mean(list)
    deviation_squared = []
    for i in list:
        deviation_squared.append((i-m)**2)
    return mean(deviation_squared)
def S_squared(list): # 표본분산 
    m = mean(list)
    deviation_squared = []
    for i in list:
        deviation_squared.append((i-m)**2)
    return sum(deviation_squared)/(len(deviation_squared)-1)
def sigma(list): # 모표준편차
    return sigma_squared(list)**(1/2)
def S(list): # 표본표준편차
    return S_squared(list)**(1/2)

# 입력값 받기
Input = input("모집단:p / 표본집단:s\n") # 모집단: False 표본집단: True
if Input == 'p':
    p_or_s = 'p'
elif Input == 's':
    p_or_s = 's'
else: quit()
while working:
    Input = input("관찰값을 입력하세요\n 입력 완료: end / 마지막 입력값 삭제: del / 중지: exit \n")
    if Input == 'end':
        working = False
    elif Input == 'del':
        del sample[-1]
    elif Input == 'exit':
        quit()
    else:
        sample.append(Input)

# 딕셔너리로 가공
for i in sample:
    try: sample_processed[i] +=1
    except: sample_processed[i] = 1


# 입력값 타입 확인
for i in sample:
    try:
        sample[sample.index(i)] = float(i)
    except:
        exist_str = True
        break


# 출력
if p_or_s == 's':
    if exist_str is False:
        print("모든 입력값이 정수입니다.")
        print("표본평균", mean(sample))
        print("표본분산", S_squared(sample))
        print("표본표준편차", S(sample))
    elif exist_str is True:
        print(sample_processed)
else:
    if exist_str is False:
        print("모든 입력값이 정수입니다.")
        print("모평균", mean(sample))
        print("모분산", sigma_squared(sample))
        print("모표준편차", sigma(sample))
    elif exist_str is True:
        print(sample_processed)



