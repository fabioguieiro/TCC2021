import matplotlib.pyplot as plt

def movement_plotter(X, Y, title='', x_label='', y_label = ''):
    plt.plot(X, Y)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.show()