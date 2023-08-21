import pytest

from src.menus.context_menu import ContextMenu


def test_display_from_context_menu(capsys):
    param = {1: 'first', 2: 'second', 3: 'third',}
    expected =  'Type number from menu below: \n1. first\n2. second\n3. third\n'
    s = ContextMenu(param)
    s.display()

    captured = capsys.readouterr()
    assert captured.out == expected