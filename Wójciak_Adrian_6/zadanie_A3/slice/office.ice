#ifndef OFFICE_ICE
#define OFFICE_ICE

module Office
{
    struct Time
    {
        int hour;
        int minute;
        int second;
    }

    struct Result
    {
        bool isResultPositive;
        Time finalEndTime;
        string caseType;
    }

    interface Responses
    {
        void getId(int suitorId);
        void getReturnResult(bool didReturnSucceed);
        void getExpectedEndTime(Time expectedEndTime);
        void getResult(Result result);
    }

    interface Requests
    {
        void onNewSuitor(Responses* responsesProxy);
        void onSuitorReturn(int suitorId, Responses* responsesProxy);
        void passportCase(string name, string surname, int duration);
        void buildPermitCase(int surface, int height, bool useSolarEnergy, bool isWooden);
        void demolitionPermitCase(int surface, int height, bool useDynamite);
    }
}

#endif