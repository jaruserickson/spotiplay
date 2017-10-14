# NOTE: spotiplay is officially deprecated. please take a look at SPOTICAST for the current version

[SPOTICAST](https://github.com/jaruserickson/spoticast)

<p align="center">
<a href='https://github.com/jaruserickson/spoticast'><img src='SPOTIPLAY.png' height='200'></a>
</p>

Search and start songs from the CLI -- with friends!

## Credit

This project wouldn't be possible without [Spotipy](https://github.com/plamere/spotipy) or [Pytify](https://github.com/bjarneo/Pytify). This project was originally forked from Pytify.

spotiplay only has LINUX and OSX support.

*Spotify must be running in the background in order to use this cli remote*

*Spotify should not be interfered with during use for the true rooms experience*

## Installation

Linux users need to install `python-dbus` package.
```bash
$ # Example using apt-get
$ apt-get install python-dbus
```
to install:
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

if missing setup.py misses any requirements:
`pip install -r requirements.txt`


### Usage
```bash
$ spotipy
> /create_room
Sending host request...
Joined room: spay-snapback
> /room
spay-snapback
> humble 
# navigate thru curses panel to add songs to queue
> /play
#listen to your tunes
> /pause
> /leave
Room spay-snapback left.
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

A socket connection is hosted on Amazon EC2, which stores a dictionary containing multiple other dictionaries each with a unique `key`, a `queue`, and `users`. When the host user performs an action, it is sent to the server, verified for host and then sends a string with the room key and action back to the users. If the room key matches, it will perform the action. 

This app is essentially a heavy socket mask over Pytify, a wonderful app which can be seen at: https://github.com/bjarneo/Pytify
