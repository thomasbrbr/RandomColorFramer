import os

class API(object):
    def __init__(self, context):
        self.context = context
        self.application = self.context.getSDApplication()
        self.ui_mgr = self.application.getQtForPythonUIMgr()
        self.graph_view_callback_id = -1
        self.main_window = self.ui_mgr.getMainWindow()
        self.toolbarResourcesDir = os.path.normpath(f'{os.path.dirname(__file__)}\\..\\resources')
