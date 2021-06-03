from Office import Responses
import os

class ResponsesI(Responses):
    def getNumber(self, number, current):
        numberFile = open('./number.txt', 'w')
        numberFile.write('{}'.format(number))
        numberFile.close()
        print('Office has given you number: {}'.format(number))

    def getReturnConfirmation(self, current):
        print('You have returned to the office without any problem. Now you can wait until your case is resolved.')

    def getExpectedEndTime(self, expectedEndTime, current):
        print('Your case will be resolved expectedly at {}:{}:{}. Now you have to wait.'.format(expectedEndTime.hour, expectedEndTime.minute, expectedEndTime.second))

    def getResult(self, result, current):
        print('Your case:\n\tof type: {}\n\twas resolved with result: {}\n\tat: {}:{}:{}'.format(
            result.caseType,
            'positively' if result.isResultPositive == True else 'negatively',
            result.finalEndTime.hour,
            result.finalEndTime.minute,
            result.finalEndTime.second
        ))
        
        if os.path.exists("./number.txt"):
            os.remove("./number.txt")