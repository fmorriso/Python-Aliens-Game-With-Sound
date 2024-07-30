import pygame as pg

from settings import Settings


class Score(pg.sprite.Sprite):
    """to keep track of the score."""

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.settings = Settings()
        self.font = pg.font.Font(None, self.settings.score_font_size)
        self.font.set_italic(1)
        self.color = "white"
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, self.settings.score_board_y)

    def update(self):
        """We only update the score in update() when it has changed."""

        if Settings.SCORE != self.lastscore:
            self.lastscore = Settings.SCORE
            msg = f"Score: {Settings.SCORE}"
            self.image = self.font.render(msg, 0, self.color)
