![spotiplay logo](https://github.com/jaruserickson/spotiplay/blob/master/SPOTIPLAY.png?raw=true)

Search and start songs from the CLI -- with friends!.
Linux and OS X support.

*Spotify must be running in the background in order to use this cli remote*

Python 3 support.

## Installation
```bash
$ pip install pytify
```

Python 2
```bash
$ pip install pytify==2.1.0
```

Linux you need to install `python-dbus` package.
```bash
$ # Example using apt-get
$ apt-get install python-dbus
```

## Credentials
This package now must use credentials in order to search for songs. 

Support for client credentials flow. Please follow these steps:

1. Register app: https://developer.spotify.com/my-applications/#!/applications
2. Edit your `~/.bashrc` to export following values:
```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```

## Clone repo
```bash
$ git clone https://github.com/bjarneo/Pytify.git
$ cd Pytify
$ sudo python setup.py install
```

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
![commands](http://i.imgur.com/r7pCYyH.png)
```
Commands:
 current              print current song
 help                 list all commands 
 next                 play next song 
 pp                   play or pause song 
 stop                 stop 
 prev                 play previous song 
 history              last five search results 

```

### Install dev dependencies
pip version must be > 9
```bash
$ pip install -r requirements.txt
```

### Dependencies
```bash
* requests
* prompt-toolkit
```
