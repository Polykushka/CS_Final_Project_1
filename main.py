from gui import *

def main():
    window = Tk()
    window.title('Grades')
    window.geometry("460x330")
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == "__main__":
    main()