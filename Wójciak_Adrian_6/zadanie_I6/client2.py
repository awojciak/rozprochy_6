import example_pb2
import example_pb2_grpc
import grpc

def run():
    with grpc.insecure_channel('localhost:21370') as channel:
        stub = example_pb2_grpc.SquaringServiceStub(channel)
        while True:
            newNumber = input('Give number to square: ')
            newSquare = stub.getSquare(example_pb2.SquareRequest(number=int(newNumber)))
            print(newSquare)
            print('The square of number is: '.format(newSquare.getSquared()))

if __name__ == '__main__':
    run()