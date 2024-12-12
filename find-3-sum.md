
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


function find3Sum(input: number[]) {
  input.sort((a, b) => (a - b));

  const result: number[][] = [];

  for (let i = 0; i < input.length - 2; i++) {
    const value1 = input[i];

    // skip the number if finds a duplicate number
    // for example [-5, -5, -4, ... ]
    // skip the next -5 since if we process it, it ends up adding it to the result as duplicate
    if (i > 0 && value1 === input[i - 1]) {
      continue;
    }

    let j = i + 1; 
    let k = input.length - 1;

    while (j < k) {
      const value2 = input[j];
      const value3 = input[k];

      const sum = value1 + value2 + value3;

      if (sum === 0) {
        result.push([value1, value2, value3]);
        // once it finds the value2 and value3 candidates
        // it should not need to find any more numbers since the only way to get
        // another sum of 0 is duplicated numbers
        break; 
      }
      else if (sum < 0) {
        j++;
      }
      else if (sum > 0) {
        k--;
      }
    }
  }

  return result;
}

function runTestCase(input: number[], expectedResult: number[][]) {
  const inputJson = JSON.stringify(input);
  const actualJson = JSON.stringify(find3Sum(input));
  const expectedJson = JSON.stringify(expectedResult);
  if (actualJson === expectedJson) {
    console.log(`TEST CASE: ${inputJson} PASS`);
  }
  else {
    console.log(`TEST CASE: ${inputJson} FAILED - EXPECTED: ${expectedJson} - ACTUAL: ${actualJson}`)
  }
}

runTestCase([-5, -2, 0, -1, 1, 1, 4], [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1]])
runTestCase([0, 0, 0, 0], [[0, 0, 0]])
runTestCase([0, 1, 2, 3], [])
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
function find3Sum(input) {
    input.sort((a, b) => (a - b));
    const result = [];
    for (let i = 0; i < input.length - 2; i++) {
        const value1 = input[i];
        // skip the number if finds a duplicate number
        // for example [-5, -5, -4, ... ]
        // skip the next -5 since if we process it, it ends up adding it to the result as duplicate
        if (i > 0 && value1 === input[i - 1]) {
            continue;
        }
        let j = i + 1;
        let k = input.length - 1;
        while (j < k) {
            const value2 = input[j];
            const value3 = input[k];
            const sum = value1 + value2 + value3;
            if (sum === 0) {
                result.push([value1, value2, value3]);
                // once it finds the value2 and value3 candidates
                // it should not need to find any more numbers since the only way to get
                // another sum of 0 is duplicated numbers
                break;
            }
            else if (sum < 0) {
                j++;
            }
            else if (sum > 0) {
                k--;
            }
        }
    }
    return result;
}
function runTestCase(input, expectedResult) {
    const inputJson = JSON.stringify(input);
    const actualJson = JSON.stringify(find3Sum(input));
    const expectedJson = JSON.stringify(expectedResult);
    if (actualJson === expectedJson) {
        console.log(`TEST CASE: ${inputJson} PASS`);
    }
    else {
        console.log(`TEST CASE: ${inputJson} FAILED - EXPECTED: ${expectedJson} - ACTUAL: ${actualJson}`);
    }
}
runTestCase([-5, -2, 0, -1, 1, 1, 4], [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1]]);
runTestCase([0, 0, 0, 0], [[0, 0, 0]]);
runTestCase([0, 1, 2, 3], []);

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

