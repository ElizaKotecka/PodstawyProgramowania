# tv_show.py file
# main program

from tv import TV

def main():
   # object creation
    tv_test = TV()
    tv_test_channels = TV()

   # object usage
    print(tv_test.show_status())
    tv_test.turn_on()
    print(tv_test.show_status())
    tv_test.set_channel(5)
    print(tv_test.show_status())
    tv_test.turn_off()
    print(tv_test.show_status())

    print()

    print(tv_test_channels.show_status())
    tv_test_channels.turn_on()
    print(tv_test_channels.show_status())
    tv_test_channels.show_channels()
    tv_test_channels.set_channels('TVP1, TVP2, Polsat, TVN, Filmbox, Discovery, HBO')
    tv_test_channels.show_channels()
    print(tv_test_channels.show_status())
    tv_test_channels.set_channel(4)
    print(tv_test_channels.show_status())
    tv_test_channels.set_channel(2)
    print(tv_test_channels.show_status())
    tv_test_channels.set_channel(7)
    print(tv_test_channels.show_status())
    tv_test_channels.volume_up()
    print(tv_test_channels.show_status())
    tv_test_channels.volume_down()
    print(tv_test_channels.show_status())
    tv_test_channels.turn_off()
    print(tv_test.show_status())


if __name__ == "__main__":
    main() 