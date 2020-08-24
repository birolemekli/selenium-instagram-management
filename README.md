# Instagram Management

- [ ] Are you too lazy to delete messages?
- [ ] Tired of the pictures popping up on your homepage, do you want to unfollow?
- [ ] Do you want to remove pictures from your profile?

- [X] Then you can do this with Python and Selenium Mobile Emulator.

###### Let's start with the requirements setup first.

`$ pip install -r requirements.txt`

###### Let's download Chromedriver and make necessary settings.
`https://chromedriver.chromium.org/downloads`

- Parameters to be set
     - chromedriver_path: Driver location specified 
     - mobile_emulator: For MacOs (Iphone 6) and for Windows (Nexus 5) it will be determined by python by looking at the operating system. You can change it if you want.
     - username: Instagram username
     - password: Instagram password
     - count: How many messages to delete starting from the beginning
     - choice: What you want to do 
        1. 1- Delete message
        2. 2- Delete image
        3. 3- Unfollow
        
## Things to pay attention

1. Performing transactions too often may be a reason to be blocked from Instagram.
2. That's why you need to set your sleep times well.
3. Max 150 people per day are recommended to unfollow.
4. If there is a message that cannot be deleted, the application will directly stream to the next message.
5. In every error, the driver is turned off. It never leaves any garbage behind.

[![Then you can do this with Python and Selenium Mobile Emulator.](http://img.youtube.com/vi/YbY02YCBnXA/0.jpg)](http://www.youtube.com/watch?v=YbY02YCBnXA)
