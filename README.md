# DevHack
***
## Running the application:
type: pip install -r requirements.txt before running

To run the application, just Run Starting_page.py

***

## For UI changes:
1. Open the file in qt designer(if required)
2. Convert the ui file to py file:
    * pyuic5 -x [source_ui_file_name] -o [targeted_py_file_name]
    * (example) pyuic5 -x Starting_Page.ui -o Starting_page1.py
    * *remember not to directly change to the targeted py file as the targeted py file may already contains some other codes which are important for the program. Copy your changes from the newly created py file to the targeted py file or just compare both and then replace carefully so that the program won't break.
3. Convert the resources file to the a py file:
    * pyrcc5 media.qrc -o media.py

***
## Snapshots of the project:

### Starting Window:
![Starting_page](https://user-images.githubusercontent.com/59555656/218637066-fbf3e128-64de-416e-89d6-2239555ea5d2.png)

### Signup Window:
![Signup_page](https://user-images.githubusercontent.com/59555656/218637246-1925f65a-fbb7-4b7d-a592-a29eb0d40444.png)

### Login Window:
![Login_page](https://user-images.githubusercontent.com/59555656/218637196-e7916316-26cd-4f9c-a5a3-ca7bf8a014ce.png)

### Home Window:
![Home_page1](https://user-images.githubusercontent.com/59555656/218637339-2f3620be-6808-4b16-ae62-8f0785cab576.png)
![Home_page2](https://user-images.githubusercontent.com/59555656/218637348-b0087f27-3770-4b7b-8f02-413f286c3324.png)
![Home_page3](https://user-images.githubusercontent.com/59555656/218637358-e5fd5337-7fdf-4de6-a8fb-a1280b16b3e6.png)
![Home_page4](https://user-images.githubusercontent.com/59555656/218637366-b454623d-b18f-4a25-9cee-d8de612b8349.png)
![Home_page5](https://user-images.githubusercontent.com/59555656/218637374-d11aa9c9-4eef-4bd5-bb68-f827d43f0630.png)

### Hackathons Window:
![Hack_page1](https://user-images.githubusercontent.com/59555656/218637418-5706197a-9063-4492-be6d-4c60bcd780b6.png)
![Hack_page2](https://user-images.githubusercontent.com/59555656/218637467-6f8b5d3e-5785-4161-bc20-e4c2f788a2b8.png)
![Hack_page3](https://user-images.githubusercontent.com/59555656/218637468-45639c90-5397-448c-b81c-aa949d6983e0.png)


### Internships Window:
![Intern_page1](https://user-images.githubusercontent.com/59555656/218637539-bd22fcdb-7bb7-4440-a068-692b73018fa9.png)
![Intern_page2](https://user-images.githubusercontent.com/59555656/218637572-5ed2df49-6c8b-4fc0-8f28-e80f7208f338.png)
![Intern_page3](https://user-images.githubusercontent.com/59555656/218637573-9965e59e-8368-4f1f-a8e2-80ae99dac560.png)


### About Window:
![About_page](https://user-images.githubusercontent.com/59555656/218637632-c8a73dca-653e-4b13-8c4e-2e41482ff2e5.png)
