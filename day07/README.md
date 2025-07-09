## 📘 문제 이름

나머지가 1이되는 수 찾기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/87389)

---

### 🧠 문제 설명

자연수를 받고 그 수를 나눈 나머지가 1이 되도록 하는 가장 작은 자연수을 return

---

### 💡 아이디어

- break사용해서 for문을 멈추게 한다.

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

return은 맨 마지막에 하기

---

### 다른 사람의 풀이

`answer = min([x for x in range(1, n+1) if n % x == 1])` 한 문장에 return
