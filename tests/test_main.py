import pytest
import pandas as pd
import os
from utmcon import Utm2latlon


@pytest.fixture
def temp_file(tmpdir):
    d = tmpdir.join("data.csv")
    d.write("""easting,northing,id
555555,5555555,MW18-100""")
    filename = os.path.join(d.dirname, d.basename)
    return filename


def test_convert(temp_file):
    inst1 = Utm2latlon(temp_file, 10, "U")
    assert 50.150 in inst1.df.latitude.values.round(3)
    assert -122.222 in inst1.df.longitude.values.round(3)


@pytest.fixture
def temp_file_no_easting(tmpdir):
    d = tmpdir.join("data.csv")
    d.write("""easti,northing,id
555555,5555555,MW18-100""")
    filename = os.path.join(d.dirname, d.basename)
    df = pd.read_csv(filename)
    return df


def test_convert_easting(temp_file_no_easting):
    with pytest.raises(Exception) as e_info:
        for index, row in df.iterrows():
            easting = row.easting






