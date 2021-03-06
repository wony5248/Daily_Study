# 인덱스
	추가적인 쓰기 작업과 저장 공간을 활용하여 DB 테이블의 검색 속도를 향상시키기 위한 자료구조
	책의 색인과 같은 역할
	데이터와 데이터의 위치를 포함한 자료구조를 생성하여 빠르게 조회할 수 있게 도와주는 기능
* 인덱스의 자료구조
	* 해시 테이블
	```
	컬럼의 값으로 생성된 해시를 기반으로 인덱스 구현
	시간 복잡도가 O(1)이라 검색 매우 빠름
	부등호(<.>)와 같은 연속적인 데이터를 위한 순차 검색 불가능
	```
	* B+Tree
	```
	자식 노드가 2개이상인 B-Tree를 개선시킨 자료구조
	B-Tree의 리프노드들을 LinkedList로 연결하여 순차 검색 용이하게 해줌
	해시 테이블보다 나쁜 O(logn)이지만 해시테이블보다 흔하게 사용
	```
	
# ORM(Object Relational Mapping)
	객체와 관계형 데이터베이스의 데이터를 자동으로 매핑해주는 것
	객체지향 프로그래밍은 클래스를 사용하고 DB는 테이블을 사용
	객체 모델과 관계형 모델 간에 불일치가 존재
	ORM을 통해 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하여 불일치 해결
* 장점
```
객체 지향적인 코드로 더 직관적이고 비즈니스 로직에 더 집중 가능
재사용 및 유지보수의 편리성 증가
DBMS에 대한 종속성 줄어듦
```
* 단점
```
완벽한 ORM만으로 서비스 구현하기 어렵다
프로시저가 많은 시스템에선 ORM의 객체 지향적인 장점 활용 어렵다.
```

# DB 정규화
* 제1정규형 
```
모든 속성 값이 원자 값을 갖도록 분해
```
* 제2정규형 
```
제1정규형을 만족하고, 기본키가 아닌 속성이 기본키에 완전 함수 종속이도록 분해
완전 함수 종속이란 기본키의 부분집합이 다른 값을 결정하지 않는 것을 의미한다.)
```
* 제3정규형  
```
제2정규형을 만족하고, 기본키가 아닌 속성이 기본키에 직접 종속하도록 분해
이행적 종속이란 A->B->C가 성립하는 것으로, 이를 A,B와 B,C로 분해하는 것이 제3정규형이다
```
* BCNF 정규형 
``` 
제3정규형을 만족하고, 함수 종속성 X -> Y 가 성립할때 모든 결정자 X가 후보키가 되도록 분해
```
# 트랜잭션
	하나 이상의 쿼리를 처리할 때 동일한 Connection 객체를 공유하여 에러가 발생한 경우 모든 과정을 되돌리기 위한 방법
* ACID
	* Atomicity(원자성) 
	```
	트랜잭션에 포함된 작업은 전부 수행되거나 전부 수행되지 않아야 한다.
	```
	* Consistency(일관성) 
	```
	트랜잭션을 수행하기 전이나 후나 데이터베이스는 항상 일관된 상태를 유지해야 한다.
	```
	* Isolation(고립성) 
	```
	수행 중인 트랜잭션에 다른 트랜잭션이 끼어들어 변경중인 데이터 값을 훼손하지 않아야 한다.
	```
	* Durability(지속성)  
	```
	수행을 성공적으로 완료한 트랜잭션은 변경한 데이터를 영구히 저장해야 한다.
	```
# DB 락의 종류
	DB락은 여러개의 트랜잭션 들이 하나의 데이터로 동시에 접근하려고 할때 제어해주는 도구
* 공유락(LS, Shard Lock)
```
트랜잭션이 읽기를 할때 사용하는 락, 데이터 읽을 수 있지만 쓸수는 없음
```
* 베타락(LX, Exclusive Lock)
```
트랜젝션이 읽고 쓰기를 할때 사용하는 락, 데이터 읽고 쓸 수 있음
```

# RDBMS와 NoSQL 차이
* RDBMS
	2차원의 행과 열로 데이터의 관계를 관리하는 DB
	* 장점
	```
	스키마에 맞추어 데이터를 관리하기에 데이터의 적합성을 보장 가능
	```
	* 단점
	```
	시스템 커질수록 쿼리가 복잡해지고 성능이 저하되고 수평적 확장이 어렵다
	```
* NoSQL
	RDBMS가 비대해짐에 따라 관계가 복잡해져, 이를 극복하기 위해 등장하게 된 DB
	* 장점
	```
	NoSQL은 스키마 없이 Key-Value 형태로 관리하기에 더 자유롭게 데이터 관리 가능
	```
	* 단점
	```
	중복데이터 추가가 가능하기에 이에 대한 관리 필요
	```
# Hint란?
	힌트란 SQL을 튜닝하기 위한 지시구문이다.
	개발자가 직접 최적의 실행 계획을 제공하는 것

# 클러스터링 vs 리플리케이션
* 클러스터링
	여러개의 DB를 수평적인 구조로 구축하여 Fail Over한 시스템을 구축하는 방식
	동기 방식으로 노드들 간의 데이터를 동기화 한다.
	* 장점
	```
	1개의 노드가 죽어도 다른 노드가 살아 있어서 시스템 장애없이 운영 가능
	```
	* 단점
	```
	여러 노드들간의 데이터를 동기화 하는 시간이 필요하므로 리플리케이션에 비해 쓰기 성능 떨어짐
	```
* 리플리케이션
	여러개의 DB를 권한에 따라 수직적인 구조(Master-Slave)로 구축하는 방식
	비동기 방식으로 노드들 간의 데이터 동기화 한다.
	* 장점
	```
	비동기 방식으로 데이터가 동기화 되기 때문에 지연시간이 거의 없음
	```
	* 단점
	```
	노드들 간의 데이터가 동기화되지 않아 일관성있는 데이터를 얻지 못할 수 있다.
	```
