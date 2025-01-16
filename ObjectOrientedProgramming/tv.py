class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel = []
        self.volume = 0

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print('Turning TV off...')
    
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print('Turning TV on...')

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        print(f'Changing channel to channel number: {new_channel_no} ({self.channel[self.channel_no - 1]})')

    def set_channels(self, channels_list):
        self.channel = channels_list.split(', ')
        print('Adding new channels...')

    def show_channels(self):
        if self.channel == []:
            print("You don't have aby channels!")
        else:
            print('Channel list:')
            for i, channel in enumerate(self.channel, start=1):
                print(f'{i}. {channel}')

    def volume_up(self):
        if self.volume in range(0,10):
            self.volume += 1
            print('Volume up!')
        else:
            print('You have reached maximum volume.')

    def volume_down(self):
        if self.volume in range(1,11):
            self.volume -= 1
            print('Volume down!')
        else:
            print('You have reached minimum volume.')

    def show_status(self):
        if self.is_on:
            if self.channel_no > len(self.channel):
                print(f"TV is on, channel {self.channel_no}. Volume: {self.volume}.")
            else:
                print(f"TV is on, channel {self.channel_no} ({self.channel[self.channel_no - 1]}). Volume: {self.volume}.")
        else:
            print("TV is off.")