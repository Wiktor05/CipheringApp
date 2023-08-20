import pytest
from src.ciphering.rot13 import Rot13


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('Et tu, Brute?', 'Rg gh, Oehgr?'),
        ("Caesar liked ciphers", 'Pnrfne yvxrq pvcuref'),
        ('ABBA nag Cheryl Baker', 'NOON ant Purely Onxre'),
    ),
)
class TestClass:
    def test_rot13(self, s, expected):
        assert Rot13.execute(self, s) == expected
    
