## 📘 문제 이름

가장 가까운 같은 글자

- 🧩 난이도: level 2
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/142086#)

---

### 🧠 문제 설명

s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자와의 거리를 반환한다. 없으면-1

### 💡 아이디어

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

---enumerate(): 반복문을 진행할 때 문자의 인덱스와 문자를 하나씩 꺼내온다.

### 다른 사람의 풀이

def solution(s):
answer = []
dic = dict()
for i in range(len(s)):
if s[i] not in dic:
answer.append(-1)
else:
answer.append(i - dic[s[i]])
dic[s[i]] = i

    return answer
