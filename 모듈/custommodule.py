def rsp():
    import random
    selectors = ['가위', '바위', '보']
    return random.choice(selectors)

paper = '보'
rock = '바위'
scissors = '가위'