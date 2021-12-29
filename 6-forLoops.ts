// Traditional for-loop

var arr = [1, 2, 3, 4]
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]) // 1, 2, 3, 4
}

// for-in loop returns *indexes* and not values.

var arr = [1, 2, 3, 4]
for (let num in arr) {
    console.log(num) // "0", "1"", "2", "3"
}

// Using var in the for-in loop keeps it around after the loop

var arr = [1, 2, 3, 4]
for (var num in arr) {
    console.log(num) // "0", "1"", "2", "3"
}
console.log(num) // "3"

// for-of loop returns values.

var arr = [1, 2, 3, 4]
for (let num of arr) {
    console.log(num) // 1, 2, 3, 4
}
