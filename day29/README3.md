## 📘 문제 이름

k번째 수

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42748#)

---

### 🧠 문제 설명

- 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구해서 배열을 만든다.

### 💡 아이디어

- commands는 2차원 배열이다. 그 배열의 요소를 for문을 이용해 뽑는다.

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

-

### 다른 사람의 풀이

`return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))`
