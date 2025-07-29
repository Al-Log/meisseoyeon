## 📘 문제 이름

이진 변환 반복하기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/70129#)

---

### 🧠 문제 설명

- 이진변환: x의 모든 0을 제거. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꾼다.
- 0과 1로 이루어진 문자열 s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return

### 💡 아이디어

- while True: s가 1이 될 때 까지 계속 반복
- s.replace("0",'')

---

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

- bin(len(s))[2:]: 이진수로 변경하고 맨 앞에 "0b"을 생략하게 해준다.

### 다른 사람의 풀이

while s != '1':
a += 1
num = s.count('1')
b += len(s) - num
s = bin(num)[2:]
return [a, b]
