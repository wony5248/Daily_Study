## React 정리
* JSX
    * React에서 사용하는 문법으로 마크업과 로직 둘 다 포함하는 컴포넌트 단위로 개발이 가능하게 하는 문법
* 함수 컴포넌트와 클래스 컴포넌트
    * 함수 컴포넌트 
    ```
    function Welcome(props) {
        return <h1>Hello, {props.name}</h1>;
    }
    ```
    * 클래스 컴포넌트
    ```
    class Welcome extends React.Component {
        render() {
            return <h1>Hello, {this.props.name}</h1>;
        }
    }
    ```
    
* 컴포넌트 합성
    * 컴포넌트는 자신의 출력에 다른 컴포넌트를 참조할 수 있다.
    * Ex) button, form
    ```
    function App() {
        return (
            <div>
                <Welcome name="Sara" />
                <Welcome name="Cahal" />
                <Welcome name="Edite" />
            </div>
         );
    }
    ```
* props
    * props는 읽기 전용이다.
    * 모든 React 컴포넌트는 자신의 props를 다룰 때 반드시 순수 함수처럼 동작해야 한다.
    * 순수함수
    ```
    function sum(a, b) {
        return a + b;
    }
    ```
    * not 순수함수
    ```
    function withdraw(account, amount) {
        account.total -= amount;
    }
    ```
 

