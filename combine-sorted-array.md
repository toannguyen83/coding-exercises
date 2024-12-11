
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

  // while loop keeps 2 pointers, one for each array
  // compare the 2 values of current pointers, if one value is smaller
  // then add it to the result, and then increment the pointer of the added array number
  // iteration notes:
  // compare 4 and -2, since -2 is smaller, add -2 to result [-2], increment array b pointer
  // compare 4 and 0, add 0 to result [-2, 0]
  // compare 4 and 2, add 2 to result [-2, 0, 2]
  // compare 4 and 3, add 3 to result [-2, 0, 3]
  // compare 4 and 5, add 4 to result [-2, 0, 3, 4], now increment array a pointer
  // compare 5 and 5, add one of them to result [-2, 0, 3, 4, 5]
  // compare 7 and 5, add 5 [-2, 0, 3, 4, 5, 5]
  // now array b index is out of range, while loop stop
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

  // at the end if there are remaining numbers in either one of array
  // we can append to result
  // at this point the remaining numbers since they are sorted, should be larger 
  // than the last number in the result.
  // in this case the last number is 5, remaining array a is [7,9], result should be 
  // [-2, 0, 2, 3, 4, 5, 5, 7, 9]

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
    // while loop keeps 2 pointers, one for each array
    // compare the 2 values of current pointers, if one value is smaller
    // then add it to the result, and then increment the pointer of the added array number
    // iteration notes:
    // compare 4 and -2, since -2 is smaller, add -2 to result [-2], increment array b pointer
    // compare 4 and 0, add 0 to result [-2, 0]
    // compare 4 and 2, add 2 to result [-2, 0, 2]
    // compare 4 and 3, add 3 to result [-2, 0, 3]
    // compare 4 and 5, add 4 to result [-2, 0, 3, 4], now increment array a pointer
    // compare 5 and 5, add one of them to result [-2, 0, 3, 4, 5]
    // compare 7 and 5, add 5 [-2, 0, 3, 4, 5, 5]
    // now array b index is out of range, while loop stop
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
    // at the end if there are remaining numbers in either one of array
    // we can append to result
    // at this point the remaining numbers since they are sorted, should be larger 
    // than the last number in the result.
    // in this case the last number is 5, remaining array a is [7,9], result should be 
    // [-2, 0, 2, 3, 4, 5, 5, 7, 9]
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

**Playground Link:** [Provided](https://www.typescriptlang.org/play/?#code/PTAEHMEsDcFMDtQCZQGcD2AnALrAJqAIaaaECeAUCEaANoAsANKAKzMDszAnALpVgAjOgFokzAAzMxoAMzMWfEP1ABjTLEK4aAMwCu8FdkjpE2ABabVhROuy7Mps7FDnnKYqTKpQAW1iZwfCJ4AkIAGww0LFw8ZW1MdB8iAXQ4UHVUXTDsZlgADwAHWEMg6HDdZ0hvWlEJKWY5UCZWeQ5uPgo9AyMTVUSBSHhYAEEQgGVo4ZJyVAAKD3IARgAuUHhdHwF-Wh5mBbIkVfXN7Z4ASlAAbwpQPvhUbHTYTOypzyONrcwd0ABeOg6tzCsEegzw+UWf1A4gA3DdQMDQSF8ih-rCKPDqAB3MyQYEI9DoAqgADWsFgBW8KAK6EGuEwqGYJmc2iwoA0KjMRGmlFu1BUiQKxGcrmQoDKYQq3nQ2lU9nU8EeNLp-kZoEgsuZ4vKlW8qB84WBmExYFciEIeAIkEe2HQLicTxeOWCBDN6oM6j8ivtzmViv8oBlPqIlqC+zWn38JvV9M0xkQ8HQuFQy2jAp8QvUTRdoFqaEGKmconVeoNYSNe0tuZQtsdWUeNSQu3dalgXse4aEfvpacFwuz1gIkhDQ5cdoy9ZE0nEfD5YHTmec9Bz0gtBBr4+ek8bdWQs9A-L7WeXg9klYIMjHdeyU93Mn3h4z-ZPIRaI+ztYnN530IazHozaJliLaeggHY8jQ3ZRnOfRPlmLA5mw75akGrhJJ+W7fnmw6NM0Ci9nBzjsIh56sLev5nk0rSsA+YBAdynigEIYL5CWga6I8QakPAgTMDieLOGEhLEg8RLwvx+KzCxeSQgAPAxSwAHTAjx5igAAZOp7rgnkKDyfsSDKQg4DmBc1y3ECILapKsCQv8+yLLQ0mLDwcIWQiVkShUqIKQcTnIrprkYu5GqgLMXm2aAsn-BFSBmfC7lftgbzkIpBS6KgZjhTqixnG57naRCADURX5bcAC+CXshEzjmQVSUpWQaUZVlsV5VVtzSUgJVlaAlUVcFB5gJYooIFasquFm-aeoQgyDOAEYnAy7rstaTiYIGQyBrK+zRlizgqNYRAFEUr4YU60Yjbi3jdsGM1zTxi1fHqBYik4ZDcs4GA4PgzCZegWQEFsCLEIEG3RuYR2imEhAPE9AaDHdmHYIp0aI+YVRWKgb2CbDjzHF8bFIfd8Dzb5NCY7QnC8MwSVoGYANhEDzjRj+w7SLh1FIZwoC8INoVSQFcm+YsRmqWY8WJcjjXNZlsyKQrDmKagYSQIWgs6bl7UDbcsA1eqsoayiUW+YZKkmRLVxVQ1PKy1lCuKQZyuq+rXVnNrfWDbY9g2NLPJwpVGJdIY8bpPoAAqzzYAAwrDsDzDyKzw98zYGR8S07LkhTFDEABKyPp18OyS3ccOEIYujhPnTpQumAxDKMeATDgjVzA5ew8nF+UCwAUmMADyAByyvYJg80amQ8wV1XyMXL88+gH3Q8j2PPET7M+RFCUeDV-W7tW+5Ar3OgwLKeg4CzAABuHACiYzh6A0fDGMN+gAAJJcS-Dw8q9QNok8OTOOVd+n8B7f1HuPf+CdPBxWAcIUAAAFZ+YxL5nHhP1aq2MD4WSPhgU+QkL7Xzvg-J+L8QFfxXpAgBicgHMA-hQn+VDoHkFgaAAAYsMAAkgAGRvgAEVzKAYY0dw4AFVhjcNAAANQkaI1+-x6FgMoWvKB5c7AzydEA1B6CKCB0wBHKOsdsazAYNRHmNNyLsz-DRZgbN6iUTwmY9oaD9HwEjg8Ix8daAuVsTOXxzAXIuIMR4uOJieaLCQosAAHFIPxljmx2NAOEyJMTkAziCW4wxoTTFvnMQk7C9jGgKFsQU5A1jHG5OcUAA)
      
