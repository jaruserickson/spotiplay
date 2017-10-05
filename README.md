<p align="center">
<a href='https://spotiplay.jaruserickson.com'><img src='SPOTIPLAY.png' height='200'></a>
</p>

Search and start songs from the CLI -- with friends!

spotiplay has Linux and OSX support.

*Spotify must be running in the background in order to use this cli remote*
*Spotify should not be interfered with for the true rooms experience*

## Installation

[PLEASE DO NOT TRY THIS YET: APP IS IN DEVELOPMENT]

Linux you need to install `python-dbus` package.
```bash
$ # Example using apt-get
$ apt-get install python-dbus
```

```bash
$ git clone https://github.com/jaruserickson/spotiplay.git
$ cd spotiplay
$ sudo python setup.py install
```

spotiplay must use credentials in order to search for songs. 
1. Register app: https://developer.spotify.com/my-applications/#!/applications
2. Edit your `~/.bashrc` to export following values:
```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```

if missing requirements:
`pip install -r requirements.txt`


### Usage
```bash
# To start the app type
$ spotipy
```

Commands  
```
Commands:
 current              print current song
 help                 list all commands 
 next                 play next song 
 pp                   play or pause song 
 stop                 stop 
 prev                 play previous song 
 history              last five search results 
 create_room          create a room
 leave                leave a room
 room                 get room addr
 queue                get room queue

```


### Logistics

A SOCK_STREAM connection is hosted on Amazon EC2, which stores a dictionary containing multiple other dictionaries each with a unique `key`, a `queue`, and `users`. When the host user performs an action, it is sent to the server, verified for host and then sends a string with the room key and action back to the users. If the room key matches, it will perform the action. 

This app is essentially a heavy socket mask over Pytify, a wonderful app which can be seen at: https://github.com/bjarneo/Pytify
