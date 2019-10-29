import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def integrate(x1, x2, func, n=10000):
    # estimate maximum of function
    point_along_function = np.linspace(x1,x2,1000)
    y1 = min((func(point_along_function)))
    y2 = max((func(point_along_function)))
    check = []
    xs = []
    ys = []
    for i in range(n):
        x = np.random.uniform(x1,x2,1)
        xs.append(x)
        y = np.random.uniform(y1,y2,1)
        ys.append(y)
        if y > func(x):
            check.append(0)
        else:
            check.append(1)

    area = (x2-x1)*(y2-y1)
    return(np.mean(check)*area, xs, ys, check)

def plot_integration(xs, ys, check, func, fig_name):
    df = pd.DataFrame()
    df['x'] = xs
    df['y'] = ys
    df['c'] = check

    X = np.linspace(df.x.min(), df.x.max(), 1000)
    fig = plt.figure()
    ax = fig.subplots()
    ax.plot(X, func(X), color='black', lw=4)
    ax.scatter(df[df['c'] == 0]['x'], df[df['c'] == 0]['y'], color='red')
    ax.scatter(df[df['c'] == 1]['x'], df[df['c'] == 1]['y'], color='blue')
    ax.set_aspect(1.0 / ax.get_data_ratio() * 1)
    fig.savefig(fig_name, dpi=600)
