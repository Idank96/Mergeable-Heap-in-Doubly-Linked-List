from settings import Settings
from instructions import *


# create instance of Settings class.
# call read_instructions with the settings from the user
def main():
    input_ = Settings()

    read_instructions(input_)


if __name__ == '__main__':
    main()
