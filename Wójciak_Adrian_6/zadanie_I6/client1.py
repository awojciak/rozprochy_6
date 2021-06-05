import example_pb2
import example_pb2_grpc
import grpc

def run():
    with grpc.insecure_channel('localhost:21370') as channel:
        stub = example_pb2_grpc.AnswersServiceStub(channel)
        while True:
            newQuestion = input('Say your question: ')
            newAnswer = stub.sayQuestion(example_pb2.QuestionRequest(question=newQuestion))
            print('The answer is: '.format(newAnswer.getAnswer()))

if __name__ == '__main__':
    run()