//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//
// Ice version 3.7.5
//
// <auto-generated>
//
// Generated from file `office.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Office;

public interface Requests extends com.zeroc.Ice.Object
{
    void onSuitorReturn(int number, ResponsesPrx responsesProxy, com.zeroc.Ice.Current current)
        throws NoKnownSuitorError;

    void passportCase(ResponsesPrx responsesProxy, String name, String surname, int duration, com.zeroc.Ice.Current current);

    void buildPermitCase(ResponsesPrx responsesProxy, int surface, int height, boolean useSolarEnergy, boolean isWooden, com.zeroc.Ice.Current current);

    void demolitionPermitCase(ResponsesPrx responsesProxy, int surface, int height, boolean useDynamite, com.zeroc.Ice.Current current);

    /** @hidden */
    static final String[] _iceIds =
    {
        "::Ice::Object",
        "::Office::Requests"
    };

    @Override
    default String[] ice_ids(com.zeroc.Ice.Current current)
    {
        return _iceIds;
    }

    @Override
    default String ice_id(com.zeroc.Ice.Current current)
    {
        return ice_staticId();
    }

    static String ice_staticId()
    {
        return "::Office::Requests";
    }

    /**
     * @hidden
     * @param obj -
     * @param inS -
     * @param current -
     * @return -
     * @throws com.zeroc.Ice.UserException -
    **/
    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_onSuitorReturn(Requests obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
        throws com.zeroc.Ice.UserException
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        int iceP_number;
        ResponsesPrx iceP_responsesProxy;
        iceP_number = istr.readInt();
        iceP_responsesProxy = ResponsesPrx.uncheckedCast(istr.readProxy());
        inS.endReadParams();
        obj.onSuitorReturn(iceP_number, iceP_responsesProxy, current);
        return inS.setResult(inS.writeEmptyParams());
    }

    /**
     * @hidden
     * @param obj -
     * @param inS -
     * @param current -
     * @return -
    **/
    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_passportCase(Requests obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        ResponsesPrx iceP_responsesProxy;
        String iceP_name;
        String iceP_surname;
        int iceP_duration;
        iceP_responsesProxy = ResponsesPrx.uncheckedCast(istr.readProxy());
        iceP_name = istr.readString();
        iceP_surname = istr.readString();
        iceP_duration = istr.readInt();
        inS.endReadParams();
        obj.passportCase(iceP_responsesProxy, iceP_name, iceP_surname, iceP_duration, current);
        return inS.setResult(inS.writeEmptyParams());
    }

    /**
     * @hidden
     * @param obj -
     * @param inS -
     * @param current -
     * @return -
    **/
    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_buildPermitCase(Requests obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        ResponsesPrx iceP_responsesProxy;
        int iceP_surface;
        int iceP_height;
        boolean iceP_useSolarEnergy;
        boolean iceP_isWooden;
        iceP_responsesProxy = ResponsesPrx.uncheckedCast(istr.readProxy());
        iceP_surface = istr.readInt();
        iceP_height = istr.readInt();
        iceP_useSolarEnergy = istr.readBool();
        iceP_isWooden = istr.readBool();
        inS.endReadParams();
        obj.buildPermitCase(iceP_responsesProxy, iceP_surface, iceP_height, iceP_useSolarEnergy, iceP_isWooden, current);
        return inS.setResult(inS.writeEmptyParams());
    }

    /**
     * @hidden
     * @param obj -
     * @param inS -
     * @param current -
     * @return -
    **/
    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_demolitionPermitCase(Requests obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
    {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        ResponsesPrx iceP_responsesProxy;
        int iceP_surface;
        int iceP_height;
        boolean iceP_useDynamite;
        iceP_responsesProxy = ResponsesPrx.uncheckedCast(istr.readProxy());
        iceP_surface = istr.readInt();
        iceP_height = istr.readInt();
        iceP_useDynamite = istr.readBool();
        inS.endReadParams();
        obj.demolitionPermitCase(iceP_responsesProxy, iceP_surface, iceP_height, iceP_useDynamite, current);
        return inS.setResult(inS.writeEmptyParams());
    }

    /** @hidden */
    final static String[] _iceOps =
    {
        "buildPermitCase",
        "demolitionPermitCase",
        "ice_id",
        "ice_ids",
        "ice_isA",
        "ice_ping",
        "onSuitorReturn",
        "passportCase"
    };

    /** @hidden */
    @Override
    default java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceDispatch(com.zeroc.IceInternal.Incoming in, com.zeroc.Ice.Current current)
        throws com.zeroc.Ice.UserException
    {
        int pos = java.util.Arrays.binarySearch(_iceOps, current.operation);
        if(pos < 0)
        {
            throw new com.zeroc.Ice.OperationNotExistException(current.id, current.facet, current.operation);
        }

        switch(pos)
        {
            case 0:
            {
                return _iceD_buildPermitCase(this, in, current);
            }
            case 1:
            {
                return _iceD_demolitionPermitCase(this, in, current);
            }
            case 2:
            {
                return com.zeroc.Ice.Object._iceD_ice_id(this, in, current);
            }
            case 3:
            {
                return com.zeroc.Ice.Object._iceD_ice_ids(this, in, current);
            }
            case 4:
            {
                return com.zeroc.Ice.Object._iceD_ice_isA(this, in, current);
            }
            case 5:
            {
                return com.zeroc.Ice.Object._iceD_ice_ping(this, in, current);
            }
            case 6:
            {
                return _iceD_onSuitorReturn(this, in, current);
            }
            case 7:
            {
                return _iceD_passportCase(this, in, current);
            }
        }

        assert(false);
        throw new com.zeroc.Ice.OperationNotExistException(current.id, current.facet, current.operation);
    }
}
