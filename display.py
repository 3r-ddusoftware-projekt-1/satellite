from lib.ssd1306 import SSD1306_I2C

class Display:
    def __init__(self, i2c):
        self.oled = SSD1306_I2C(64, 48, i2c)

    def write(self, text):
        text = str(text)
        self.clear()

        for n, line in zip(range(5), self.to_lines(text)):
            self.oled.text(line, 0, 9*n)

        self.oled.show()

    def clear(self):
        self.oled.fill(0)

    def to_lines(self, text):
        raw_lines = text.split("\n")
        lines = []
        line_length = 8
        for raw_line in raw_lines:
            for i in range(0, len(raw_line), line_length):
                lines.append(raw_line[i: i + line_length])
        return lines
