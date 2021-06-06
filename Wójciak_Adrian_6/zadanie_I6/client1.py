import example_pb2
import example_pb2_grpc
import grpc

def run():
    with grpc.insecure_channel('localhost:21370') as channel:
        stub = example_pb2_grpc.AnswersServiceStub(channel)
        print('Client is running...')
        while True:
            try:
                newQuestion = input('Say your question: ')
                try:
                    newAnswer = stub.sayQuestion(example_pb2.QuestionRequest(question=newQuestion))
                    print('The answer is: {}'.format(newAnswer.answer))
                except grpc.RpcError as rpc_error:
                    print("There was an exception. Try again.")
                    print('Details: {}'.format(rpc_error))
            except:
                channel.close()
                print("\nClient has stopped.")
                break

if __name__ == '__main__':
    run()