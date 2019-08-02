from app import app, db
from app.models import User, Post, Section, SectionBid, UserBids
import csv
import datetime
import test_user_data


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,
            'Section': Section, 'SectionBid': SectionBid,
            'UserBids': UserBids}


class Sect:
    def __init__(self, choice, course, start, end,
                 MW, TTh, MTWTh, taken_by, units, room):
        self.choice = choice  # eg, 1 or 127
        self.index = 0  # index in av, user_bids.sect_bids MUST BE SET
        self.course = course  # eg 110 or 275
        self.start = start  # datetime.time object
        self.end = end      # datetime.time object
        self.MW = MW        # boolean
        self.TTh = TTh      # boolean
        self.MTWTh = MTWTh  # boolean
        self.taken_by = taken_by  # string: 'Tchertchian E' or 'Hoglund W'
        self.units = units  # int
        self.room = room    # string, eg '1003B'

    def __repr__(self):
        return('choice: {}  index: {}  course: {}  taken_by: {}'
                .format(self.choice, self.index, self.course, self.taken_by))


class UBids:
    def __init__(self, user, semester, timestamp):
        self.user = user  # User.id from db
        self.index = 0  # index in ub, av MUST BE SET
        self.semester = semester  # eg 'Fa2020'
        self.timestamp = timestamp  # datetime.datetime
        self.bid_1_prep = 0
        self.bid_2_prep = 0
        self.bid_3_prep = 0
        self.bid_4_prep = 0
        self.bid_5_prep = 0
        self.sect_bids = []  # list of bids MUST BE indexed same as s!
        self.min_acc_units = 12  # minimum number of units acceptable
        self.max_acc_units = 18
        self.min_des_units = 14  # minimum number of units desired
        self.max_des_units = 16

    def __repr__(self):
        return('user: {} index: {} semester: {} timestamp: {} \
               preps: 1-{} 2-{} 3-{} 4-{} 5-{} min_acc_units: {} \
               min_des_units: {} max_des_units: {} max_acc_units: {}'.format(
                    self.user, self.index, self.semester, self.timestamp,
                    self.bid_1_prep, self.bid_2_prep, self.bid_3_prep,
                    self.bid_4_prep, self.bid_5_prep, self.min_acc_units,
                    self.min_des_units, self.max_des_units,
                    self.max_acc_units))


class USchedOpt:
    # List of sections chosen so far for one user
    # data: list of sections, user's index, unit_total, total_bid?
    # methods: evaluate added value eval_av(self,sect)
    def __init__(self, index):
        self.unit_total = 0
        self.total_bid = 0
        self.s = []
        self.index = index
        self.done = false

    def add(self, sect):
        self.unit_total += sect.units
        self.total_bid += av[sect.index][self.index]  # av MUST be kept up to date!

    #def remove(self, sect):

'''
# evaluate added value; updates av[si][ui]
# si = sect.index, ui = user_bids.index
def eval_av(si, ui):
    #BIG TODO

# evaluate change in total value if user si
# trades si_old for si_new
def eval_trade(si_old, si_new, ui):
    #big TODO
'''

ub = []  # global list of user_bids
r = []  # global list of lists of USchedOpts result;
        # each row is one schedule
        # each schedule is a list of USchedOpts indexed by user_bids.index
        # r[schedoption][user] is one USchedOpt 
av = []  # global matrix of added value for sections: [sect.index][user.index] = added value
s = []  # global list of sects; each sect's index 
        # MUST line up with the bids in each UBids.sect_bids
semester = 'Fa2019'
non_participants = ['tchertea', 'lehavisa']

def load_sects(semester):
    global s
    sects = Section.query.filter_by(semester=semester).order_by(Section.choice_num).all()
    #s_length = max([j.choice_num for j in sects + 1])
    s = []
    i = 0
    skip = False
    for x in sects:
        for np in non_participants:
            if x.taken_by.lower().strip()[0:5] == np[0:5]:
                skip = True
        if skip:
            skip = False
            continue
        t = Sect(choice=x.choice_num, course=x.course, start=x.start_time,
                 end=x.end_time, MW=x.mon_wed, TTh=x.tue_thu, MTWTh=x.mtwth,
                 taken_by=x.taken_by, units=x.units, room=x.room)
        t.index = i
        i += 1
        s.append(t)

# load round 1 user bids from db into ub
# assuming non_participants don't have bids in db and 
# there are no bids on non_participant's classes!
def load_ub(semester):
    global ub
    ub = []
    bids = UserBids.query.filter_by(primary=True).all()
    i = 0
    # length of sect_bids
    sb_length = max([s.choice_num for s in Section.query.filter_by(
        semester=semester).all()]) + 1
    for b in bids:
        if b.primary:
            t = UBids(user=b.user_id, semester=semester, timestamp=b.timestamp)
            t.index = i
            i += 1
            t.bid_1_prep = b.bid_1_prep
            t.bid_2_prep = b.bid_2_prep
            t.bid_3_prep = b.bid_3_prep
            t.bid_4_prep = b.bid_4_prep
            t.bid_5_prep = b.bid_5_prep
            t.min_acc_units = b.min_acc_units
            t.max_acc_units = b.max_acc_units
            t.min_des_units = b.min_des_units
            t.max_des_units = b.max_des_units
            sbs = SectionBid.query.filter_by(user_bids_id=b.id).all()
            t.sect_bids = [None for j in range(sb_length)]
            for sb in sbs:
                choice_num = Section.query.filter_by(id=sb.section_id).first().choice_num
                t.sect_bids[choice_num] = sb.bid
            # remove all Nones from list; should be in same order as s now
            t.sect_bids = [x for x in t.sect_bids if x is not None]
            ub.append(t)

