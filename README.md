<p align="center">
<a href='https://spotiplay.jaruserickson.com'><img src='SPOTIPLAY.png' height='200'></a>
</p>

Search and start songs from the CLI -- with friends!.
spotiplay has Linux and OS X support.

*Spotify must be running in the background in order to use this cli remote*

## Installation
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
$ pytify

# next song
$ pytify -n

# prev song
$ pytify -p

# play and pause song
$ pytify -pp

# Current playing song
$ pytify -c
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

```

