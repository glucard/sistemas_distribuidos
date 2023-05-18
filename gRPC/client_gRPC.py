import grpc
import my_service_pb2
import my_service_pb2_grpc

import click

@click.command()
@click.option('--addr', prompt='host adress',
              help='Define host adress', default = 'localhost')
@click.option('--port', prompt='host port',
              help='Define host port', default='50051')

def run(addr, port):
    host = f'{addr}:{port}'
    with grpc.insecure_channel(host) as channel:
        while True:
            msg = input("Command ('quit' to exit): ")
            if msg == 'quit':
                break

            stub = my_service_pb2_grpc.MyServiceStub(channel)
            response = stub.Command(my_service_pb2.CommandRequest(command=msg))
            print(response.command)


if __name__ == "__main__":
    # run('localhost','50051')
    run()
