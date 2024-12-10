
```ts
// given 2 sorted array
// a [4, 5, 7, 9]
// b [-2, 0, 2, 3, 5]
//
// create a function that can return the the 2 arrays merged and also sorted
// from above result, expected value is [-2, 0, 2, 3, 4, 5, 5, 7, 9]

function combineAndSortArrays(array1: number[], array2: number[]) {
  const resultArray: number[] = []

  let index1 = 0;
  let index2 = 0;

  while (index1 < array1.length && index2 < array2.length) {
    let value1 = array1[index1];
    let value2 = array2[index2];

    if (value1 <= value2) {
      resultArray.push(value1);
      index1++;
    }
    else {
      resultArray.push(value2);
      index2++;
    }
  }

  if (index1 < array1.length) {
    resultArray.push(...array1.slice(index1));
  }
  else if (index2 < array2.length) {
    resultArray.push(...array2.slice(index2));
  }

  return resultArray;
}


function runTestCase(array1: number[], array2: number[], expectedResult: number[]) {
  const actualResult = combineAndSortArrays(array1, array2);
  if (JSON.stringify(actualResult) === JSON.stringify(expectedResult)) {
    console.log(`TEST CASE ${JSON.stringify(array1)} ${JSON.stringify(array2)} - PASS`)
  }
  else {
    console.log(`TEST CASE ${JSON.stringify(array1)}, ${JSON.stringify(array2)} FAILED - ACTUAL VALUE = ${JSON.stringify(actualResult)}`)
  }
}

runTestCase([4, 5, 7, 9], [-2, 0, 2, 3, 5], [-2, 0, 2, 3, 4, 5, 5, 7, 9])
runTestCase([1], [0], [0, 1])
runTestCase([7, 15, 18, 20], [-2, 0], [-2, 0, 7, 15, 18, 20])
runTestCase([4, 5, 7, 9], [-2, 0, 2, 3, 5], [-2, 0, 2, 3, 4, 5, 5, 7, 9])
```



<details><summary><b>Output</b></summary>

```ts
"use strict";
// given 2 sorted array
// a [4, 5, 7, 9]
// b [-2, 0, 2, 3, 5]
//
// create a function that can return the the 2 arrays merged and also sorted
// from above result, expected value is [-2, 0, 2, 3, 4, 5, 5, 7, 9]
function combineAndSortArrays(array1, array2) {
    const resultArray = [];
    let index1 = 0;
    let index2 = 0;
    while (index1 < array1.length && index2 < array2.length) {
        let value1 = array1[index1];
        let value2 = array2[index2];
        if (value1 <= value2) {
            resultArray.push(value1);
            index1++;
        }
        else {
            resultArray.push(value2);
            index2++;
        }
    }
    if (index1 < array1.length) {
        resultArray.push(...array1.slice(index1));
    }
    else if (index2 < array2.length) {
        resultArray.push(...array2.slice(index2));
    }
    return resultArray;
}
function runTestCase(array1, array2, expectedResult) {
    const actualResult = combineAndSortArrays(array1, array2);
    if (JSON.stringify(actualResult) === JSON.stringify(expectedResult)) {
        console.log(`TEST CASE ${JSON.stringify(array1)} ${JSON.stringify(array2)} - PASS`);
    }
    else {
        console.log(`TEST CASE ${JSON.stringify(array1)}, ${JSON.stringify(array2)} FAILED - ACTUAL VALUE = ${JSON.stringify(actualResult)}`);
    }
}
runTestCase([4, 5, 7, 9], [-2, 0, 2, 3, 5], [-2, 0, 2, 3, 4, 5, 5, 7, 9]);
runTestCase([1], [0], [0, 1]);
runTestCase([7, 15, 18, 20], [-2, 0], [-2, 0, 7, 15, 18, 20]);
runTestCase([4, 5, 7, 9], [-2, 0, 2, 3, 5], [-2, 0, 2, 3, 4, 5, 5, 7, 9]);

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

**Playground Link:** [Provided](https://www.typescriptlang.org/play/?#code/PTAEHMEsDcFMDtQCZQGcD2AnALrAJqAIaaaECeAUCEaANoAsANKAKzMDszAnALpVgAjOgFokzAAzMxoAMzMWfEP1ABjTLEK4aAMwCu8FdkjpE2ABabVhROuy7Mps7FDnnKYqTKpQAW1iZwfCJ4AkIAGww0LFw8ZW1MdB8iAXQ4UHVUXTDsZlgADwAHWEMg6HDdZ0hvWlEJKWY5UCZWeQ5uPgo9AyMTVUSBSHhYAEEQgGVo4ZJyVAAKD3IARgAuUHhdHwF-Wh5mBbIkVfXN7Z4ASlAAbwpQPvhUbHTYTOypzyONrcwd0ABeOg6tzCsEegzw+UWf1A4gA3DdQMDQSF8ih-rCKPCAO5mSDA0CzMEQ0AAHiI0zIiwAdMD4OBzKAAGQM0CEvIoUn7JDUhB0swXa63IEg0BlMIVSH-faLWisxY8OGChHC0UVVFkzxIGXItnyjGKyDafEq2CQ4n-Y1IfnwxUZLLYN7kSkFXSoMyzY2LM4KxUs7WLADU-u9twAvtbQLAIs4BT7ba9yU6XW6LV7w7dWUhA8HQGHQ3qWYaCX6SeqltzaeYrTbnnaHWRE67ZpTm1LKagwpAVLAi+C8p7U3nbpHUJVCxmS5zy7yq4K4-aE87G83KZP253uxmzgOc-nbPYbDX4544WGMV1DMYbPoACrPbAAYUII-m5JWa0+pz25MO75O312EaFMUMQAEqHtgHx-jsM4qCYDxEIYujhGBLyPP8sGbIMIzjJM5JzFKX4atuBr4gAUmMADyABybbYJggxQNoZDzIhyHgRcvycaA5HUbR9G0gazH5EUJR4Chdpblc4awfc6DAtS6DgLMAAG14AKJjNeoD3sMYxqaAAAklw8TRDz8YxzFSmcIaGcZlGmXRDGCS+RE2cIoAAAq6WMylnPCuYRlGUmKjJGDyWEikqepmnabp+lGSZfFOUxLlLNZzAJfZSUCSlnLWaAABiwwAJIADJqQAIqA7nDPe14AKrDKVoAAGpNfV+n-JlvFmcllmsWE4nZNZvn+RQp6YDed6Ps+DCtKAnCgLwzA1NIkjIA08gAatdQbbIzDNGwLQLe0fmTfAt4PDN3a0HKK3iNt61ymdU1XU+N2LYsR2LAAHFID0rbU0LbUD62fd9f3IA9L0XdN72zHNx2LctIhrfU+2sCDaN7Y0h3zcj5xAA)
      
