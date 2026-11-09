

const a = Number(prompt('First integer:'));
const b = Number(prompt('Second integer:'));
const c = Number(prompt('Third integer:'));

document.querySelector('#result').innerHTML =
    `Sum: ${a + b + c}<br>Product: ${a * b * c}<br>Average: ${(a + b + c) / 3}`;