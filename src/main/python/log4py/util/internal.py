from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.io.ObjectOutputStream as ObjectOutputStream
import org.apache.logging.log4j.util.internal.SerializationUtil as __SerializationUtil
__SerializationUtil = __SerializationUtil
import java.io.ObjectInputStream as ObjectInputStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.io.Serializable as Serializable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SerializationUtil():
    """org.apache.logging.log4j.util.internal.SerializationUtil"""
 
    @staticmethod
    def __wrap(java_value: __SerializationUtil) -> 'SerializationUtil':
        return SerializationUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SerializationUtil):
        """
        Dynamic initializer for SerializationUtil.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def readWrappedObject(in: 'ObjectInputStream') -> object:
        """public static java.lang.Object org.apache.logging.log4j.util.internal.SerializationUtil.readWrappedObject(java.io.ObjectInputStream) throws java.io.IOException,java.lang.ClassNotFoundException"""
        return object.__wrap(__SerializationUtil.readWrappedObject(in))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def assertFiltered(stream: 'ObjectInputStream'):
        """public static void org.apache.logging.log4j.util.internal.SerializationUtil.assertFiltered(java.io.ObjectInputStream)"""
        __SerializationUtil.assertFiltered(stream)

    @staticmethod
    @overload
    def writeWrappedObject(obj: 'Serializable', out: 'ObjectOutputStream'):
        """public static void org.apache.logging.log4j.util.internal.SerializationUtil.writeWrappedObject(java.io.Serializable,java.io.ObjectOutputStream) throws java.io.IOException"""
        __SerializationUtil.writeWrappedObject(obj, out)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: org.apache.logging.log4j.util.internal.SerializationUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.io.ObjectOutputStream as ObjectOutputStream
import org.apache.logging.log4j.util.internal.SerializationUtil as __SerializationUtil
__SerializationUtil = __SerializationUtil
import java.io.ObjectInputStream as ObjectInputStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.io.Serializable as Serializable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SerializationUtil():
    """org.apache.logging.log4j.util.internal.SerializationUtil"""
 
    @staticmethod
    def __wrap(java_value: __SerializationUtil) -> 'SerializationUtil':
        return SerializationUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SerializationUtil):
        """
        Dynamic initializer for SerializationUtil.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def readWrappedObject(in: 'ObjectInputStream') -> object:
        """public static java.lang.Object org.apache.logging.log4j.util.internal.SerializationUtil.readWrappedObject(java.io.ObjectInputStream) throws java.io.IOException,java.lang.ClassNotFoundException"""
        return object.__wrap(__SerializationUtil.readWrappedObject(in))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def assertFiltered(stream: 'ObjectInputStream'):
        """public static void org.apache.logging.log4j.util.internal.SerializationUtil.assertFiltered(java.io.ObjectInputStream)"""
        __SerializationUtil.assertFiltered(stream)

    @staticmethod
    @overload
    def writeWrappedObject(obj: 'Serializable', out: 'ObjectOutputStream'):
        """public static void org.apache.logging.log4j.util.internal.SerializationUtil.writeWrappedObject(java.io.Serializable,java.io.ObjectOutputStream) throws java.io.IOException"""
        __SerializationUtil.writeWrappedObject(obj, out)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: org.apache.logging.log4j.util.internal.SerializationUtil