class GPIO:
    BOARD = "BOARD"
    BCM = "BCM"
    OUT = "OUT"
    IN = "IN"
    LOW = 0
    HIGH = 1

    @staticmethod
    def setmode(mode):
        print(f"GPIO mode set to {mode}")

    @staticmethod
    def setup(pin, mode):
        print(f"Setting up pin {pin} as {mode}")

    @staticmethod
    def output(pin, state):
        print(f"Setting pin {pin} to state {state}")

    @staticmethod
    def input(pin):
        print(f"Reading input from pin {pin}")
        return GPIO.LOW  # Zwracaj stan niski jako domyślny

    @staticmethod
    def cleanup():
        print("Cleaning up GPIO pins")
