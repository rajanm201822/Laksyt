'use strict';

const dogs = [];

for (let i = 1; i <= 6; i++) {
  dogs.push(prompt(`Enter the name of dog ${i}:`));
}

dogs.sort((a, b) => b.localeCompare(a));

const list = document.getElementById('dogs');

for (const dog of dogs) {
  const li = document.createElement('li');
  li.textContent = dog;
  list.appendChild(li);
}