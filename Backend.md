# WAS 와 WS의 차이
* WAS(Web Application Server)
```
비즈니스 로직을 넣을 수 있다.
Tomcat, PHP, ASP, .Net
```
* WS(Web Server)
```
비즈니스 로직 불가
Nginx, Apache
```

# 많은 트래픽에 대처하는 법
* 스케일업 
```
서버에 CPU나 RAM을 추가하여 하드웨어 스펙 향상
```
* 스케일 아웃 
```
서버를 여러 대 추가하여 시스템을 증가시키는 방법
```

# CORS (Cross Origin Resource Sharing)
	도메인이 다른 2개의 사이트가 데이터를 주고 받을 때 발생하는 문제
	서버내에서 요청이 허락된 도메인에만 데이터를 주기위해 사용
	Response의 헤더에 추가해서 요청을 허락할 수 있다.

# Apache
아파치는 기본적으로 멀티프로세스로 구현되어 있지만 설정에 따라 멀티 쓰레드를 같이 운용할 수 있다.

# Tomcat
톰캣은 요청을 처리하기 위한 쓰레드 풀을 관리하고 잇다. 
요청이 오면 쓰레드 풀에서 쓰레드를 꺼내 요청을 처리하도록 한다.

# 디자인 패턴
* 생성패턴

	* 팩토리 패턴 
	``` 
	객체 생성하기 위한 디자인 패턴
	```
	* 추상 팩토리 패턴 
	```
	객체를 생성하는 팩토리를 생성하기 위한 디자인 패턴
	```
	* 빌더 패턴 
	```
	상황에 따라 동적인 인자 필요로 하는 객체 생성하기 위한 디자인 패턴
	```
	* 싱글톤 패턴 
	```
	객체를 1개만 생성하여 항상 참조 가능하게끔 고안된 디자인 패턴
	```
* 구조패턴
	* 어댑터 패턴  
	```
	호환성이 맞지 않는 두 클래스를 연결하여 사용하기 위한 디자인 패턴
	```
	* 프록시 패턴 
	```
	어떤 객체에 접근하기 위해 대리인을 사용하는 디자인 패턴
	```	
	* 데코레이터 패턴
	
	* 퍼사드 패턴  
	```
	어떤 복합적인 기능에 대해 간략화된 인터페이스를 제공하는 디자인 패턴
	```
* 행위 패턴
	* 전략 패턴 
	```
	상황에 따라 다른 전략을 사용하기 위한 디자인 패턴
	```
	* 옵저버 패턴 
	```
	값을 관찰하여 빠르게 반영하기 위한 디자인 패턴
	```
	* 커맨드 패턴 
	```
	실행될 기능을 캡슐화 하여 재사용성이 높은 클래스를 설계하기 위한 디자인 패턴
	```
* DatabaseController=> SingletonPattern을 사용하여 데이터베이스를 제어하는 하나의 인스턴스만을 생성

* DatabasePool => ObjectPool Pattern을 사용하여 데이터베이스 객체를 미리 생성하여 Performance 향상

* UnitFactory => FactoryPattern을 사용하여 객체 생성을 최적화 + Singleton Pattern을 사용하여 하나의 공장을 사용

* BaseFrame => ObserverPattern을 사용하여 사용자의 정보가 생신되면 View의 값들도 갱신되게 함

* PlayerInfo => StrategyPattern을 사용하여 상황에 따라 다른 스킬을 사용


# Servlet 이란?
	서블릿이란 클라이언트의 요청을 처리하고, 그 결과를 반환하는 Servlet 클래스의 구현 규칙을 지킨 자바 웹 프로그래밍 기술이다.
	Spring MVC에서 Controller로 이용된다.

## DI - Dependency Injection 
	한 객체에서 다른 객체를 필요로 하여 의존성을 갖게 하는 기술
## DL - Dependency Look-up 
	한 객체에서 필요로 하는 다른 객체를 찾아서 사용하는 기술
## IoC - Inversion of Control  
	직접 제어해야 하는 부분에 대한 권한을 프레임워크 등에 넘기는 기술
## AOP - Aspect Oriented Programming 
	공통의 관심사항 추출하여 원하는 곳에 적용하는 기술
## VO(Value Object) 
	실제 데이터만을 저장하는 클래스
## DTO(Data Transfer Object)
	데이터를 주고 받기 위해 사용하는 클래스
## BO(Business Object)
	여러 DAO를 활용해 비지니스 로직을 처리하는 클래스
## DAO(Data Access Object) 
	DB에 접근하여 실제 데이터 조회 또는 조작하는 클래스 - Repository 또는 Mapper에 해당

# 디스패처 서블릿
	톰캣과 같은 서블릿 컨테이너를 통해 들어오는 모든 요청을 제일 앞에서 받는 컨트롤러

# Spring에서의 싱글톤
	스프링 컨테이너가 관리하는 객체인 Bean을 싱글톤 패턴으로 구현하여 제공
	private나 static 메소드 없이 객체를 싱글톤으로 관리하여 객체지향 개발 가능

# MVC 패턴이란
	Model-View-Controller 패턴은 아키텍쳐 설계하기위한 디자인 패턴
* Model  
	데이터를 저장하는 컴포넌트
* View  
 	사용자 인터페이스(UI) 컴포넌트
* Controller
	 사용자의 요청을 처리하고 Model과 View를 중개하는 컴포넌트

# Spring MVC
	웹 애플리케이션 개발을 위한 MVC 패턴기반의 웹 프레임 워크
	Dispatcher Servlet: 클라이언트 요청 먼저 받아들이는 서블릿, 요청에 맞는 컨트롤러에게 요청 전달
	Handler Mapping: 해당 요청이 어떤 컨트롤러에게 온 요청인지 검사
	Controller: 클라이언트 요청 받아 처리하여 결과를 디스패처 서블릿에 전달
	ViewResolver: View의 이름을 통해 알맞은 View를 찾음
	View : 사용자에게 보여질 UI
	장점
		의존성 주입을 통해 컴포넌트간의 결합도 낮출 수 있어 단위테스트 용이
		제어의 역전을 통해 빈Bean(객체) 의 생명주기에 관여하지 않고 개발에 집중 가능
	단점
		XML 기반으로 하는 프로젝트 설정 너무 많은 시간 필요함
		톰캣과 같은 WAS를 별도로 설치해야함
	해결책
		Spring Boot
			자동설정을 도입하여 Dispatcher Servlet등과 같은 설정 시간 줄여줌
			프로젝트의 의존성을 독립적으로 선택하지 않고 spring-boot-starter로 모아두어 외부 도구 이용 편리
			내장 톰캣을 제공하여 별도의 WAS 필요 없음

CDN (Content Delivery Network)
	물리적으로 떨어져 잇는 사용자에게 컨텐츠 더 빨리 제공하기 위해 고안된 기술
	CDN은 콘텐츠에 대한 요청 발생시 사용자와 가장 가까운 위치에 존재하는 서버로 매핑시켜, 요청된 파일의 캐싱된 버전으로 요청을 처리
