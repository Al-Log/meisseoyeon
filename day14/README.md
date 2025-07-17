## 📘 문제 이름

음양 더하기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/76501)

---

### 🧠 문제 설명

정수들의 절대값을 담은 배열과 부호를 담은 배열이 주어진다. 실제 정수들의 합을 구하라

### 💡 아이디어

---마이너스인 것만 부호를 바꾸어서 넣어준다.

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

---

### 다른 사람의 풀이

`return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))`
