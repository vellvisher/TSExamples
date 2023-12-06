// Type inference FTW.
let strings = ["a", "b", "c"];

let strings2: string[] = ["d", "e", "f"];

let strings3: string[] = [];

let strings4: string[] = new Array(3).fill("hey");

// Appending.
strings.push("d", "e");
strings.push("f", "g");

// Joining.
strings3 = [...strings, ...strings2];

// Checking length.
console.log(strings.length);

// Accessing elements.
console.log(strings[0]);
console.log(strings[strings.length - 1]);

// Assigning elements.
strings[0] = "a";

// Slices.
strings.splice(0, 1, "a");
strings.splice(0, 2, "a", "b");
strings.slice(0, 4);
strings.slice(0, strings.length);

// Methods.
if (strings.length === 0) {
  console.log("empty");
} else {
  console.log("populated");
}
strings.splice(0, 0, "a");
console.log(strings.shift());
strings = strings.map(str => str + "0");
strings.pop();

// Clearing.
strings.length = 0;
strings = [];

// Using a loop to create a multidimensional array.
let rows = 10, cols = 10;
let dimensional: number[][] = [];
for (let col = 0; col < 10; col++) {
  dimensional.push(new Array(rows).fill(0));
}
