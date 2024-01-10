import sys

def which_platform():
    platform = sys.platform
    if platform.startswith('linux'):
        print("Linux")
    elif platform.startswith('windows'):
        print("Windows")
    else:
        print("The platform is not known")

if __name__ == "__main__":
    which_platform()
