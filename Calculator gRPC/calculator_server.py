import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

# Exploring gRPC

# server-side gRPC server

# setup instructions:
"""

source venv/bin/activate  # On Linux or macOS
# or
.\venv\Scripts\activate   # On Windows


pip install -r requirements.txt

# This will generate calculator_pb2.py and calculator_pb2_grpc.py in the same directory as your .proto file.
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto


"""

# run instructions:
"""
To run:
python calculator_server.py

python calculator_client.py


"""

# NOTE: every time I modify the server-side code or the `.proto` file I have to re-run this line:
# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.operand1 + request.operand2
        return calculator_pb2.AddResponse(result=result)
    
    def Subtract(self, request, context):
        result = request.operand1 - request.operand2
        return calculator_pb2.SubtractResponse(result=result)
    
    def Multiply(self, request, context):
        result = request.operand1 * request.operand2
        return calculator_pb2.MultiplyResponse(result=result)
    
    def Divide(self, request, context):
        result = request.operand1 / request.operand2
        return calculator_pb2.DivideResponse(result=result)
# class CalculatorServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
# def serve()

if __name__ == '__main__':
    serve()
# if __name__ == '__main__':

