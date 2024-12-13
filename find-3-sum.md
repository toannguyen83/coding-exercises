```ts
// given an array of numbers
// a: [-5, -2, 0, -1, 1, 1, 4]
// find groups of 3 numbers having sum of 0
// expected result: [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1]]

// solution approach
// it might be better to sort the array first
// [-5, -2, -1, 0, 1, 1, 4]
// traverse from -5 -> 1   (i)
// for each i number, find the next 2 number candidates (j, k) that can have sum of 0
// for j, iterate from i + 1
// for k, iterate at the end of array backward, i think it's more efficient when
// left side has negative number and right side has positive number

// first iteration
// i: -5, j: -2, k: 4  sum: -3, since sum < 0, increment j because if we decrement k,
// the sum will be smaller
// i: -5, j: 0, k: 4: sum: -1, increment j
// i: -5, j: 1, k: 4, sum 0, found group [-5, 1, 4], keep increment j
// i: -5, j: 4, K: 4, sum 0 // we might need a way to skip duplicate numbers we only want to report unique groups
// once j index == k index, stop the search

function find3Sum(array: number[]) {
  array.sort((a, b) => a - b);

  const result: number[][] = [];

  for (let i = 0; i < array.length - 2; i++) {
    const value1 = array[i];

    // skip the number if finds a duplicate number
    // for example [-5, -5, -4, ... ]
    // skip the next -5 since if we process it, it ends up adding it to the result as duplicate
    if (i > 0 && value1 === array[i - 1]) {
      continue;
    }

    let j = i + 1;
    let k = array.length - 1;

    while (j < k) {
      const value2 = array[j];
      const value3 = array[k];

      const sum = value1 + value2 + value3;

      if (sum === 0) {
        result.push([value1, value2, value3]);
        j++;
        // since we found a match, if the next array[j] is the same as previous
        // we should skip it to prevent adding duplicate results
        // but also constraint it to have j < k index
        while (j < k && array[j] === array[j - 1]) {
          j++;
        }
      } else if (sum < 0) {
        j++;
      } else if (sum > 0) {
        k--;
      }
    }
  }

  return result;
}

function runTest(input: number[], expectedResult: number[][]) {
  const inputJson = JSON.stringify(input);
  const actualJson = JSON.stringify(find3Sum(input));
  const expectedJson = JSON.stringify(expectedResult);
  if (actualJson === expectedJson) {
    console.log(`PASS ${inputJson} => ${actualJson}`);
  } else {
    console.log(`FAIL ${inputJson} => ${actualJson} EXPECTED ${expectedJson}`);
  }
}

runTest(
  [-5, -2, 0, -1, 1, 1, 4],
  [
    [-5, 1, 4],
    [-2, 1, 1],
    [-1, 0, 1],
  ]
);
runTest([0, 0, 0, 0], [[0, 0, 0]]);
runTest([0, 1, 2, 3], []);
// corner cases
runTest(
  [-5, -5, -4, -4, 0, 1, 1, 4, 4, 2, 2, 3, 3],
  [
    [-5, 1, 4],
    [-5, 2, 3],
    [-4, 0, 4],
    [-4, 1, 3],
    [-4, 2, 2],
  ]
);
```

<details><summary><b>Output</b></summary>

