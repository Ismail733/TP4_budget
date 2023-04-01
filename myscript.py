import os

good_hash = 'e4cfc6f'
bad_hash = 'c1a4be0'

os.system(f"git bisect start {bad_hash} {good_hash}")

os.system('git bisect run python manage.py test')
