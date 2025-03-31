class Television:
    def __init__(self, channel, min_channel, max_channel):
        self.channel = channel
        self.min_channel = min_channel
        self.max_channel =max_channel

    def channel_down(self):
        self.channel -= 1

    def channel_up(self):
        self.channel += 1


def main():
    tv_1 = Television(20, 2, 20)
    tv_2 = Television(1, 1, 20)
    print(f'channel is: {tv_1.channel}')
    print(f'channel is: {tv_2.channel}')

    for x in range(1, 20):
        tv_1.channel_down()
        print(f'Channel: {tv_1.channel}')

    for x in range(1, 20):
        tv_2.channel_up()
        print(f'Channel: {tv_2.channel}')

if __name__ == "__main__":
    main()









