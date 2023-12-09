from gui3 import *
from logic3 import *

def main() -> None:
    """
    Main method that runs GUI
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()