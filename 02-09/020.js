class Person {
    constructor(name, age){
        this.age = 40;
    }
    sayName(){
        console.log(`${this.name}, ${this.age}`)
    }
}

const p = new Person("hello", 30);
console.log(p.name)
console.log(p.age)