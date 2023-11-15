#!/usr/bin/node

const { dict } = require('./101-data');

// Function to invert the dictionary
function invertDictionary (inputDict) {
  const outputDict = {};

  // Iterate over the keys in the input dictionary
  Object.keys(inputDict).forEach(key => {
    // Get the value for the current key
    const value = inputDict[key];

    // If the value is not a key in the output dictionary, create an array with the current key
    if (!outputDict[value]) {
      outputDict[value] = [key.toString()];
    } else {
      // If the value is already a key in the output dictionary, append the current key to the array
      outputDict[value].push(key.toString());
    }
  });

  return outputDict;
}

// Invert the dictionary
const invertedDict = invertDictionary(dict);

// Print the inverted dictionary
console.log(invertedDict);
