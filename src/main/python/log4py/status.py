from __future__ import annotations
from overload import overload


 
import java.io.Closeable as __Closeable
__Closeable = __Closeable
import org.apache.logging.log4j.status.StatusListener as __StatusListener
__StatusListener = __StatusListener
from abc import abstractmethod, ABC
 
class StatusListener(ABC, __Closeable, Closeable, __EventListener, EventListener):
    """org.apache.logging.log4j.status.StatusListener"""
 
    @staticmethod
    def __wrap(java_value: __StatusListener) -> 'StatusListener':
        return StatusListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StatusListener):
        """
        Dynamic initializer for StatusListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def close(self, ):
        """public abstract void java.io.Closeable.close() throws java.io.IOException"""
        pass

    @abstractmethod
    def getStatusLevel(self, ):
        """public abstract org.apache.logging.log4j.Level org.apache.logging.log4j.status.StatusListener.getStatusLevel()"""
        pass

    @abstractmethod
    def log(self, data: 'StatusData'):
        """public abstract void org.apache.logging.log4j.status.StatusListener.log(org.apache.logging.log4j.status.StatusData)"""
        pass

 
 
 
# CLASS: org.apache.logging.log4j.status.StatusListener
import java.io.Closeable as __Closeable
__Closeable = __Closeable
import org.apache.logging.log4j.status.StatusListener as __StatusListener
__StatusListener = __StatusListener
from abc import abstractmethod, ABC
 
class StatusListener(ABC, __Closeable, Closeable, __EventListener, EventListener):
    """org.apache.logging.log4j.status.StatusListener"""
 
    @staticmethod
    def __wrap(java_value: __StatusListener) -> 'StatusListener':
        return StatusListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StatusListener):
        """
        Dynamic initializer for StatusListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def close(self, ):
        """public abstract void java.io.Closeable.close() throws java.io.IOException"""
        pass

    @abstractmethod
    def getStatusLevel(self, ):
        """public abstract org.apache.logging.log4j.Level org.apache.logging.log4j.status.StatusListener.getStatusLevel()"""
        pass

    @abstractmethod
    def log(self, data: 'StatusData'):
        """public abstract void org.apache.logging.log4j.status.StatusListener.log(org.apache.logging.log4j.status.StatusData)"""
        pass

 
 
 
# CLASS: org.apache.logging.log4j.status.StatusListener 
 
 
# CLASS: org.apache.logging.log4j.status.StatusData
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.status.StatusData as __StatusData
__StatusData = __StatusData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import org.apache.logging.log4j.Level as __Level
__Level = __Level
from builtins import int
 
