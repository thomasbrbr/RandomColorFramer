import os
import sd
import importlib
from lib import api, rcftoolbar
from PySide6 import QtGui

importlib.reload(rcftoolbar)
importlib.reload(api)

API = api.API(sd.getContext())

def add_toolbar_to_graph_view(graph_view_id):
    API.ui_mgr.addToolbarToGraphView(graph_view_id,
                                     rcftoolbar.RCFToolbar(API),
                                     icon=QtGui.QIcon(os.path.join(API.toolbarResourcesDir,'rcf_toolbar_icon.png')),
                                     tooltip="Random Color Framer")


def initializeSDPlugin():
    API.graph_view_callback_id = API.ui_mgr.registerGraphViewCreatedCallback(add_toolbar_to_graph_view)

def uninitializeSDPlugin():
    API.ui_mgr.unregisterCallback(API.graph_view_callback_id)