```ts
"use strict";
// given an array of numbers
// a: [-5, -2, 0, -1, 1, 1, 4]
// find groups of 3 numbers having sum of 0
// expected result: [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1]]
// solution approach
// it might be better to sort the array first
// [-5, -2, -1, 0, 1, 1, 4]
// traverse from -5 -> 1   (i)
// for each i number, find the next 2 number candidates (j, k) that can have sum of 0
// for j, iterate from i + 1
// for k, iterate at the end of array backward, i think it's more efficient when
// left side has negative number and right side has positive number
// first iteration
// i: -5, j: -2, k: 4  sum: -3, since sum < 0, increment j because if we decrement k,
// the sum will be smaller
// i: -5, j: 0, k: 4: sum: -1, increment j
// i: -5, j: 1, k: 4, sum 0, found group [-5, 1, 4], keep increment j
// i: -5, j: 4, K: 4, sum 0 // we might need a way to skip duplicate numbers we only want to report unique groups
// once j index == k index, stop the search
function find3Sum(array) {
  array.sort((a, b) => a - b);
  const result = [];
  for (let i = 0; i < array.length - 2; i++) {
    const value1 = array[i];
    // skip the number if finds a duplicate number
    // for example [-5, -5, -4, ... ]
    // skip the next -5 since if we process it, it ends up adding it to the result as duplicate
    if (i > 0 && value1 === array[i - 1]) {
      continue;
    }
    let j = i + 1;
    let k = array.length - 1;
    while (j < k) {
      const value2 = array[j];
      const value3 = array[k];
      const sum = value1 + value2 + value3;
      if (sum === 0) {
        result.push([value1, value2, value3]);
        j++;
        // since we found a match, if the next array[j] is the same as previous
        // we should skip it to prevent adding duplicate results
        // but also constraint it to have j < k index
        while (j < k && array[j] === array[j - 1]) {
          j++;
        }
      } else if (sum < 0) {
        j++;
      } else if (sum > 0) {
        k--;
      }
    }
  }
  return result;
}
function runTest(input, expectedResult) {
  const inputJson = JSON.stringify(input);
  const actualJson = JSON.stringify(find3Sum(input));
  const expectedJson = JSON.stringify(expectedResult);
  if (actualJson === expectedJson) {
    console.log(`PASS ${inputJson} => ${actualJson}`);
  } else {
    console.log(`FAIL ${inputJson} => ${actualJson} EXPECTED ${expectedJson}`);
  }
}
runTest(
  [-5, -2, 0, -1, 1, 1, 4],
  [
    [-5, 1, 4],
    [-2, 1, 1],
    [-1, 0, 1],
  ]
);
runTest([0, 0, 0, 0], [[0, 0, 0]]);
runTest([0, 1, 2, 3], []);
// corner cases
runTest(
  [-5, -5, -4, -4, 0, 1, 1, 4, 4, 2, 2, 3, 3],
  [
    [-5, 1, 4],
    [-5, 2, 3],
    [-4, 0, 4],
    [-4, 1, 3],
    [-4, 2, 2],
  ]
);
```

</details>

