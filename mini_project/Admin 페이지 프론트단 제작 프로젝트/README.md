# Admin 페이지 프론트단 제작 프로젝트

## 프로젝트 소개
KREAM의 신규 데이터가 담겨있는 데이터베이스 정보를 보여주는 admin page 만들기
- KREAM을 크롤링한 데이터를 데이터베이스에 저장되었다고 가정
- 데이터베이스에 저장된 데이터를 Admin page 방식으로 구현하는게 목표
- Admin page 방식은 Bootstrap(v5.3) 활용


## 프로젝트 기간
2024.03.26 ~ 2024.03.31


## 사용 기술
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">


## 프로젝트 내용

### 기본 요구 사항
-  카테고리(셀렉트)를 클릭하면 상의, 하의, 신발, 패션잡화 메뉴가 나오게 코드 작성
- 입력 버튼 안에 “제품명을 입력해주세요"
- 조회 버튼이 입력창 옆에 붙어 있도록 코드 작성
- 테이블을 이용해 최 상단에는 속성 값을 넣고 하단에는 데이터가 입력되도록 코드 작성
- 최하단에는 페이지 네이션 기능이 나타나도록 코드 작성

### 더 만들어 볼 기능
- 성별로 구별할 수 있는 버튼 또는 테이블 속성값에 성별을 구분할 수 있는 속성 넣기
- 카테고리 앞에 체크 박스를 하나씩 넣어주고, 선택된 체크 박스를 삭제하는 버튼을 만들기  
  (그 위치는 조회 버튼이 있는 라인의 가장 끝)
- 신규 등록 상품 옆에  신규 등록 상품 (2024-01-22) 형태로 변경  
  (날짜는 업데이트된 일자가 반영되도록)
- 테이블 하단 또는 상단에 github 아이콘을 삽입 & 이미지 클릭하면 여러분의 깃허브 주소로 이동
  

## 실행화면
### 메인 화면
  <img width="997" alt="전체 스크린샷" src="https://github.com/dayeonkimm/OZ/assets/164486991/6e6d24bf-a1bb-4318-9c66-eddbe2979ba9">


---
### 카테고리 필터링
  ![카테고리 필터링](https://github.com/dayeonkimm/OZ/assets/164486991/ff3a1893-1053-4ac2-b107-9872e62619fc)
select 를 이용해서 상의, 하의, 신발, 패션잡화 카테고리 필터링 가능

---
### 성별 필터링
![성별 필터링](https://github.com/dayeonkimm/OZ/assets/164486991/1a083abb-3819-4414-b657-00b951bdac63)
radio 를 이용해서 남성, 여성 성별 필터링 가능

---
### 제품명 검색
![제품 검색 필터링](https://github.com/dayeonkimm/OZ/assets/164486991/9ab78503-2952-4f6f-8cda-76a662f7ea6e)
텍스트 입력 후 조회 버튼 클릭 시 텍스트 포함한 제품 검색 가능

---
### 카테고리/성별/제품명 동시 필터링 가능
![필터링 한번에](https://github.com/dayeonkimm/OZ/assets/164486991/704ba08b-8c7c-44a0-8782-03ce760b3851)

---
### 체크박스 전체선택/전체선택 해제 및 삭제
![체크박스 삭제](https://github.com/dayeonkimm/OZ/assets/164486991/ccbe8192-bfd0-4e65-aeea-4bda0c830b7e)
체크박스 전체선택 및 해제 가능
체크박스 선택 후 삭제 버튼 클릭 시 삭제

---
### 깃허브 아이콘 클릭 시 나의 깃허브 링크로 이동
![깃허브 이동](https://github.com/dayeonkimm/OZ/assets/164486991/64c531ba-cbe6-4219-a7f4-8ab9a71fa7ff)

---

## 더 구현해볼 것
- 제품명 검색 시 빈칸이면 "제품명을 입력하세요" alert창
- 제품명 검색 시 포함되는 제품 없을 시 "해당 제품이 없습니다" alert창
- 페이지네이션 실제 작동되도록 구현
