from os import getenv

from dotenv import load_dotenv

load_dotenv()

Environment = getenv('FLASK_ENV')

print('Flask running on : %s' % Environment, 'mode')