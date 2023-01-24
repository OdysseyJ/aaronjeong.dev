import sys

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours

N = int(input())
words = set()
for _ in range(N):
    word = sys.stdin.readline().strip()
    words.add(word)

sorted_words = sorted(words, key=lambda x: (len(x), x))
for word in sorted_words:
    print(word)