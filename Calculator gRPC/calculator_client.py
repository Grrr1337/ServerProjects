import grpc
import calculator_pb2
import calculator_pb2_grpc

# Exploring gRPC

# client-side code to interact with the gRPC server
def test_functions(operand1: int, operand2: int):
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Make an 'add' request
    req_add = calculator_pb2.AddRequest(operand1=operand1, operand2=operand2)
    resp_add = stub.Add(req_add)
    print(f"Add Result: {resp_add.result}")

    req_subtract = calculator_pb2.SubtractRequest(operand1=operand1, operand2=operand2)
    resp_subtract = stub.Subtract(req_subtract)
    print(f"Subtract Result: {resp_subtract.result}")

    req_multiply = calculator_pb2.MultiplyRequest(operand1=float(operand1), operand2=float(operand2))
    resp_multiply = stub.Multiply(req_multiply)
    print(f"Multiply Result: {str(resp_multiply.result)}")

    req_divide = calculator_pb2.DivideRequest(operand1=float(operand1), operand2=float(operand2))
    resp_divide = stub.Divide(req_divide)
    print(f"Divide Result: {resp_divide.result}")
# def test_functions

if __name__ == '__main__':
    test_functions(5, 4)

# print output:
# Add Result: 9
# Subtract Result: 1
# Multiply Result: 20.0
# Divide Result: 1.25
