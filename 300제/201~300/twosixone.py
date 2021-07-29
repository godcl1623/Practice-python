'''
오답현황(~210729)
265
266
270

'''
'''
261 Stock 클래스 생성
주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. 클래스는 속성과 메서드를 갖고 있지 않습니다.
'''
"""
class Stock:
    pass;
"""

'''
262 생성자
Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.

삼성 = Stock("삼성전자", "005930")
'''
"""
class Stock:
    def __init__(self, title, code):
        print(title, code);
삼성 = Stock("삼성전자", "005930")
"""

'''
263 메서드
객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.

a = Stock(None, None)
a.set_name("삼성전자")
'''
"""
class Stock:
    def __init__(self, title, code):
        self.title = title;
        self.code = code;
        print(title, code);

    def set_name(self, title):
        self.title = title;
        print(f'종목명: {self.title}');

a = Stock(None, None);
a.set_name('삼성전자');
"""

'''
264 메서드
객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.

a = Stock(None, None)
a.set_code("005930")
'''
"""
class Stock:
    def __init__(self, title, code):
        self.title = title;
        self.code = code;
        print(title, code);

    def set_name(self, title):
        self.title = title;
        print(f'종목명: {self.title}');

    def set_code(self, code):
        self.code = code;
        print(f'코드: {self.code}');

a = Stock(None, None)
a.set_code("005930")
"""

'''
265 메서드
종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.

삼성 = Stock("삼성전자", "005930")
'''

'''
266 객체의 속성값 업데이트
생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.(추가 문제: float 타입 설정이 필요한가?)
'''

'''
267 객체 생성
266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.

항목	정보
종목명	삼성전자
종목코드	005930
PER	15.79
PBR	1.33
배당수익률	2.83
'''
"""
class Stock:
    def __init__(self, title, code, per, pbr, dividend):
        self.title = title;
        self.code = code;
        self.per = float(per);
        self.pbr = float(pbr);
        self.dividend = float(dividend);
        print(self.title, self.code, self.per, self.pbr, self.dividend)
samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
"""

'''
268 객체의 속성 수정
PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.
'''
class Stock:
    def __init__(self, title, code, per, pbr, dividend):
        self.title = title;
        self.code = code;
        self.per = float(per);
        self.pbr = float(pbr);
        self.dividend = float(dividend);
        print(self.title, self.code, self.per, self.pbr, self.dividend)
    
    def set_per(self, per):
        self.per = per;
        print(self.per);

    def set_pbr(self, pbr):
        self.pbr = pbr;
        print(self.pbr);

    def set_dividend(self, dividend):
        self.dividend = dividend;
        print(self.dividend);

samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)

'''
269 객체의 속성 수정
267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.
'''
samsung.set_per(12.75);

'''
270 여러 종목의 객체 생성
아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.(메서드 만들지 말고)

종목명	종목코드	PER	PBR	배당수익률
삼성전자	005930	15.79	1.33	2.83
현대차	005380	8.70	0.35	4.27
LG전자	066570	317.34	0.69	1.37
'''
