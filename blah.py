import socket
import re

def solve_math_expression(expr):
    try:
        return str(eval(expr))  # Use eval to compute the math expression
    except Exception as e:
        print(f"Error evaluating expression '{expr}': {e}")
        return None

def extract_math_problem(data):
    # Regex pattern to identify math problems
    pattern = r'(\d+\s[+\-*/]\s\d+)'
    match = re.search(pattern, data)
    if match:
        return match.group(1)
    return None

def interact_with_math_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Read and print the initial server message first
    initial_message = s.recv(4096).decode()
    print(initial_message)

    for _ in range(101):
        # Extract the math problem from the received data
        problem = extract_math_problem(initial_message)
        if not problem:
            print("No math problem found!")
            break

        print(f"Received: {problem}")

        # Solve the math problem
        answer = solve_math_expression(problem)
        if answer is not None:
            print(f"Answer: {answer}")
            s.sendall((answer + "\n").encode())

        # Receive the next data from the server
        initial_message = s.recv(1024).decode().strip()

    s.close()

if __name__ == "__main__":
    SERVER_HOST = "chals.sekai.team"
    SERVER_PORT = 9000

    interact_with_math_server(SERVER_HOST, SERVER_PORT)