<details><summary><b>Compiler Options</b></summary>

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictPropertyInitialization": true,
    "strictBindCallApply": true,
    "noImplicitThis": true,
    "noImplicitReturns": true,
    "alwaysStrict": true,
    "esModuleInterop": true,
    "declaration": true,
    "target": "ES2017",
    "jsx": "react",
    "module": "ESNext",
    "moduleResolution": "node"
  }
}
```

</details>

**Playground Link:** [Provided](https://www.typescriptlang.org/play/?#code/PTAEHMEsDcFMDtQENFIE5qQT1AewGajwCuAtgEaxoDOAUCMgFygDaAtAKwA0obATDwAMPNgEYe40JIAsAXXph8keABMIaXMQAO1PIQDMRMpRqgAFkmjLwoamT2hBC0LAAeW2AGMALrDVpYOwAbb2YWdm4pHjkedgEoqVlYsSEJWXlnalwg4m9IXFQtLQ0kTzNnSG9QUkhwMyrKUEpvXzRQb1xbXDQq7zNYZAxsUCUab2cIkXiUxwk50Dlnb0w4GgH8DVJeDl4APilQQ4AKSABKZ3xul1KzUEgjCioeJVV2-qI3Kr4Hk1BPFBUkBUSF8uiOACseABrU5vEF-FDmSwDOxbAiOC5XSF3Vog9abO6gADUUkxbShPEqVDxyF67wQanR6EwOHIpShAHd0CpKW9lFCcQByXSkboDWD4JSeSAIKoc-rwZxBCVVahAgYWXTwWDgEEwAYkR5tAGgNC1eq2dVI3RaXBqvJwH5UWgXSBjHHUvIFCrMTg8cG++JQ5jSQ6o336Hhq+CeFH2AA8szuMYCpFloHBTS8SGI1AGkEIHIGKi8qfTFKW71RoA5kCCQSztlISHrzoYkF9kQDSeDC2Y4d4kmUnjL8Cq4J9239zEkvekUfswhGmle4A02lYfoSMVAUNgsC0yZHsDTY4zk633fnoAA0iGF1tBKAGEXquaqtq-Mga8MOrYoZAh4qNoQSQP8vhOqYr4FEEOBcmef4BLaPSgMQ8CQAAjsQAxrpoOjOAUsYZsmJauKAAC85G7iRbhRh0h59CisDoGULq0PgaE+PkiAvCo+gAMpkEczLYMwhomCwsiwgA3rQhwiVgAB0WQ9Ecwk8OQsLkfswm8E0pynAA3C6hyeAU1BVAEwShJBkmSRRrCyMZcnLm0RzKlU9xUYIhmEomCmKcq8DgH0el8L5kBEkSMkuaZ5lVNALbYaIDkKSwkBOSZhzPmA1AAQx7ziVQdyELxuhIKAwFaKB4EGsYzrZTlrkuK4SCkNVAyTFOvDXopfWgPIjUMHlgFvAanzbJaMb5oWAzFLgsbULolSUlUDK6BuSAqICwU4u0nSMaagTECEyC6FVNV4rFJWgCcoD7E+ABkj2gIlOSwCllFUWl9xsIkMWNXFY7KNhxmNQAvllhwecRVH3CSoi+ddMMCt9QxKUFIW3H9iNQzWZh1gMEKgImMKgLJgN-PFr1JbA3xoyyLDgpllNmfAFk0+9hgM9gLBQpl11Axz1ZUW9yXEpz2HfCSYuwPozmUwWt0i5RjgA5TR3WYpWi5mYRwsLLkiy-Esv6FJYMa+CUUW5Tw3DgMr6XGhagVc23hlJShCHdqrhVGlzN3Loh3UG1AxIDaARWJodAa01r7UGYmhBGoI2HpU+2gMUsBwGeW07TYF1gTSVknd4Mcaww5C5MgQRZFT7PLEgyieb0nQWI6makzRriC9l8qE7dnfUc9gyMwHX2j7zmY41J5O941VtEjbgOQ5Tq+A7AtczcrCZq3PseL8vhzr41m95jdRzVg96uU1CbBsEfoAn0-LmQy5ATeMQaCICXITGW-HEYxeh-mhAAKoEbwJx4A6xskVNAkkeBuA8D4PwAAlY6IQxL1XgbISS6s2Yc2UDAgAUlkRAVFiH8QAPIADllLLGsAWLAUCYFGRcgQv2PhiAtlIQUBylDaH0LNMFJhRxeICSEkQ3IBkLYcJasg3wKheHkNAAIuhFlhFQHwMwpBXhFHoOsmww4SthJcJ4WQiiqtdEoKUWQm+9csjKkCrgcARwAAGAAFAAgvxfioAAAk0kpHeGUeDCi+xAmlE-uYgo4M3FGJfocM+AwKbZQIdkWAzjXFuIAGJeIAJIABkAlBOgbkUJ4SSlRO4UECpABRAAGh4upABhUBdSAAiJTrGKNCfE1+tA35oDARA-WW5+CpEHPMGQSRWBdRmckeIkhRCzPYJIJcKypK0GGfAcBFl9ZLkOUIVZLAjmOHSOcHZezIGnPmPEM2sQtkMDMt-Yq-w8x0CuaM66XVxnXjYNeDZ8xrzXniPcngDyfnzOiKsrc9zYWAphcka8kgHmblBTwPg6QuC0FOEAA)