def test_db_load():
    for b in ub:
        print(b)
        print(len(b.sect_bids),len(s))
        user_name = User.query.filter_by(id=b.user).first().username
        db_ub_id = UserBids.query.filter_by(user_id=b.user, primary=True).first().id
        sbs = SectionBid.query.filter_by(user_bids_id=db_ub_id).all()
        for i in range(len(b.sect_bids)):
            choice_num = s[i].choice
            sect_id = Section.query.filter_by(choice_num=choice_num).first().id
            db_bid = SectionBid.query.filter_by(section_id=sect_id, user_bids_id=db_ub_id).first().bid
            if db_bid != b.sect_bids[i]:
                print('Error! DB bid doesn\'t line up with ub bid!\
                      User: {}, sect index: {}, Choice: {}, DB Bid: {}, \
                      b.sect_bid: {}'.format(user_name, i, choice_num,
                      db_bid, b.sect_bids[i]))

def remove_bids_on_non_participants_sections():
    count = 0
    for sec in Section.query.all():
        for np in non_participants:
            if sec.taken_by.lower().strip()[0:5] == np[0:5]:
                deletos = SectionBid.query.filter_by(section_id=sec.id).all()
                for d in deletos:
                    db.session.delete(d)
                    count += 1
    print('removed ', count, ' section bids!')
    db.session.commit()

#remove_bids_on_non_participants_sections()
load_ub('Fa2019')
load_sects('Fa2019')
test_db_load()


############################################
# code to populate r for first round:
############################################
''' load_ub, load_sects
get order from orderer.py
for each row in order:
    forward = true #make this false when going backwards in list
    done = false
    r.append([USchedOpt(i) for i in row])
    while not done:'''
        




############################################
#Code below inputs sample schedule into database!
############################################
'''sample_file = open('sample_schedule.csv')
reader = csv.reader(sample_file)
sem = 'Fa2019'
sect_list = []

for row in reader:
    MW = row[4] == 'MW'
    TTh = row[4] == 'TTh'
    MTWTh = row[4] == 'MTWTh'
    sect_list.append(sect(choice=int(row[0]), course=row[1],
                          start=datetime.datetime.time(datetime.datetime.strptime(row[2], '%I:%M %p')),
                          end=datetime.datetime.time(datetime.datetime.strptime(row[3], '%I:%M %p')),
                          MW=MW, TTh=TTh, MTWTh=MTWTh, taken_by=row[5],
                          units=int(row[6]), room=row[7]))
for sec in sect_list:
    print(sec.choice, sec.course, 
          sec.start.strftime('%I:%M %p'),
          sec.end.strftime('%I:%M %p'),
          #datetime.time.strftime('%I:%M %p', sec.start),
          #datetime.time.strftime('%I:%M %p', sec.end),
          sec.MW, sec.TTh, sec.MTWTh, sec.taken_by, sec.units, sec.room)

for sec in sect_list:
    s = Section(choice_num=sec.choice, start_time=sec.start, end_time=sec.end,
                mon_wed=sec.MW, tue_thu=sec.TTh, mtwth=sec.MTWTh,
                course=sec.course, room=sec.room, units=sec.units,
                semester=sem, taken_by=sec.taken_by)
    db.session.add(s)
db.session.commit()'''

#############################################
# Code below inputs test_r1_bids into database!
############################################
'''from test_r1_bids import b  # list of user_bids
for u in b:
    user_ref = User.query.filter_by(username=u.user).first()
    ub = UserBids(bidder=user_ref, primary=True, timestamp=u.timestamp,
        bid_1_prep=u.bid_1_prep, bid_2_prep=u.bid_2_prep,
        bid_3_prep=u.bid_3_prep, bid_4_prep=u.bid_4_prep, bid_5_prep=u.bid_5_prep,
        min_acc_units=u.min_acc_units, max_acc_units=u.max_acc_units,
        min_des_units=u.min_des_units, max_des_units=u.max_des_units)
    db.session.add(ub)
db.session.commit()'''

'''for u in b:
    print(u.user,u.bid_3_prep,len(u.sect_bids))
    user_id = User.query.filter_by(username=u.user).first().id
    print('user_id: ', user_id)
    ub_ref = UserBids.query.filter_by(user_id=user_id,primary=True).first()
    print('ub_ref: ', ub_ref)
    for x in u.sect_bids:
        sect_ref = Section.query.filter_by(choice_num=x[0]).first()
        #print('sect_ref: ', sect_ref, ' bid: ', x[1])
        sb = SectionBid(bid=x[1], from_userbids=ub_ref, sect=sect_ref)
        db.session.add(sb)
db.session.commit()'''


