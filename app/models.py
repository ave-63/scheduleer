from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    r1_bids = db.relationship('UserBids', backref='bidder', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bids = db.relationship('SectionBid', backref='sect', lazy='dynamic')
    choice_num = db.Column(db.Integer, unique=True)  # 1-127 or so, to match spreadsheet
    start_time = db.Column(db.Time)  # use with datetime.time()
    end_time = db.Column(db.Time)
    mon_wed = db.Column(db.Boolean)  # class meets Monday Wednesday
    tue_thu = db.Column(db.Boolean)  # class meets Tuesday Thursday
    mtwth = db.Column(db.Boolean)   # class meets 4 days: MTWTh
    course = db.Column(db.String(4))  # eg '228A'
    room = db.Column(db.String(6))   # eg '1003B'
    units = db.Column(db.Integer)   # eg, 3 or 5
    semester = db.Column(db.String(6))  # eg, 'Sp2020' or 'Fa2020'
    taken_by = db.Column(db.String(25))  # eg 'Tchertchian E'

    def __repr__(self):
        return '<Section choice {}, math {}, id {}>'.format(self.choice_num, self.course, self.id)


class SectionBid(db.Model):
    # each row represents one teacher's bid on one class
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    user_bids_id = db.Column(db.Integer, db.ForeignKey('user_bids.id'))

    def __repr__(self):
        return '<SectionBid id {}, bid {}, section_id {}, user_bids_id {}>'.format(self.id, 
            self.bid, self.section_id, self.user_bids_id)



class UserBids(db.Model):
    # collection of one teacher's round 1 bids
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    primary = db.Column(db.Boolean)  # only 1 UserBids w/ this true per user
    bid_1_prep = db.Column(db.Integer)
    bid_2_prep = db.Column(db.Integer)
    bid_3_prep = db.Column(db.Integer)
    bid_4_prep = db.Column(db.Integer)
    bid_5_prep = db.Column(db.Integer)
    min_acc_units = db.Column(db.Integer)  # minimum acceptable unit total, eg, 13
    max_acc_units = db.Column(db.Integer)  # maximum acceptable unit total, eg, 17
    min_des_units = db.Column(db.Integer)  # minimum desired unit total, eg 14
    max_des_units = db.Column(db.Integer)  # maximum desired unit total, eg 16
    section_bids = db.relationship('SectionBid', backref='from_userbids', lazy='dynamic')

    def __repr__(self):
        return '<UserBids id {}, user_id {}, primary {}>'.format(self.id,
            self.user_id, self.primary)

# TODO: SchedOpt, SchedOptSection, SchedOptProj (joining table?)

