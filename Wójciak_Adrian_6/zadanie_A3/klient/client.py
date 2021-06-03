import sys
import Ice
import Office
import os
import time
from ResponsesI import ResponsesI

with Ice.initialize(sys.argv) as communicator:
    try:
        base = communicator.propertyToProxy('Requests.Proxy')
        requests_proxy = Office.RequestsPrx.checkedCast(base)

        adapter = communicator.createObjectAdapter("")
        responsesPrx = Office.ResponsesPrx.uncheckedCast(adapter.addWithUUID(ResponsesI()))
        requests_proxy.ice_getCachedConnection().setAdapter(adapter)
        requests_proxy.ice_getCachedConnection().setACM(Ice.Unset, Ice.Unset, Ice.ACMHeartbeat.HeartbeatAlways)

        if os.path.exists("./number.txt"):
            print('You have case number - wait until it resolves.')
            numberFile = open('./number.txt', 'r')
            number = int(numberFile.read())
            numberFile.close()
            requests_proxy.onSuitorReturn(number, responsesPrx)

            while True:
                if not os.path.exists("./number.txt"):
                    break

                time.sleep(10)

        case_type = input('Now you can give us a new case. Select type:\n\tP - passport\n\tB - build permit\n\tD - demolition permit\n')

        if case_type == 'P':
            name = input('Name: ')
            surname = input('Surname: ')
            duration = input('Duration: ')

            requests_proxy.passportCase(responsesPrx, name, surname, int(duration))
        elif case_type == 'P':
            surface = input('Surface: ')
            height = input('Height: ')
            useSolarEnergy = input('Will use solar energy [y/n]:')
            isWooden = input('Will be wooden [y/n]:')

            requests_proxy.buildPermitCase(
                responsesPrx,
                int(surface),
                int(height),
                True if useSolarEnergy == 'y' else False,
                True if isWooden == 'y' else False
            )
        else:
            surface = input('Surface: ')
            height = input('Height: ')
            useDynamite = input('Will there be used dynamite [y/n]:')

            requests_proxy.demolitionPermitCase(
                responsesPrx,
                int(surface),
                int(height),
                True if useDynamite == 'y' else False,
            )

        while True:
            time.sleep(10)

            if not os.path.exists("./number.txt"):
                break
    except Exception:
        print('There was an exception.')
    finally:
        print('Client is going off.')