import pytest
import utmcon
import pandas as pd
import os


@pytest.fixture
def temp_file(tmpdir):
    d = tmpdir.join("data.csv")
    d.write("""latitude,longitude,id
555555,5555555,MW18-100""")
    filename = os.path.join(d.dirname, d.basename)
    df = pd.read_csv(filename)
    return df


def test_convert(temp_file):
    column_names = list(temp_file.columns.values)
    first_row = list(temp_file.loc[0])
    assert "latitude" in column_names
    assert "longitude" in column_names
    assert 555555, 5555555 in first_row




