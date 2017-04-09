# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from window_main import mainWindow
        
def main():
    app = QApplication(sys.argv)
    
    main_ui = mainWindow()
    if not main_ui.error:
    	main_ui.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
