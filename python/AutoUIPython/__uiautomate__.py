""" Module  Name
* Copyright (c) 2022, Tech Lovers. All rights reserved
* Project Name    : AutoUIPython
* Feature         : AutoUIPython is a Python tool that provides a convenient way to interact with UI elements using the UI Automation framework.
* Creation Date   : yyyy.MM.dd
* Programming language used: Python
* Author          : DEmodoriGatsuO https://github.com/DEmodoriGatsuO
* Twitter         : https://twitter.com/DemodoriGatsuo Follow Me!
* Sorry           : I like English. But I can't use English.


Todo:
   
   * import comtypes

"""
#%% Import Module
import comtypes
from comtypes.client import GetModule
GetModule('UIAutomationCore.dll')
from comtypes import CoCreateInstance
import comtypes.client
from comtypes.gen.UIAutomationClient import *
import time

class UiAutomate:
   def __init__(self):
      global __uia, __root
      __uia = CoCreateInstance(CUIAutomation._reg_clsid_
                           ,interface=IUIAutomation
                           ,clsctx=comtypes.CLSCTX_INPROC_SERVER)

      __root = __uia.GetRootElement()
      return
   
   def find_control(self,__base,ctltype):
      __condition = __uia.CreatePropetyaCondition(UIA_ControlTypePropertyId, ctltype)
      __ctl_elements = __base.FindAll(TreeScope_Subtree, __condition)
      return [ __ctl_elements.Getelement(i) for i in range(__ctl_elements.length)]

   def lookup_by_name(self,elements,name):
      __RETRY = 5
      for i in range(__RETRY + 1):
         try:
            for element in elements:
               if element.CurrentName == name:
                  return element
         except Exception as e:
            if i >= __RETRY:
               raise e
            else:
               time.sleep(3)
               pass

   def lookup_by_automation_id(self,elements,automation_id):
      __RETRY = 5
      for i in range(__RETRY + 1):
         try:
            for element in elements:
               if element.CurrentName == automation_id:
                  return element
         except Exception as e:
            if i >= __RETRY:
               raise e
            else:
               time.sleep(3)
               pass

   def get_element(self,display):
      __RETRY = 5
      for i in range(__RETRY + 1):
         try:
            __window = __root.FindFirst(TreeScope_Children,
                                       __uia.CreatePropertyCondition(
                                       UIA_NamePropertyId, display))
            __edits   = self.find_control(__window, UIA_EditControlTypeId)
            __buttons = self.find_control(__window, UIA_ButtonControlTypeId)
            __texts   = self.find_control(__window, UIA_TextControlTypeId)
            return __window, __edits, __buttons, __texts

         except Exception as e:
            if i >= __RETRY:
               raise e
            else:
               time.sleep(3)
               pass
      return

   def click(self,element):
      isClickable = element.GetCurrentPropetyValue(UIA_IsInvokePatternAvailablePropertyId)
      if isClickable:
         # __ptn = element.GetCurrentPropetyValue(UIA_ValuePatternId)
         __ptn = element.GetCurrentPattern(UIA_InvokePatternId)
         __ptn.QueryInterface(IUIAutomationInvokePattern).Invoke()
      return

   def set_value(self,element,value):
      isAvailable = element.GetCurrentPropetyValue(UIA_IsValuePatternAvailablePropertyId)
      if isAvailable:
         __ptn = element.GetCurrentPattern(UIA_ValuePatternId)
         __ptn.QueryInterface(IUIAutomationValuePattern).SetValue(value)
      return

   def get_value(self,element):
      isAvailable = element.GetCurrentPropetyValue(UIA_IsValuePatternAvailablePropertyId)
      if isAvailable:
         __ptn = element.GetCurrentPattern(UIA_ValuePatternId)
         __ptn.QueryInterface(IUIAutomationValuePattern).CurrentValue
      return

if __name__ == "__main__":
   uia = UiAutomate()