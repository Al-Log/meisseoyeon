## 📘 문제 이름

제일 작은 수 제거하기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12935#)

---

### 🧠 문제 설명

가운데 글자를 반환

---가장 작은 수를 제거한 배열을 리턴하는 함수. 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴

### 💡 아이디어

- remove(min())

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

---

### 다른 사람의 풀이

`return [i for i in mylist if i > min(mylist)]`
