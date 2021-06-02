import com.zeroc.Ice.Communicator;
import com.zeroc.Ice.Identity;
import com.zeroc.Ice.ObjectAdapter;
import com.zeroc.Ice.Util;

public class Server {
    public static void main(String[] args) {
        int status = 0;
        Communicator communicator = null;

        try	{
            communicator = Util.initialize(args);
            ObjectAdapter adapter = communicator.createObjectAdapter("Adapter1");

            RequestsI requests = new RequestsI();

            adapter.add(requests, new Identity("requests", "office"));

            adapter.activate();
            System.out.println("Entering event processing loop...");
            communicator.waitForShutdown();
        } catch (Exception e) {
            System.err.println(e);
            status = 1;
        }

        if (communicator != null) {
            try {
                communicator.destroy();
            } catch (Exception e) {
                System.err.println(e);
                status = 1;
            }
        }

        System.exit(status);
    }
}
