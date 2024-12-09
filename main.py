from accounts import *

def main():
    '''
    This will mostly deal with the handling of the three or four different windows used in the program.
    Should be able to navigate between each window.

    Will be able to write more once all window UI files are created.
    '''

    application = QApplication([])
    window = accounts()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()
