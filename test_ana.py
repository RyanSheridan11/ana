from typer.testing import CliRunner
from .ana import app
import base64

"""Run from cli using pytest
pip3 install -U pytest
pytest -q test_ana.py

"""

clean_data = [
    'ABCDEFG',
    '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', # 100 chars
    'Ryan is cool'
]

hashes = [
    ("Base64", 'QUJDREVGRw=='),
    ("Base64", 'MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MA=='),
    ("Base64", 'UnlhbiBpcyBjb29s'),
    ("MD5", '$1$O3JMY.Tw$AdLnLjQ/5jXF9.MTp3gHv/'),
    ("MD5",	'8743b52063cd84097a65d1633f5c74f5'),
    ("MD5:SALT", 	"01dfae6e5d4d90d9892622325959afbe:7050461"),
    ("SALT:MD5", 	"f0fda58630310a6dd91a7d8f0a4ceda2:4225637426"),
    ("SHA1", 'b89eaac7e61417341b710b727768294d0e6a277b'),
    ("SHA256", '$5$MnfsQ4iN$ZMTppKN16y/tIsUYs/obHlhdP.Os80yXhTurpBMUbA5'),
    ("SHA256", '$5$rounds=5000$usesomesillystri$KqJWpanXZHKq2BOB43TSaYhEWsQ1Lr5QNyPCDH/Tp.6	'),
    ("SHA512", '$6$zWwwXKNj$gLAOoZCjcr8p/.VgV/FkGC3NX7BsXys3KHYePfuIGMNjY83dVxugPYlxVg/evpcVEJLT/rSwZcDMlVVf/bhf.1'),
    ("SHA512", '$6$rounds=5000$usesomesillystri$D4IrlXatmP7rx3P3InaxBeoomnAihCKRVQP22JZ6EY47Wc6BkroIuUUBOov1i.S5KPgErtP/EN5mcO.ChWQW21'),
    ("BCRYPT", '$2a$05$bvIG6Nmid91Mu9RcmmWZfO5HJIMCT8riNW0hEp8f6/FuA2/mHZFpe')


]


runner = CliRunner()


def test_app():
    # result = runner.invoke(app, ["hashexamplemd5"])
    # print(f"StdOut: {result.stdout}")
    # assert "Hello World" in result.stdout
    base_64_tests()

def base_64_tests():
    for data in hashes:
        print(data)
        base_64_data = data.encode('utf-8')
        encoded_data = base64.b64encode(base_64_data)



        result = runner.invoke(app, [encoded_data])
        assert result.exit_code == 0

        print(f"StdOut: {result.stdout}")
