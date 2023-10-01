```python
import unittest
from unittest.mock import patch
from src import user_interface

class TestUserInterface(unittest.TestCase):

    @patch('src.user_interface.tkinter')
    def test_create_input_field(self, mock_tkinter):
        user_interface.create_input_field()
        mock_tkinter.Entry.assert_called_once()

    @patch('src.user_interface.tkinter')
    def test_create_submit_button(self, mock_tkinter):
        user_interface.create_submit_button()
        mock_tkinter.Button.assert_called_once()

    @patch('src.user_interface.tkinter')
    def test_create_message_box(self, mock_tkinter):
        user_interface.create_message_box()
        mock_tkinter.Message.assert_called_once()

    @patch('src.user_interface.tkinter')
    def test_create_window(self, mock_tkinter):
        user_interface.create_window()
        mock_tkinter.Tk.assert_called_once()

    @patch('src.user_interface.tkinter')
    def test_run_app(self, mock_tkinter):
        user_interface.run_app()
        mock_tkinter.mainloop.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```