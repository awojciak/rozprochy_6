import Office.Requests;
import Office.ResponsesPrx;
import com.zeroc.Ice.Current;

public class RequestsI implements Requests {
    SuitorsData data = SuitorsData.getInstance();

    @Override
    public void onNewSuitor(ResponsesPrx responsesProxy, Current current) {
        data.putNewSuitor(responsesProxy);
    }

    @Override
    public void onSuitorReturn(int suitorId, ResponsesPrx responsesProxy, Current current) {
        data.putNewSuitorProxy(suitorId, responsesProxy);
    }

    @Override
    public void passportCase(String name, String surname, int duration, Current current) {

    }

    @Override
    public void buildPermitCase(int surface, int height, boolean useSolarEnergy, boolean isWooden, Current current) {

    }

    @Override
    public void demolitionPermitCase(int surface, int height, boolean useDynamite, Current current) {

    }
}
