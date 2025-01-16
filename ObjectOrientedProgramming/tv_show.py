# tv_show.py file
# main program

from tv import TV

def main():
   # object creation
    tv_test_channels = TV()

   # object usage
    tv_test_channels.show_status()
    tv_test_channels.turn_on()
    tv_test_channels.show_status()
    tv_test_channels.show_channels()
    tv_test_channels.set_channels('TVP1, TVP2, Polsat, TVN, Filmbox, Discovery, HBO')
    tv_test_channels.show_channels()
    tv_test_channels.show_status()
    tv_test_channels.set_channel(4)
    tv_test_channels.show_status()
    tv_test_channels.set_channel(2)
    tv_test_channels.show_status()
    tv_test_channels.set_channel(7)
    tv_test_channels.show_status()
    tv_test_channels.volume_up()
    tv_test_channels.show_status()
    tv_test_channels.volume_down()
    tv_test_channels.show_status()
    tv_test_channels.turn_off()
    tv_test_channels.show_status()



if __name__ == "__main__":
    main() 