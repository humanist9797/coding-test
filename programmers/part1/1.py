def solution(line):
    cross = set() # 여러 직선들 중 같은 교점이 여러 번 나올 수 있어 set()자료형을 사용해 저장
    for a in range(len(line)):
        for b in range(len(line)):
            if a==b: 
                continue
            point = getIntCross(line[a], line[b]) # getIntCross 함수로 두 직선의 정수 교점을 얻고, if point로 false 값이 리턴된 경우 거름
            
            if point: 
                cross.add(point)
    
    xs, ys = list(map(lambda x: x[0], cross)), list(map(lambda x: x[1], cross)) # x좌표, y좌표 분리

    startX, startY = min(xs), min(ys) # 0 이상으로 맞추기 위한 변수
    height = max(ys) - startY + 1 # 높이
    width = max(xs) - startX + 1 # 너비
    
    cross = list(map(lambda x: (x[0]-startX, x[1]-startY), cross)) # 0 이상으로 맞춤
    
    answer = ['.' * width for _ in range(height)]
  
    for x, y in cross:
        answer[y] = answer[y][:x]+'*'+answer[y][x+1:] # 별 삽입
    
    return answer[::-1] # 좌표는 y값이 클 수록 위로, python 인덱스에서는 y값이 클 수록 아래로

def getIntCross(l1, l2): # 두 직선이 주어졌을 때 교점을 구하는 함수
    a, b, e = l1
    c, d, f = l2

    if a * d - b * c == 0: 
        return False
    
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)

    return (int(x), int(y)) if x==int(x) and y==int(y) else False # 만약 두 직선이 평행하거나 정수 값이 아니면 false 그렇지 않으면 (x,y)좌표를 리턴
    