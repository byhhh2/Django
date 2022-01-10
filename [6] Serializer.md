- 서버와 클라이언트는 JSON 형식으로 데이터를 주고 받도록 약속 되어있음
- JSON -> Django / Django -> JSON이 Serializer의 역할

<br />

### ModelSerializer

- 모델과 상응하는 기본적인 serializer를 알아서 생성

### 일반 Serializer

- ForeignKey로 연결된 테이블의 정보를 보아야 할 때
