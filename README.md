# teamspeak3-musicbot
a cute and simple music bot made for teamspeak


To create a music bot for Teamspeak 3 in Python, you will need to use the pyTSon plugin and the TS3 Python API wrapper. Here is a general outline of how you can create a music bot:

1.  Install the pyTSon plugin for Teamspeak 3. This plugin allows you to use Python scripts within Teamspeak.
    
2.  Install the TS3 Python API wrapper. This will allow you to interact with the Teamspeak 3 server using Python. You can install it using pip:
    

`pip install ts3` 

3.  Connect to the Teamspeak 3 server using the TS3 Python API. You will need to specify the server address, login credentials, and a nickname for the bot.
    
4.  Create a function to play music from a specific channel. You can use the `playback_start` method from the TS3 Python API to start playing a file in a specific channel.
    
5.  Create a function to stop the music. You can use the `playback_stop` method from the TS3 Python API to stop the playback of a file.
    
6.  Create a function to list the available music files. You can use the `ft_list` method from the TS3 Python API to list the files in a specific directory on the server.
    
7.  Create a function to handle commands from users. You can use the `onTextMessageEvent` method from the pyTSon plugin to listen for messages from users and execute the appropriate function based on the command.
