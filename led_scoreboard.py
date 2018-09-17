#!/usr/bin/env python
import time
import sys
import os
import util.team_colors as team_colors

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image

class LedScoreboard:

    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 32
        options.chain_length = 4
        options.gpio_slowdown = 2
        options.parallel = 1
        options.hardware_mapping = 'regular'
        self.matrix = RGBMatrix(options = options)
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()
        self.home_score = 0
        self.away_score = 0
        self.configure_text()
        self.image_directory = 'resources/tsn_pixelated_logos'
        self.filename_template = '%s.ppm'
        pass

    def set_home_team(self, team_name):
        self.home_team = team_name
        self.home_logo = Image.open(os.path.join(self.image_directory, self.filename_template % self.home_team.lower()))
        self.home_logo.thumbnail((20, 20), Image.ANTIALIAS)

    def set_away_team(self, team_name):
        self.away_team = team_name
        self.away_logo = Image.open(os.path.join(self.image_directory, self.filename_template % self.away_team.lower()))
        self.away_logo.thumbnail((20, 20), Image.ANTIALIAS)

    def draw_home_team(self):
        pass

    def draw_away_team(self):
        pass

    def set_home_score(self, score):
        self.home_score = score
        self.update_scoreboard()

    def set_away_score(self, score):
        self.away_score = score
        self.update_scoreboard()

    def set_score(self, score):
        self.home_score = score.get("home")
        self.away_score = score.get("away")
        self.update_scoreboard()

    def increase_home_score(self):
        self.home_score = self.home_score + 1
        self.update_scoreboard()

    def increase_away_score(self):
        self.away_score = self.away_score + 1
        self.update_scoreboard()

        
    def configure_text(self):
        self.font = graphics.Font()
        self.font.LoadFont("fonts/5x7.bdf")
        self.score_ypos = 18
        self.score_xpos = 24
        self.textColor = graphics.Color(128,0,0)

    def update_scoreboard(self):
        self.offscreen_canvas.Clear()
        graphics.DrawText(self.offscreen_canvas,
                          self.font,
                          self.score_xpos,
                          self.score_ypos,
                          self.textColor,
                          "%d-%d"%(self.home_score, self.away_score)
                          )
        self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
        self.matrix.SetImage(self.home_logo.convert('RGB'), offset_y=5, offset_x=0, unsafe=False)
        self.matrix.SetImage(self.away_logo.convert('RGB'), offset_y=5, offset_x=44, unsafe=False)

    def display_play_description(self, description):
        pos = self.offscreen_canvas.width
##        i = 0
##        while i < 3:
##        print(team_colors.AVALANCHE)
        for color in team_colors.AVALANCHE:
            i = 0
            while(i == 0):
##                print(color)
                self.offscreen_canvas.Clear()
                len = graphics.DrawText(self.offscreen_canvas,
                                  self.font,
                                  pos,
                                  32,
                                  color,
                                  description
                                  )
                pos -= 1
                if (pos + len < 0):
                    pos = self.offscreen_canvas.width
                    i += 1
                    
                
                graphics.DrawText(self.offscreen_canvas,
                              self.font,
                              self.score_xpos,
                              self.score_ypos,
                              self.textColor,
                              "%d-%d"%(self.home_score, self.away_score)
                              )
                self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)
                self.matrix.SetImage(self.home_logo.convert('RGB'), offset_y=5, offset_x=0, unsafe=False)
                self.matrix.SetImage(self.away_logo.convert('RGB'), offset_y=5, offset_x=44, unsafe=False)
                time.sleep(0.01)

if __name__ == '__main__':
    led_board = LedScoreboard()
    led_board.update_scoreboard()
    for i in range(10):
        led_board.increase_home_score()
        for j in range(10):
            led_board.increase_away_score()
            time.sleep(1)
        led_board.set_away_score(0)
        
    

##    if len(sys.argv) < 3:
##        sys.exit("Require two image arguments")
##    else:
##        team1_image_file = sys.argv[1]
##        team2_image_file = sys.argv[2]
##
##    logo1 = Image.open(team1_image_file)
##    logo2 = Image.open(team2_image_file)
##
##    # Configuration for the matrix
##    options = RGBMatrixOptions()
##    options.rows = 32
##    options.chain_length = 4
##    options.gpio_slowdown = 2
##    options.parallel = 1
##    options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
##
##    matrix = RGBMatrix(options = options)
##
##    offscreen_canvas = matrix.CreateFrameCanvas()
##    font = graphics.Font()
##    font.LoadFont("fonts/5x7.bdf")
##    textColor = graphics.Color(255, 0, 0)
##    pos = 20#offscreen_canvas.width
##    graphics.DrawText(offscreen_canvas, font, pos, 18, textColor, "10-10")
##    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
##
##    # Make image fit our screen.
##    logo1.thumbnail((20, 20), Image.ANTIALIAS)
##    logo2.thumbnail((20, 20), Image.ANTIALIAS)
##
##    matrix.SetImage(logo1.convert('RGB'), offset_y=5, offset_x=0, unsafe=False)
##    matrix.SetImage(logo2.convert('RGB'), offset_y=5, offset_x=44, unsafe=False)


    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)

