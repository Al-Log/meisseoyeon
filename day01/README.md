## 📘 문제 이름

자릿수 더하기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12931#)

---

### 🧠 문제 설명

자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 문제.

---

### 💡 아이디어

- 정수를 문자로 받아온다. `str(n)`
- 더할 때는 `int`로 형 변환한다.

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

`for i in lst:` lst(문자열)의 각 문자(자릿수)를 하나씩 꺼내서 i에 담아 반복

---

### 다른 사람의 풀이

`return sum([int(i) for i in str(n)])` 한 문장에 sum까지 해서 return
