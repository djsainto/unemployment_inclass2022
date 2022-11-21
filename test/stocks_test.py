
from app.stocks import format_usd

def test_usd_formatting():
  
   # assert 2+2 == 4
    assert format_usd(4.5) == "$4.50"

