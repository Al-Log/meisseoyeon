## 📘 문제 이름

약수의 합

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12928)

---

### 🧠 문제 설명

정수 n을 입력 받아 n의 약수를 모두 더한 값값

---

### 💡 아이디어

- 약수를 구할 때는 어떤 수로 나누어지는지를 확인하면 된다.

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

`for i in n:` n(리스트, 문자열)일 때만 사용 가능. n이 정수라면 오류가 발생.
`for i in range(1,n)` 1부터 n까지의 정수를 차래로 i에 대입한다. `range()`는 지정한 범위의 정수 시퀀스를 생성한다.

---

### 다른 사람의 풀이

`return sum([i for i in range(1, n+1) if n % i == 0])` 한 문장에 sum, 반복문, 조건문까지 해서 return
