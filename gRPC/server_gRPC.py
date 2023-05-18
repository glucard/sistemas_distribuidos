import grpc
import my_service_pb2
import my_service_pb2_grpc
from  concurrent import futures

import subprocess

class MyService(my_service_pb2_grpc.MyServiceServicer):
    def Command(self, request, context):
        print(f"Running: {request.command}")
        result = subprocess.run(request.command.split(), capture_output=True, text=True).stdout
        return my_service_pb2.CommandResponse(command_output=f"{result}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
