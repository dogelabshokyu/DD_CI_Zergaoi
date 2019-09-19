Vi 주요키워드
==========
## 1. 이동
* n : n번째 줄로 이동
* $ : 마지막줄로 이동
* /춤 : 춤을 춘다.

## 2. 입력모드 전환
* i : 커서 앞
* a : 커서 뒤
* o : 커서밑
* ESC : 명령모드

## 3. 복사 & 붙여넣기
* yy : 줄단위 복사 → 앞에 정수를 붙이면 커서가 위치한 줄 포함 붙인 정수만큼의 줄 복사 
* p : 붙이기
  
  ex)'n'yy (n은 임의의 정수)
   ![1](https://user-images.githubusercontent.com/53134813/65257789-bef8ae00-db3c-11e9-992a-3e730b7d663b.JPG)
     ↑ 커서를 4번째 줄에 위치시키고 '4yy' 명령으로 4~7번째 줄 복사
   ![캡처2](https://user-images.githubusercontent.com/53134813/65257801-c4ee8f00-db3c-11e9-9d41-07aed20b51e3.JPG)
     ↑ 복사 후 커서를 7번째 줄에 위치시키고 'p' 명령으로 7번째 줄 아래에 붙여넣기


## 4. 삭제
* dd : 줄단위 삭제  → 앞에 정수를 붙이면 커서가 위치한 줄 포함 붙인 정수만큼의 줄 삭제
* x : 글자 삭제

 ex) 'n'dd (n은 임의의 정수)
 ![1](https://user-images.githubusercontent.com/53134813/65258771-73470400-db3e-11e9-9d47-2aa92604e458.JPG)
    ↑ 커서를 9번째 줄에 위치시키고 '3dd' 명령 입력
 ![2](https://user-images.githubusercontent.com/53134813/65258775-7510c780-db3e-11e9-9ab3-8365c7a9a506.JPG)
    ↑ 9~11번째 줄 삭제 

## 5. 기타
* u : 취소
