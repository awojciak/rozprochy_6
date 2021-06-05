import example_pb2
import example_pb2_grpc
import grpc
from concurrent import futures

class SquaringService(example_pb2_grpc.SquaringServiceServicer):
    def getSquare(self, request, context):
        print('Now squaring number {}'.format(request.number))
        return example_pb2.Squared(squared=(int(request.number) ** 2))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_SquaringServiceServicer_to_server(SquaringService(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    print('Server is running')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()