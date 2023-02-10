# DevHack

To run the application, just Run Starting_page.py

***

## For UI changes:
1. Open the file in qt designer(if required)
2. Convert the ui file to py file:
    * pyuic5 -x [source_ui_file_name] -o [targeted_py_file_name]
    * (example) pyuic5 -x Starting_Page.ui -o Starting_page1.py
    * *remember not to directly change to the targeted py file as the targeted py file may already contains some other codes which are important for the program. Copy your changes from the newly created py file to the targeted py file or just compare both and then replace carefully so that the program won't break.
3. Convert the resources file to the a py file:
    *pyrcc5 media.qrc -o media.py
