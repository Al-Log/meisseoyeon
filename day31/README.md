## 📘 문제 이름

피보나치 수

- 🧩 난이도: level 2
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12945#)

---

### 🧠 문제 설명

피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수

### 💡 아이디어

- 재귀

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

---재귀 로 하면 런타임 에러가 발생하기에 리스트로 문제를 풀어줘야함.

### 다른 사람의 풀이

`def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a`