**Playground Link:** [Provided](https://www.typescriptlang.org/play/?#code/PTAEHMEsDcFMDtQENFIE5qQT1AewGajwCuAtgEaxoDOAUCMgFygDaAtAKwA0obATDwAMPNgEYe40JIAsAXXph8keABMIaXMQAO1PIQDMRMpRqgAFkmjLwoamT2hBC0LAAeW2AGMALrDVpYOwAbb2YWdm4pHjkedgEoqVlYsSEJWXlnalwg4m9IXFQtLQ0kTzNnSG9QUkhwMyrKUEpvXzRQb1xbXDQq7zNYZAxsUCUab2cIkXiUxwk50Dlnb0w4GgH8DVJeDl4APilQQ4AKSABKZ3xul1KzUEgjCioeJVV2-qI3Kr4Hk1BPFBUkBUSF8uiOACseABrU5vEF-FDmSwDOxbAiOC5XSF3Vog9abO6gADUUkxbShPEqVDxyF67wQanR6EwOHIpShAHd0CpKW9lFCcQByXSkboDWD4JSeSAIKoc-rwZxBCVVahAgYWXTwWDgEEwAYkR5tAGgNC1eq2dVI3RaXBqvJwH5UWgXSBjHHUvIFCrMTg8cG++JQ5jSQ6o336Hhq+CeFH2AA8szuMYCpFloHBTS8SGI1AGkEIHIGKi8qfTFKW71RoA5kCCQSztlISHrzoYkF9kQDSeDC2Y4d4kmUnjL8Cq4J9239zEkvekUfswhGmle4A02lYfoSMVAUNgsC0yZHsDTY4zk633fnoAA0iGF1tBKAGEXquaqtq-Mga8MOrYoZAh4qNoQSQP8vhOqYr4FEEOBcmef4BLaPSgMQ8CQAAjsQAxrpoOjOAUsYZsmJauKAAC85G7iRbhRh0h59CisDoGULq0PgaE+PkiAvCo+gAMpkCc8BaLkzCGiYLCyLCADetCHMooneAAdFkPRHEcSA8OQsLkfsmm8E0pynAA3C6hyeAU1BVAEwShJBUlSRRrCyGZ8nLm0RzKlU9xUYIJmEomim5MpyrwOAfSGXwAWQESRKye5FlWVU0AtthojOcF3gsJArnmYcz5gNQAEMe8ElUHchC8boSCgMBWigeBBrGM6BWFR5LiuEgpANQMkxTrw17KcNoDyG1DDFYBbwGp82yWjG+aFgMxS4LG1C6JUlJVAyugbkgKiAuFOLtJ0jGmoExAhMguj1Y1eKJZVoAnKA+xPgAZG9oCpTksAZZRVFZTlhmiNJoByW1SVjso2FmW1AC++WHN5xEA8SUgBQ9yMCgDIkhWFEW3Gw6OIzWZh1gMEKgImMJgw9kPWV9aWwN8ONKSw4J5RDfzJYzP2GKzuQsFCeV09z8AM9WVHfelaPS8zstM-oblcwWT2S5RjgJVzhy2ZdKmidQZhHCwcuSHL8Ry-o0mw9rDCEfmVTVdNvPYd8JqWwiqhAnidDa+1lS2GYmhBGo8C4B++5qH+vHIPAOCigEkG6NGRFnTBcG-p04CwOMfsMCg4f9G01bok+kA3SBYF4qHLU0KLhzkAESBQhjXMI1zsBBHmj1HNWiaCFr2vgnFNvw6Lnfd6rvf2K9g9c1CbBsKPBXtyv7kI+5ATeMQaCILrIRmRvHExl6e9oQAKoE3gAMJIHmwlKeJtdSTwbgeD4fgAEoXSET9Go5oNwZiwZllAAUlkRAVFQH8QAPIADlVLLGsAWLAD9cimXcpZcWVRSjbxbOAgozloHwMQWacKKCji8QEkJLKxkbZYIZm-LwvgVAEMgaAYhCDrJkKgPgVBTCP4qG-nZDBClCCaR8MQfBECKIawESwthc9gHZFgKFXA4AjgAANz4AFF+Ln1ANfAAgvxHRzAAAkMkwEQLhqAAACiY-imjRGgFXhPAYQD6YqLURo7ReiDHGNMRYqxuNvBsNsQAMSMQASQADI6IACKGR0QADTsTo6+uiEnBPkX4cJhkjGZIAKpGNicE3BUigjhOcevWgG80AXyvrfe+-V+CpEHPMGQSRWD9S6ckeIkgQbJEkEuEG0laANPgJfayzTYDGyXAsoQ3TwiLMcOkc4kzpk3zvnMlgoyeDxCtrEaSQA)
      
