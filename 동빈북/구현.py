'''
# 실전 1. 왕실의 나이트 - 답은 맞는데 권장 풀이 방법과 차이 있음 -> 교재 참조
kn = input()
r = [i+1 for i in range(8)]
c = [chr(ord('a')+i) for i in range(8)]
knr = int(kn[1])
knc = kn[0]
possible_knr = 0
possible_knc = 0
if c.index(knc) < 2 or c.index(knc) > 5:
  possible_knc += 1
else:
  possible_knc += 2
if r.index(knr) < 1 or r.index(knr) > 6:
  possible_knr += 2
elif r.index(knr) < 2 or r.index(knr) > 5:
  possible_knr += 3
else:
  possible_knr += 4
print(possible_knr * possible_knc)
'''
# 실전 2. 게임 개발 - 예외처리 실패로 인한 오답
