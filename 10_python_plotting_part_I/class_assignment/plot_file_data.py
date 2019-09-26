import matplotlib.pyplot as plt


class PlottingData(object):
    """
    Stores the x and y data found in a CSV file
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_plotting_data_from_csv_file(file_name):
    # TODO
    # 1) check to see if file exist using try: / except block
    # 2) load all lines from the file using a file handler f.readlines()
    # 3) create x and y lists
    # 4) iterate through each line and save split each line over comma .split(",")
    # 5) save data from each line into x and y lists, make sure to convert values into floats
    # 6) create new PlottingData object with x and y lists
    # 7) return PlottingData object
    pass

def plot_data(plot_data, plot_type, x_axis_label, y_axis_label, plot_file):
    # TODO
    # 1) plot_type can be scatter, line, or bar
    # 2) create new figure and axis
    # 3) plot data based plot_type variable
    # 4) save figure to plot_file path
    pass


#co2_ppm_plotting_data = get_plotting_data_from_csv_file("data/co2_ppm.csv")
#annual_temp_plotting_data = get_plotting_data_from_csv_file("data/annual_tem.csv")
#glacier_ice_plotting_data = get_plotting_data_from_csv_file("data/glacier_ice.csv")

#plot_data(co2_ppm_plotting_data, "line", "year", "Co2 (PPM)", "co2_ppm_per_year.png")
#plot_data(annual_temp_plotting_data, "bar", "year", "temperature", "annual_temp_per_year.png")
#plot_data(glacier_ice_plotting_data, "bar", "year",  "ice mass", "ice_mass_per_year.png")