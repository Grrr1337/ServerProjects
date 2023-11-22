import requests

def calculate(operation, x, y):
    url = f"http://127.0.0.1:8000/{operation}"
    params = {"x": x, "y": y}
    
    response = requests.get(url, params=params)
    
   
    if response.status_code == 200:
        # Check if 'result' key is present in the JSON response
        result = response.json().get("result")
        error = response.json().get("error")
        if result is not None:
            print(f"Result of {operation}({x}, {y}): {result}")
        elif error is not None:
            print(f"Error occured: {error}")
        else:
            print(f"Error: 'result' key not found in the response JSON")
    else:
        # Handle error case
        print(f"Error: {response.json().get('error', 'Unknown error')}")
    
if __name__ == '__main__':
    a, b = 5.0, 4.0
    # Example usage
    calculate("add", a, b)
    calculate("subtract", a, b)
    calculate("multiply", a, b)
    calculate("divide", a, b)
    calculate("divide", a, 0)  # This will result in an error
