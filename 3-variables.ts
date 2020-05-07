// Declare a block-scoped variable
let myNum = 1.0
myNum++
myNum += 5.0
console.log(myNum)   // 7.0

// Cannot re-declare a block scoped variable.
/* let myNum: string = "hello" */

// Function-scoped or var-scoped variables like JavaScript.
var myVarNum = 1.0
console.log(myVarNum)   // 1.0

// Caution: Can re-declare var-scoped variables and shadow the previous variable.
var myVarNum = 5.0
console.log(myVarNum)   // 5.0

// Cannot re-declare a var-scoped variable with a different type.
/* var myVarNum: string = "hello" // Subsequent variable declarations must have the same type. */

// Declare multiple variables as comma-separated values.
let myNum1 = 1.0, myNum2 = 4.0, result = " result"
console.log(myNum1 + myNum2 + result)  // 5.0 result

// Variables can be declared without a type, then set later and have their type changed.
let hey
console.log(hey)  // undefined
hey = "hello"
console.log(hey)  // hello
hey = 5
console.log(hey)  // 5
