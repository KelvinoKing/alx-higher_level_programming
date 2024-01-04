#!/usr/bin/node

const request = require('request');

// Get the API URL from command line argument
const apiUrl = process.argv[2];

// Function to fetch data from the API
function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Main function to compute completed tasks by user id
async function computeCompletedTasks (apiUrl) {
  try {
    // Fetch data from the API
    const todos = await fetchData(apiUrl);

    // Initialize an object to store completed tasks by user id
    const completedTasksByUserId = {};

    // Filter completed tasks and count them
    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasksByUserId[todo.userId]) {
          completedTasksByUserId[todo.userId]++;
        } else {
          completedTasksByUserId[todo.userId] = 1;
        }
      }
    });

    // Print the result
    console.log(completedTasksByUserId);
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

// Run the main function
computeCompletedTasks(apiUrl);
