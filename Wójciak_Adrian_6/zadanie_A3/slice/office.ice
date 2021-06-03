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
        void getNumber(int number);
        void getReturnConfirmation();
        void getExpectedEndTime(Time expectedEndTime);
        void getResult(Result result);
    }

    interface Requests
    {
        void onSuitorReturn(int number, Responses* responsesProxy);
        void passportCase(Responses* responsesProxy, string name, string surname, int duration);
        void buildPermitCase(Responses* responsesProxy, int surface, int height, bool useSolarEnergy, bool isWooden);
        void demolitionPermitCase(Responses* responsesProxy, int surface, int height, bool useDynamite);
    }
}

#endif