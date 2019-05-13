"""
Unit and regression test for the util module.
"""

# Import package, test suite, and other packages as needed
import molssi_devops
import pytest
import sys

def test_title_case():
    """Test the title case function."""
    test_string = 'ThIS is a STRinG to BE ConVerTeD.'
    expected = 'This Is A String To Be Converted. '
    calculated =  molssi_devops.title_case(test_string)
    assert expected == calculated

def test_type_error():
    test_case = ['this', 'is', 'not', 'a', 'string']

    with pytest.raises(TypeError):
        molssi_devops.title_case(test_case)


