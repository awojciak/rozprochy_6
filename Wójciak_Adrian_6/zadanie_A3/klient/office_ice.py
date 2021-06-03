# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.5
#
# <auto-generated>
#
# Generated from file `office.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Office
_M_Office = Ice.openModule('Office')
__name__ = 'Office'

if 'Time' not in _M_Office.__dict__:
    _M_Office.Time = Ice.createTempClass()
    class Time(object):
        def __init__(self, hour=0, minute=0, second=0):
            self.hour = hour
            self.minute = minute
            self.second = second

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.hour)
            _h = 5 * _h + Ice.getHash(self.minute)
            _h = 5 * _h + Ice.getHash(self.second)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_Office.Time):
                return NotImplemented
            else:
                if self.hour is None or other.hour is None:
                    if self.hour != other.hour:
                        return (-1 if self.hour is None else 1)
                else:
                    if self.hour < other.hour:
                        return -1
                    elif self.hour > other.hour:
                        return 1
                if self.minute is None or other.minute is None:
                    if self.minute != other.minute:
                        return (-1 if self.minute is None else 1)
                else:
                    if self.minute < other.minute:
                        return -1
                    elif self.minute > other.minute:
                        return 1
                if self.second is None or other.second is None:
                    if self.second != other.second:
                        return (-1 if self.second is None else 1)
                else:
                    if self.second < other.second:
                        return -1
                    elif self.second > other.second:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_Office._t_Time)

        __repr__ = __str__

    _M_Office._t_Time = IcePy.defineStruct('::Office::Time', Time, (), (
        ('hour', (), IcePy._t_int),
        ('minute', (), IcePy._t_int),
        ('second', (), IcePy._t_int)
    ))

    _M_Office.Time = Time
    del Time

if 'Result' not in _M_Office.__dict__:
    _M_Office.Result = Ice.createTempClass()
    class Result(object):
        def __init__(self, isResultPositive=False, finalEndTime=Ice._struct_marker, caseType=''):
            self.isResultPositive = isResultPositive
            if finalEndTime is Ice._struct_marker:
                self.finalEndTime = _M_Office.Time()
            else:
                self.finalEndTime = finalEndTime
            self.caseType = caseType

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.isResultPositive)
            _h = 5 * _h + Ice.getHash(self.finalEndTime)
            _h = 5 * _h + Ice.getHash(self.caseType)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_Office.Result):
                return NotImplemented
            else:
                if self.isResultPositive is None or other.isResultPositive is None:
                    if self.isResultPositive != other.isResultPositive:
                        return (-1 if self.isResultPositive is None else 1)
                else:
                    if self.isResultPositive < other.isResultPositive:
                        return -1
                    elif self.isResultPositive > other.isResultPositive:
                        return 1
                if self.finalEndTime is None or other.finalEndTime is None:
                    if self.finalEndTime != other.finalEndTime:
                        return (-1 if self.finalEndTime is None else 1)
                else:
                    if self.finalEndTime < other.finalEndTime:
                        return -1
                    elif self.finalEndTime > other.finalEndTime:
                        return 1
                if self.caseType is None or other.caseType is None:
                    if self.caseType != other.caseType:
                        return (-1 if self.caseType is None else 1)
                else:
                    if self.caseType < other.caseType:
                        return -1
                    elif self.caseType > other.caseType:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_Office._t_Result)

        __repr__ = __str__

    _M_Office._t_Result = IcePy.defineStruct('::Office::Result', Result, (), (
        ('isResultPositive', (), IcePy._t_bool),
        ('finalEndTime', (), _M_Office._t_Time),
        ('caseType', (), IcePy._t_string)
    ))

    _M_Office.Result = Result
    del Result

_M_Office._t_Responses = IcePy.defineValue('::Office::Responses', Ice.Value, -1, (), False, True, None, ())

