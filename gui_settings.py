from typing import ClassVar

import pyautogui
import pygame as pg
from pygame import Rect


class GuiSettings:
    SCORE: ClassVar[int] = 0
    # game constants:
    MAX_SHOTS: ClassVar[int] = 2  # most player bullets onscreen
    ALIEN_ODDS: ClassVar[float] = 22.0  # chances a new alien appears
    BOMB_ODDS: ClassVar[float] = 60.0  # chances a new bomb will drop
    ALIEN_RELOAD: ClassVar[int]  = 12  # frames between new aliens
    ONE_TIME_COUNT: ClassVar[int] = 0 # for one-time print() calls

    __screen_pct: float = 0.0

    @property
    def screen_pct(self):
        return self.__screen_pct

    __device_width: int = 0

    @property
    def device_width(self) -> int:
        return self.__device_width

    __device_height: int = 0

    @property
    def device_height(self) -> int:
        return self.__device_height

    __scaled_width: int = 0

    @property
    def scaled_width(self) -> int:
        return self.__scaled_width

    __scaled_height: int = 0

    @property
    def scaled_height(self) -> int:
        return self.__scaled_height

    __screen_rectangle: Rect = None

    @property
    def screen_rectangle(self) -> Rect:
        return self.__screen_rectangle

    def __init__(self, pct: float = 0.75, square: bool = False, multiple_of: int = 100):
        """Initialize the game's settings."""
        # Screen settings

        # calculate game size as a percentage of device screen size
        self.__device_width, self.__device_height = pyautogui.size()
        self.screenPct: float = float(0.85)
        self.__screen_pct: float = float(pct)

        # ratio to original hard-coded values of 640 (w) x 480 (h) in the PyGame.examples.aliens GitHub repo
        self.__scaled_height: int = int(
            (self.device_height * self.__screen_pct // multiple_of) * multiple_of)
        self.__scaled_width: int = self.scaled_height if square else int(
            (self.device_width * self.__screen_pct // multiple_of) * multiple_of)

        if GuiSettings.ONE_TIME_COUNT == 0:
            print(f'device width: {self.device_width}, height: {self.device_height}')
            print(f'scaled width: {self.scaled_width}, height: {self.scaled_height}')


        self.screen_width = self.scaled_width
        self.screen_height = self.scaled_height
        self.near_bottom = self.scaled_height * 0.90
        self.score_board_y = self.scaled_height * 0.95
        self.score_font_size = int(self.device_height * 0.03)
        self.SCREEN_RECTANGLE = pg.Rect(0, 0, self.screen_width, self.screen_height)

        GuiSettings.ONE_TIME_COUNT += 1