class StatusData(__Serializable, Serializable):
    """org.apache.logging.log4j.status.StatusData"""
 
    @staticmethod
    def __wrap(java_value: __StatusData) -> 'StatusData':
        return StatusData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StatusData):
        """
        Dynamic initializer for StatusData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getLevel(self) -> 'log4py.Level':
        """public org.apache.logging.log4j.Level org.apache.logging.log4j.status.StatusData.getLevel()"""
        return 'log4py.Level'.__wrap(super(StatusData, self).getLevel())

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.status.StatusData.getThrowable()"""
        return 'Throwable'.__wrap(super(StatusData, self).getThrowable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMessage(self) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.status.StatusData.getMessage()"""
        return 'message.Message'.__wrap(super(StatusData, self).getMessage())

    @overload
    def getTimestamp(self) -> int:
        """public long org.apache.logging.log4j.status.StatusData.getTimestamp()"""
        return int.__wrap(super(StatusData, self).getTimestamp())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, caller: 'StackTraceElement', level: 'Level', msg: 'Message', t: 'Throwable', threadName: str):
        """public org.apache.logging.log4j.status.StatusData(java.lang.StackTraceElement,org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable,java.lang.String)"""
        val = __StatusData(caller, level, msg, t, threadName)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getStackTraceElement(self) -> 'StackTraceElement':
        """public java.lang.StackTraceElement org.apache.logging.log4j.status.StatusData.getStackTraceElement()"""
        return 'StackTraceElement'.__wrap(super(StatusData, self).getStackTraceElement())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getFormattedStatus(self) -> str:
        """public java.lang.String org.apache.logging.log4j.status.StatusData.getFormattedStatus()"""
        return str.__wrap(super(StatusData, self).getFormattedStatus())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.status.StatusData.toString()"""
        return str.__wrap(super(StatusData, self).toString())

    @overload
    def getThreadName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.status.StatusData.getThreadName()"""
        return str.__wrap(super(StatusData, self).getThreadName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.status.StatusConsoleListener
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.apache.logging.log4j.status.StatusConsoleListener as __StatusConsoleListener
__StatusConsoleListener = __StatusConsoleListener
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

import java.lang.Integer as __int
from builtins import bool
import org.apache.logging.log4j.Level as __Level
__Level = __Level
from builtins import int
 
class StatusConsoleListener(__StatusListener, StatusListener):
    """org.apache.logging.log4j.status.StatusConsoleListener"""
 
    @staticmethod
    def __wrap(java_value: __StatusConsoleListener) -> 'StatusConsoleListener':
        return StatusConsoleListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StatusConsoleListener):
        """
        Dynamic initializer for StatusConsoleListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setLevel(self, level: 'Level'):
        """public void org.apache.logging.log4j.status.StatusConsoleListener.setLevel(org.apache.logging.log4j.Level)"""
        super(__StatusConsoleListener, self).setLevel(level)

    @override
    @overload
    def close(self):
        """public void org.apache.logging.log4j.status.StatusConsoleListener.close() throws java.io.IOException"""
        super(StatusConsoleListener, self).close()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def log(self, data: 'StatusData'):
        """public void org.apache.logging.log4j.status.StatusConsoleListener.log(org.apache.logging.log4j.status.StatusData)"""
        super(__StatusConsoleListener, self).log(data)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, level: 'Level', stream: 'PrintStream'):
        """public org.apache.logging.log4j.status.StatusConsoleListener(org.apache.logging.log4j.Level,java.io.PrintStream)"""
        val = __StatusConsoleListener(level, stream)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getStatusLevel(self) -> 'log4py.Level':
        """public org.apache.logging.log4j.Level org.apache.logging.log4j.status.StatusConsoleListener.getStatusLevel()"""
        return 'log4py.Level'.__wrap(super(StatusConsoleListener, self).getStatusLevel())

    @overload
    def setFilters(self, *filters: str):
        """public void org.apache.logging.log4j.status.StatusConsoleListener.setFilters(java.lang.String...)"""
        super(__StatusConsoleListener, self).setFilters(filters)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, level: 'Level'):
        """public org.apache.logging.log4j.status.StatusConsoleListener(org.apache.logging.log4j.Level)"""
        val = __StatusConsoleListener(level)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.status.StatusLogger
from pyquantum_helper import import_once as __import_once__
import org.apache.logging.log4j.message.EntryMessage as __EntryMessage
__EntryMessage = __EntryMessage
import org.apache.logging.log4j.LogBuilder as __LogBuilder
__LogBuilder = __LogBuilder
from builtins import type
import org.apache.logging.log4j.message.MessageFactory as __MessageFactory
__MessageFactory = __MessageFactory
import org.apache.logging.log4j.message.FlowMessageFactory as __FlowMessageFactory
__FlowMessageFactory = __FlowMessageFactory
import java.lang.Class as __Class
__Class = __Class
try:
    from log4py import spi
except ImportError:
    spi = __import_once__("log4py.spi")

import java.lang.String as __string
import org.apache.logging.log4j.spi.AbstractLogger as __AbstractLogger
__AbstractLogger = __AbstractLogger
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.lang.Iterable as Iterable
from builtins import object
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

