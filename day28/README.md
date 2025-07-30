## 📘 문제 이름

이상한 문자 만들기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12917#)

---

### 🧠 문제 설명

각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수

### 💡 아이디어

- for문중첩

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

새로운 리스트를 만들어서 단어를 넣고 그 단어마다 포문을 돌린다.

### 다른 사람의 풀이

`return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))`
