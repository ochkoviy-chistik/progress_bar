import sys
import time


class Bar:
    def __init__(self, size, length):
        self.size = size
        self.length = length
        self.progress = 1
        self.percent = '\r0 '
        self.bar_string = '[{:▭<{}}]'
        self.progress_bar = self.bar_string.format('', self.size)

    def update(self):
        self.progress += 1
        self.percent = f'\r{str(round(self.progress / self.length * 100, 2))}% '
        self.progress_bar = self.bar_string.format('█' * int(self.progress / self.length * self.size), self.size)

    def reboot(self):
        self.progress = 1

    def show(self):
        output_bar = self.percent+self.progress_bar
        sys.stdout.writelines(output_bar)
        sys.stdout.flush()
        if round(self.progress / self.length * 100, 2) >= 100:
            sys.stdout.writelines(' SUCCESS!')
            sys.stdout.flush()
            print()
        self.update()


def main():
    n = 300
    bar = Bar(50, n)
    for i in range(n):
        bar.show()
        time.sleep(0.05)


if __name__ == '__main__':
    main()
