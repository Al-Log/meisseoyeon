## 📘 문제 이름

두 정수 사이의 합

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12912)

---

### 🧠 문제 설명

두 정수 사이에 속한 모든 정수의 합을 리턴한다. a와b의 대소관계는 정해져있지 않다.

### 💡 아이디어

조건문을 사용하여 a,b의 대소관계를 나누고 for문을 이용하여 정수의 합을 구한다.

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

---

### 다른 사람의 풀이

`return sum(range(min(a, b), max(a, b) + 1))`
