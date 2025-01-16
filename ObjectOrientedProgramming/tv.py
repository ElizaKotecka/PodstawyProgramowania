class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel = []
        self.volume = 0

    def turn_off(self):
        if self.is_on:
            self.is_on = False
    
    def turn_on(self):
        if not self.is_on:
            self.is_on = True

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channel = channels_list.split(', ')

    def show_channels(self):
        print('Channel list:')
        for i, channel in enumerate(self.channel, start=1):
            print(f'{i}. {channel}')

    def volume_up(self):
        if self.volume in range(0,10):
            self.volume += 1

    def volume_down(self):
        if self.volume in range(1,11):
            self.volume -= 1




    
    def show_status(self):
        if self.is_on:
            if self.channel_no > len(self.channel):
                return f"TV is on, channel {self.channel_no}. Volume: {self.volume}."
            else:
                return f"TV is on, channel {self.channel_no} ({self.channel[self.channel_no - 1]}). Volume: {self.volume}."
        else:
            return "TV is off."