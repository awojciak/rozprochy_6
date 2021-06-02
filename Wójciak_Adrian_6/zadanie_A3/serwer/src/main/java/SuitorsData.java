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

    public int putNewSuitor(ResponsesPrx proxy) {
        topId++;
        suitors.put(topId, proxy);
        return topId;
    }

    public boolean putNewSuitorProxy(Integer suitorId, ResponsesPrx proxy) {
        if (suitors.containsKey(suitorId)) {
            suitors.put(suitorId, proxy);
            return true;
        }

        return false;
    }

    public ResponsesPrx getSuitorProxy(Integer suitorId) {
        return suitors.get(suitorId);
    }
}
