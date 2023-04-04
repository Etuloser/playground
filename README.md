# README

> Library reference
>
> [gRPC](https://grpc.io/)
>
> [grpc branch](https://github.com/Etuloser/playground.git)

## Python

### Install

```bash
python3 -m pip install grpcio grpcio-tools
```

### Helloworld

*protos/helloworld.proto*

```protobuf
syntax = "proto3";

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}

  rpc SayHelloStreamReply (HelloRequest) returns (stream HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

*python/Makefile*

```makefile
ARTIFACTS=

ARTIFACTS += helloworld/helloworld_pb2.py
ARTIFACTS += helloworld/helloworld_pb2_grpc.py
ARTIFACTS += helloworld/helloworld_pb2.pyi

.PHONY: all
all: ${ARTIFACTS}

helloworld/helloworld_pb2.py helloworld/helloworld_pb2_grpc.py helloworld/helloworld_pb2.pyi: ../protos/helloworld.proto
	python3 -m grpc_tools.protoc --python_out=helloworld --grpc_python_out=helloworld --pyi_out=helloworld -I ../protos ../protos/helloworld.proto
```

```bash
mkdir -p python/helloworld
make all
```

![image-20230404220722306](D:\develop\OneDrive\图片\文章截图\image-20230404220722306.png)

*python/helloworld/greeter_server.py*

```python
from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    port = '30080'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
```

*python/helloworld/greeter_client.py*

```python
from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:30080') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
```

