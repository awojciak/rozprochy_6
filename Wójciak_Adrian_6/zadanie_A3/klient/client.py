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
            try:
                requests_proxy.onSuitorReturn(number, responsesPrx)
            except:
                print('You have invalid number')
                if os.path.exists("./number.txt"):
                    os.remove("./number.txt")
            finally:
                while True:
                    if not os.path.exists("./number.txt"):
                        break

                    time.sleep(10)
        while True:
            case_type = input('Now you can give us a new case. Select type:\n\tP - passport\n\tB - build permit\n\tD - demolition permit\nType: ')

            if case_type == 'P':
                name = input('Name: ')
                surname = input('Surname: ')
                duration = input('Duration: ')

                try:
                    requests_proxy.passportCase(responsesPrx, name, surname, int(duration))
                except:
                    base = communicator.propertyToProxy('Requests.Proxy')
                    requests_proxy = Office.RequestsPrx.checkedCast(base)

                    adapter = communicator.createObjectAdapter("")
                    responsesPrx = Office.ResponsesPrx.uncheckedCast(adapter.addWithUUID(ResponsesI()))
                    requests_proxy.ice_getCachedConnection().setAdapter(adapter)
                    requests_proxy.ice_getCachedConnection().setACM(Ice.Unset, Ice.Unset, Ice.ACMHeartbeat.HeartbeatAlways)

                    requests_proxy.passportCase(responsesPrx, name, surname, int(duration))
            elif case_type == 'B':
                surface = input('Surface: ')
                height = input('Height: ')
                useSolarEnergy = input('Will use solar energy [y/n]: ')
                isWooden = input('Will be wooden [y/n]: ')

                try:
                    requests_proxy.buildPermitCase(
                        responsesPrx,
                        int(surface),
                        int(height),
                        True if useSolarEnergy == 'y' else False,
                        True if isWooden == 'y' else False
                    )
                except:
                    base = communicator.propertyToProxy('Requests.Proxy')
                    requests_proxy = Office.RequestsPrx.checkedCast(base)

                    adapter = communicator.createObjectAdapter("")
                    responsesPrx = Office.ResponsesPrx.uncheckedCast(adapter.addWithUUID(ResponsesI()))
                    requests_proxy.ice_getCachedConnection().setAdapter(adapter)
                    requests_proxy.ice_getCachedConnection().setACM(Ice.Unset, Ice.Unset, Ice.ACMHeartbeat.HeartbeatAlways)

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
                useDynamite = input('Will there be used dynamite [y/n]: ')

                try:
                    requests_proxy.demolitionPermitCase(
                        responsesPrx,
                        int(surface),
                        int(height),
                        True if useDynamite == 'y' else False,
                    )
                except:
                    base = communicator.propertyToProxy('Requests.Proxy')
                    requests_proxy = Office.RequestsPrx.checkedCast(base)

                    adapter = communicator.createObjectAdapter("")
                    responsesPrx = Office.ResponsesPrx.uncheckedCast(adapter.addWithUUID(ResponsesI()))
                    requests_proxy.ice_getCachedConnection().setAdapter(adapter)
                    requests_proxy.ice_getCachedConnection().setACM(Ice.Unset, Ice.Unset, Ice.ACMHeartbeat.HeartbeatAlways)

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
    except:
        print('There was an exception.')
    finally:
        print('Client is going off.')