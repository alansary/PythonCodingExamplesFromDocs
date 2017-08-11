#!/usr/bin/env python3
def main():
    print("This is the syntax.py file.")
    egg()

def egg():
    print('egg')

if __name__ == "__main__": main()
# The previous line allows us to call functions before their definitions
# if __name__ == "__main__": allows this to only be run when this file is called as the main module (it is not mandatory)
