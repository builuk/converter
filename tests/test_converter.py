import pytest
from helper.converter_helper import *

def test_inches_to_centimeters():
    assert inches_to_centimeters(1) == 2.54


def test_feet_to_meters():
    assert feet_to_meters(1) == 0.3048


def test_pounds_to_kilograms():
    assert pounds_to_kilograms(1) == 0.453592


def test_centimeters_to_inches():
    assert centimeters_to_inches(2.54) == 1


def test_meters_to_feet():
    assert meters_to_feet(0.3048) == 1


def test_kilograms_to_pounds():
    assert kilograms_to_pounds(0.453592) == 1
