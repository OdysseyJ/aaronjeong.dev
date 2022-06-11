text = "hello world jane aaron"

# 기본적으로 있을때는 똑같이 동작한다.
f_result = text.find("jane")
i_result = text.index("jane")
range_find = text.find("h", 0, 1)
print(range_find)
print(f_result)
print(i_result)