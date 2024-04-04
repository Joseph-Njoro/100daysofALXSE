// randomNumber.js

export function generateRandomNumber(min, max) {
    return Mathfloor(Math.random() * (max - min + 1)) + min;
  