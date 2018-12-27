import pytest
import os
from utmcon import Utm2latlon


#####
#   Test if conversion is successful.
#####


@pytest.fixture
def temp_file(tmpdir):
    """
    Creates a temporary file to test conversion.
    :param tmpdir:
    :return:
    """
    filepath = tmpdir.join("data.csv")
    filepath.write("""easting,northing,id
555555,5555555,MW18-100""")
    return filepath


def test_conversion(temp_file):
    inst1 = Utm2latlon(temp_file, 10, "U")
    assert 50.150 in inst1.df.latitude.values.round(3)
    assert -122.222 in inst1.df.longitude.values.round(3)


#####
#   Test with incorrect column headings
#####

@pytest.fixture
def temp_file_no_easting(tmpdir):
    """
    Creates temporary file with spelling error for
    "easting" column heading.
    :param tmpdir:
    :return:
    """
    d = tmpdir.join("data.csv")
    d.write("""easti,northin,id
555555,5555555,MW18-100""")
    return d


def test_readfile_no_easting(temp_file_no_easting):
    """
    Testing if file with incorrect "easting" column
    heading is handled correctly.
    :param temp_file_no_easting:
    :return:
    """
    with pytest.raises(AttributeError) as e_info:
        Utm2latlon(temp_file_no_easting, 10, "U")

#####
#   Test file with wrong extension.
#####


@pytest.fixture
def temp_file_wrong_extension(tmpdir):
    """
    Creates temporary file that does not have the
    correct extension.
    :param tmpdir:
    :return:
    """
    d = tmpdir.join("data.doc")
    filename = os.path.join(d.dirname, d.basename)
    return filename


def test_readfile_wrong_ext(temp_file_wrong_extension, capfd):
    Utm2latlon(temp_file_wrong_extension, 10, "U")
    out, err = capfd.readouterr()
    assert out == "ERROR: File must be a CSV or Excel file.\n"