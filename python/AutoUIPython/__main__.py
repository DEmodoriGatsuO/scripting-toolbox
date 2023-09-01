""" Module  Name
* Copyright (c) 2022, Tech Lovers. All rights reserved
* Project Name    : Let's RPA by Python
* Feature         : Pythonでレガシーアプリ
* Creation Date   : 2022.08.22
* Programming language used: Python
* Author          : DEmodoriGatsuO https://github.com/DEmodoriGatsuO
* Twitter         : https://twitter.com/DemodoriGatsuo Follow Me!
* Sorry           : I like English. But I can't use English.


Todo:
   
   * import __uiautomate__

"""

# https://memo.tyoshida.me/power-platform/power-automate/power-automate-desktop-sample-legacy-app-japanese-available/

import __uiautomate__
import os
import subprocess
import time

working_folder = r"~~請求デモアプリ"
os.chdir(working_folder)
subprocess.Popen("LegacyInvoicingApp.exe")

time.sleep(2)

uia = __uiautomate__.UiAutomate()
display = "Contoso Invoicing"
window, edits, buttons, texts = uia.get_element(display)
input()
