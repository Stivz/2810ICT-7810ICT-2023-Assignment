# import wx
# import pytest
# import sys
# import pandas as pd
# import os
#
# sys.path.append('../Python Files')
# from Main_Menu import MainMenu  # Make sure the import path is correct
#
#
# @pytest.fixture
# def app():
#     app = wx.App(False)
#     yield app
#     app.Destroy()
#
# @pytest.fixture
# def main_menu(data, reviews_data, calendardata):
#     frame = MainMenu(None, data, reviews_data, calendardata)
#     frame.Show()
#     yield frame
#     frame.Close()
#
#
#
# def test_top_rated_button_click(app, main_menu):
#     button = main_menu.m_button15
#     assert button.IsEnabled()
#     button.Command(wx.CommandEvent(wx.EVT_BUTTON.typeId))
#     assert main_menu.top_rated_clicked is True
#
# @pytest.fixture
# def data():
#     # Load your data DataFrame from a CSV file or any other source
#     script_directory = os.path.dirname(os.path.abspath(__file__))
#     data_file_path = os.path.join(script_directory, "..", "csv files", "listings_dec18.csv")
#     return pd.read_csv(data_file_path)
#
# @pytest.fixture
# def reviews_data():
#     # Load your reviews_data DataFrame from a CSV file or any other source
#     script_directory = os.path.dirname(os.path.abspath(__file__))
#     reviews_file_path = os.path.join(script_directory, "..", "csv files", "reviews_dec18.csv")
#     return pd.read_csv(reviews_file_path)
#
# @pytest.fixture
# def calendardata():
#     # Load your reviews_data DataFrame from a CSV file or any other source
#     script_directory = os.path.dirname(os.path.abspath(__file__))
#     calendar_file_path = os.path.join(script_directory, "..", "csv files", "calendar_dec18.csv")
#     return pd.read_csv(calendar_file_path)
#
