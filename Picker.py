# -*-coding:utf-8-*-
"""
Class defining list picker using curses
Original repo - https://github.com/wong2/pick
Deleted multiselect, simplified and reformatted code
Formatted title in bold
"""

import curses

KEYS_UP = (curses.KEY_UP, ord("k"))
KEYS_DOWN = (curses.KEY_DOWN, ord("j"))
KEYS_SELECT = (curses.KEY_RIGHT, ord(" "), curses.KEY_ENTER, ord("\n"), ord("\r"))


class Picker(object):
    def __init__(self, title: str, options: list[str], indicator="->") -> None:
        if len(options) == 0:
            raise ValueError("Options must not be empty")

        self.title = title
        self.options = options
        self.indicator = indicator

        self.index = 0

    def move_up(self) -> None:
        self.index = max(self.index - 1, 0)

    def move_down(self) -> None:
        self.index = min(self.index + 1, len(self.options) - 1)

    def get_selected(self) -> tuple[str, int]:
        return self.options[self.index], self.index

    def get_title_lines(self) -> list[str]:
        if self.title:
            return self.title.split("\n") + [""]
        return []

    def get_options_lines(self) -> list[str]:
        lines = []
        for index, option in enumerate(self.options):
            if index == self.index:
                prefix = self.indicator
            else:
                prefix = len(self.indicator) * " "

            line = prefix + " " + option
            lines.append(line)

        return lines

    def get_lines(self) -> tuple[list[str], int]:
        title_lines = self.get_title_lines()
        options_lines = self.get_options_lines()
        lines = title_lines + options_lines
        current_line = len(title_lines) + 1 + self.index
        return lines, current_line

    def draw(self) -> None:
        self.screen.clear()

        x, y = 1, 1
        max_y, max_x = self.screen.getmaxyx()
        max_rows = max_y - y

        lines, cur_line = self.get_lines()

        scroll_top = getattr(self, "scroll_top", 0)
        if cur_line <= scroll_top:
            scroll_top = 0
        elif cur_line - scroll_top > max_rows:
            scroll_top = cur_line - max_rows
        self.scroll_top = scroll_top

        lines_to_draw = lines[scroll_top : scroll_top + max_rows]

        title_is_bold_flag = False
        if scroll_top == 0:
            title_is_bold_flag = False
        else:
            title_is_bold_flag = True
        for line in lines_to_draw:
            if type(line) is tuple:
                self.screen.addnstr(y, x, line[0], max_x - 2, line[1])
            else:
                if not title_is_bold_flag:
                    self.screen.addnstr(y, x, line, max_x - 2, curses.A_BOLD)
                    title_is_bold_flag = True
                else:
                    self.screen.addnstr(y, x, line, max_x - 2)
            y += 1

        self.screen.refresh()

    def run_loop(self):
        while True:
            self.draw()
            c = self.screen.getch()
            if c in KEYS_UP:
                self.move_up()
            elif c in KEYS_DOWN:
                self.move_down()
            elif c in KEYS_SELECT:
                return self.get_selected()

    def _start(self, screen):
        self.screen = screen
        curses.initscr()
        curses.curs_set(0)
        return self.run_loop()

    def start(self):
        return curses.wrapper(self._start)
