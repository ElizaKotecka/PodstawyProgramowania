from thermometer import Thermometer

def main():
    measure1 = Thermometer()
    measure1.turn_on()
    measure1.measure_and_display_temp()
    measure1.turn_off()

if __name__ == '__main__':
    main()