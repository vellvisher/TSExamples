// Initialization
let emptyDictionary: {[key: string]: number} = {};
let anotherEmptyDict: {[key: string]: number} = {};
let strings: {[key: string]: string} = {
    'a': 'A',
    'b': 'B',
};

// Accessing and assigning elements
console.log(strings['a']);
strings['a'] = 'AZ';
strings['a'] = 'AX';

// Handling non-existing keys
let a = strings['a'];
if (a) console.log(a);

// Removing
delete strings['a'];
delete strings['nope'];

// Updating
strings['a'] = 'A';

// Iterating
for (const [key, val] of Object.entries(strings)) console.log(`${key}: ${val}`);
for (const key of Object.keys(strings)) console.log(`KEY: ${key}`);
for (const val of Object.values(strings)) console.log(`VAL: ${val}`);

// Getting all keys & values
let keys = Object.keys(strings);
let vals = Object.values(strings);

// Clearing everything
strings = {};

console.log(Object.keys(strings).length);
