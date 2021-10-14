"""
# 1712 손익분기점
'''
고정: A만원
가변: B만원
노트북 = C만원
판매수 = D개
C * D = A + B * D
D = a/(c-b)
'''
a, b, c = map(int, input().split(' '));
if c - b <= 0:
  print(-1);
else:
  print(int(a / (c - b)) + 1);
"""
"""
# 2292 벌집 - 다시 풀기
'''
1: 1개
2~7: 2개 -> 6개 - 6의 배수가 1개
8~19: 3개 -> 12개 - 6의 배수가 2개
20~37: 4개 -> 18개 - 6의 배수가 3개
38~61: 5개 -> 24개 - 6의 배수가 4개
62~91: 6개 -> 30개 - 6의 배수가 5개
'''
given = int(input());
nums_pileup = 1;
count = 1;
while given > nums_pileup:
  nums_pileup += 6 * count;
  count += 1;
print(count);
"""
"""
# 1193 분수찾기 - 다시 풀기
'''
1/1 -> 2, 1번째
(1/2 -> 2/1) -> 3, 2~3번째
(3/1 -> 2/2 -> 1/3) -> 4, 4~6번째
(1/4 -> 2/3 -> 3/2 -> 4/1) -> 5, 7~10번째
(5/1 -> 4/2 -> 3/3 -> 2/4 -> 1/5) -> 6, 11~15번째
(1/6 -> 2/5 -> 3/4 -> 4/3 -> 5/2 -> 6/1) -> 7, 16~21번째
(1/7 2/6 3/5 4/4 5/3 6/2 7/1) -> 8, 22~28번째
n/m일 때,
합이 짝수 = n부터 시작
합이 홀수 = m부터 시작
'''
input_num = int(input());
max_num = 0;
line = 0;
while input_num > max_num:
  line += 1;
  max_num += line;
gap = max_num - input_num;
if line % 2 == 0:
  top = line - gap;
  under = gap + 1;
else:
  top = gap + 1;
  under = line - gap;
print(f'{top}/{under}')
"""
"""
# 2869 달팽이는 올라가고 싶다 - 다시 풀기
'''
나무: V미터
달팽이
  낮: A미터
  밤: -B미터
일수: C일
정상 도달시 미끄러지지 X
힌트: a * days - b * (days - 1) >= climbed
'''
a, b, v = map(int, input().split(' '));
days = 0;
climbed = 0;
while climbed < v:
  days += 1;
  climbed += a;
  if climbed < v:
    climbed -= b;
  print(days, climbed)
print(days);
"""
"""
# 10250 ACM 호텔
'''
W: 방 수
H: 층 수
정문에서 가까울수록 선호
정문 = 엘리베이터
걷는 거리가 같으면 아래층의 방 선호
  즉, 103 < 1101이지만, 103 > 1103
초깅 모든 방 빔, N번째로 도착한 손님에게 배정될 방 번호 구하기
101, 201, 301, ..., 102, 202, 302, ... 순으로 배정
'''
attempt = int(input());
situs = [];
for i in range(attempt):
  temp = [];
  h, w, n = map(int, input().split(' '));
  temp.append(h);
  temp.append(w);
  temp.append(n);
  situs.append(temp);

hotel = [];
for i in range(len(situs)):
  temp = [];
  for j in range(1, situs[i][1] + 1):
    for k in range(1, situs[i][0] + 1):
      if j < 10:
        temp.append(f'{k}0{j}');
      else:
        temp.append(f'{k}{j}');
  hotel.append(temp);

for i in range(len(situs)):
  print(hotel[i][situs[i][2] - 1]);
"""
"""
# 2775 부녀회장이 될테야 - 다시 풀기
'''
a층 b호 살려면 (a-1)층 1호~b호까지 사람들 수의 합만큼 사람들을 데려와 살아야 함
힌트: 1층 1호는 0층 1호, 2층 1호는 1층 1호, 1층 2호는 0층 2호까지
k층 n호 몇 명 사는지?
아파트 0층부터, 각 층 1호부터, 0층 i호는 i명 거주
'''
t = int(input())

for _ in range(t):
  floor = int(input())
  num = int(input())
  f0 = [x for x in range(1, num+1)]
  for k in range(floor):
    for i in range(1, num):
      f0[i] += f0[i-1]
  print(f0[-1])
"""
"""
# 2839 설탕 배달 - 다시 풀기
'''
설탕 3kg, 5kg 2종류
최대한 적은 수로 배달
'''
'''
원래 풀이
pack = int(input());
attempt = pack // 3;
cnt = 0;

fivePack = '';
threePack = '';
while True:
  exc = [1, 2, 4, 7];
  if pack in exc:
    fivePack = -1;
    threePack = 0;
    break;
  elif pack % 5 == 0:
    fivePack = pack // 5;
    threePack = 0;
    break;
  # elif pack % 3 == 0:
  else:
    temp = pack - 5 * (attempt - cnt);
    print(temp)
    if attempt - cnt > 0 and temp > 0 and temp % 3 == 0:
      fivePack = attempt - cnt;
      threePack = temp // 3;
      break;
    cnt += 1;

print(fivePack + threePack);
'''
sugar = int(input());

bag = 0;
while sugar >= 0:
  if sugar % 5 == 0:
    bag += (sugar // 5);
    print(bag);
    break;
  sugar -= 3;
  bag += 1;
else:
  print(-1);
"""
"""
# 10757 큰 수 A+B
a, b = map(int, input().split(' '));
print(a + b)
"""
# 1011 Fly me to the Alpha Centauri - 다시풀기
'''
직전 이동 거리 k(단, 1 이상)
  -> 직전 이동 거리가 0이면, 즉 첫 사용은 무조건 1
이번 이동 거리: k-1, k, k+1 중 하나
목적지 도착 직전에는 반드시 이동거리 = 1
  -> 대칭 이루도록?
'''
t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)