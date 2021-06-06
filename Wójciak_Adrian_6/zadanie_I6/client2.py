import example_pb2
import example_pb2_grpc
import grpc

def run():
    with grpc.insecure_channel('localhost:21370') as channel:
        stub = example_pb2_grpc.SquaringServiceStub(channel)
        print('Client is running...')
        while True:
            try:
                newNumber = input('Give number to square: ')
                try:
                    newSquare = stub.getSquare(example_pb2.SquareRequest(number=int(newNumber)))
                    print('The square of number is: {}'.format(newSquare.squared))
                except grpc.RpcError as rpc_error:
                    print("There was an exception. Try again.")
                    print('Details: {}'.format(rpc_error))
            except:
                channel.close()
                print("\nClient has stopped.")
                break

if __name__ == '__main__':
    run()