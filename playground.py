number_dic_ko = ("", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구")
place_value1_ko = ("", "십", "백", "천")
place_value2_ko = ("", "만", "억", "조", "경")


def split_number(number, n):
    """number를 n자리씩 끊어서 리스트로 반환한다."""
    res = []
    div = 10**n
    while number > 0:
        number, remainder = divmod(number, div)
        res.append(remainder)
    return res


def convert_lt_10000(number, delimiter):
    """10000 미만의 수를 한글로 변환한다.
       delimiter가 ''이면 1을 무조건 '일'로 바꾼다."""
    res = ""
    return res


print(split_number(9999, 1))
print(convert_lt_10000(9999, 'A'))