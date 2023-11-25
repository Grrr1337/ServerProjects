
// node client2.js
const axios = require('axios');

async function calculate(operation, x, y) {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/${operation}`, {
      params: { x, y },
    });

    const result = response.data.result;
    const error = response.data.error;

    if (result !== undefined) {
      console.log(`Result of ${operation}(${x}, ${y}): ${result}`);
    } else if (error !== undefined) {
      console.log(`Error occurred: ${error}`);
    } else {
      console.log("Error: 'result' key not found in the response JSON");
    }
  } catch (error) {
    console.log(`Error: ${error.response.data.error || 'Unknown error'}`);
  }
}

const a = 5.0;
const b = 4.0;

// Example usage with async/await
(async () => {
  await calculate('add', a, b);
  await calculate('subtract', a, b);
  await calculate('multiply', a, b);
  await calculate('divide', a, b);
  await calculate('divide', a, 0);  // This will result in an error
})();

