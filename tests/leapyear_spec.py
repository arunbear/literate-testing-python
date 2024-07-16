import pytest

from leapyear import is_leap_year


class LeapYearSpec:
    class A_year_is_a_leap_year:
        @pytest.mark.parametrize("year", [2004, 1984, 4])
        def if_it_is_divisible_by_4_but_not_by_100(self, year):
            assert is_leap_year(year)

        @pytest.mark.parametrize("year", [2000, 1600, 400])
        def if_it_is_divisible_by_400(self, year):
            assert is_leap_year(year)

    class A_year_is_not_a_leap_year:
        @pytest.mark.parametrize("year", [2022, 2019, 1999, 1])
        def if_it_is_not_divisible_by_4(self, year):
            assert not is_leap_year(year)

        @pytest.mark.parametrize("year", [2100, 1900, 100])
        def if_it_is_divisible_by_100_but_not_by_400(self, year):
            assert not is_leap_year(year)

    class A_year_is_supported:
        @pytest.mark.parametrize("year", [1, 100])
        def if_it_is_positive(self, year):
            is_leap_year(year)

