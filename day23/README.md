## 📘 문제 이름

내적

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/70128#)

---

### 🧠 문제 설명

가운데 글자를 반환

--- 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]\*b[n-1]

### 💡 아이디어

- 곱한것의 합

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

---

### 다른 사람의 풀이

`return sum([x*y for x, y in zip(a,b)])`
