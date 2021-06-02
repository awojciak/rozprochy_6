import Office.ResponsesPrx;

import java.util.LinkedHashMap;
import java.util.Map;

public class SuitorsData {
    Map<Integer, ResponsesPrx> suitors = new LinkedHashMap<>();
    Integer topId = 0;

    public static final SuitorsData instance = new SuitorsData();

    private SuitorsData() {
    }

    public static SuitorsData getInstance() {
        return instance;
    }

    public void putNewSuitor(ResponsesPrx proxy) {
        suitors.put(topId, proxy);
        topId++;
    }

    public void putNewSuitorProxy(Integer suitorId, ResponsesPrx proxy) {
        suitors.put(suitorId, proxy);
    }

    public ResponsesPrx getSuitorProxy(Integer suitorId) {
        return suitors.get(suitorId);
    }
}
