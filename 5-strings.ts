// Common operations
let hello = "Hello"
console.log(hello.length)  // 5
console.log(hello.toLowerCase())  // hello
console.log(hello.toUpperCase())  // HELLO

// Unicode
let namaste = "नमस्ते"
console.log(namaste)  // नमस्ते

// Length of string

// Caution: Not unicode-aware length.
let smiley = "😁"
console.log(smiley.length)  // 2

// Unicode-aware length.
console.log([...smiley].length)  // 1

// Loop over characters of string

// Caution: Not unicode-aware length.
for (let i = 0; i < smiley.length; i++) {
    console.log(smiley.charAt(i))  // Malformed characters.
}

// Unicode-safe way to loop over string.
const chars = [...smiley]
chars.forEach (function (char) {
    console.log(char)  // 😁
})

// Substrings

// Using number of characters
let helloWorld = "Hello World"
console.log(helloWorld.substr(6, 5))  // World

// Allows overflow.
console.log(helloWorld.substr(6, 30))  // World

// Between two indices.
console.log(helloWorld.substring(6, 11))  // World

// Allows overflow.
console.log(helloWorld.substring(6, 30))  // World

// TODO: Slice function

// Includes/contains substring
console.log(hello.includes("llo"))  // true
console.log(hello.includes("wor"))  // false

// Split
console.log(helloWorld.split(" "))  // [ 'Hello', 'World' ]
