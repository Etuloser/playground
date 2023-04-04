ARTIFACTS=

ARTIFACTS += helloworld/helloworld_pb2.py
ARTIFACTS += helloworld/helloworld_pb2_grpc.py
ARTIFACTS += helloworld/helloworld_pb2.pyi

.PHONY: all
all: ${ARTIFACTS}

helloworld/helloworld_pb2.py helloworld/helloworld_pb2_grpc.py helloworld/helloworld_pb2.pyi: ../protos/helloworld.proto
	python3 -m grpc_tools.protoc --python_out=helloworld --grpc_python_out=helloworld --pyi_out=helloworld -I ../protos ../protos/helloworld.proto