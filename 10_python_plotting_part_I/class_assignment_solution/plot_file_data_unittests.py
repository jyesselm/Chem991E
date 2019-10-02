import unittest

import plot_file_data


class PlotFileDataUnittest(unittest.TestCase):

    def test_get_plotting_data(self):
        csv_path = "data/co2_ppm.csv"
        ploting_data = plot_file_data.get_plotting_data_from_csv_file(csv_path)

        # check to make sure there is actual data in object
        self.assertGreater(len(ploting_data.x), 0)
        self.assertGreater(len(ploting_data.y), 0)

    def test_invalid_path(self):
        fake_path = "data/fake_file.csv"

        with self.assertRaises(IOError):
            plot_file_data.get_plotting_data_from_csv_file(fake_path)

    def test_invalid_plot_type(self):
        csv_path = "data/co2_ppm.csv"
        ploting_data = plot_file_data.get_plotting_data_from_csv_file(csv_path)

        with self.assertRaises(ValueError):
            plot_file_data.plot_data(ploting_data,
                                     "fake_type", "year", "Co2 (PPM)",
                                     "co2_ppm_per_year.png")


unittest.main()