rock = '바위'
scissors = '가위'
paper = '보'

mine = scissors
yours = paper

win = '이김'
lose = '짐'
draw = '비김'

if mine == yours:
    result = draw
else:
    if mine == rock:
        if yours == rock:
            result = draw
        elif yours == paper:
            result = lose
        else:
            result = win
    elif mine == scissors:
        if yours == rock:
            result = lose
        elif yours == paper:
            result = win
        else:
            result = draw
    elif mine == paper:
        if yours == rock:
            result = win
        elif yours == paper:
            result = draw
        else:
            result = lose
    else:
        result = "That can't be possible"

print(result)