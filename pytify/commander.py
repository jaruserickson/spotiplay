from __future__ import absolute_import, unicode_literals


class Commander():
    def __init__(self, Pytifylib, Room):
        self.pytify = Pytifylib
        self.room = Room

    def parse(self, command):
        if command and command[0] != '/':
            return ''

        command = command.replace('/', '')

        return command

    def commands(self):
        return {
            'help': 'list all commands',
            'current': 'print current song',
            'next': 'play next song',
            'prev': 'play previous song',
            'pp': 'play or pause song',
            'stop': 'stop',
            'history': 'last ten history entries',
            'create_room': 'create a room',
            'leave': 'leave a room',
            'room': 'get room addr',
            'queue': 'get room queue'
        }

    def validate(self, command):
        for key in self.commands():
            if command != key:
                continue

            return True

        return False

    def help(self):
        print('\nCommands:')

        for key, val in self.commands().items():
            print(' {0:20} {1:75}'.format(key, val))

        print('\n')

    def run(self, command):
        command = self.parse(command)

        if not command:
            return False

        if not self.validate(command):
            self.help()

        if command == 'help':
            self.help()

        elif command == 'current':
            print(self.pytify.get_current_playing())

        elif command == 'next':
            self.pytify.next()

        elif command == 'prev':
            self.pytify.prev()

        elif command == 'pp':
            self.pytify.play_pause()

        elif command == 'stop':
            self.pytify.stop()

        elif command == 'history':
            self.pytify.print_history()

        elif command == 'room':
            if self.room:
                print(self.room.get_addr())
            else:
                print("You're not in a room!")

        elif command == 'queue':
            if self.room:
                print(self.room.get_queue())
            else:
                print("You're not in a room!")


        return True
