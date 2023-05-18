# Description
 This is a remote control application. It uses a gRPC to simulate a server and its clients.\
 The client can send any bash command to the gRPC server and, then, it will execute.\
#### Requirements:
`pip install grpcio==1.54.2 grpcio-tools==1.54.2`

#### How to use:
    First execute `python3 server_gRPC.py`
    Then start your client using `python3 client_gRPC.py`

#### Showcase:

![grpc_showcase](https://github.com/glucard/sistemas_distribuidos/blob/main/gRPC/imgs/grpc_showcase.png)