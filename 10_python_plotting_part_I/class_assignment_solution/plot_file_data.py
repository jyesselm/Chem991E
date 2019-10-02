import matplotlib.pyplot as plt


class PlottingData(object):
    """
    Stores the x and y data found in a CSV file
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_plotting_data_from_csv_file(file_name):
    """processes a csv file into two columns of data x and y
    returns it in a PlottingData object

    Args:
        file_name: the path of the csv file

    Returns:
        PlottingData object with both x and y lists of data

    """
    try:
        f = open(file_name)
    except:
        raise IOError("supplied file: " + file_name + " does not exist")

    lines = f.readlines()
    f.close()

    x = []
    y = []

    for l in lines:
        spl = l.split(",")
        x.append(float(spl[0]))
        y.append(float(spl[1]))

    return PlottingData(x, y)


def plot_data(plot_data, plot_type, x_axis_label, y_axis_label, plot_file):
    """Takes plot parameters and generates a plot and saves it to file

    Args:
        plot_data: A PlottingData object stores both x and y lists of data
        plot_type: A string for which type of plot you want: line, bar or scatter
        x_axis_label: A string for the x_axis label
        y_axis_label: A string for the y_axis label
        plot_file: the output path for plot to be saved

    Returns:
        None
    """

    fig = plt.figure()
    ax = fig.subplots()
    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)

    if   plot_type == "line":
        ax.plot(plot_data.x, plot_data.y)
    elif plot_type == "bar":
        ax.bar(plot_data.x, plot_data.y)
    elif plot_type == "scatter":
        ax.scatter(plot_data.x, plot_data.y)
    else:
        raise ValueError("plot type: " + plot_type + "not supported")

    fig.savefig(plot_file)



co2_ppm_plotting_data = get_plotting_data_from_csv_file("data/co2_ppm.csv")
annual_temp_plotting_data = get_plotting_data_from_csv_file("data/annual_temp.csv")
glacier_ice_plotting_data = get_plotting_data_from_csv_file("data/glacier_ice.csv")

plot_data(co2_ppm_plotting_data, "line", "year", "Co2 (PPM)", "co2_ppm_per_year.png")
plot_data(annual_temp_plotting_data, "bar", "year", "temperature", "annual_temp_per_year.png")
plot_data(glacier_ice_plotting_data, "bar", "year",  "ice mass", "ice_mass_per_year.png")