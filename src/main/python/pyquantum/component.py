from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
from pyquantum_helper import override
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.Object as __object
from builtins import type
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GameComponent(ABC):
    """dev.ultreon.quantum.component.GameComponent"""
 
    @staticmethod
    def __wrap(java_value: __GameComponent) -> 'GameComponent':
        return GameComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameComponent):
        """
        Dynamic initializer for GameComponent.
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

    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(GameComponent, self).getHolder())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

 
 
 
# CLASS: dev.ultreon.quantum.component.GameComponent
from builtins import str
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
from pyquantum_helper import override
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.Object as __object
from builtins import type
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GameComponent(ABC):
    """dev.ultreon.quantum.component.GameComponent"""
 
    @staticmethod
    def __wrap(java_value: __GameComponent) -> 'GameComponent':
        return GameComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameComponent):
        """
        Dynamic initializer for GameComponent.
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

    @overload
    def getHolder(self) -> 'type.Class':
        """public java.lang.Class<? extends T> dev.ultreon.quantum.component.GameComponent.getHolder()"""
        return 'type.Class'.__wrap(super(GameComponent, self).getHolder())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

 
 
 
# CLASS: dev.ultreon.quantum.component.GameComponent 
 
 
# CLASS: dev.ultreon.quantum.component.GameComponentHolder
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Collection as __Collection
__Collection = __Collection
import java.util.Collection as Collection
from abc import abstractmethod, ABC
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
 
class GameComponentHolder(ABC):
    """dev.ultreon.quantum.component.GameComponentHolder"""
 
    @staticmethod
    def __wrap(java_value: __GameComponentHolder) -> 'GameComponentHolder':
        return GameComponentHolder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameComponentHolder):
        """
        Dynamic initializer for GameComponentHolder.
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
    def componentRegistry(self, ):
        """public abstract java.util.Map<dev.ultreon.quantum.util.Identifier, T> dev.ultreon.quantum.component.GameComponentHolder.componentRegistry()"""
        pass

    @abstractmethod
    def getComponent(self, arg0: 'Identifier', arg1: 'GameComponent'):
        """public abstract <T2 extends dev.ultreon.quantum.component.GameComponent<?>> T2 dev.ultreon.quantum.component.GameComponentHolder.getComponent(dev.ultreon.quantum.util.Identifier,T2[])"""
        pass

    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(GameComponentHolder, self).components())