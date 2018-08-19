__author__ = 'brycerich'
from PIL import Image, ImageTk
import tkinter as tk
import os
import time

class Scoreboard:

    def __init__(self):
        self.image_directory = 'resources/NHL_pixelated_logos'
        self.filename_template = '%s_pixelated.png'
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=64, height=32)
        self.canvas.pack()
        self.home_score = 0
        self.away_score = 0
        self.home_team_id = None
        self.away_team_id = None
        self.score = self.canvas.create_text(35,16,text="%d-%d"%(self.home_score, self.away_score))

    def set_home_team(self, team_name):
        pilImage = Image.open(os.path.join(self.image_directory, self.filename_template % team_name.lower()))
        self.home_team = (team_name, ImageTk.PhotoImage(pilImage), 0) #contains team name, image, and score
        self.draw_home_team()

    def set_away_team(self, team_name):
        pilImage = Image.open(os.path.join(self.image_directory, self.filename_template % team_name.lower()))
        self.away_team = (team_name, ImageTk.PhotoImage(pilImage)) #contains team name, image, and score
        self.draw_away_team()

    def draw_home_team(self):
        if self.home_team_id is None:
            self.home_team_id = self.canvas.create_image(13,16, image=self.home_team[1])
        else:
            self.canvas.itemconfig(self.home_team_id, image=self.home_team[1])
        self.root.update()

    def draw_away_team(self):
        if self.away_team_id is None:
            self.away_team_id = self.canvas.create_image(57,16, image=self.away_team[1])
        else:
            self.canvas.itemconfig(self.away_team_id, image=self.away_team[1])
        self.root.update()

    # def draw_score(self):
    #     self.root.update()

    def set_home_score(self, score):
        self.home_score = score

    def set_away_score(self, score):
        self.away_score = score

    def increase_home_score(self):
        self.home_score = self.home_score + 1
        self.canvas.itemconfigure(self.score, text="%d-%d"%(self.home_score, self.away_score))
        self.canvas.update()

    def increase_away_score(self):
        self.away_score = self.away_score + 1
        self.canvas.itemconfigure(self.score, text="%d-%d"%(self.home_score, self.away_score))
        self.canvas.update()

if __name__ == '__main__':
    board = Scoreboard()
    board.set_home_team("Avalanche")
    board.set_away_team("Avalanche")
    # board.draw_home_team()
    # board.draw_away_team()
    time.sleep(1)
    board.set_away_team("Penguins")
    for i in range(10):
        board.increase_home_score()
        board.increase_away_score()
        time.sleep(1)
    board.root.mainloop()


    # root = tk.Tk()
    # canvas = tk.Canvas(root,width=64, height=32)
    #
    # canvas.pack()
    #
    #
    # directory = 'resources/NHL_pixelated_logos'
    #
    # score1 = 0
    # score2 = 0
    # for filename in os.listdir(directory):
    #     if filename.endswith(".png"):
    #         # print(os.path.join(out_directory, filename[:-4]+"_pixelated.png"))
    #         # pilImage = Image.open("resources/NHL_pixelated_logos/avalanche_pixelated.png")
    #         #
    #         #
    #         # pilImage2 = Image.open("resources/NHL_pixelated_logos/penguins_pixelated.png")
    #         # im2 = ImageTk.PhotoImage(pilImage2)
    #         #
    #         # imagesprite2 = canvas.create_image(59,16,image=im2)
    #         score1 = score1+1
    #         score2 = score2+1
    #         pilImage = Image.open(os.path.join(directory, filename))
    #         im = ImageTk.PhotoImage(pilImage)
    #         imagesprite = canvas.create_image(13,16,image=im)
    #         root.update()
    #         time.sleep(0.25)
    #         canvas.delete("all")
    #         im2 = im
    #         imagesprite = canvas.create_image(57,16,image=im2)
    #         canvas.create_text(35,16,text="%d-%d"%(score1,score2))
    #
    #         # image_small = img.resize((20,20), resample=Image.BICUBIC)
    #
    #         # result = image_small.resize(img.size, resample=Image.NEAREST)
    #         # image_small.save(os.path.join(out_directory, filename[:-4]+"_pixelated.png"))
    #
    #         # img.close()
    #
    #     else:
    #         continue
    #
    # root.mainloop()
    #
