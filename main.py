import ts3

server = ts3.TS3Server("server_address")
server.login("username", "password")
server.use_nickname("MusicBot")

def play_music(channel_id, filepath):
    server.playback_start(channel_id, filepath)

def stop_music(channel_id):
    server.playback_stop(channel_id)

def list_music(directory):
    files = server.ft_list(directory)
    for file in files:
        print(file["name"])

def handle_command(event):
    command = event["msg"].lower()
    if command == "!play":
        play_music(event["cid"], "filepath.mp3")
    elif command == "!stop":
        stop_music(event["cid"])
    elif command == "!list":
        list_music("music_directory")

server.onTextMessageEvent = handle_command
server.serve_forever()
