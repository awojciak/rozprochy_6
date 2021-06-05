import Office.ResponsesPrx;
import Office.Result;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.concurrent.CompletableFuture;

public class SuitorsData {
    Map<Integer, ResponsesPrx> suitors = new LinkedHashMap<>();
    Map<Integer, CompletableFuture<Result>> results = new LinkedHashMap<>();
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

    public boolean putNewSuitorProxy(Integer number, ResponsesPrx proxy) {
        if (suitors.containsKey(number)) {
            suitors.put(number, proxy);
            return true;
        }

        return false;
    }

    public ResponsesPrx getSuitorProxy(Integer number) {
        return suitors.get(number);
    }

    public void putCase(Integer number, CompletableFuture<Result> newCase) {
        results.put(number, newCase);
    }

    public CompletableFuture<Result> getResult(Integer number) {
        return results.get(number);
    }
}
