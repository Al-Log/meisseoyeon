## 📘 문제 이름

자연수 뒤집어 배열로 만들기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12932)

---

### 🧠 문제 설명

자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴

---

### 💡 아이디어

- reverse()함수 사용

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

`reverse()`함수는 문자형으로 바꾼 후 사용 가능
`map`은 각 요소에 특정 함수를 일괄적으로 적용할 때 사용한다. 모든 요소를 int형으로 변환할때 사용한다.

---

### 다른 사람의 풀이

`rreturn list(map(int, reversed(str(n))))` 한 문장에 return
