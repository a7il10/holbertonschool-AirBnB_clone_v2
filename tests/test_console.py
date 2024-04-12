import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def test_prompt(self):
        self.assertEqual(self.hbnb_cmd.prompt, '(hbnb) ')

    def test_precmd(self):
        line = 'create BaseModel'
        new_line = self.hbnb_cmd.precmd(line)
        self.assertEqual(new_line, 'create BaseModel')

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.hbnb_cmd.do_quit(None)

    @patch('builtins.print')
    def test_help_quit(self, mock_print):
        self.hbnb_cmd.help_quit()
        mock_print.assert_called_with("Exits the program with formatting\n")

    def test_do_EOF(self):
        with patch('sys.exit') as mock_exit:
            self.hbnb_cmd.do_EOF(None)
            mock_exit.assert_called_once()

    @patch('builtins.print')
    def test_help_EOF(self, mock_print):
        self.hbnb_cmd.help_EOF()
        mock_print.assert_called_with("Exits the program without formatting\n")

    def test_emptyline(self):
        self.assertIsNone(self.hbnb_cmd.emptyline())

    def test_key_value_parser(self):
        args = ['name="John"', 'age=25', 'is_active=True']
        result = self.hbnb_cmd._key_value_parser(args)
        expected_result = {'name': 'John', 'age': 25, 'is_active': True}
        self.assertEqual(result, expected_result)

    @patch('builtins.print')
    def test_do_create(self, mock_print):
        with patch.object(HBNBCommand.classes['BaseModel'],
                          'save') as mock_save:
            self.hbnb_cmd.do_create
            ('BaseModel name="test" age=20 is_active=True')
            mock_save.assert_called_once()
            mock_print.assert_called_with(mock_save().id)

    def test_help_create(self):
        with patch('builtins.print') as mocked_print:
            self.instance.help_create()
            mocked_print.assert_called_with("Creates a class of any type")
            mocked_print.assert_called_with("[Usage]: create <className>\n")

    def test_do_show_missing_class_name(self):
        with patch('builtins.print') as mocked_print:
            args = ""
            self.instance.do_show(args)
            mocked_print.assert_called_with("** class name missing **")

    def test_do_show_nonexistent_class(self):
        with patch('builtins.print') as mocked_print:
            args = "NonExistentClass 123"
            self.instance.do_show(args)
            mocked_print.assert_called_with("** class doesn't exist **")

    def test_do_update_missing_class_name(self):
        with patch('builtins.print') as mocked_print:
            HBNBCommand().do_update(" ")
            mocked_print.assert_called_with("** class name missing **")

    def test_do_update_invalid_class_name(self):
        with patch('builtins.print') as mocked_print:
            HBNBCommand().do_update("InvalidClass 1")
            mocked_print.assert_called_with("** class doesn't exist **")

    def test_do_update_missing_instance_id(self):
        with patch('builtins.print') as mocked_print:
            HBNBCommand().do_update("ValidClass ")
            mocked_print.assert_called_with("** instance id missing **")

    # Add more test cases for different scenarios in do_update method

    def test_help_update_output(self):
        with patch('builtins.print') as mocked_print:
            HBNBCommand().help_update()
            mocked_print.assert_called_with
            ("Updates an object with new information")
            mocked_print.assert_called_with
            ("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == '__main__':
    unittest.main()
