import pytest

from leapyear import is_leap_year


class LeapYearSpec:
    class A_year_is_a_leap_year:
        @pytest.mark.parametrize("year", [2004, 1984, 4])
        def if_it_is_divisible_by_4_but_not_by_100(self, year):
            assert is_leap_year(year)
