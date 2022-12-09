from bar import Bar
import time


def main():
    n = 200
    bar = Bar(50, n)
    for i in range(n):
        bar.show()
        time.sleep(0.05)

    bar.reboot()

    for i in range(n):
        bar.show()
        time.sleep(0.05)


if __name__ == '__main__':
    main()
