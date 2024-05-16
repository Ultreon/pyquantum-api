from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.client.gui.screens.container.ContainerScreen as __ContainerScreen
__ContainerScreen = __ContainerScreen
import java.util.Collection as Collection
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class ContainerScreen(ABC, client.__Screen, gui.Screen):
    """dev.ultreon.quantum.client.gui.screens.container.ContainerScreen"""
 
    @staticmethod
    def __wrap(java_value: __ContainerScreen) -> 'ContainerScreen':
        return ContainerScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContainerScreen):
        """
        Dynamic initializer for ContainerScreen.
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
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__gui.Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__ContainerScreen, self).onClose(arg0))

    @overload
    def onItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerScreen, self).onItemChanged(__int.valueOf(arg0), arg1)

    @overload
    def top(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.top()"""
        return int.__wrap(super(ContainerScreen, self).top())

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setup(self, arg0: 'List'):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.setup(java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        super(__ContainerScreen, self).setup(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ContainerScreen, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getMaxSlots(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.getMaxSlots()"""
        return int.__wrap(super(ContainerScreen, self).getMaxSlots())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool.__wrap(super(gui.Screen, self).canClose())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'.__wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onClosed()"""
        super(ContainerScreen, self).onClosed()

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__gui.Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).titleTranslation(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(gui.Screen, self).path())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__ContainerScreen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def emitUpdate(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.emitUpdate()"""
        super(ContainerScreen, self).emitUpdate()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public final void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(__ContainerScreen, self).build(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @overload
    def renderForeground(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.renderForeground(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ContainerScreen, self).renderForeground(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @abstractmethod
    def backgroundWidth(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.backgroundWidth()"""
        pass

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(__Screen).parentScreen(value)

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__gui.Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__gui.Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__gui.Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def left(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.left()"""
        return int.__wrap(super(ContainerScreen, self).left())

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__gui.Screen, self).add(arg0))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @abstractmethod
    def backgroundHeight(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.backgroundHeight()"""
        pass

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(gui.Screen, self).back())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool.__wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(gui.Screen, self).getName())

    @abstractmethod
    def getBackground(self, ):
        """public abstract dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.getBackground()"""
        pass

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @overload
    def get(self, arg0: int) -> 'menu.ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.get(int)"""
        return 'menu.ItemSlot'.__wrap(super(__ContainerScreen, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(gui.Screen, self).getRawTitle())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.container.ContainerScreen
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.client.gui.screens.container.ContainerScreen as __ContainerScreen
__ContainerScreen = __ContainerScreen
import java.util.Collection as Collection
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import java.lang.Double as __double
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.nio.file.Path as Path
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
from builtins import int
 
class ContainerScreen(ABC, client.__Screen, gui.Screen):
    """dev.ultreon.quantum.client.gui.screens.container.ContainerScreen"""
 
    @staticmethod
    def __wrap(java_value: __ContainerScreen) -> 'ContainerScreen':
        return ContainerScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContainerScreen):
        """
        Dynamic initializer for ContainerScreen.
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
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__gui.Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__ContainerScreen, self).onClose(arg0))

    @overload
    def onItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerScreen, self).onItemChanged(__int.valueOf(arg0), arg1)

    @overload
    def top(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.top()"""
        return int.__wrap(super(ContainerScreen, self).top())

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setup(self, arg0: 'List'):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.setup(java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        super(__ContainerScreen, self).setup(arg0)

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ContainerScreen, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getMaxSlots(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.getMaxSlots()"""
        return int.__wrap(super(ContainerScreen, self).getMaxSlots())

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool.__wrap(super(gui.Screen, self).canClose())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'.__wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onClosed()"""
        super(ContainerScreen, self).onClosed()

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__gui.Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).titleTranslation(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(gui.Screen, self).path())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__ContainerScreen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @overload
    def emitUpdate(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.emitUpdate()"""
        super(ContainerScreen, self).emitUpdate()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public final void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(__ContainerScreen, self).build(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @overload
    def renderForeground(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.renderForeground(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ContainerScreen, self).renderForeground(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @abstractmethod
    def backgroundWidth(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.backgroundWidth()"""
        pass

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(__Screen).parentScreen(value)

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__gui.Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__gui.Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__gui.Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def left(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.left()"""
        return int.__wrap(super(ContainerScreen, self).left())

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__gui.Screen, self).add(arg0))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @abstractmethod
    def backgroundHeight(self, ):
        """public abstract int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.backgroundHeight()"""
        pass

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(gui.Screen, self).back())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool.__wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(gui.Screen, self).getName())

    @abstractmethod
    def getBackground(self, ):
        """public abstract dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.getBackground()"""
        pass

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @overload
    def get(self, arg0: int) -> 'menu.ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.get(int)"""
        return 'menu.ItemSlot'.__wrap(super(__ContainerScreen, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(gui.Screen, self).getRawTitle())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0)

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.container.ContainerScreen 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.container.InventoryScreen
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.nio.file.Path as __Path
__Path = __Path
import dev.ultreon.quantum.client.gui.screens.container.ContainerScreen as __ContainerScreen
__ContainerScreen = __ContainerScreen
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Double as __double
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
import java.util.List as __List
__List = __List
import java.lang.Float as __float
import dev.ultreon.quantum.client.gui.screens.container.InventoryScreen as __InventoryScreen
__InventoryScreen = __InventoryScreen
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
from builtins import int
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.menu.Inventory as __Inventory
__Inventory = __Inventory
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.nio.file.Path as Path
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
 
class InventoryScreen(__ContainerScreen, ContainerScreen):
    """dev.ultreon.quantum.client.gui.screens.container.InventoryScreen"""
 
    @staticmethod
    def __wrap(java_value: __InventoryScreen) -> 'InventoryScreen':
        return InventoryScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InventoryScreen):
        """
        Dynamic initializer for InventoryScreen.
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
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__gui.Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__ContainerScreen, self).onClose(arg0))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ContainerScreen, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def getMaxSlots(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.getMaxSlots()"""
        return int.__wrap(super(ContainerScreen, self).getMaxSlots())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @overload
    def __init__(self, arg0: 'Inventory', arg1: 'TextObject'):
        """public dev.ultreon.quantum.client.gui.screens.container.InventoryScreen(dev.ultreon.quantum.menu.Inventory,dev.ultreon.quantum.text.TextObject)"""
        val = __InventoryScreen(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def backgroundWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.backgroundWidth()"""
        return int.__wrap(super(InventoryScreen, self).backgroundWidth())

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def onItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerScreen, self).onItemChanged(__int.valueOf(arg0), arg1)

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool.__wrap(super(gui.Screen, self).canClose())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'.__wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onClosed()"""
        super(ContainerScreen, self).onClosed()

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__gui.Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__InventoryScreen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).titleTranslation(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(gui.Screen, self).path())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getInventory(self) -> 'menu.Inventory':
        """public dev.ultreon.quantum.menu.Inventory dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.getInventory()"""
        return 'menu.Inventory'.__wrap(super(InventoryScreen, self).getInventory())

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public final void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(__ContainerScreen, self).build(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(__Screen).parentScreen(value)

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def top(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.top()"""
        return int.__wrap(super(ContainerScreen, self).top())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__gui.Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def backgroundHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.backgroundHeight()"""
        return int.__wrap(super(InventoryScreen, self).backgroundHeight())

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__gui.Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @overload
    def previousPage(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.previousPage()"""
        super(InventoryScreen, self).previousPage()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__gui.Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__gui.Screen, self).add(arg0))

    @override
    @overload
    def setup(self, arg0: 'List'):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.setup(java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        super(__ContainerScreen, self).setup(arg0)

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @override
    @overload
    def emitUpdate(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.emitUpdate()"""
        super(InventoryScreen, self).emitUpdate()

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @overload
    def nextPage(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.nextPage()"""
        super(InventoryScreen, self).nextPage()

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(gui.Screen, self).back())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def getBackground(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.getBackground()"""
        return 'util.Identifier'.__wrap(super(InventoryScreen, self).getBackground())

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool.__wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(gui.Screen, self).getName())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @overload
    def get(self, arg0: int) -> 'menu.ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.get(int)"""
        return 'menu.ItemSlot'.__wrap(super(__ContainerScreen, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def left(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.left()"""
        return int.__wrap(super(InventoryScreen, self).left())

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(gui.Screen, self).getRawTitle())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def renderForeground(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.container.InventoryScreen.renderForeground(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__InventoryScreen, self).renderForeground(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0) 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.container.CrateScreen
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.client.gui import widget
except ImportError:
    widget = __import_once__("pyquantum.client.gui.widget")

import java.util.function.Supplier as Supplier
import java.nio.file.Path as __Path
__Path = __Path
import dev.ultreon.quantum.menu.CrateMenu as __CrateMenu
__CrateMenu = __CrateMenu
import dev.ultreon.quantum.client.gui.screens.container.ContainerScreen as __ContainerScreen
__ContainerScreen = __ContainerScreen
import java.util.Collection as Collection
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
try:
    from pyquantum import component
except ImportError:
    component = __import_once__("pyquantum.component")

try:
    from pyquantum.client import gui
except ImportError:
    gui = __import_once__("pyquantum.client.gui")

import java.lang.Double as __double
from builtins import bool
import dev.ultreon.quantum.client.gui.widget.UIContainer as __UIContainer
__UIContainer = __UIContainer
import dev.ultreon.quantum.client.gui.screens.container.CrateScreen as __CrateScreen
__CrateScreen = __CrateScreen
import dev.ultreon.quantum.component.GameComponentHolder as __GameComponentHolder
__GameComponentHolder = __GameComponentHolder
import java.util.List as __List
__List = __List
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
from builtins import int
import dev.ultreon.quantum.client.gui.Size as __Size
__Size = __Size
import dev.ultreon.quantum.client.gui.Screen as __Screen
__Screen = __Screen
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.menu.ItemSlot as __ItemSlot
__ItemSlot = __ItemSlot
import java.util.function.Consumer as Consumer
import dev.ultreon.quantum.client.gui.Dialog as __Dialog
__Dialog = __Dialog
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.client.gui.Position as __Position
__Position = __Position
import dev.ultreon.quantum.client.gui.widget.layout.Layout as __Layout
__Layout = __Layout
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.client.gui.widget.Widget as __Widget
__Widget = __Widget
try:
    from pyquantum.client.gui.widget import layout
except ImportError:
    layout = __import_once__("pyquantum.client.gui.widget.layout")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.nio.file.Path as Path
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.component.GameComponent as __GameComponent
__GameComponent = __GameComponent
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Integer as __int
import dev.ultreon.quantum.client.gui.Bounds as __Bounds
__Bounds = __Bounds
import java.util.Map as Map
import java.util.List as List
 
class CrateScreen(__ContainerScreen, ContainerScreen):
    """dev.ultreon.quantum.client.gui.screens.container.CrateScreen"""
 
    @staticmethod
    def __wrap(java_value: __CrateScreen) -> 'CrateScreen':
        return CrateScreen(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrateScreen):
        """
        Dynamic initializer for CrateScreen.
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
 
    # public static final dev.ultreon.quantum.client.gui.widget.UIContainer<?> dev.ultreon.quantum.client.gui.widget.UIContainer.ROOT
    ROOT: 'widget.UIContainer' = __wrap(__widget.UIContainer.ROOT)


    @overload
    def mouseWheel(self, arg0: int, arg1: int, arg2: float) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseWheel(int,int,double)"""
        return bool.__wrap(super(__gui.Screen, self).mouseWheel(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @property
    def directHovered(self) -> Widget:
        return Widget.__wrap(super(__Screen).directHovered())

    @override
    @overload
    def isClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isClickable()"""
        return bool.__wrap(super(widget.Widget, self).isClickable())

    @overload
    def onClose(self, arg0: 'Screen') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onClose(dev.ultreon.quantum.client.gui.Screen)"""
        return bool.__wrap(super(__ContainerScreen, self).onClose(arg0))

    @override
    @overload
    def components(self) -> 'Collection':
        """public default java.util.Collection<T> dev.ultreon.quantum.component.GameComponentHolder.components()"""
        return 'Collection'.__wrap(super(component.GameComponentHolder, self).components())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def renderWidget(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.renderWidget(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ContainerScreen, self).renderWidget(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def mouseDrag(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseDrag(int,int,int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseDrag(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def getBackground(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.gui.screens.container.CrateScreen.getBackground()"""
        return 'util.Identifier'.__wrap(super(CrateScreen, self).getBackground())

    @override
    @overload
    def getMaxSlots(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.getMaxSlots()"""
        return int.__wrap(super(ContainerScreen, self).getMaxSlots())

    @override
    @overload
    def x(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.x(int)"""
        super(__widget.Widget, self).x(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Bounds'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setBounds(dev.ultreon.quantum.client.gui.Bounds)"""
        super(__widget.Widget, self).setBounds(arg0)

    @overload
    def __init__(self, arg0: 'CrateMenu', arg1: 'TextObject'):
        """public dev.ultreon.quantum.client.gui.screens.container.CrateScreen(dev.ultreon.quantum.menu.CrateMenu,dev.ultreon.quantum.text.TextObject)"""
        val = __CrateScreen(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setPreferredHeight(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredHeight(int)"""
        super(__widget.Widget, self).setPreferredHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def title(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def onItemChanged(self, arg0: int, arg1: 'ItemStack'):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onItemChanged(int,dev.ultreon.quantum.item.ItemStack)"""
        super(__ContainerScreen, self).onItemChanged(__int.valueOf(arg0), arg1)

    @override
    @overload
    def canClose(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canClose()"""
        return bool.__wrap(super(gui.Screen, self).canClose())

    @override
    @overload
    def getDialog(self) -> 'gui.Dialog':
        """public dev.ultreon.quantum.client.gui.Dialog dev.ultreon.quantum.client.gui.Screen.getDialog()"""
        return 'gui.Dialog'.__wrap(super(gui.Screen, self).getDialog())

    @override
    @overload
    def onClosed(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.onClosed()"""
        super(ContainerScreen, self).onClosed()

    @override
    @overload
    def onFocusGained(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusGained()"""
        super(widget.Widget, self).onFocusGained()

    @override
    @overload
    def setPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(int,int)"""
        super(__widget.Widget, self).setPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getLayout(self) -> 'layout.Layout':
        """public dev.ultreon.quantum.client.gui.widget.layout.Layout dev.ultreon.quantum.client.gui.widget.UIContainer.getLayout()"""
        return 'layout.Layout'.__wrap(super(widget.UIContainer, self).getLayout())

    @override
    @overload
    def getPreferredHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredHeight()"""
        return int.__wrap(super(widget.Widget, self).getPreferredHeight())

    @overload
    def charType(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.charType(char)"""
        return bool.__wrap(super(__gui.Screen, self).charType(__char.valueOf(arg0)))

    @override
    @overload
    def getPreferredSize(self) -> 'gui.Size':
        """public dev.ultreon.quantum.client.gui.Size dev.ultreon.quantum.client.gui.widget.Widget.getPreferredSize()"""
        return 'gui.Size'.__wrap(super(widget.Widget, self).getPreferredSize())

    @overload
    def getWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setEnabled(boolean)"""
        super(__widget.Widget, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def title(self, arg0: 'TextObject') -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.title(dev.ultreon.quantum.text.TextObject)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).title(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def titleTranslation(self, arg0: str) -> 'gui.Screen':
        """public dev.ultreon.quantum.client.gui.Screen dev.ultreon.quantum.client.gui.Screen.titleTranslation(java.lang.String)"""
        return 'gui.Screen'.__wrap(super(__gui.Screen, self).titleTranslation(arg0))

    @override
    @overload
    def path(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.client.gui.Screen.path()"""
        return 'Path'.__wrap(super(gui.Screen, self).path())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def mouseClick(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.mouseClick(int,int,int,int)"""
        return bool.__wrap(super(__ContainerScreen, self).mouseClick(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hide(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.hide()"""
        super(widget.Widget, self).hide()

    @override
    @overload
    def getPreferredWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredWidth()"""
        return int.__wrap(super(widget.Widget, self).getPreferredWidth())

    @override
    @overload
    def getPreferredX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredX()"""
        return int.__wrap(super(widget.Widget, self).getPreferredX())

    @override
    @overload
    def closeDialog(self, arg0: 'Dialog'):
        """public void dev.ultreon.quantum.client.gui.Screen.closeDialog(dev.ultreon.quantum.client.gui.Dialog)"""
        super(__gui.Screen, self).closeDialog(arg0)

    @override
    @overload
    def build(self, arg0: 'GuiBuilder'):
        """public final void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.build(dev.ultreon.quantum.client.gui.GuiBuilder)"""
        super(__ContainerScreen, self).build(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def revalidate(self):
        """public void dev.ultreon.quantum.client.gui.Screen.revalidate()"""
        super(gui.Screen, self).revalidate()

    @property
    def focused(self, value: 'widget.Widget'):
        super(__Screen).focused(value)

    @property
    def parentScreen(self, value: 'gui.Screen'):
        super(__Screen).parentScreen(value)

    @override
    @overload
    def renderForeground(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.renderForeground(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__ContainerScreen, self).renderForeground(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def backgroundWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.CrateScreen.backgroundWidth()"""
        return int.__wrap(super(CrateScreen, self).backgroundWidth())

    @override
    @overload
    def componentRegistry(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.util.Identifier, dev.ultreon.quantum.client.gui.widget.components.UIComponent> dev.ultreon.quantum.client.gui.widget.Widget.componentRegistry()"""
        return 'Map'.__wrap(super(widget.Widget, self).componentRegistry())

    @override
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getX()"""
        return int.__wrap(super(widget.Widget, self).getX())

    @override
    @overload
    def top(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.top()"""
        return int.__wrap(super(ContainerScreen, self).top())

    @override
    @overload
    def init(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.init(int,int)"""
        super(__gui.Screen, self).init(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isWithinBounds(self, arg0: int, arg1: int) -> bool:
        """public final boolean dev.ultreon.quantum.client.gui.widget.Widget.isWithinBounds(int,int)"""
        return bool.__wrap(super(__widget.Widget, self).isWithinBounds(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def withComponent(self, arg0: 'Identifier', arg1: 'Consumer', *arg2: 'component.GameComponent'):
        """public final <T extends dev.ultreon.quantum.component.GameComponent<?>> void dev.ultreon.quantum.client.gui.widget.Widget.withComponent(dev.ultreon.quantum.util.Identifier,java.util.function.Consumer<T>,T...)"""
        super(__widget.Widget, self).withComponent(arg0, arg1, arg2)

    @override
    @overload
    def backgroundHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.CrateScreen.backgroundHeight()"""
        return int.__wrap(super(CrateScreen, self).backgroundHeight())

    @override
    @overload
    def renderChild(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float, arg4: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.renderChild(dev.ultreon.quantum.client.gui.Renderer,int,int,float,dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).renderChild(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def y(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.y(int)"""
        super(__widget.Widget, self).y(__int.valueOf(arg0))

    @override
    @overload
    def emitUpdate(self):
        """public void dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.emitUpdate()"""
        super(ContainerScreen, self).emitUpdate()

    @override
    @overload
    def remove(self, arg0: 'Widget'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.remove(dev.ultreon.quantum.client.gui.widget.Widget)"""
        super(__widget.UIContainer, self).remove(arg0)

    @override
    @overload
    def height(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.height(int)"""
        super(__widget.Widget, self).height(__int.valueOf(arg0))

    @overload
    def keyRelease(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyRelease(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyRelease(__int.valueOf(arg0)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isEnabled()"""
        return bool.__wrap(super(widget.Widget, self).isEnabled())

    @staticmethod
    @overload
    def isPosWithin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean dev.ultreon.quantum.client.gui.widget.Widget.isPosWithin(int,int,int,int,int,int)"""
        return bool.__wrap(__Widget.isPosWithin(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def setPreferredX(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredX(int)"""
        super(__widget.Widget, self).setPreferredX(__int.valueOf(arg0))

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isFocused()"""
        return bool.__wrap(super(widget.Widget, self).isFocused())

    @overload
    def getMenu(self) -> 'menu.CrateMenu':
        """public dev.ultreon.quantum.menu.CrateMenu dev.ultreon.quantum.client.gui.screens.container.CrateScreen.getMenu()"""
        return 'menu.CrateMenu'.__wrap(super(CrateScreen, self).getMenu())

    @override
    @overload
    def showDialog(self, arg0: 'DialogBuilder'):
        """public void dev.ultreon.quantum.client.gui.Screen.showDialog(dev.ultreon.quantum.client.gui.DialogBuilder)"""
        super(__gui.Screen, self).showDialog(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public final void dev.ultreon.quantum.client.gui.Screen.resize(int,int)"""
        super(__gui.Screen, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setVisible(boolean)"""
        super(__widget.Widget, self).setVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def left(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.left()"""
        return int.__wrap(super(ContainerScreen, self).left())

    @overload
    def keyPress(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.keyPress(int)"""
        return bool.__wrap(super(__gui.Screen, self).keyPress(__int.valueOf(arg0)))

    @override
    @overload
    def onFocusLost(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onFocusLost()"""
        super(widget.Widget, self).onFocusLost()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def onDisconnect(self, arg0: 'UIContainer'):
        """public <T extends dev.ultreon.quantum.client.gui.widget.UIContainer<T>> void dev.ultreon.quantum.client.gui.widget.Widget.onDisconnect(dev.ultreon.quantum.client.gui.widget.UIContainer<T>)"""
        super(__widget.Widget, self).onDisconnect(arg0)

    @override
    @overload
    def getPreferredPos(self) -> 'gui.Position':
        """public dev.ultreon.quantum.client.gui.Position dev.ultreon.quantum.client.gui.widget.Widget.getPreferredPos()"""
        return 'gui.Position'.__wrap(super(widget.Widget, self).getPreferredPos())

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(int,int)"""
        super(__widget.Widget, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def children(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.children()"""
        return 'List'.__wrap(super(widget.UIContainer, self).children())

    @override
    @overload
    def setup(self, arg0: 'List'):
        """public void dev.ultreon.quantum.client.gui.screens.container.CrateScreen.setup(java.util.List<dev.ultreon.quantum.item.ItemStack>)"""
        super(__CrateScreen, self).setup(arg0)

    @override
    @overload
    def mouseMove(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.Screen.mouseMove(int,int)"""
        super(__gui.Screen, self).mouseMove(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPos(self, arg0: 'Position'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPos(dev.ultreon.quantum.client.gui.Position)"""
        super(__widget.Widget, self).setPos(arg0)

    @override
    @overload
    def render(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public final void dev.ultreon.quantum.client.gui.Screen.render(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def disable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.disable()"""
        super(widget.Widget, self).disable()

    @override
    @overload
    def setLayout(self, arg0: 'Layout'):
        """public void dev.ultreon.quantum.client.gui.widget.UIContainer.setLayout(dev.ultreon.quantum.client.gui.widget.layout.Layout)"""
        super(__widget.UIContainer, self).setLayout(arg0)

    @override
    @overload
    def getPreferredY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getPreferredY()"""
        return int.__wrap(super(widget.Widget, self).getPreferredY())

    @override
    @overload
    def setPreferredPos(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredPos(int,int)"""
        super(__widget.Widget, self).setPreferredPos(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getWidgets(self) -> 'List':
        """public java.util.List<? extends dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgets()"""
        return 'List'.__wrap(super(widget.UIContainer, self).getWidgets())

    @overload
    def add(self, arg0: 'Widget') -> 'widget.Widget':
        """public <C extends dev.ultreon.quantum.client.gui.widget.Widget> C dev.ultreon.quantum.client.gui.Screen.add(C)"""
        return 'widget.Widget'.__wrap(super(__gui.Screen, self).add(arg0))

    @overload
    def filesDropped(self, arg0: 'List') -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.filesDropped(java.util.List<com.badlogic.gdx.files.FileHandle>)"""
        return bool.__wrap(super(__gui.Screen, self).filesDropped(arg0))

    @override
    @overload
    def setPreferredWidth(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredWidth(int)"""
        super(__widget.Widget, self).setPreferredWidth(__int.valueOf(arg0))

    @overload
    def position(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.position(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Position>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).position(arg0))

    @override
    @overload
    def back(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.back()"""
        return bool.__wrap(super(gui.Screen, self).back())

    @overload
    def bounds(self, arg0: 'Supplier') -> 'widget.UIContainer':
        """public dev.ultreon.quantum.client.gui.widget.UIContainer<T> dev.ultreon.quantum.client.gui.widget.UIContainer.bounds(java.util.function.Supplier<dev.ultreon.quantum.client.gui.Bounds>)"""
        return 'widget.UIContainer'.__wrap(super(__widget.UIContainer, self).bounds(arg0))

    @overload
    def getExactWidgetAt(self, arg0: int, arg1: int) -> 'widget.Widget':
        """public dev.ultreon.quantum.client.gui.widget.Widget dev.ultreon.quantum.client.gui.widget.UIContainer.getExactWidgetAt(int,int)"""
        return 'widget.Widget'.__wrap(super(__widget.UIContainer, self).getExactWidgetAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def canCloseWithEsc(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.canCloseWithEsc()"""
        return bool.__wrap(super(gui.Screen, self).canCloseWithEsc())

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.client.gui.Screen.getName()"""
        return str.__wrap(super(gui.Screen, self).getName())

    @override
    @overload
    def enable(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.enable()"""
        super(widget.Widget, self).enable()

    @override
    @overload
    def isHovered(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isHovered()"""
        return bool.__wrap(super(widget.Widget, self).isHovered())

    @overload
    def getComponent(self, arg0: 'Identifier', *arg1: 'component.GameComponent') -> 'component.GameComponent':
        """public <T extends dev.ultreon.quantum.component.GameComponent<?>> T dev.ultreon.quantum.client.gui.widget.Widget.getComponent(dev.ultreon.quantum.util.Identifier,T...)"""
        return 'component.GameComponent'.__wrap(super(__widget.Widget, self).getComponent(arg0, arg1))

    @overload
    def get(self, arg0: int) -> 'menu.ItemSlot':
        """public dev.ultreon.quantum.menu.ItemSlot dev.ultreon.quantum.client.gui.screens.container.ContainerScreen.get(int)"""
        return 'menu.ItemSlot'.__wrap(super(__ContainerScreen, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def setPreferredSize(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredSize(int,int)"""
        super(__widget.Widget, self).setPreferredSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @property
    def directHovered(self, value: 'widget.Widget'):
        super(__Screen).directHovered(value)

    @overload
    def mouseRelease(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mouseRelease(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mouseRelease(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.widget.Widget.isVisible()"""
        return bool.__wrap(super(widget.Widget, self).isVisible())

    @override
    @overload
    def renderChildren(self, arg0: 'Renderer', arg1: int, arg2: int, arg3: float):
        """public void dev.ultreon.quantum.client.gui.Screen.renderChildren(dev.ultreon.quantum.client.gui.Renderer,int,int,float)"""
        super(__gui.Screen, self).renderChildren(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getTitle(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.client.gui.Screen.getTitle()"""
        return 'text.TextObject'.__wrap(super(gui.Screen, self).getTitle())

    @override
    @overload
    def width(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.width(int)"""
        super(__widget.Widget, self).width(__int.valueOf(arg0))

    @override
    @overload
    def onRevalidate(self, arg0: 'RevalidateListener'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.onRevalidate(dev.ultreon.quantum.client.gui.widget.Widget$RevalidateListener)"""
        super(__widget.Widget, self).onRevalidate(arg0)

    @overload
    def mousePress(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.mousePress(int,int,int)"""
        return bool.__wrap(super(__gui.Screen, self).mousePress(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getWidgetsAt(self, arg0: int, arg1: int) -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.gui.widget.Widget> dev.ultreon.quantum.client.gui.widget.UIContainer.getWidgetsAt(int,int)"""
        return 'List'.__wrap(super(__widget.UIContainer, self).getWidgetsAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @property
    def focused(self) -> Widget:
        return Widget.__wrap(super(__Screen).focused())

    @override
    @overload
    def getWidth(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getWidth()"""
        return int.__wrap(super(widget.Widget, self).getWidth())

    @property
    def parentScreen(self) -> Screen:
        return Screen.__wrap(super(__Screen).parentScreen())

    @override
    @overload
    def getRawTitle(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.gui.Screen.getRawTitle()"""
        return str.__wrap(super(gui.Screen, self).getRawTitle())

    @override
    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getY()"""
        return int.__wrap(super(widget.Widget, self).getY())

    @override
    @overload
    def show(self):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.show()"""
        super(widget.Widget, self).show()

    @override
    @overload
    def getBounds(self) -> 'gui.Bounds':
        """public dev.ultreon.quantum.client.gui.Bounds dev.ultreon.quantum.client.gui.widget.Widget.getBounds()"""
        return 'gui.Bounds'.__wrap(super(widget.Widget, self).getBounds())

    @override
    @overload
    def getHeight(self) -> int:
        """public int dev.ultreon.quantum.client.gui.widget.Widget.getHeight()"""
        return int.__wrap(super(widget.Widget, self).getHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def isHoveringClickable(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.Screen.isHoveringClickable()"""
        return bool.__wrap(super(gui.Screen, self).isHoveringClickable())

    @override
    @overload
    def setPreferredY(self, arg0: int):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setPreferredY(int)"""
        super(__widget.Widget, self).setPreferredY(__int.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Size'):
        """public void dev.ultreon.quantum.client.gui.widget.Widget.setSize(dev.ultreon.quantum.client.gui.Size)"""
        super(__widget.Widget, self).setSize(arg0)