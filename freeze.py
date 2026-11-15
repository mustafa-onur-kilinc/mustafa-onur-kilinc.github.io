"""
Resources used to write this code:
Frozen-Flask n.d., Simon Sapin, accessed 14 November 2026,
<https://frozen-flask.readthedocs.io/en/latest/>

John Yang 2026, "sitebuilder.py", GitHub, Inc., accessed 14 November 2026,
<https://github.com/john-b-yang/john-b-yang.github.io/blob/master/sitebuilder.py>
"""

from flask_frozen import Freezer
from server import app

freezer = Freezer(app)

FREEZER_RELATIVE_URLS = True

if __name__ == "__main__":
    freezer.freeze()