if 'ResponsesPrx' not in _M_Office.__dict__:
    _M_Office.ResponsesPrx = Ice.createTempClass()
    class ResponsesPrx(Ice.ObjectPrx):

        def getNumber(self, number, context=None):
            return _M_Office.Responses._op_getNumber.invoke(self, ((number, ), context))

        def getNumberAsync(self, number, context=None):
            return _M_Office.Responses._op_getNumber.invokeAsync(self, ((number, ), context))

        def begin_getNumber(self, number, _response=None, _ex=None, _sent=None, context=None):
            return _M_Office.Responses._op_getNumber.begin(self, ((number, ), _response, _ex, _sent, context))

        def end_getNumber(self, _r):
            return _M_Office.Responses._op_getNumber.end(self, _r)

        def getReturnConfirmation(self, context=None):
            return _M_Office.Responses._op_getReturnConfirmation.invoke(self, ((), context))

        def getReturnConfirmationAsync(self, context=None):
            return _M_Office.Responses._op_getReturnConfirmation.invokeAsync(self, ((), context))

        def begin_getReturnConfirmation(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Office.Responses._op_getReturnConfirmation.begin(self, ((), _response, _ex, _sent, context))

        def end_getReturnConfirmation(self, _r):
            return _M_Office.Responses._op_getReturnConfirmation.end(self, _r)

        def getExpectedEndTime(self, expectedEndTime, context=None):
            return _M_Office.Responses._op_getExpectedEndTime.invoke(self, ((expectedEndTime, ), context))

        def getExpectedEndTimeAsync(self, expectedEndTime, context=None):
            return _M_Office.Responses._op_getExpectedEndTime.invokeAsync(self, ((expectedEndTime, ), context))

        def begin_getExpectedEndTime(self, expectedEndTime, _response=None, _ex=None, _sent=None, context=None):
            return _M_Office.Responses._op_getExpectedEndTime.begin(self, ((expectedEndTime, ), _response, _ex, _sent, context))

        def end_getExpectedEndTime(self, _r):
            return _M_Office.Responses._op_getExpectedEndTime.end(self, _r)

        def getResult(self, result, context=None):
            return _M_Office.Responses._op_getResult.invoke(self, ((result, ), context))

        def getResultAsync(self, result, context=None):
            return _M_Office.Responses._op_getResult.invokeAsync(self, ((result, ), context))

        def begin_getResult(self, result, _response=None, _ex=None, _sent=None, context=None):
            return _M_Office.Responses._op_getResult.begin(self, ((result, ), _response, _ex, _sent, context))

        def end_getResult(self, _r):
            return _M_Office.Responses._op_getResult.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Office.ResponsesPrx.ice_checkedCast(proxy, '::Office::Responses', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Office.ResponsesPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Office::Responses'
    _M_Office._t_ResponsesPrx = IcePy.defineProxy('::Office::Responses', ResponsesPrx)

    _M_Office.ResponsesPrx = ResponsesPrx
    del ResponsesPrx

    _M_Office.Responses = Ice.createTempClass()
    class Responses(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Office::Responses')

        def ice_id(self, current=None):
            return '::Office::Responses'

        @staticmethod
        def ice_staticId():
            return '::Office::Responses'

        def getNumber(self, number, current=None):
            raise NotImplementedError("servant method 'getNumber' not implemented")

        def getReturnConfirmation(self, current=None):
            raise NotImplementedError("servant method 'getReturnConfirmation' not implemented")

        def getExpectedEndTime(self, expectedEndTime, current=None):
            raise NotImplementedError("servant method 'getExpectedEndTime' not implemented")

        def getResult(self, result, current=None):
            raise NotImplementedError("servant method 'getResult' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Office._t_ResponsesDisp)

        __repr__ = __str__

    _M_Office._t_ResponsesDisp = IcePy.defineClass('::Office::Responses', Responses, (), None, ())
    Responses._ice_type = _M_Office._t_ResponsesDisp

    Responses._op_getNumber = IcePy.Operation('getNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, ())
    Responses._op_getReturnConfirmation = IcePy.Operation('getReturnConfirmation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Responses._op_getExpectedEndTime = IcePy.Operation('getExpectedEndTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Office._t_Time, False, 0),), (), None, ())
    Responses._op_getResult = IcePy.Operation('getResult', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Office._t_Result, False, 0),), (), None, ())

    _M_Office.Responses = Responses
    del Responses

_M_Office._t_Requests = IcePy.defineValue('::Office::Requests', Ice.Value, -1, (), False, True, None, ())

if 'RequestsPrx' not in _M_Office.__dict__:
    _M_Office.RequestsPrx = Ice.createTempClass()
    class RequestsPrx(Ice.ObjectPrx):

        def onSuitorReturn(self, number, responsesProxy, context=None):
            return _M_Office.Requests._op_onSuitorReturn.invoke(self, ((number, responsesProxy), context))

        def onSuitorReturnAsync(self, number, responsesProxy, context=None):
            return _M_Office.Requests._op_onSuitorReturn.invokeAsync(self, ((number, responsesProxy), context))

        def begin_onSuitorReturn(self, number, responsesProxy, _response=None, _ex=None, _sent=None, context=None):
            return _M_Office.Requests._op_onSuitorReturn.begin(self, ((number, responsesProxy), _response, _ex, _sent, context))

        def end_onSuitorReturn(self, _r):
            return _M_Office.Requests._op_onSuitorReturn.end(self, _r)

        def passportCase(self, responsesProxy, name, surname, duration, context=None):
            return _M_Office.Requests._op_passportCase.invoke(self, ((responsesProxy, name, surname, duration), context))

        def passportCaseAsync(self, responsesProxy, name, surname, duration, context=None):
            return _M_Office.Requests._op_passportCase.invokeAsync(self, ((responsesProxy, name, surname, duration), context))

        def begin_passportCase(self, responsesProxy, name, surname, duration, _response=None, _ex=None, _sent=None, context=None):
            return _M_Office.Requests._op_passportCase.begin(self, ((responsesProxy, name, surname, duration), _response, _ex, _sent, context))

        def end_passportCase(self, _r):
            return _M_Office.Requests._op_passportCase.end(self, _r)

        def buildPermitCase(self, responsesProxy, surface, height, useSolarEnergy, isWooden, context=None):
            return _M_Office.Requests._op_buildPermitCase.invoke(self, ((responsesProxy, surface, height, useSolarEnergy, isWooden), context))

        def buildPermitCaseAsync(self, responsesProxy, surface, height, useSolarEnergy, isWooden, context=None):
            return _M_Office.Requests._op_buildPermitCase.invokeAsync(self, ((responsesProxy, surface, height, useSolarEnergy, isWooden), context))

        def begin_buildPermitCase(self, responsesProxy, surface, height, useSolarEnergy, isWooden, _response=None, _ex=None, _sent=None, context=None):
            return _M_Office.Requests._op_buildPermitCase.begin(self, ((responsesProxy, surface, height, useSolarEnergy, isWooden), _response, _ex, _sent, context))

        def end_buildPermitCase(self, _r):
            return _M_Office.Requests._op_buildPermitCase.end(self, _r)

        def demolitionPermitCase(self, responsesProxy, surface, height, useDynamite, context=None):
            return _M_Office.Requests._op_demolitionPermitCase.invoke(self, ((responsesProxy, surface, height, useDynamite), context))

        def demolitionPermitCaseAsync(self, responsesProxy, surface, height, useDynamite, context=None):
            return _M_Office.Requests._op_demolitionPermitCase.invokeAsync(self, ((responsesProxy, surface, height, useDynamite), context))

        def begin_demolitionPermitCase(self, responsesProxy, surface, height, useDynamite, _response=None, _ex=None, _sent=None, context=None):
            return _M_Office.Requests._op_demolitionPermitCase.begin(self, ((responsesProxy, surface, height, useDynamite), _response, _ex, _sent, context))

        def end_demolitionPermitCase(self, _r):
            return _M_Office.Requests._op_demolitionPermitCase.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Office.RequestsPrx.ice_checkedCast(proxy, '::Office::Requests', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Office.RequestsPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Office::Requests'
    _M_Office._t_RequestsPrx = IcePy.defineProxy('::Office::Requests', RequestsPrx)

    _M_Office.RequestsPrx = RequestsPrx
    del RequestsPrx

    _M_Office.Requests = Ice.createTempClass()
    class Requests(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Office::Requests')

        def ice_id(self, current=None):
            return '::Office::Requests'

        @staticmethod
        def ice_staticId():
            return '::Office::Requests'

        def onSuitorReturn(self, number, responsesProxy, current=None):
            raise NotImplementedError("servant method 'onSuitorReturn' not implemented")

        def passportCase(self, responsesProxy, name, surname, duration, current=None):
            raise NotImplementedError("servant method 'passportCase' not implemented")

        def buildPermitCase(self, responsesProxy, surface, height, useSolarEnergy, isWooden, current=None):
            raise NotImplementedError("servant method 'buildPermitCase' not implemented")

        def demolitionPermitCase(self, responsesProxy, surface, height, useDynamite, current=None):
            raise NotImplementedError("servant method 'demolitionPermitCase' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Office._t_RequestsDisp)

        __repr__ = __str__

    _M_Office._t_RequestsDisp = IcePy.defineClass('::Office::Requests', Requests, (), None, ())
    Requests._ice_type = _M_Office._t_RequestsDisp

    Requests._op_onSuitorReturn = IcePy.Operation('onSuitorReturn', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), _M_Office._t_ResponsesPrx, False, 0)), (), None, ())
    Requests._op_passportCase = IcePy.Operation('passportCase', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Office._t_ResponsesPrx, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0)), (), None, ())
    Requests._op_buildPermitCase = IcePy.Operation('buildPermitCase', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Office._t_ResponsesPrx, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_bool, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    Requests._op_demolitionPermitCase = IcePy.Operation('demolitionPermitCase', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Office._t_ResponsesPrx, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())

    _M_Office.Requests = Requests
    del Requests

# End of module Office
