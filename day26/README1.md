## 📘 문제 이름

부족한 금액 계산하기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/82612#)

---

### 🧠 문제 설명

- 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 함.
- 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return
- 단, 금액이 부족하지 않으면 0을 return

### 💡 아이디어

- 최종 금액이 -가 되지 않도록 하기
- for문 이용

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

단을 조심할 것.

### 다른 사람의 풀이

`return abs(min(money - sum([price*i for i in range(1,count+1)]),0))`

- if문 대신 min()함수로 부족한 금액이 양수일 경우는 0이 선택되고 음수일 경우는 음수가 선택되어 절댓값을 적용시켰다.
