#!/usr/bin/python3
# Exercises 11-2 through 11-4 combined
# Page 233
import temp_conv, sys

if __name__ == "__main__":
    run_help = "Please run as c2f_mod.py [Temp] F or C"

    try:
        usr_temp = float(sys.argv[1])
        usr_fc = sys.argv[2].lower()

        if usr_fc == 'f':
            print("{:2f}".format(temp_conv.f2c(usr_temp)))
        elif usr_fc == 'c':
            print(temp_conv.c2f(usr_temp))
        else:
            raise AttributeError
    except ValueError:
        print("Invalid number for Temperature")
        print(run_help)
    except IndexError:
        print("Incorrect number of arguments")
        print(run_help)
    except TypeError:
        print("Temperature must be a number")
        print(run_help)
    except AttributeError:
        print("Temperature must be followed by F or C")
        print(run_help)
