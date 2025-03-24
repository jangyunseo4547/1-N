## 1-N
- 하나의 상위 개념에 속해있을 때
- 정규화 : 데이터 베이스는 셀 하나에 하나의 데이터를 지향함.   
    - 정규 이상 
    - 삭제 이상
- 테이블 2개 만들기 / post_id의 중복 제거 (게시글의 내용이 같더라도 고유의 아이디 지님.)
    - 테이블 1 : id(post) / title, comment
    - 테이블 2 : id (primary key) / post_id / comments

## 0. django 설정
`pip install django`
- 프로젝트 생성 django-admin startproject crud . (. 현재 파일에 생성)
- 앱 생성 django-admin startapp posts (posts라는 앱 생성)
- 앱 등록 (setting)
    posts (앱 이름 적어주기) 

- temlates 폴더 생성 
    `'DIRS': [BASE_DIR / 'templates'],`
