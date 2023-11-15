#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

// Get file paths from command line arguments
const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

// Read the content of the first file
fs.readFile(file1Path, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1Path}: ${err.message}`);
    process.exit(1);
  }

  // Read the content of the second file
  fs.readFile(file2Path, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2Path}: ${err.message}`);
      process.exit(1);
    }

    // Concatenate the content of both files
    const concatenatedContent = `${data1}${data2}`;

    // Write the concatenated content to the destination file
    fs.writeFile(destinationPath, concatenatedContent, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationPath}: ${err.message}`);
        process.exit(1);
      }
    });
  });
});
