'use strict';

const target = document.getElementById('target');

const first = document.createElement('li');
first.textContent = 'First item';
first.classList.add('my-item');
target.appendChild(first);

const second = document.createElement('li');
second.textContent = 'Second item';
first.classList.add('my-item');
target.appendChild(second);

const third = document.createElement('li');
third.textContent = 'Third item';
first.classList.add('my-item');
target.appendChild(third);