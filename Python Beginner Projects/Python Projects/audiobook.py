import pyttsx3 as p


class audiobook:
    #file_name = None
    def __init__(self,file_name):
        self.file_name = file_name

    def ReadBook(self):
        with open(self.file_name,'r') as book:
            text= book.readlines()
        for line in text:
            engine = p.init()
            engine.say(line)
            engine.runAndWait()

if __name__ == '__main__':
    b1 = audiobook('storybook.txt')
    b1.ReadBook()