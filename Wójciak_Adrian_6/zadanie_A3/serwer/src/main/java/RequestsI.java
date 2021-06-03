import Office.Requests;
import Office.ResponsesPrx;
import Office.Result;
import Office.Time;
import com.zeroc.Ice.Current;

import java.time.LocalTime;
import java.util.Random;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

public class RequestsI implements Requests {
    SuitorsData data = SuitorsData.getInstance();
    Random rand = new Random();

    @Override
    public void onSuitorReturn(int number, ResponsesPrx responsesProxy, Current current) {
        data.putNewSuitorProxy(number, responsesProxy.ice_fixed(current.con));
        responsesProxy.ice_fixed(current.con).getReturnConfirmation();

        if (data.getResult(number).isDone()) {
            try {
                responsesProxy.ice_fixed(current.con).getResult(data.getResult(number).get());
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public void passportCase(ResponsesPrx responsesProxy, String name, String surname, int duration, Current current) {
        Integer newId = data.putNewSuitor(responsesProxy.ice_fixed(current.con));
        responsesProxy.ice_fixed(current.con).getNumber(newId);

        Integer expectedDuration = rand.nextInt(60) + 60;
        LocalTime time = LocalTime.now();
        Time expectedEndTime = new Time(
                (time.getHour() + ((time.getMinute() + ((time.getSecond() + expectedDuration) / 60)) / 60)) % 24,
                (time.getMinute() + ((time.getSecond() + expectedDuration) / 60)) % 60,
                (time.getSecond() + expectedDuration) % 60
        );
        responsesProxy.ice_fixed(current.con).getExpectedEndTime(expectedEndTime);

        Integer delay = rand.nextInt(30);
        Time finalEndTime = new Time(
                (time.getHour() + ((time.getMinute() + ((time.getSecond() + expectedDuration + delay) / 60)) / 60)) % 24,
                (time.getMinute() + ((time.getSecond() + expectedDuration + delay) / 60)) % 60,
                (time.getSecond() + expectedDuration + delay) % 60
        );
        String caseType = "passport";
        boolean isResultPositive = duration < 120;
        Result result = new Result(isResultPositive, finalEndTime, caseType);

        data.putCase(newId, CompletableFuture.supplyAsync(
                () -> {
                    try {
                        Thread.sleep((expectedDuration + delay) * 1000);
                        SuitorsData.getInstance().getSuitorProxy(newId).getResult(result);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    return result;
                }
        ));
    }

    @Override
    public void buildPermitCase(ResponsesPrx responsesProxy, int surface, int height, boolean useSolarEnergy, boolean isWooden, Current current) {
        Integer newId = data.putNewSuitor(responsesProxy.ice_fixed(current.con));
        responsesProxy.ice_fixed(current.con).getNumber(newId);

        Integer expectedDuration = rand.nextInt(60) + 60;
        LocalTime time = LocalTime.now();
        Time expectedEndTime = new Time(
                (time.getHour() + ((time.getMinute() + ((time.getSecond() + expectedDuration) / 60)) / 60)) % 24,
                (time.getMinute() + ((time.getSecond() + expectedDuration) / 60)) % 60,
                (time.getSecond() + expectedDuration) % 60
        );
        responsesProxy.ice_fixed(current.con).getExpectedEndTime(expectedEndTime);

        Integer delay = rand.nextInt(30);
        Time finalEndTime = new Time(
                (time.getHour() + ((time.getMinute() + ((time.getSecond() + expectedDuration + delay) / 60)) / 60)) % 24,
                (time.getMinute() + ((time.getSecond() + expectedDuration + delay) / 60)) % 60,
                (time.getSecond() + expectedDuration + delay) % 60
        );
        String caseType = "build permit";
        boolean isResultPositive = (surface < 60) && (height < 15) && (!isWooden || useSolarEnergy);
        Result result = new Result(isResultPositive, finalEndTime, caseType);

        data.putCase(newId, CompletableFuture.supplyAsync(
                () -> {
                    try {
                        Thread.sleep((expectedDuration + delay) * 1000);
                        SuitorsData.getInstance().getSuitorProxy(newId).getResult(result);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    return result;
                }
        ));
    }

    @Override
    public void demolitionPermitCase(ResponsesPrx responsesProxy, int surface, int height, boolean useDynamite, Current current) {
        Integer newId = data.putNewSuitor(responsesProxy);
        responsesProxy.getNumber(newId);

        Integer expectedDuration = rand.nextInt(60) + 60;
        LocalTime time = LocalTime.now();
        Time expectedEndTime = new Time(
                (time.getHour() + ((time.getMinute() + ((time.getSecond() + expectedDuration) / 60)) / 60)) % 24,
                (time.getMinute() + ((time.getSecond() + expectedDuration) / 60)) % 60,
                (time.getSecond() + expectedDuration) % 60
        );
        responsesProxy.getExpectedEndTime(expectedEndTime);

        Integer delay = rand.nextInt(30);
        Time finalEndTime = new Time(
                (time.getHour() + ((time.getMinute() + ((time.getSecond() + expectedDuration + delay) / 60)) / 60)) % 24,
                (time.getMinute() + ((time.getSecond() + expectedDuration + delay) / 60)) % 60,
                (time.getSecond() + expectedDuration + delay) % 60
        );
        String caseType = "build permit";
        boolean isResultPositive = (surface < 100) && (height < 10) && (!useDynamite);
        Result result = new Result(isResultPositive, finalEndTime, caseType);

        data.putCase(newId, CompletableFuture.supplyAsync(
                () -> {
                    try {
                        Thread.sleep((expectedDuration + delay) * 1000);
                        SuitorsData.getInstance().getSuitorProxy(newId).getResult(result);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    return result;
                }
        ));
    }
}
