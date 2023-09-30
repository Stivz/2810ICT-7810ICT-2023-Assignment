import wx
import pytest
import sys
import pandas as pd
import os

# Make sure the import path is correct
sys.path.append('../Python Files')
from Keyword_Seach import keyword
from Main_Menu import MainMenu

@pytest.fixture
def app():
    app = wx.App(False)
    yield app
    app.Destroy()

def test_keyword_search(app):
    data = pd.DataFrame({'id': [1, 2, 3], 'name': [1, 10, 2323], 'amenities': ['A', 'B', 'C']})
    reviews_data = pd.DataFrame({'id': [1, 2, 3], 'review': ['Good', 'Excellent', 'Average']})
    calendardata = pd.DataFrame({'date': ['2019-01-01', '2019-01-02', '2019-01-03'], 'listing_id': [1, 2, 3], 'available': ['t', 't', 't'], 'price': [100, 150, 200]})

    # Create an instance of the Keyword class
    keyword_frame = keyword(None, data, reviews_data, calendardata)

    # Simulate interactions with the Keyword class and make assertions
    # For example, you can call keyword_frame.on_confirm_button_click() with different inputs and check the results.

    # After testing, you can close the frame if needed
    keyword_frame.Close()

def test_keyword_back_to_main_menu(app):
    data = pd.DataFrame({'id': [1, 2, 3], 'name': ['Property 1', 'Property 2', 'Property 3'], 'amenities': ['A, B', 'B, C', 'D']})
    reviews_data = pd.DataFrame({'id': [1, 2, 3], 'review': ['Good', 'Excellent', 'Average']})
    calendardata = pd.DataFrame({'date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'listing_id': [1, 2, 3], 'available': ['t', 't', 't'], 'price': [100, 150, 200]})

    # Create an instance of the Keyword class
    keyword_frame = keyword(None, data, reviews_data, calendardata)

    # Simulate the "Back To Main Menu" button click event
    keyword_frame.on_back_button_click(None)  # Pass None as the event for simulation

    if keyword_frame:
        # If the frame is not None, ensure that it's destroyed
        keyword_frame.Destroy()

    # Now check if a new instance of the MainMenu class is created (if the frame was not closed)
    assert isinstance(wx.GetApp().GetTopWindow(), MainMenu)





if __name__ == "__main__":
    pytest.main(["-v", __file__])