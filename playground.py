text = "hello world jane aaron"

# 기본적으로 있을때는 똑같이 동작한다.
f_result = text.find("jane")
i_result = text.index("jane")
range_find = text.find("h", 0, 1)
print(range_find)
print(f_result)
print(i_result)

# Find와 Index는 없을때 차이가 난다.
# ff_result = text.find("z")
# ii_result = text.index("z")
# print(ff_result)
# print(ii_result)

# Count
c_result = text.count(" ")
print(c_result)

# Startswith
s_result = text.startswith("h")
ss_result = text.startswith("j")
S_result = text.startswith("H")
SS_result = text.upper().startswith("H")
print(s_result)
print(ss_result)
print(S_result)
print(SS_result)

test = "hello world"
print("#####")
print(test.capitalize())
print(test.upper())
print("#####")
print(len("assdf"))

print(sorted([10, 5, 20], reverse=True))