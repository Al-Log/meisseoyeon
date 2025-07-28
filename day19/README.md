## 📘 문제 이름

핸드폰 번호 가리기

- 🧩 난이도: level 1
- 🛠 사용 언어: Python
- [문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12948)

### 🧠 문제 설명

전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 \*으로 가린 문자열을 리턴

### 💡 아이디어

---for문 이용하고 별이랑 문자열 합치기

### 배운 것, 느낀 점, 아직 이해되지 않은 점 (선택)

---

### 다른 사람의 풀이

`return '*' * (len(phone_number)-4) + phone_number[-4:]`
