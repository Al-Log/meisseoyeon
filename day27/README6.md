## 📘 문제 이름

3진법 뒤집기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/68935#)

---

### 🧠 문제 설명

- 을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return

### 💡 아이디어

- 3진법으로 하려면 3으로 나눈 나머지를 문자열로 바꾸어 더하면 된다.

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

- int(n, base)를 통해 base진법을 10진법으로 변환

### 다른 사람의 풀이

while n:
tmp += str(n % 3)
n = n // 3

    answer = int(tmp, 3)
