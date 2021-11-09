const factorial = (num) => {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
};

const fn = (N) => {
  const reminder = N % 2;
  const twos = Math.floor(N / 2);

  let possibilities = 0;
  for (let i = twos + 1; i <= N; i++) {
    possibilities += factorial(i) / (factorial(N - i) * factorial(i - N + i));
  }
  possibilities = reminder ? possibilities : possibilities + 1;
  console.log(possibilities);
};
