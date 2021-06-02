from Office import Responses

class ResponsesI(Responses):
    def getId(self, suitorId, current):
        idFile = open('id.txt', 'w')
        idFile.write('{}'.format(suitorId))
        idFile.close()

    def getReturnResult(self, didReturnSucceed, current):
        pass

    def getExpectedEndTime(self, expectedEndTime, current):
        pass

    def getResult(self, result, current):
        pass