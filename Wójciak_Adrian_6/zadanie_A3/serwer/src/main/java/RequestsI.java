import Office.Requests;
import Office.ResponsesPrx;
import com.zeroc.Ice.Current;

public class RequestsI implements Requests {
    SuitorsData data = SuitorsData.getInstance();

    @Override
    public void onNewSuitor(ResponsesPrx responsesProxy, Current current) {
        Integer newId = data.putNewSuitor(responsesProxy);
        responsesProxy.getId(newId);
    }

    @Override
    public void onSuitorReturn(int suitorId, ResponsesPrx responsesProxy, Current current) {
        boolean returnResult = data.putNewSuitorProxy(suitorId, responsesProxy);
        responsesProxy.getReturnResult(returnResult);
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
