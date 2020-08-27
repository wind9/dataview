import matplotlib.pyplot as plt
import random


def get_random_data(data_num):
    data_list = []
    for i in range(data_num):
        data_list.append(random.randint(0,100))
    return data_list


if __name__ == '__main__':
    x = []
    for i in range(10):
        x.append(i)
    y = get_random_data(10)
    plt.plot(x, y)
    plt.show()
