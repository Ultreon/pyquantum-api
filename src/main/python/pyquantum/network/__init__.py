from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

from pyquantum_helper import override
import java.net.InetAddress as InetAddress
import java.lang.Object as __object
import dev.ultreon.quantum.network.ServerConnections as __ServerConnections
__ServerConnections = __ServerConnections
from builtins import type
import dev.ultreon.quantum.network.system.TcpNetworker as __TcpNetworker
__TcpNetworker = __TcpNetworker
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
import dev.ultreon.quantum.network.NetworkChannel as __NetworkChannel
__NetworkChannel = __NetworkChannel
import java.util.Collection as Collection
import dev.ultreon.quantum.network.MemoryNetworker as __MemoryNetworker
__MemoryNetworker = __MemoryNetworker
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class ServerConnections():
    """dev.ultreon.quantum.network.ServerConnections"""
 
    @staticmethod
    def __wrap(java_value: __ServerConnections) -> 'ServerConnections':
        return ServerConnections(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerConnections):
        """
        Dynamic initializer for ServerConnections.
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

    @staticmethod
    @overload
    def registerChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.ServerConnections.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel.__wrap(__ServerConnections.registerChannel(arg0))

    @overload
    def stop(self):
        """public void dev.ultreon.quantum.network.ServerConnections.stop()"""
        super(ServerConnections, self).stop()

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.network.ServerConnections.tick()"""
        super(ServerConnections, self).tick()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.ServerConnections.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel.__wrap(__ServerConnections.getChannel(arg0))

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.network.ServerConnections.getServer()"""
        return 'server.QuantumServer'.__wrap(super(ServerConnections, self).getServer())

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

    @staticmethod
    @overload
    def getChannels() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.quantum.network.NetworkChannel> dev.ultreon.quantum.network.ServerConnections.getChannels()"""
        return Collection.__wrap(__ServerConnections.getChannels())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'QuantumServer'):
        """public dev.ultreon.quantum.network.ServerConnections(dev.ultreon.quantum.server.QuantumServer)"""
        val = __ServerConnections(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.ServerConnections.toString()"""
        return str.__wrap(super(ServerConnections, self).toString())

    @overload
    def startMemoryServer(self, arg0: 'MemoryConnection') -> 'MemoryNetworker':
        """public dev.ultreon.quantum.network.MemoryNetworker dev.ultreon.quantum.network.ServerConnections.startMemoryServer(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        return 'MemoryNetworker'.__wrap(super(__ServerConnections, self).startMemoryServer(arg0))

    @overload
    def startTcpServer(self, arg0: 'InetAddress', arg1: int) -> 'system.TcpNetworker':
        """public dev.ultreon.quantum.network.system.TcpNetworker dev.ultreon.quantum.network.ServerConnections.startTcpServer(java.net.InetAddress,int) throws dev.ultreon.quantum.network.ServerHostingException"""
        return 'system.TcpNetworker'.__wrap(super(__ServerConnections, self).startTcpServer(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.network.ServerConnections.isRunning()"""
        return bool.__wrap(super(ServerConnections, self).isRunning())

 
 
 
# CLASS: dev.ultreon.quantum.network.ServerConnections
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

from pyquantum_helper import override
import java.net.InetAddress as InetAddress
import java.lang.Object as __object
import dev.ultreon.quantum.network.ServerConnections as __ServerConnections
__ServerConnections = __ServerConnections
from builtins import type
import dev.ultreon.quantum.network.system.TcpNetworker as __TcpNetworker
__TcpNetworker = __TcpNetworker
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
import dev.ultreon.quantum.network.NetworkChannel as __NetworkChannel
__NetworkChannel = __NetworkChannel
import java.util.Collection as Collection
import dev.ultreon.quantum.network.MemoryNetworker as __MemoryNetworker
__MemoryNetworker = __MemoryNetworker
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class ServerConnections():
    """dev.ultreon.quantum.network.ServerConnections"""
 
    @staticmethod
    def __wrap(java_value: __ServerConnections) -> 'ServerConnections':
        return ServerConnections(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerConnections):
        """
        Dynamic initializer for ServerConnections.
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

    @staticmethod
    @overload
    def registerChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.ServerConnections.registerChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel.__wrap(__ServerConnections.registerChannel(arg0))

    @overload
    def stop(self):
        """public void dev.ultreon.quantum.network.ServerConnections.stop()"""
        super(ServerConnections, self).stop()

    @overload
    def tick(self):
        """public void dev.ultreon.quantum.network.ServerConnections.tick()"""
        super(ServerConnections, self).tick()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.ServerConnections.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel.__wrap(__ServerConnections.getChannel(arg0))

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.network.ServerConnections.getServer()"""
        return 'server.QuantumServer'.__wrap(super(ServerConnections, self).getServer())

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

    @staticmethod
    @overload
    def getChannels() -> 'Collection':
        """public static java.util.Collection<dev.ultreon.quantum.network.NetworkChannel> dev.ultreon.quantum.network.ServerConnections.getChannels()"""
        return Collection.__wrap(__ServerConnections.getChannels())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'QuantumServer'):
        """public dev.ultreon.quantum.network.ServerConnections(dev.ultreon.quantum.server.QuantumServer)"""
        val = __ServerConnections(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.ServerConnections.toString()"""
        return str.__wrap(super(ServerConnections, self).toString())

    @overload
    def startMemoryServer(self, arg0: 'MemoryConnection') -> 'MemoryNetworker':
        """public dev.ultreon.quantum.network.MemoryNetworker dev.ultreon.quantum.network.ServerConnections.startMemoryServer(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        return 'MemoryNetworker'.__wrap(super(__ServerConnections, self).startMemoryServer(arg0))

    @overload
    def startTcpServer(self, arg0: 'InetAddress', arg1: int) -> 'system.TcpNetworker':
        """public dev.ultreon.quantum.network.system.TcpNetworker dev.ultreon.quantum.network.ServerConnections.startTcpServer(java.net.InetAddress,int) throws dev.ultreon.quantum.network.ServerHostingException"""
        return 'system.TcpNetworker'.__wrap(super(__ServerConnections, self).startTcpServer(arg0, __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.network.ServerConnections.isRunning()"""
        return bool.__wrap(super(ServerConnections, self).isRunning())

 
 
 
# CLASS: dev.ultreon.quantum.network.ServerConnections 
 
 
# CLASS: dev.ultreon.quantum.network.DataOverflowException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.DataOverflowException as __DataOverflowException
__DataOverflowException = __DataOverflowException
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DataOverflowException(__PacketException, PacketException):
    """dev.ultreon.quantum.network.DataOverflowException"""
 
    @staticmethod
    def __wrap(java_value: __DataOverflowException) -> 'DataOverflowException':
        return DataOverflowException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataOverflowException):
        """
        Dynamic initializer for DataOverflowException.
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

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public dev.ultreon.quantum.network.DataOverflowException(java.lang.String,int,int)"""
        val = __DataOverflowException(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.network.Networker
import java.io.Closeable as __Closeable
__Closeable = __Closeable
from abc import abstractmethod, ABC
import dev.ultreon.quantum.network.Networker as __Networker
__Networker = __Networker
 
class Networker(ABC, __Closeable, Closeable):
    """dev.ultreon.quantum.network.Networker"""
 
    @staticmethod
    def __wrap(java_value: __Networker) -> 'Networker':
        return Networker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Networker):
        """
        Dynamic initializer for Networker.
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
    def tick(self, ):
        """public abstract void dev.ultreon.quantum.network.Networker.tick()"""
        pass

    @abstractmethod
    def isRunning(self, ):
        """public abstract boolean dev.ultreon.quantum.network.Networker.isRunning()"""
        pass

    @abstractmethod
    def getConnections(self, ):
        """public abstract java.util.List<? extends dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.server.ServerPacketHandler, dev.ultreon.quantum.network.client.ClientPacketHandler>> dev.ultreon.quantum.network.Networker.getConnections()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.network.PacketIO
from pyquantum_helper import import_once as __import_once__
import java.net.Socket as Socket
import java.util.UUID as UUID
import dev.ultreon.libs.commons.v0.vector.Vec2i as __Vec2i
__Vec2i = __Vec2i
import dev.ultreon.libs.commons.v0.vector.Vec4f as __Vec4f
__Vec4f = __Vec4f
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.world.BlockPos as __BlockPos
__BlockPos = __BlockPos
import java.util.BitSet as BitSet
import java.nio.ByteOrder as ByteOrder
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.Double as __double
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
import java.util.BitSet as __BitSet
__BitSet = __BitSet
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import java.lang.CharSequence as CharSequence
from builtins import float
import dev.ultreon.libs.commons.v0.vector.Vec3f as __Vec3f
__Vec3f = __Vec3f
from typing import List
import java.lang.Enum as Enum
import java.util.List as __List
__List = __List
import dev.ultreon.libs.commons.v0.tuple.Pair as __Pair
__Pair = __Pair
import java.lang.Float as __float
import dev.ultreon.quantum.world.ChunkPos as __ChunkPos
__ChunkPos = __ChunkPos
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

try:
    from pyquantum.network import partial
except ImportError:
    partial = __import_once__("pyquantum.network.partial")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.vector.Vec2d as __Vec2d
__Vec2d = __Vec2d
import dev.ultreon.quantum.network.PacketIO as __PacketIO
__PacketIO = __PacketIO
from builtins import int
import java.nio.channels.FileChannel as FileChannel
import java.lang.Character as __char
import java.nio.charset.Charset as Charset
import java.lang.Boolean as __boolean
import dev.ultreon.libs.commons.v0.vector.Vec2f as __Vec2f
__Vec2f = __Vec2f
from builtins import type
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = __import_once__("pycorelibs.commons.v0.tuple")

import dev.ultreon.libs.commons.v0.vector.Vec4i as __Vec4i
__Vec4i = __Vec4i
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.block.state.BlockProperties as __BlockProperties
__BlockProperties = __BlockProperties
import dev.ultreon.libs.commons.v0.vector.Vec4d as __Vec4d
__Vec4d = __Vec4d
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.vector.Vec3d as __Vec3d
__Vec3d = __Vec3d
import java.nio.channels.ScatteringByteChannel as ScatteringByteChannel
import java.nio.ByteOrder as __ByteOrder
__ByteOrder = __ByteOrder
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import dev.ultreon.libs.commons.v0.vector.Vec3i as __Vec3i
__Vec3i = __Vec3i
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.network.partial.PartialPacket as __PartialPacket
__PartialPacket = __PartialPacket
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.io.InputStream as InputStream
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.Map as Map
import java.util.List as List
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class PacketIO():
    """dev.ultreon.quantum.network.PacketIO"""
 
    @staticmethod
    def __wrap(java_value: __PacketIO) -> 'PacketIO':
        return PacketIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketIO):
        """
        Dynamic initializer for PacketIO.
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
 
    @overload
    def readUnsignedShort(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readUnsignedShort()"""
        return int.__wrap(super(PacketIO, self).readUnsignedShort())

    @overload
    def isWritable(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isWritable(int)"""
        return bool.__wrap(super(__PacketIO, self).isWritable(__int.valueOf(arg0)))

    @overload
    def readUbo(self, *arg0: 'types.DataType') -> 'types.DataType':
        """public final <T extends dev.ultreon.ubo.types.DataType<?>> T dev.ultreon.quantum.network.PacketIO.readUbo(T...)"""
        return 'types.DataType'.__wrap(super(__PacketIO, self).readUbo(arg0))

    @overload
    def readableBytes(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readableBytes()"""
        return int.__wrap(super(PacketIO, self).readableBytes())

    @overload
    def readDoubleArray(self) -> List[float]:
        """public double[] dev.ultreon.quantum.network.PacketIO.readDoubleArray()"""
        return List[float].__wrap(super(PacketIO, self).readDoubleArray())

    @overload
    def readId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.network.PacketIO.readId()"""
        return 'util.Identifier'.__wrap(super(PacketIO, self).readId())

    @overload
    def readIntArray(self) -> List[int]:
        """public int[] dev.ultreon.quantum.network.PacketIO.readIntArray()"""
        return List[int].__wrap(super(PacketIO, self).readIntArray())

    @overload
    def readChar(self) -> str:
        """public char dev.ultreon.quantum.network.PacketIO.readChar()"""
        return str.__wrap(super(PacketIO, self).readChar())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def readLong(self) -> int:
        """public long dev.ultreon.quantum.network.PacketIO.readLong()"""
        return int.__wrap(super(PacketIO, self).readLong())

    @overload
    def writeVec2i(self, arg0: 'Vec2i'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec2i(dev.ultreon.libs.commons.v0.vector.Vec2i)"""
        super(__PacketIO, self).writeVec2i(arg0)

    @overload
    def readBlockMeta(self) -> 'state.BlockProperties':
        """public dev.ultreon.quantum.block.state.BlockProperties dev.ultreon.quantum.network.PacketIO.readBlockMeta()"""
        return 'state.BlockProperties'.__wrap(super(PacketIO, self).readBlockMeta())

    @overload
    def isDirect(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isDirect()"""
        return bool.__wrap(super(PacketIO, self).isDirect())

    @overload
    def capacity(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.capacity()"""
        return int.__wrap(super(PacketIO, self).capacity())

    @overload
    def writeBytes(self, arg0: bytes) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBytes(byte[])"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeBytes(bytes))

    @overload
    def writeVarInt(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeVarInt(int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeVarInt(__int.valueOf(arg0)))

    @overload
    def readBoolean(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.readBoolean()"""
        return bool.__wrap(super(PacketIO, self).readBoolean())

    @overload
    def readBitSet(self) -> 'BitSet':
        """public java.util.BitSet dev.ultreon.quantum.network.PacketIO.readBitSet()"""
        return 'BitSet'.__wrap(super(PacketIO, self).readBitSet())

    @overload
    def writeFloatArray(self, arg0: 'float') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeFloatArray(float[])"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeFloatArray(arg0))

    @overload
    def readVec4d(self) -> 'vector.Vec4d':
        """public dev.ultreon.libs.commons.v0.vector.Vec4d dev.ultreon.quantum.network.PacketIO.readVec4d()"""
        return 'vector.Vec4d'.__wrap(super(PacketIO, self).readVec4d())

    @overload
    def writeVec2f(self, arg0: 'Vec2f'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec2f(dev.ultreon.libs.commons.v0.vector.Vec2f)"""
        super(__PacketIO, self).writeVec2f(arg0)

    @overload
    def flush(self):
        """public void dev.ultreon.quantum.network.PacketIO.flush()"""
        super(PacketIO, self).flush()

    @overload
    def order(self, arg0: 'ByteOrder') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.order(java.nio.ByteOrder)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).order(arg0))

    @overload
    def readVec2d(self) -> 'vector.Vec2d':
        """public dev.ultreon.libs.commons.v0.vector.Vec2d dev.ultreon.quantum.network.PacketIO.readVec2d()"""
        return 'vector.Vec2d'.__wrap(super(PacketIO, self).readVec2d())

    @overload
    def writeItemStack(self, arg0: 'ItemStack') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeItemStack(dev.ultreon.quantum.item.ItemStack)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeItemStack(arg0))

    @overload
    def writeBytes(self, arg0: 'ScatteringByteChannel', arg1: int):
        """public void dev.ultreon.quantum.network.PacketIO.writeBytes(java.nio.channels.ScatteringByteChannel,int)"""
        super(__PacketIO, self).writeBytes(arg0, __int.valueOf(arg1))

    @overload
    def readMediumArray(self, arg0: int) -> List[int]:
        """public int[] dev.ultreon.quantum.network.PacketIO.readMediumArray(int)"""
        return List[int].__wrap(super(__PacketIO, self).readMediumArray(__int.valueOf(arg0)))

    @overload
    def writeId(self, arg0: 'Identifier'):
        """public void dev.ultreon.quantum.network.PacketIO.writeId(dev.ultreon.quantum.util.Identifier)"""
        super(__PacketIO, self).writeId(arg0)

    @overload
    def writeByte(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeByte(int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeByte(__int.valueOf(arg0)))

    @overload
    def order(self) -> 'ByteOrder':
        """public java.nio.ByteOrder dev.ultreon.quantum.network.PacketIO.order()"""
        return 'ByteOrder'.__wrap(super(PacketIO, self).order())

    @overload
    def readVec2f(self) -> 'vector.Vec2f':
        """public dev.ultreon.libs.commons.v0.vector.Vec2f dev.ultreon.quantum.network.PacketIO.readVec2f()"""
        return 'vector.Vec2f'.__wrap(super(PacketIO, self).readVec2f())

    @overload
    def writeUuid(self, arg0: 'UUID'):
        """public void dev.ultreon.quantum.network.PacketIO.writeUuid(java.util.UUID)"""
        super(__PacketIO, self).writeUuid(arg0)

    @overload
    def readFloat(self) -> float:
        """public float dev.ultreon.quantum.network.PacketIO.readFloat()"""
        return float.__wrap(super(PacketIO, self).readFloat())

    @overload
    def writeMedium(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeMedium(int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeMedium(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def writeMediumArray(self, arg0: 'int') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeMediumArray(int[])"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeMediumArray(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def readVec3f(self) -> 'vector.Vec3f':
        """public dev.ultreon.libs.commons.v0.vector.Vec3f dev.ultreon.quantum.network.PacketIO.readVec3f()"""
        return 'vector.Vec3f'.__wrap(super(PacketIO, self).readVec3f())

    @overload
    def writePair(self, arg0: 'Pair', arg1: 'BiConsumer', arg2: 'BiConsumer') -> 'PacketIO':
        """public <F,S> dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writePair(dev.ultreon.libs.commons.v0.tuple.Pair<F, S>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, F>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, S>)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writePair(arg0, arg1, arg2))

    @overload
    def toString(self, arg0: 'Charset') -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketIO.toString(java.nio.charset.Charset)"""
        return str.__wrap(super(__PacketIO, self).toString(arg0))

    @overload
    def writeVec2f(self, arg0: 'Vec2d'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec2f(dev.ultreon.libs.commons.v0.vector.Vec2d)"""
        super(__PacketIO, self).writeVec2f(arg0)

    @overload
    def readVec2i(self) -> 'vector.Vec2i':
        """public dev.ultreon.libs.commons.v0.vector.Vec2i dev.ultreon.quantum.network.PacketIO.readVec2i()"""
        return 'vector.Vec2i'.__wrap(super(PacketIO, self).readVec2i())

    @overload
    def readUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.network.PacketIO.readUuid()"""
        return 'UUID'.__wrap(super(PacketIO, self).readUuid())

    @overload
    def readShort(self) -> int:
        """public short dev.ultreon.quantum.network.PacketIO.readShort()"""
        return int.__wrap(super(PacketIO, self).readShort())

    @overload
    def writeBytes(self, arg0: 'FileChannel', arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.writeBytes(java.nio.channels.FileChannel,long,int)"""
        return int.__wrap(super(__PacketIO, self).writeBytes(arg0, __long.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def readBlockPos(self) -> 'world.BlockPos':
        """public dev.ultreon.quantum.world.BlockPos dev.ultreon.quantum.network.PacketIO.readBlockPos()"""
        return 'world.BlockPos'.__wrap(super(PacketIO, self).readBlockPos())

    @overload
    def readBytes(self, arg0: 'FileChannel', arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readBytes(java.nio.channels.FileChannel,long,int)"""
        return int.__wrap(super(__PacketIO, self).readBytes(arg0, __long.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def isReadOnly(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isReadOnly()"""
        return bool.__wrap(super(PacketIO, self).isReadOnly())

    @overload
    def isReadable(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isReadable()"""
        return bool.__wrap(super(PacketIO, self).isReadable())

    @overload
    def readVec4i(self) -> 'vector.Vec4i':
        """public dev.ultreon.libs.commons.v0.vector.Vec4i dev.ultreon.quantum.network.PacketIO.readVec4i()"""
        return 'vector.Vec4i'.__wrap(super(PacketIO, self).readVec4i())

    @overload
    def readInt(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readInt()"""
        return int.__wrap(super(PacketIO, self).readInt())

    @overload
    def writeBlockPos(self, arg0: 'BlockPos') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBlockPos(dev.ultreon.quantum.world.BlockPos)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeBlockPos(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.equals(java.lang.Object)"""
        return bool.__wrap(super(__PacketIO, self).equals(arg0))

    @overload
    def writeVec4d(self, arg0: 'Vec4d'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec4d(dev.ultreon.libs.commons.v0.vector.Vec4d)"""
        super(__PacketIO, self).writeVec4d(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'InputStream', arg1: 'OutputStream'):
        """public dev.ultreon.quantum.network.PacketIO(java.io.InputStream,java.io.OutputStream)"""
        val = __PacketIO(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def writeUTF(self, arg0: str, arg1: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeUTF(java.lang.String,int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeUTF(arg0, __int.valueOf(arg1)))

    @overload
    def writeChar(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeChar(int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeChar(__int.valueOf(arg0)))

    @overload
    def readDoubleArray(self, arg0: int) -> List[float]:
        """public double[] dev.ultreon.quantum.network.PacketIO.readDoubleArray(int)"""
        return List[float].__wrap(super(__PacketIO, self).readDoubleArray(__int.valueOf(arg0)))

    @overload
    def memoryAddress(self) -> int:
        """public long dev.ultreon.quantum.network.PacketIO.memoryAddress()"""
        return int.__wrap(super(PacketIO, self).memoryAddress())

    @overload
    def writeChar(self, arg0: str) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeChar(char)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeChar(__char.valueOf(arg0)))

    @overload
    def hasMemoryAddress(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.hasMemoryAddress()"""
        return bool.__wrap(super(PacketIO, self).hasMemoryAddress())

    @overload
    def writeLongArray(self, arg0: 'long') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeLongArray(long[])"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeLongArray(arg0))

    @overload
    def unwrap(self) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.unwrap()"""
        return 'PacketIO'.__wrap(super(PacketIO, self).unwrap())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isReadable(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isReadable(int)"""
        return bool.__wrap(super(__PacketIO, self).isReadable(__int.valueOf(arg0)))

    @overload
    def writeBitSet(self, arg0: 'BitSet') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBitSet(java.util.BitSet)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeBitSet(arg0))

    @overload
    def asPacketBuffer(self) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.asPacketBuffer()"""
        return 'PacketIO'.__wrap(super(PacketIO, self).asPacketBuffer())

    @overload
    def readFloatArray(self, arg0: int) -> List[float]:
        """public float[] dev.ultreon.quantum.network.PacketIO.readFloatArray(int)"""
        return List[float].__wrap(super(__PacketIO, self).readFloatArray(__int.valueOf(arg0)))

    @overload
    def readMap(self, arg0: 'Function', arg1: 'Function') -> 'Map':
        """public <K,V> java.util.Map<K, V> dev.ultreon.quantum.network.PacketIO.readMap(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, K>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, V>)"""
        return 'Map'.__wrap(super(__PacketIO, self).readMap(arg0, arg1))

    @overload
    def writeList(self, arg0: 'List', arg1: 'BiConsumer') -> 'PacketIO':
        """public <T> dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeList(java.util.List<T>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, T>)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeList(arg0, arg1))

    @overload
    def readBytes(self, arg0: bytes) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.readBytes(byte[])"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).readBytes(bytes))

    @overload
    def split(self, arg0: int, arg1: int) -> List['partial.PartialPacket']:
        """public dev.ultreon.quantum.network.partial.PartialPacket[] dev.ultreon.quantum.network.PacketIO.split(int,long)"""
        return List['partial.PartialPacket'].__wrap(super(__PacketIO, self).split(__int.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def readLongArray(self) -> List[int]:
        """public long[] dev.ultreon.quantum.network.PacketIO.readLongArray()"""
        return List[int].__wrap(super(PacketIO, self).readLongArray())

    @overload
    def hasArray(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.hasArray()"""
        return bool.__wrap(super(PacketIO, self).hasArray())

    @overload
    def readMap(self, arg0: 'Function', arg1: 'Function', arg2: int) -> 'Map':
        """public <K,V> java.util.Map<K, V> dev.ultreon.quantum.network.PacketIO.readMap(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, K>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, V>,int)"""
        return 'Map'.__wrap(super(__PacketIO, self).readMap(arg0, arg1, __int.valueOf(arg2)))

    @overload
    def writeVec4i(self, arg0: 'Vec4i'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec4i(dev.ultreon.libs.commons.v0.vector.Vec4i)"""
        super(__PacketIO, self).writeVec4i(arg0)

    @overload
    def readLongArray(self, arg0: int) -> List[int]:
        """public long[] dev.ultreon.quantum.network.PacketIO.readLongArray(int)"""
        return List[int].__wrap(super(__PacketIO, self).readLongArray(__int.valueOf(arg0)))

    @overload
    def readItemStack(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.network.PacketIO.readItemStack()"""
        return 'item.ItemStack'.__wrap(super(PacketIO, self).readItemStack())

    @overload
    def readDouble(self) -> float:
        """public double dev.ultreon.quantum.network.PacketIO.readDouble()"""
        return float.__wrap(super(PacketIO, self).readDouble())

    @overload
    def writeVec4f(self, arg0: 'Vec4f'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec4f(dev.ultreon.libs.commons.v0.vector.Vec4f)"""
        super(__PacketIO, self).writeVec4f(arg0)

    @overload
    def writeBoolean(self, arg0: bool) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBoolean(boolean)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeBoolean(__boolean.valueOf(arg0)))

    @overload
    def readList(self, arg0: 'Function', arg1: int) -> 'List':
        """public <T> java.util.List<T> dev.ultreon.quantum.network.PacketIO.readList(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, T>,int)"""
        return 'List'.__wrap(super(__PacketIO, self).readList(arg0, __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'InputStream', arg1: 'OutputStream', arg2: 'List'):
        """public dev.ultreon.quantum.network.PacketIO(java.io.InputStream,java.io.OutputStream,java.util.List<dev.ultreon.quantum.network.partial.PartialPacket>) throws dev.ultreon.quantum.network.PacketIntegrityException"""
        val = __PacketIO(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.clear()"""
        return 'PacketIO'.__wrap(super(PacketIO, self).clear())

    @overload
    def writeBlockMeta(self, arg0: 'BlockProperties'):
        """public void dev.ultreon.quantum.network.PacketIO.writeBlockMeta(dev.ultreon.quantum.block.state.BlockProperties)"""
        super(__PacketIO, self).writeBlockMeta(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def readFloatArray(self) -> List[float]:
        """public float[] dev.ultreon.quantum.network.PacketIO.readFloatArray()"""
        return List[float].__wrap(super(PacketIO, self).readFloatArray())

    @overload
    def array(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.network.PacketIO.array()"""
        return List[int].__wrap(super(PacketIO, self).array())

    @overload
    def writeUbo(self, arg0: 'DataType'):
        """public void dev.ultreon.quantum.network.PacketIO.writeUbo(dev.ultreon.ubo.types.DataType<?>)"""
        super(__PacketIO, self).writeUbo(arg0)

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.readBytes(byte[],int,int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).readBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def readVec3d(self) -> 'vector.Vec3d':
        """public dev.ultreon.libs.commons.v0.vector.Vec3d dev.ultreon.quantum.network.PacketIO.readVec3d()"""
        return 'vector.Vec3d'.__wrap(super(PacketIO, self).readVec3d())

    @overload
    def readEnum(self, arg0: 'Enum') -> 'Enum':
        """public <T extends java.lang.Enum<T>> T dev.ultreon.quantum.network.PacketIO.readEnum(T)"""
        return 'Enum'.__wrap(super(__PacketIO, self).readEnum(arg0))

    @overload
    def readCharSequence(self, arg0: int, arg1: 'Charset') -> 'CharSequence':
        """public java.lang.CharSequence dev.ultreon.quantum.network.PacketIO.readCharSequence(int,java.nio.charset.Charset)"""
        return 'CharSequence'.__wrap(super(__PacketIO, self).readCharSequence(__int.valueOf(arg0), arg1))

    @overload
    def writeShortArray(self, arg0: 'short') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeShortArray(short[])"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeShortArray(arg0))

    @overload
    def readChunkPos(self) -> 'world.ChunkPos':
        """public dev.ultreon.quantum.world.ChunkPos dev.ultreon.quantum.network.PacketIO.readChunkPos()"""
        return 'world.ChunkPos'.__wrap(super(PacketIO, self).readChunkPos())

    @overload
    def readTextObject(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.network.PacketIO.readTextObject()"""
        return 'text.TextObject'.__wrap(super(PacketIO, self).readTextObject())

    @overload
    def writeInt(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeInt(int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeInt(__int.valueOf(arg0)))

    @overload
    def arrayOffset(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.arrayOffset()"""
        return int.__wrap(super(PacketIO, self).arrayOffset())

    @overload
    def maxCapacity(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.maxCapacity()"""
        return int.__wrap(super(PacketIO, self).maxCapacity())

    @overload
    def writeByteArray(self, arg0: bytes, arg1: int):
        """public void dev.ultreon.quantum.network.PacketIO.writeByteArray(byte[],int)"""
        super(__PacketIO, self).writeByteArray(bytes, __int.valueOf(arg1))

    @overload
    def readVec4f(self) -> 'vector.Vec4f':
        """public dev.ultreon.libs.commons.v0.vector.Vec4f dev.ultreon.quantum.network.PacketIO.readVec4f()"""
        return 'vector.Vec4f'.__wrap(super(PacketIO, self).readVec4f())

    @overload
    def writeTextObject(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.network.PacketIO.writeTextObject(dev.ultreon.quantum.text.TextObject)"""
        super(__PacketIO, self).writeTextObject(arg0)

    @overload
    def getVarIntSize(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.getVarIntSize(int)"""
        return int.__wrap(super(__PacketIO, self).getVarIntSize(__int.valueOf(arg0)))

    @overload
    def writeShort(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeShort(int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeShort(__int.valueOf(arg0)))

    @overload
    def writeBytes(self, arg0: 'InputStream', arg1: int):
        """public void dev.ultreon.quantum.network.PacketIO.writeBytes(java.io.InputStream,int)"""
        super(__PacketIO, self).writeBytes(arg0, __int.valueOf(arg1))

    @overload
    def readShortArray(self, arg0: int) -> List[int]:
        """public short[] dev.ultreon.quantum.network.PacketIO.readShortArray(int)"""
        return List[int].__wrap(super(__PacketIO, self).readShortArray(__int.valueOf(arg0)))

    @overload
    def readString(self, arg0: int) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketIO.readString(int)"""
        return str.__wrap(super(__PacketIO, self).readString(__int.valueOf(arg0)))

    @overload
    def validate(self, arg0: 'List') -> 'List':
        """public final java.util.List<io.netty.buffer.ByteBuf> dev.ultreon.quantum.network.PacketIO.validate(java.util.List<dev.ultreon.quantum.network.partial.PartialPacket>) throws dev.ultreon.quantum.network.PacketIntegrityException"""
        return 'List'.__wrap(super(__PacketIO, self).validate(arg0))

    @overload
    def __init__(self, arg0: 'Socket'):
        """public dev.ultreon.quantum.network.PacketIO(java.net.Socket) throws java.io.IOException"""
        val = __PacketIO(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def readBytes(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.readBytes(int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).readBytes(__int.valueOf(arg0)))

    @overload
    def writeFloat(self, arg0: float) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeFloat(float)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeFloat(__float.valueOf(arg0)))

    @overload
    def writeVec3f(self, arg0: 'Vec3f'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec3f(dev.ultreon.libs.commons.v0.vector.Vec3f)"""
        super(__PacketIO, self).writeVec3f(arg0)

    @overload
    def writeDoubleArray(self, arg0: 'double') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeDoubleArray(double[])"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeDoubleArray(arg0))

    @overload
    def readVec3i(self) -> 'vector.Vec3i':
        """public dev.ultreon.libs.commons.v0.vector.Vec3i dev.ultreon.quantum.network.PacketIO.readVec3i()"""
        return 'vector.Vec3i'.__wrap(super(PacketIO, self).readVec3i())

    @overload
    def readList(self, arg0: 'Function') -> 'List':
        """public <T> java.util.List<T> dev.ultreon.quantum.network.PacketIO.readList(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, T>)"""
        return 'List'.__wrap(super(__PacketIO, self).readList(arg0))

    @overload
    def writeVec3i(self, arg0: 'Vec3i'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec3i(dev.ultreon.libs.commons.v0.vector.Vec3i)"""
        super(__PacketIO, self).writeVec3i(arg0)

    @overload
    def readMediumArray(self) -> List[int]:
        """public int[] dev.ultreon.quantum.network.PacketIO.readMediumArray()"""
        return List[int].__wrap(super(PacketIO, self).readMediumArray())

    @overload
    def isWritable(self) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketIO.isWritable()"""
        return bool.__wrap(super(PacketIO, self).isWritable())

    @overload
    def readPair(self, arg0: 'Function', arg1: 'Function') -> 'tuple.Pair':
        """public <F,S> dev.ultreon.libs.commons.v0.tuple.Pair<F, S> dev.ultreon.quantum.network.PacketIO.readPair(java.util.function.Function<dev.ultreon.quantum.network.PacketIO, F>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, S>)"""
        return 'tuple.Pair'.__wrap(super(__PacketIO, self).readPair(arg0, arg1))

    @overload
    def capacity(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.capacity(int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).capacity(__int.valueOf(arg0)))

    @overload
    def readIntArray(self, arg0: int) -> List[int]:
        """public int[] dev.ultreon.quantum.network.PacketIO.readIntArray(int)"""
        return List[int].__wrap(super(__PacketIO, self).readIntArray(__int.valueOf(arg0)))

    @overload
    def readByteArray(self, arg0: int) -> List[int]:
        """public byte[] dev.ultreon.quantum.network.PacketIO.readByteArray(int)"""
        return List[int].__wrap(super(__PacketIO, self).readByteArray(__int.valueOf(arg0)))

    @overload
    def readUnsignedByte(self) -> int:
        """public short dev.ultreon.quantum.network.PacketIO.readUnsignedByte()"""
        return int.__wrap(super(PacketIO, self).readUnsignedByte())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketIO.toString()"""
        return str.__wrap(super(PacketIO, self).toString())

    @overload
    def writeVec3d(self, arg0: 'Vec3d'):
        """public void dev.ultreon.quantum.network.PacketIO.writeVec3d(dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        super(__PacketIO, self).writeVec3d(arg0)

    @overload
    def readVarInt(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readVarInt()"""
        return int.__wrap(super(PacketIO, self).readVarInt())

    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeBytes(byte[],int,int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def readMedium(self) -> int:
        """public int dev.ultreon.quantum.network.PacketIO.readMedium()"""
        return int.__wrap(super(PacketIO, self).readMedium())

    @overload
    def writeLong(self, arg0: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeLong(long)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeLong(__long.valueOf(arg0)))

    @overload
    def readShortArray(self) -> List[int]:
        """public short[] dev.ultreon.quantum.network.PacketIO.readShortArray()"""
        return List[int].__wrap(super(PacketIO, self).readShortArray())

    @overload
    def readBytes(self, arg0: 'OutputStream', arg1: int) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.readBytes(java.io.OutputStream,int)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).readBytes(arg0, __int.valueOf(arg1)))

    @overload
    def writeDouble(self, arg0: float) -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeDouble(double)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeDouble(__double.valueOf(arg0)))

    @overload
    def readByte(self) -> int:
        """public byte dev.ultreon.quantum.network.PacketIO.readByte()"""
        return int.__wrap(super(PacketIO, self).readByte())

    @overload
    def writeChunkPos(self, arg0: 'ChunkPos') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeChunkPos(dev.ultreon.quantum.world.ChunkPos)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeChunkPos(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def writeIntArray(self, arg0: 'int') -> 'PacketIO':
        """public dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeIntArray(int[])"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeIntArray(arg0))

    @overload
    def writeMap(self, arg0: 'Map', arg1: 'BiConsumer', arg2: 'BiConsumer') -> 'PacketIO':
        """public <K,V> dev.ultreon.quantum.network.PacketIO dev.ultreon.quantum.network.PacketIO.writeMap(java.util.Map<K, V>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, K>,java.util.function.BiConsumer<dev.ultreon.quantum.network.PacketIO, V>)"""
        return 'PacketIO'.__wrap(super(__PacketIO, self).writeMap(arg0, arg1, arg2)) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketHandler
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.network.PacketHandler as __PacketHandler
__PacketHandler = __PacketHandler
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

from abc import abstractmethod, ABC
from builtins import bool
 
class PacketHandler(ABC):
    """dev.ultreon.quantum.network.PacketHandler"""
 
    @staticmethod
    def __wrap(java_value: __PacketHandler) -> 'PacketHandler':
        return PacketHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketHandler):
        """
        Dynamic initializer for PacketHandler.
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
    def context(self, ):
        """public abstract dev.ultreon.quantum.network.PacketContext dev.ultreon.quantum.network.PacketHandler.context()"""
        pass

    @overload
    def isAsync(self) -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.isAsync()"""
        return bool.__wrap(super(PacketHandler, self).isAsync())

    @abstractmethod
    def destination(self, ):
        """public abstract dev.ultreon.quantum.network.api.PacketDestination dev.ultreon.quantum.network.PacketHandler.destination()"""
        pass

    @abstractmethod
    def onDisconnect(self, arg0: str):
        """public abstract void dev.ultreon.quantum.network.PacketHandler.onDisconnect(java.lang.String)"""
        pass

    @abstractmethod
    def isAcceptingPackets(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isAcceptingPackets()"""
        pass

    @abstractmethod
    def isDisconnected(self, ):
        """public abstract boolean dev.ultreon.quantum.network.PacketHandler.isDisconnected()"""
        pass

    @overload
    def shouldHandlePacket(self, arg0: 'Packet') -> bool:
        """public default boolean dev.ultreon.quantum.network.PacketHandler.shouldHandlePacket(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return bool.__wrap(super(__PacketHandler, self).shouldHandlePacket(arg0))

    @abstractmethod
    def reply(self, arg0: int):
        """public abstract dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.PacketHandler.reply(long)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.network.PacketException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.network.PacketException as __PacketException
__PacketException = __PacketException
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.network.PacketException"""
 
    @staticmethod
    def __wrap(java_value: __PacketException) -> 'PacketException':
        return PacketException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketException):
        """
        Dynamic initializer for PacketException.
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

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.PacketException()"""
        val = __PacketException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.network.PacketException(java.lang.String,java.lang.Throwable)"""
        val = __PacketException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.network.PacketException(java.lang.Throwable)"""
        val = __PacketException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.PacketException(java.lang.String)"""
        val = __PacketException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.PacketException()"""
        val = __PacketException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.network.MemoryNetworker
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.system.MemoryConnection as __MemoryConnection
__MemoryConnection = __MemoryConnection
import dev.ultreon.quantum.network.MemoryNetworker as __MemoryNetworker
__MemoryNetworker = __MemoryNetworker
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

import java.util.List as List
from builtins import int
 
class MemoryNetworker(__Networker, Networker):
    """dev.ultreon.quantum.network.MemoryNetworker"""
 
    @staticmethod
    def __wrap(java_value: __MemoryNetworker) -> 'MemoryNetworker':
        return MemoryNetworker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MemoryNetworker):
        """
        Dynamic initializer for MemoryNetworker.
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
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.network.MemoryNetworker.isRunning()"""
        return bool.__wrap(super(MemoryNetworker, self).isRunning())

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
    def getOtherSide(self) -> 'system.MemoryConnection':
        """public dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.MemoryNetworker.getOtherSide()"""
        return 'system.MemoryConnection'.__wrap(super(MemoryNetworker, self).getOtherSide())

    @overload
    def setOtherSide(self, arg0: 'MemoryConnection'):
        """public void dev.ultreon.quantum.network.MemoryNetworker.setOtherSide(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        super(__MemoryNetworker, self).setOtherSide(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def tick(self):
        """public void dev.ultreon.quantum.network.MemoryNetworker.tick()"""
        super(MemoryNetworker, self).tick()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.network.MemoryNetworker.close()"""
        super(MemoryNetworker, self).close()

    @override
    @overload
    def getConnections(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.network.system.ServerMemoryConnection> dev.ultreon.quantum.network.MemoryNetworker.getConnections()"""
        return 'List'.__wrap(super(MemoryNetworker, self).getConnections())

    @overload
    def __init__(self, arg0: 'QuantumServer', arg1: 'MemoryConnection'):
        """public dev.ultreon.quantum.network.MemoryNetworker(dev.ultreon.quantum.server.QuantumServer,dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        val = __MemoryNetworker(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.PacketData
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketData():
    """dev.ultreon.quantum.network.PacketData"""
 
    @staticmethod
    def __wrap(java_value: __PacketData) -> 'PacketData':
        return PacketData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketData):
        """
        Dynamic initializer for PacketData.
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
    def decode(self, arg0: int, arg1: 'PacketIO') -> 'packets.Packet':
        """public dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.PacketData.decode(int,dev.ultreon.quantum.network.PacketIO)"""
        return 'packets.Packet'.__wrap(super(__PacketData, self).decode(__int.valueOf(arg0), arg1))

    @overload
    def handle(self, arg0: 'Packet', arg1: 'PacketContext', arg2: 'PacketHandler'):
        """public void dev.ultreon.quantum.network.PacketData.handle(dev.ultreon.quantum.network.packets.Packet<T>,dev.ultreon.quantum.network.PacketContext,T)"""
        super(__PacketData, self).handle(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getId(self, arg0: 'Packet') -> int:
        """public int dev.ultreon.quantum.network.PacketData.getId(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return int.__wrap(super(__PacketData, self).getId(arg0))

    @overload
    def __init__(self, arg0: 'PacketCollection'):
        """public dev.ultreon.quantum.network.PacketData(dev.ultreon.quantum.network.PacketCollection<T>)"""
        val = __PacketData(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def encode(self, arg0: 'Packet', arg1: 'PacketIO'):
        """public void dev.ultreon.quantum.network.PacketData.encode(dev.ultreon.quantum.network.packets.Packet<?>,dev.ultreon.quantum.network.PacketIO)"""
        super(__PacketData, self).encode(arg0, arg1)

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketOverflowException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import dev.ultreon.quantum.network.PacketOverflowException as __PacketOverflowException
__PacketOverflowException = __PacketOverflowException
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketOverflowException(__PacketException, PacketException):
    """dev.ultreon.quantum.network.PacketOverflowException"""
 
    @staticmethod
    def __wrap(java_value: __PacketOverflowException) -> 'PacketOverflowException':
        return PacketOverflowException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketOverflowException):
        """
        Dynamic initializer for PacketOverflowException.
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

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public dev.ultreon.quantum.network.PacketOverflowException(java.lang.String,int,int)"""
        val = __PacketOverflowException(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.network.ReplyPacket
import dev.ultreon.quantum.network.ReplyPacket as __ReplyPacket
__ReplyPacket = __ReplyPacket
 
class ReplyPacket(ABC):
    """dev.ultreon.quantum.network.ReplyPacket"""
 
    @staticmethod
    def __wrap(java_value: __ReplyPacket) -> 'ReplyPacket':
        return ReplyPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReplyPacket):
        """
        Dynamic initializer for ReplyPacket.
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
 
 
# CLASS: dev.ultreon.quantum.network.NetworkChannel
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network.api import packet
except ImportError:
    packet = __import_once__("pyquantum.network.api.packet")

import java.lang.Runnable as Runnable
import java.util.function.Function as __Function
__Function = __Function
import dev.ultreon.quantum.network.NetworkChannel as __NetworkChannel
__NetworkChannel = __NetworkChannel
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
import java.lang.Integer as __int
import java.util.function.BiConsumer as __BiConsumer
__BiConsumer = __BiConsumer
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
import java.util.List as List
 
class NetworkChannel():
    """dev.ultreon.quantum.network.NetworkChannel"""
 
    @staticmethod
    def __wrap(java_value: __NetworkChannel) -> 'NetworkChannel':
        return NetworkChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NetworkChannel):
        """
        Dynamic initializer for NetworkChannel.
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
 
    @overload
    def id(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.network.NetworkChannel.id()"""
        return 'util.Identifier'.__wrap(super(NetworkChannel, self).id())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getChannel(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.NetworkChannel.getChannel(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel.__wrap(__NetworkChannel.getChannel(arg0))

    @overload
    def sendToPlayers(self, arg0: 'List', arg1: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.NetworkChannel.sendToPlayers(java.util.List<dev.ultreon.quantum.server.player.ServerPlayer>,dev.ultreon.quantum.network.api.packet.ModPacket<T>)"""
        super(__NetworkChannel, self).sendToPlayers(arg0, arg1)

    @overload
    def sendToServer(self, arg0: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.NetworkChannel.sendToServer(dev.ultreon.quantum.network.api.packet.ModPacket<T>)"""
        super(__NetworkChannel, self).sendToServer(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setC2sConnection(self, arg0: 'IConnection'):
        """public void dev.ultreon.quantum.network.NetworkChannel.setC2sConnection(dev.ultreon.quantum.network.system.IConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        super(__NetworkChannel, self).setC2sConnection(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.NetworkChannel.queue(java.lang.Runnable)"""
        super(__NetworkChannel, self).queue(arg0)

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

    @overload
    def getEncoder(self, arg0: 'Class') -> 'BiConsumer':
        """public java.util.function.BiConsumer<? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>, dev.ultreon.quantum.network.PacketIO> dev.ultreon.quantum.network.NetworkChannel.getEncoder(java.lang.Class<? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>>)"""
        return 'BiConsumer'.__wrap(super(__NetworkChannel, self).getEncoder(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getId(self, arg0: 'ModPacket') -> int:
        """public int dev.ultreon.quantum.network.NetworkChannel.getId(dev.ultreon.quantum.network.api.packet.ModPacket<?>)"""
        return int.__wrap(super(__NetworkChannel, self).getId(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getConsumer(self, arg0: 'Class') -> 'BiConsumer':
        """public java.util.function.BiConsumer<? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>, java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>> dev.ultreon.quantum.network.NetworkChannel.getConsumer(java.lang.Class<? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>>)"""
        return 'BiConsumer'.__wrap(super(__NetworkChannel, self).getConsumer(arg0))

    @staticmethod
    @overload
    def create(arg0: 'Identifier') -> 'NetworkChannel':
        """public static dev.ultreon.quantum.network.NetworkChannel dev.ultreon.quantum.network.NetworkChannel.create(dev.ultreon.quantum.util.Identifier)"""
        return NetworkChannel.__wrap(__NetworkChannel.create(arg0))

    @overload
    def getDecoder(self, arg0: int) -> 'Function':
        """public java.util.function.Function<dev.ultreon.quantum.network.PacketIO, ? extends dev.ultreon.quantum.network.api.packet.ModPacket<?>> dev.ultreon.quantum.network.NetworkChannel.getDecoder(int)"""
        return 'Function'.__wrap(super(__NetworkChannel, self).getDecoder(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def register(self, arg0: 'Class', arg1: 'BiConsumer', arg2: 'Function', arg3: 'BiConsumer'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T>> void dev.ultreon.quantum.network.NetworkChannel.register(java.lang.Class<T>,java.util.function.BiConsumer<T, dev.ultreon.quantum.network.PacketIO>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, T>,java.util.function.BiConsumer<T, java.util.function.Supplier<dev.ultreon.quantum.network.api.packet.ModPacketContext>>)"""
        super(__NetworkChannel, self).register(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def sendToPlayer(self, arg0: 'ServerPlayer', arg1: 'ModPacket'):
        """public <T extends dev.ultreon.quantum.network.api.packet.ModPacket<T> & dev.ultreon.quantum.network.api.packet.ClientEndpoint> void dev.ultreon.quantum.network.NetworkChannel.sendToPlayer(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.network.api.packet.ModPacket<T>)"""
        super(__NetworkChannel, self).sendToPlayer(arg0, arg1) 
 
 
# CLASS: dev.ultreon.quantum.network.ServerHostingException
import dev.ultreon.quantum.network.ServerHostingException as __ServerHostingException
__ServerHostingException = __ServerHostingException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ServerHostingException(__ServerStatusException, ServerStatusException):
    """dev.ultreon.quantum.network.ServerHostingException"""
 
    @staticmethod
    def __wrap(java_value: __ServerHostingException) -> 'ServerHostingException':
        return ServerHostingException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerHostingException):
        """
        Dynamic initializer for ServerHostingException.
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

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.ServerHostingException()"""
        val = __ServerHostingException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.network.ServerHostingException(java.lang.String,java.lang.Throwable)"""
        val = __ServerHostingException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.ServerHostingException()"""
        val = __ServerHostingException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.ServerHostingException(java.lang.String)"""
        val = __ServerHostingException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.network.ServerHostingException(java.lang.Throwable)"""
        val = __ServerHostingException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.network.PacketListener
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import dev.ultreon.quantum.network.PacketListener as __PacketListener
__PacketListener = __PacketListener
 
class PacketListener(ABC):
    """dev.ultreon.quantum.network.PacketListener"""
 
    @staticmethod
    def __wrap(java_value: __PacketListener) -> 'PacketListener':
        return PacketListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketListener):
        """
        Dynamic initializer for PacketListener.
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
 
    @staticmethod
    @overload
    def onFailure(arg0: 'Supplier') -> 'PacketListener':
        """public static dev.ultreon.quantum.network.PacketListener dev.ultreon.quantum.network.PacketListener.onFailure(java.util.function.Supplier<dev.ultreon.quantum.network.packets.Packet<?>>)"""
        return PacketListener.__wrap(__PacketListener.onFailure(arg0))

    @overload
    def onSuccess(self):
        """public default void dev.ultreon.quantum.network.PacketListener.onSuccess()"""
        super(PacketListener, self).onSuccess()

    @overload
    def onFailure(self) -> 'packets.Packet':
        """public default dev.ultreon.quantum.network.packets.Packet<?> dev.ultreon.quantum.network.PacketListener.onFailure()"""
        return 'packets.Packet'.__wrap(super(PacketListener, self).onFailure())

    @staticmethod
    @overload
    def onEither(arg0: 'Runnable') -> 'PacketListener':
        """public static dev.ultreon.quantum.network.PacketListener dev.ultreon.quantum.network.PacketListener.onEither(java.lang.Runnable)"""
        return PacketListener.__wrap(__PacketListener.onEither(arg0))

    @staticmethod
    @overload
    def onSuccess(arg0: 'Runnable') -> 'PacketListener':
        """public static dev.ultreon.quantum.network.PacketListener dev.ultreon.quantum.network.PacketListener.onSuccess(java.lang.Runnable)"""
        return PacketListener.__wrap(__PacketListener.onSuccess(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketIntegrityException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import dev.ultreon.quantum.network.PacketIntegrityException as __PacketIntegrityException
__PacketIntegrityException = __PacketIntegrityException
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketIntegrityException(__IOException, IOException):
    """dev.ultreon.quantum.network.PacketIntegrityException"""
 
    @staticmethod
    def __wrap(java_value: __PacketIntegrityException) -> 'PacketIntegrityException':
        return PacketIntegrityException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketIntegrityException):
        """
        Dynamic initializer for PacketIntegrityException.
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

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.PacketIntegrityException()"""
        val = __PacketIntegrityException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.PacketIntegrityException()"""
        val = __PacketIntegrityException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.PacketIntegrityException(java.lang.String)"""
        val = __PacketIntegrityException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.network.PacketIntegrityException(java.lang.Throwable)"""
        val = __PacketIntegrityException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.network.PacketIntegrityException(java.lang.String,java.lang.Throwable)"""
        val = __PacketIntegrityException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.network.MemoryConnectionContext
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.network.MemoryConnectionContext as __MemoryConnectionContext
__MemoryConnectionContext = __MemoryConnectionContext
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.system.MemoryConnection as __MemoryConnection
__MemoryConnection = __MemoryConnection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class MemoryConnectionContext():
    """dev.ultreon.quantum.network.MemoryConnectionContext"""
 
    @staticmethod
    def __wrap(java_value: __MemoryConnectionContext) -> 'MemoryConnectionContext':
        return MemoryConnectionContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MemoryConnectionContext):
        """
        Dynamic initializer for MemoryConnectionContext.
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
    def __init__(self):
        """public dev.ultreon.quantum.network.MemoryConnectionContext()"""
        val = __MemoryConnectionContext()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.MemoryConnectionContext()"""
        val = __MemoryConnectionContext()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def set(arg0: 'MemoryConnection'):
        """public static void dev.ultreon.quantum.network.MemoryConnectionContext.set(dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler>)"""
        __MemoryConnectionContext.set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get() -> 'system.MemoryConnection':
        """public static dev.ultreon.quantum.network.system.MemoryConnection<dev.ultreon.quantum.network.client.ClientPacketHandler, dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.MemoryConnectionContext.get()"""
        return system.MemoryConnection.__wrap(__MemoryConnectionContext.get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.S2CReplyPacket
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.network.S2CReplyPacket as __S2CReplyPacket
__S2CReplyPacket = __S2CReplyPacket
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.network import client
except ImportError:
    client = __import_once__("pyquantum.network.client")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class S2CReplyPacket(network.__Packet, packets.Packet, __ReplyPacket, ReplyPacket):
    """dev.ultreon.quantum.network.S2CReplyPacket"""
 
    @staticmethod
    def __wrap(java_value: __S2CReplyPacket) -> 'S2CReplyPacket':
        return S2CReplyPacket(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __S2CReplyPacket):
        """
        Dynamic initializer for S2CReplyPacket.
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
    def __init__(self, arg0: int):
        """public <T extends dev.ultreon.quantum.network.PacketHandler> dev.ultreon.quantum.network.S2CReplyPacket(long)"""
        val = __S2CReplyPacket(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PacketIO'):
        """public dev.ultreon.quantum.network.S2CReplyPacket(dev.ultreon.quantum.network.PacketIO)"""
        val = __S2CReplyPacket(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def handle(self, arg0: 'PacketContext', arg1: 'ClientPacketHandler'):
        """public void dev.ultreon.quantum.network.S2CReplyPacket.handle(dev.ultreon.quantum.network.PacketContext,dev.ultreon.quantum.network.client.ClientPacketHandler)"""
        super(__S2CReplyPacket, self).handle(arg0, arg1)

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

    @override
    @overload
    def toBytes(self, arg0: 'PacketIO'):
        """public void dev.ultreon.quantum.network.S2CReplyPacket.toBytes(dev.ultreon.quantum.network.PacketIO)"""
        super(__S2CReplyPacket, self).toBytes(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketSequence
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.network.PacketSequence as __PacketSequence
__PacketSequence = __PacketSequence
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketSequence():
    """dev.ultreon.quantum.network.PacketSequence"""
 
    @staticmethod
    def __wrap(java_value: __PacketSequence) -> 'PacketSequence':
        return PacketSequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketSequence):
        """
        Dynamic initializer for PacketSequence.
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

    @overload
    def sequence(self) -> int:
        """public long dev.ultreon.quantum.network.PacketSequence.sequence()"""
        return int.__wrap(super(PacketSequence, self).sequence())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketSequence.equals(java.lang.Object)"""
        return bool.__wrap(super(__PacketSequence, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.PacketSequence.hashCode()"""
        return int.__wrap(super(PacketSequence, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: 'Packet'):
        """public dev.ultreon.quantum.network.PacketSequence(long,dev.ultreon.quantum.network.packets.Packet<T>)"""
        val = __PacketSequence(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketSequence.toString()"""
        return str.__wrap(super(PacketSequence, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def packet(self) -> 'packets.Packet':
        """public dev.ultreon.quantum.network.packets.Packet<T> dev.ultreon.quantum.network.PacketSequence.packet()"""
        return 'packets.Packet'.__wrap(super(PacketSequence, self).packet()) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketCollection
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.network.PacketCollection as __PacketCollection
__PacketCollection = __PacketCollection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = __import_once__("pycorelibs.commons.v0.tuple")

import dev.ultreon.quantum.network.packets.Packet as __Packet
__Packet = __Packet
try:
    from pyquantum.network import packets
except ImportError:
    packets = __import_once__("pyquantum.network.packets")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
from builtins import int
 
class PacketCollection():
    """dev.ultreon.quantum.network.PacketCollection"""
 
    @staticmethod
    def __wrap(java_value: __PacketCollection) -> 'PacketCollection':
        return PacketCollection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketCollection):
        """
        Dynamic initializer for PacketCollection.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def handle(self, arg0: 'Packet', arg1: 'Pair'):
        """public void dev.ultreon.quantum.network.PacketCollection.handle(dev.ultreon.quantum.network.packets.Packet<H>,dev.ultreon.libs.commons.v0.tuple.Pair<dev.ultreon.quantum.network.PacketContext, H>)"""
        super(__PacketCollection, self).handle(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.PacketCollection()"""
        val = __PacketCollection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.PacketCollection()"""
        val = __PacketCollection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def decode(self, arg0: int, arg1: 'PacketIO') -> 'packets.Packet':
        """public dev.ultreon.quantum.network.packets.Packet<H> dev.ultreon.quantum.network.PacketCollection.decode(int,dev.ultreon.quantum.network.PacketIO)"""
        return 'packets.Packet'.__wrap(super(__PacketCollection, self).decode(__int.valueOf(arg0), arg1))

    @overload
    def getId(self, arg0: 'Packet') -> int:
        """public int dev.ultreon.quantum.network.PacketCollection.getId(dev.ultreon.quantum.network.packets.Packet<?>)"""
        return int.__wrap(super(__PacketCollection, self).getId(arg0))

    @overload
    def encode(self, arg0: 'Packet', arg1: 'PacketIO'):
        """public void dev.ultreon.quantum.network.PacketCollection.encode(dev.ultreon.quantum.network.packets.Packet<?>,dev.ultreon.quantum.network.PacketIO)"""
        super(__PacketCollection, self).encode(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'Class', arg1: 'BiConsumer', arg2: 'Function', arg3: 'BiConsumer') -> int:
        """public int dev.ultreon.quantum.network.PacketCollection.add(java.lang.Class<? extends dev.ultreon.quantum.network.packets.Packet<?>>,java.util.function.BiConsumer<dev.ultreon.quantum.network.packets.Packet<?>, dev.ultreon.quantum.network.PacketIO>,java.util.function.Function<dev.ultreon.quantum.network.PacketIO, dev.ultreon.quantum.network.packets.Packet<H>>,java.util.function.BiConsumer<dev.ultreon.quantum.network.packets.Packet<H>, dev.ultreon.libs.commons.v0.tuple.Pair<dev.ultreon.quantum.network.PacketContext, H>>)"""
        return int.__wrap(super(__PacketCollection, self).add(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.WriteOnlyBufferException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.network.WriteOnlyBufferException as __WriteOnlyBufferException
__WriteOnlyBufferException = __WriteOnlyBufferException
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WriteOnlyBufferException(__UnsupportedOperationException, UnsupportedOperationException):
    """dev.ultreon.quantum.network.WriteOnlyBufferException"""
 
    @staticmethod
    def __wrap(java_value: __WriteOnlyBufferException) -> 'WriteOnlyBufferException':
        return WriteOnlyBufferException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WriteOnlyBufferException):
        """
        Dynamic initializer for WriteOnlyBufferException.
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
    def __init__(self):
        """public dev.ultreon.quantum.network.WriteOnlyBufferException()"""
        val = __WriteOnlyBufferException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.WriteOnlyBufferException()"""
        val = __WriteOnlyBufferException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.network.ServerStatusException
import dev.ultreon.quantum.network.ServerStatusException as __ServerStatusException
__ServerStatusException = __ServerStatusException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ServerStatusException(__IOException, IOException):
    """dev.ultreon.quantum.network.ServerStatusException"""
 
    @staticmethod
    def __wrap(java_value: __ServerStatusException) -> 'ServerStatusException':
        return ServerStatusException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerStatusException):
        """
        Dynamic initializer for ServerStatusException.
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

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.ServerStatusException()"""
        val = __ServerStatusException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.ServerStatusException()"""
        val = __ServerStatusException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.network.ServerStatusException(java.lang.String,java.lang.Throwable)"""
        val = __ServerStatusException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.network.ServerStatusException(java.lang.Throwable)"""
        val = __ServerStatusException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.network.ServerStatusException(java.lang.String)"""
        val = __ServerStatusException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.network.PacketContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.util.Env as __Env
__Env = __Env
import dev.ultreon.quantum.network.system.IConnection as __IConnection
__IConnection = __IConnection
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.PacketContext as __PacketContext
__PacketContext = __PacketContext
import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
 
class PacketContext():
    """dev.ultreon.quantum.network.PacketContext"""
 
    @staticmethod
    def __wrap(java_value: __PacketContext) -> 'PacketContext':
        return PacketContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketContext):
        """
        Dynamic initializer for PacketContext.
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.network.PacketContext.toString()"""
        return str.__wrap(super(PacketContext, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ServerPlayer', arg1: 'IConnection', arg2: 'Env'):
        """public dev.ultreon.quantum.network.PacketContext(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.network.system.IConnection<?, ?>,dev.ultreon.quantum.util.Env)"""
        val = __PacketContext(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def requirePlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.PacketContext.requirePlayer()"""
        return 'player.ServerPlayer'.__wrap(super(PacketContext, self).requirePlayer())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.network.PacketContext.equals(java.lang.Object)"""
        return bool.__wrap(super(__PacketContext, self).equals(arg0))

    @overload
    def getPlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.network.PacketContext.getPlayer()"""
        return 'player.ServerPlayer'.__wrap(super(PacketContext, self).getPlayer())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.network.PacketContext.hashCode()"""
        return int.__wrap(super(PacketContext, self).hashCode())

    @overload
    def getConnection(self) -> 'system.IConnection':
        """public dev.ultreon.quantum.network.system.IConnection<?, ?> dev.ultreon.quantum.network.PacketContext.getConnection()"""
        return 'system.IConnection'.__wrap(super(PacketContext, self).getConnection())

    @overload
    def getDestination(self) -> 'util.Env':
        """public dev.ultreon.quantum.util.Env dev.ultreon.quantum.network.PacketContext.getDestination()"""
        return 'util.Env'.__wrap(super(PacketContext, self).getDestination())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def queue(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.network.PacketContext.queue(java.lang.Runnable)"""
        super(__PacketContext, self).queue(arg0)