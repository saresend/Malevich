from Canvas import Canvas 
from Icon import Icon



def main():
    c = Canvas(width=600, height=600, backgroundcolor=(255,255,255,255))
    i = Icon("http://simpleicon.com/wp-content/uploads/cloud-10.png", size=(150, 150))
    c.addElement(i, 225, 225)
    c.Render()

if __name__ == "__main__":
    main()