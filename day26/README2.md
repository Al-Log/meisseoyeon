## 📘 문제 이름

문자열 다루기 기본

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12918#)

---

### 🧠 문제 설명

- 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수

### 💡 아이디어

- len()
- or을 쓸 때는 len을 생략하면 안됨

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

s.isdigit() : 숫자인지 판별

### 다른 사람의 풀이

`return s.isdigit() and len(s) in [4,6]`

- len(s) 값이 4,6에 있는지 확인하는 문법
