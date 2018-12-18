import utm
import pandas as pd


class Utm2latlon():

    def __init__(self):
        self.file_name = input("File name? ")
        self.zone_number = int(input("UTM zone number? "))
        self.zone_letter = input("UTM zone? ")
        # self.file_name = "Surface_water.csv"
        # self.zone_number = 10
        # self.zone_letter = "U"
        self.df = pd.read_csv("{}".format(self.file_name))
        self.lat = "latitude"
        self.lon = "longitude"
        self.convert(self.df)

    def convert(self, df_convert):
        df_convert[self.lat] = 0
        df_convert[self.lon] = 0
        for index, row in df_convert.iterrows():
            easting = row.easting
            northing = row.northing
            utm_lat, utm_lon =\
                utm.to_latlon(easting, northing, self.zone_number, self.zone_letter)
            df_convert.loc[index, self.lat] = utm_lat
            df_convert.loc[index, self.lon] = utm_lon
        self.write_file(df_convert)

    def write_file(self, df_write):
        df_write.to_csv(self.file_name + "_output.csv", index=False)


