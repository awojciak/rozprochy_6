import example_pb2
import example_pb2_grpc
import grpc
from concurrent import futures

class AnswersService(example_pb2_grpc.AnswersServiceServicer):
    def sayQuestion(self, request, context):
        print('Question {} was asked'.format(request.question))
        newAnswer = 'I cannot answer this question.'

        if request.question == 'What is love?':
            newAnswer = 'Baby, dont hurt me. Dont hurt me. No more.'

        return example_pb2.QuestionAnswer(answer=newAnswer)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_AnswersServiceServicer_to_server(AnswersService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print('Server is running...')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()