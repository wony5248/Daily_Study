const arr = [1, 2, 3, 4, 5, 6, 7];

let result= arr.reduce((acc, cur)=> {
    acc.push(cur * 10)
    return acc
}, [])


let result1= arr.reduce((acc, cur)=> {
    if (cur % 2 == 0)
        acc.push(cur)
    return acc
}, [])
console.log(result)
console.log(result1)