import org.apache.logging.log4j.status.StatusLogger as __StatusLogger
__StatusLogger = __StatusLogger
import java.lang.StackTraceElement as StackTraceElement
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import org.apache.logging.log4j.Level as __Level
__Level = __Level
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class StatusLogger(log4py.__AbstractLogger, spi.AbstractLogger):
    """org.apache.logging.log4j.status.StatusLogger"""
 
    @staticmethod
    def __wrap(java_value: __StatusLogger) -> 'StatusLogger':
        return StatusLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StatusLogger):
        """
        Dynamic initializer for StatusLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(messageSupplier, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def info(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(message, throwable)

    @overload
    def registerListener(self, listener: 'StatusListener'):
        """public void org.apache.logging.log4j.status.StatusLogger.registerListener(org.apache.logging.log4j.status.StatusListener)"""
        super(__StatusLogger, self).registerListener(listener)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def info(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).trace(marker, message, paramSuppliers)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__spi.AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def isFatalEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__spi.AbstractLogger, self).isFatalEnabled(marker))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1, p2)

    @overload
    def traceExit(self, message: 'Message', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        return object.__wrap(super(__spi.AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def log(self, level: 'Level', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        super(__spi.AbstractLogger, self).log(level, message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1, p2)

    @override
    @overload
    def traceExit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit()"""
        super(spi.AbstractLogger, self).traceExit()

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0)

    @override
    @overload
    def info(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0)

    @overload
    def traceExit(self, message: 'EntryMessage', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        return object.__wrap(super(__spi.AbstractLogger, self).traceExit(message, result))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0))

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).info(message, params)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).warn(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, throwable)

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'.__wrap(super(__spi.AbstractLogger, self).atLevel(level))

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5)

    @overload
    def clear(self):
        """public void org.apache.logging.log4j.status.StatusLogger.clear()"""
        super(StatusLogger, self).clear()

    @override
    @overload
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1, p2)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def getFlowMessageFactory(self) -> 'message.FlowMessageFactory':
        """public org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.spi.AbstractLogger.getFlowMessageFactory()"""
        return 'message.FlowMessageFactory'.__wrap(super(spi.AbstractLogger, self).getFlowMessageFactory())

    @overload
    def throwing(self, level: 'Level', throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(org.apache.logging.log4j.Level,T)"""
        return 'Throwable'.__wrap(super(__spi.AbstractLogger, self).throwing(level, throwable))

    @override
    @overload
    def info(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String)"""
        super(__spi.AbstractLogger, self).info(message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__spi.AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, t))

    @overload
    def isWarnEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__spi.AbstractLogger, self).isWarnEnabled(marker))

    @override
    @overload
    def info(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).info(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message))

    @override
    @overload
    def error(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).error(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).log(level, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).catching(level, throwable)

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atDebug()"""
        return 'log4py.LogBuilder'.__wrap(super(spi.AbstractLogger, self).atDebug())

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1)

    @override
    @overload
    def getMessageFactory(self) -> 'message.MessageFactory':
        """public <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.spi.AbstractLogger.getMessageFactory()"""
        return 'message.MessageFactory'.__wrap(super(spi.AbstractLogger, self).getMessageFactory())

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message)

    @overload
    def exit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.exit(R)"""
        return object.__wrap(super(__spi.AbstractLogger, self).exit(result))

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def isFatalEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled()"""
        return bool.__wrap(super(spi.AbstractLogger, self).isFatalEnabled())

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0)

    @overload
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'.__wrap(super(__spi.AbstractLogger, self).traceEntry(format, paramSuppliers))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1)

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled()"""
        return bool.__wrap(super(spi.AbstractLogger, self).isDebugEnabled())

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def debug(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String)"""
        super(__spi.AbstractLogger, self).debug(message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, params)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atTrace()"""
        return 'log4py.LogBuilder'.__wrap(super(spi.AbstractLogger, self).atTrace())

    @override
    @overload
    def fatal(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).warn(messageSupplier)

    @overload
    def traceEntry(self, message: 'Message') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.message.Message)"""
        return 'message.EntryMessage'.__wrap(super(__spi.AbstractLogger, self).traceEntry(message))

    @override
    @overload
    def debug(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).debug(message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1)

    @override
    @overload
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def isDebugEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__spi.AbstractLogger, self).isDebugEnabled(marker))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def entry(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry()"""
        super(spi.AbstractLogger, self).entry()

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1)

    @overload
    def traceEntry(self, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'.__wrap(super(__spi.AbstractLogger, self).traceEntry(paramSuppliers))

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, *params: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, params))

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def isInfoEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__spi.AbstractLogger, self).isInfoEnabled(marker))

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def trace(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).trace(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1, p2))

    @override
    @overload
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).warn(message)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4)

    @overload
    def isEnabled(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level)"""
        return bool.__wrap(super(__spi.AbstractLogger, self).isEnabled(level))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.AbstractLogger.getName()"""
        return str.__wrap(super(spi.AbstractLogger, self).getName())

    @override
    @overload
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(marker, message, throwable)

    @overload
    def getListeners(self) -> 'Iterable':
        """public java.lang.Iterable<org.apache.logging.log4j.status.StatusListener> org.apache.logging.log4j.status.StatusLogger.getListeners()"""
        return 'Iterable'.__wrap(super(StatusLogger, self).getListeners())

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def fatal(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).fatal(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__spi.AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4)

    @staticmethod
    @overload
    def getRecursionDepth() -> int:
        """public static int org.apache.logging.log4j.spi.AbstractLogger.getRecursionDepth()"""
        return int.__wrap(__AbstractLogger.getRecursionDepth())

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def error(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled()"""
        return bool.__wrap(super(spi.AbstractLogger, self).isTraceEnabled())

    @override
    @overload
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0)

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atError()"""
        return 'log4py.LogBuilder'.__wrap(super(spi.AbstractLogger, self).atError())

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def error(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def trace(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).warn(marker, message, params)

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atWarn()"""
        return 'log4py.LogBuilder'.__wrap(super(spi.AbstractLogger, self).atWarn())

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1, p2, p3)

    @override
    @overload
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).error(message, paramSuppliers)

    @override
    @overload
    def info(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message)

    @override
    @overload
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def traceEntry(self) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry()"""
        return 'message.EntryMessage'.__wrap(super(spi.AbstractLogger, self).traceEntry())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).trace(marker, messageSupplier)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4))

    @override
    @overload
    def debug(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).log(level, message)

    @override
    @overload
    def catching(self, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).catching(throwable)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def traceExit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(R)"""
        return object.__wrap(super(__spi.AbstractLogger, self).traceExit(result))

    @override
    @overload
    def debug(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(message, throwable)

    @overload
    def isErrorEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__spi.AbstractLogger, self).isErrorEnabled(marker))

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1, p2, p3)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled()"""
        return bool.__wrap(super(spi.AbstractLogger, self).isWarnEnabled())

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).info(marker, message)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(marker, message, throwable)

    @overload
    def throwing(self, throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(T)"""
        return 'Throwable'.__wrap(super(__spi.AbstractLogger, self).throwing(throwable))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def getStatusData(self) -> 'List':
        """public java.util.List<org.apache.logging.log4j.status.StatusData> org.apache.logging.log4j.status.StatusLogger.getStatusData()"""
        return 'List'.__wrap(super(StatusLogger, self).getStatusData())

    @override
    @overload
    def debug(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).debug(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atFatal()"""
        return 'log4py.LogBuilder'.__wrap(super(spi.AbstractLogger, self).atFatal())

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: object, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def warn(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).warn(message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled()"""
        return bool.__wrap(super(spi.AbstractLogger, self).isInfoEnabled())

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).fatal(message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message)

    @override
    @overload
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).info(message)

    @overload
    def updateListenerLevel(self, status: 'Level'):
        """public void org.apache.logging.log4j.status.StatusLogger.updateListenerLevel(org.apache.logging.log4j.Level)"""
        super(__StatusLogger, self).updateListenerLevel(status)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).trace(message, params)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).printf(level, marker, format, params)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5)

    @overload
    def reset(self):
        """public void org.apache.logging.log4j.status.StatusLogger.reset()"""
        super(StatusLogger, self).reset()

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).trace(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).debug(marker, message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def debug(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).debug(message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def getLevel(self) -> 'log4py.Level':
        """public org.apache.logging.log4j.Level org.apache.logging.log4j.status.StatusLogger.getLevel()"""
        return 'log4py.Level'.__wrap(super(StatusLogger, self).getLevel())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__spi.AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__spi.AbstractLogger, self).error(marker, message)

    @override
    @overload
    def error(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).error(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def entry(self, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry(java.lang.Object...)"""
        super(__spi.AbstractLogger, self).entry(params)

    @override
    @overload
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).warn(message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def warn(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String)"""
        super(__spi.AbstractLogger, self).warn(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).debug(marker, message, params)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, paramSuppliers)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__spi.AbstractLogger, self).info(marker, message)

    @override
    @overload
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).trace(message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).warn(marker, message, paramSuppliers)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(__spi.AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1, p2)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).fatal(message, params)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def trace(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String)"""
        super(__spi.AbstractLogger, self).trace(message)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).error(marker, message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1, p2)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled()"""
        return bool.__wrap(super(spi.AbstractLogger, self).isErrorEnabled())

    @overload
    def traceExit(self, format: str, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(java.lang.String,R)"""
        return object.__wrap(super(__spi.AbstractLogger, self).traceExit(format, result))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).info(message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0, p1)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(marker, messageSupplier, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker))

    @override
    @overload
    def error(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).error(message, params)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, params)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1, p2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def exit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.exit()"""
        super(spi.AbstractLogger, self).exit()

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1, p2)

    @override
    @overload
    def traceExit(self, message: 'EntryMessage'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        super(__spi.AbstractLogger, self).traceExit(message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1))

    @override
    @overload
    def log(self, level: 'Level', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).log(level, message, params)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1, p2, p3)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).error(marker, message, paramSuppliers)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).info(marker, message, paramSuppliers)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1, p2)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atInfo()"""
        return 'log4py.LogBuilder'.__wrap(super(spi.AbstractLogger, self).atInfo())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1, p2)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(marker, message, throwable)

    @staticmethod
    @overload
    def checkMessageFactory(logger: 'ExtendedLogger', messageFactory: 'MessageFactory'):
        """public static void org.apache.logging.log4j.spi.AbstractLogger.checkMessageFactory(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.message.MessageFactory)"""
        __AbstractLogger.checkMessageFactory(logger, messageFactory)

    @override
    @overload
    def fatal(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String)"""
        super(__spi.AbstractLogger, self).fatal(message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(__spi.AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.always()"""
        return 'log4py.LogBuilder'.__wrap(super(spi.AbstractLogger, self).always())

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @overload
    def isTraceEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        return bool.__wrap(super(__spi.AbstractLogger, self).isTraceEnabled(marker))

    @override
    @overload
    def warn(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).error(marker, message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(marker, message, p0)

    @override
    @overload
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).info(marker, message, params)

    @override
    @overload
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1)

    @override
    @overload
    def error(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String)"""
        super(__spi.AbstractLogger, self).error(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def traceEntry(self, format: str, *params: object) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,java.lang.Object...)"""
        return 'message.EntryMessage'.__wrap(super(__spi.AbstractLogger, self).traceEntry(format, params))

    @staticmethod
    @overload
    def getLogger() -> 'StatusLogger':
        """public static org.apache.logging.log4j.status.StatusLogger org.apache.logging.log4j.status.StatusLogger.getLogger()"""
        return StatusLogger.__wrap(__StatusLogger.getLogger())

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).debug(message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__spi.AbstractLogger, self).log(level, message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1, p2, p3))

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(__spi.AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def trace(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).trace(message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(messageSupplier, throwable)

    @overload
    def removeListener(self, listener: 'StatusListener'):
        """public void org.apache.logging.log4j.status.StatusLogger.removeListener(org.apache.logging.log4j.status.StatusListener)"""
        super(__StatusLogger, self).removeListener(listener)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def setLevel(self, level: 'Level'):
        """public void org.apache.logging.log4j.status.StatusLogger.setLevel(org.apache.logging.log4j.Level)"""
        super(__StatusLogger, self).setLevel(level)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).info(marker, message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> bool:
        """public boolean org.apache.logging.log4j.status.StatusLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__StatusLogger, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logMessage(self, fqcn: str, level: 'Level', marker: 'Marker', msg: 'Message', t: 'Throwable'):
        """public void org.apache.logging.log4j.status.StatusLogger.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__StatusLogger, self).logMessage(fqcn, level, marker, msg, t)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, p0, p1)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).fatal(marker, message, params)

    @override
    @overload
    def error(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).error(message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).info(message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def trace(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message)

    @override
    @overload
    def error(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(__spi.AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def printf(self, level: 'Level', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(__spi.AbstractLogger, self).printf(level, format, params)

    @override
    @overload
    def fatal(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence)"""
        super(__spi.AbstractLogger, self).fatal(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(__spi.AbstractLogger, self).info(marker, message, throwable)