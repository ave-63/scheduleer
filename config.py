import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# when you bid on an adjunct's section, scheduleer will treat the bid like 
# it's this much less, making it less likely to be chosen,
# but you still pay the full price that you bid.
# results: with penalty = 6, there were about 0.9 - 1.0 adjuncts knocked per schedule
#          with penalty = 4, it was more like 2 or 3.
knocking_adj_penalty = 6

semester = 'Fa2019'

non_participants = ['tchertea', 'lehavisa']