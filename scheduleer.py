'''
END OF SUMMER NOTES:

-Big Problem: currently, it produces just 20 schedules for 20 different orders, and they are often fairly similar. This will make too few schedules for round 2 bidding, possibly leaving someone with only schedules they didn't really want. Some ways to fix this:
    - Make more schedules, about 2 more for each user, where that user picks their entire schedule first before doing a lottery with everyone else.
    - Make more schedules, where half of the people randomly pick twice in a row. Or maybe just completely random order and not lottery-style back and forth.
    - During lottery rounds, when picking the maximum-new-value section, pick randomly from the list of ties for max-nv, instead of just picking the first one.
    - Do more rounds of trading, where you occasionally randomly allow for some zero-value trades.

-Assigning bids is trickier than I thought for users. I ended up with a 7:00 PM class because the sect_bid wasn't negative enough for to overcome my preps_bid. Users should be advised that: 
    - They will definitely get some sections they bid high on. Note that that gives all sections of those courses automatic bonuses according to their preps_bid.
    - After they have their 2 favorites, simulate some third options, assuming their favorites are gone. Does the total  bids line up in the order that they want them?

-TODO:
    - Finish testing correctness of want_tables
    - Make database models for round 1 results
    - Make database models for round 2 bids and round 2 results
    - Write back-end code for round 2 bidding and testing
    - The whole dang front end
'''

from app import app, db
from app.models import User, Post, Section, SectionBid, UserBids
import csv
import datetime
import test_user_data
from copy import deepcopy
from orderer import orderer
import cycler
from config import semester, non_participants, knocking_adj_penalty
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,
            'Section': Section, 'SectionBid': SectionBid,
            'UserBids': UserBids}


class Sect:
    def __init__(self, choice, course, start, end,
                 MW, TTh, MTWTh, taken_by, units, room):
        self.choice = choice  # eg, 1 or 127
        self.index = 0  # index in nv, user_bids.sect_bids MUST BE SET
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
        self.index = 0  # index in ub, nv MUST BE SET
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
        #line1 = 'user: {} index: {} semester: {} timestamp: {}\n'.format(self.user, 
        #    self.index, self.semester, self.timestamp)
        #line2 = 'preps: 1:{} 2:{} 3:{} 4:{} 5:{} min_acc_units: {}'.format()
        return('user: {} index: {} semester: {} timestamp: {} \n'
               'preps: 1:{} 2:{} 3:{} 4:{} 5:{} min_acc_units: {} '
               'min_des_units: {} max_des_units: {} max_acc_units: {}'.format(
                    self.user, self.index, self.semester, self.timestamp,
                    self.bid_1_prep, self.bid_2_prep, self.bid_3_prep,
                    self.bid_4_prep, self.bid_5_prep, self.min_acc_units,
                    self.min_des_units, self.max_des_units,
                    self.max_acc_units))


class USchedOpt:
    # List of sections chosen so far for one user
    def __init__(self, index):
        self.unit_total = 0
        self.sects_bid = 0
        self.units_bid = 0
        self.preps_bid = 0
        self.total_bid = 0  # simply total of sects, units, preps
        self.knocking_adj_penalty = 0  # unnecessary? might want to keep track
        self.s = []  # list of section indices (si)
        self.courses  = []  # len(self.courses) is number of preps
        self.index = index  # self's index in r; matches ub
        self.done = False

    def __repr__(self):
        sects = ''
        for si in self.s:
            sects += str(s[si].course) + ' at ' + s[si].start.strftime('%I:%M %p')+' choice: '+str(s[si].choice)+\
                ' index: ' + str(si) + '\n'
        user_name = User.query.filter_by(id=ub[self.index].user).first().username
        return('{} sects_bid: {} units: {} units_bid: {} preps_bid: {} total_bid: {}\n{}'.format(
            user_name, self.sects_bid, self.unit_total, self.units_bid, self.preps_bid, self.total_bid, sects))

    def add(self, si):
        self.unit_total += s[si].units
        if self.unit_total >= ub[self.index].min_des_units and self.unit_total <= ub[self.index].max_des_units:
            self.units_bid = 4
        else:
            self.units_bid = 0
        self.sects_bid += ub[self.index].sect_bids[s[si].index]
        if s[si].taken_by is not '':
            self.knocking_adj_penalty += knocking_adj_penalty
        if s[si].course not in self.courses:
            self.courses.append(s[si].course)
            if len(self.courses) == 1:
                self.preps_bid = ub[self.index].bid_1_prep
            elif len(self.courses) == 2:
                self.preps_bid = ub[self.index].bid_2_prep
            elif len(self.courses) == 3:
                self.preps_bid = ub[self.index].bid_3_prep
            elif len(self.courses) == 4:
                self.preps_bid = ub[self.index].bid_4_prep
            elif len(self.courses) == 5:
                self.preps_bid = ub[self.index].bid_5_prep
        self.total_bid = self.units_bid + self.sects_bid + self.preps_bid
        self.s.append(si)

    def remove(self, si):
        self.unit_total -= s[si].units
        if ( self.unit_total >= ub[self.index].min_des_units and
             self.unit_total <= ub[self.index].max_des_units ):
            self.units_bid = 4
        else:
            self.units_bid = 0
        self.sects_bid -= ub[self.index].sect_bids[s[si].index]
        if s[si].taken_by is not '':
            self.knocking_adj_penalty -= knocking_adj_penalty
        self.courses = []
        i = 0
        while i < len(self.s):
            if self.s[i] == si:
                self.s.pop(i)   # remove it
            elif s[self.s[i]].course not in self.courses:
                self.courses.append(s[self.s[i]].course)
            i += 1
        if len(self.courses) == 1:
            self.preps_bid = ub[self.index].bid_1_prep
        elif len(self.courses) == 2:
            self.preps_bid = ub[self.index].bid_2_prep
        elif len(self.courses) == 3:
            self.preps_bid = ub[self.index].bid_3_prep
        elif len(self.courses) == 4:
            self.preps_bid = ub[self.index].bid_4_prep
        elif len(self.courses) == 5:
            self.preps_bid = ub[self.index].bid_5_prep
        self.total_bid = self.units_bid + self.sects_bid + self.preps_bid

    # returns new value after s[si] is added,
    # or None if new units > max_acc_units or if schedule conflict
    def eval_if_added(self, si):
        new_units = self.unit_total + s[si].units
        if new_units > ub[self.index].max_acc_units:
            return None
        if s[si].MTWTh:
            for my_si in self.s:
                if ( (s[my_si].start <= s[si].start <= s[my_si].end) or
                     (s[my_si].start <= s[si].end <= s[my_si].end) ):
                    return None
        elif s[si].MW:
            for my_si in self.s:
                if s[my_si].MW or s[my_si].MTWTh:
                    if ( (s[my_si].start <= s[si].start <= s[my_si].end) or
                         (s[my_si].start <= s[si].end <= s[my_si].end) ):
                        return None
        elif s[si].TTh:
            for my_si in self.s:
                if s[my_si].TTh or s[my_si].MTWTh:
                    if ( (s[my_si].start <= s[si].start <= s[my_si].end) or
                         (s[my_si].start <= s[si].end <= s[my_si].end) ):
                        return None
        if ( new_units >= ub[self.index].min_des_units and 
             new_units <= ub[self.index].max_des_units ):
            new_tot = 4
        else:
            new_tot = 0
        new_tot += ub[self.index].sect_bids[si]  # additional sect bid
        if s[si].taken_by is not '':
            new_tot -= knocking_adj_penalty
        new_tot += self.sects_bid  # old sects_bid
        if s[si].course in self.courses:
            new_tot += self.preps_bid # preps_bid is unchanged
        else:
            preps = len(self.courses) + 1
            if preps == 1:
                new_tot += ub[self.index].bid_1_prep
            elif preps == 2:
                new_tot += ub[self.index].bid_2_prep
            elif preps == 3:
                new_tot += ub[self.index].bid_3_prep
            elif preps == 4:
                new_tot += ub[self.index].bid_4_prep
            elif preps == 5:
                new_tot += ub[self.index].bid_5_prep
        return new_tot

    # returns change in total value if user
    # trades si_old for si_new, or None if too many units or schedule conflict
    def eval_trade(self, si_old, si_new):
        new_units = self.unit_total - s[si_old].units + s[si_new].units
        if new_units > ub[self.index].max_acc_units:
            return None
        if s[si_new].MTWTh:
            for my_si in self.s:
                if s[my_si].index != si_old:
                    if ( (s[my_si].start <= s[si_new].start <= s[my_si].end) or
                         (s[my_si].start <= s[si_new].end <= s[my_si].end) ):
                        return None
        elif s[si_new].MW:
            for my_si in self.s:
                if s[my_si].index != si_old:
                    if s[my_si].MW or s[my_si].MTWTh:
                        if ( (s[my_si].start <= s[si_new].start <= s[my_si].end) or
                             (s[my_si].start <= s[si_new].end <= s[my_si].end) ):
                            return None
        elif s[si_new].TTh:
            for my_si in self.s:
                if s[my_si].index != si_old:
                    if s[my_si].TTh or s[my_si].MTWTh:
                        if ( (s[my_si].start <= s[si_new].start <= s[my_si].end) or
                             (s[my_si].start <= s[si_new].end <= s[my_si].end) ):
                            return None
        if ( new_units >= ub[self.index].min_des_units and
             new_units <= ub[self.index].max_des_units ):
            new_tot = 4
        else:
            new_tot = 0
        new_tot += self.sects_bid - ub[self.index].sect_bids[si_old] + ub[self.index].sect_bids[si_new]
        if s[si_new].taken_by is not '':
            new_tot -= knocking_adj_penalty
        if s[si_old].taken_by is not '':
            new_tot += knocking_adj_penalty
        new_courses = [s[si_new].course]
        for my_si in self.s:
            if s[my_si].index != si_old and s[my_si].course not in new_courses:
                new_courses.append(s[my_si].course)
        if len(new_courses) == 1:
            new_tot += ub[self.index].bid_1_prep
        elif len(new_courses) == 2:
            new_tot += ub[self.index].bid_2_prep
        elif len(new_courses) == 3:
            new_tot += ub[self.index].bid_3_prep
        elif len(new_courses) == 4:
            new_tot += ub[self.index].bid_4_prep
        elif len(new_courses) == 5:
            new_tot += ub[self.index].bid_5_prep
        return new_tot - self.total_bid



def load_sects(semester):
    global s
    sects = Section.query.filter_by(semester=semester).order_by(Section.choice_num).all()
    # s_length = max([j.choice_num for j in sects + 1])
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
                 taken_by=x.taken_by.strip(), units=x.units, room=x.room)
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

# r is a schedule, ie a list of USchedOpts
# returns the USchedOpt.index (user index in r, ub) of the owner of s[si]
# returns None if it's unclaimed, and -1 if it's taken by adjunct
def find_owner(r, si):
    for u in r:
        if si in u.s:
            return u.index
    if s[si].taken_by is not '':
        return -1
    return None


ub = []  # global list of user_bids
results = []  # global list of lists of USchedOpts result;
        # each row is one schedule
        # each schedule is a list of USchedOpts indexed by user_bids.index
        # results[schedoption][user] is one USchedOpt 
#r = []  # current USchedOpts for putting in results; indexed like ub
nv = []  # nv[sect.index][user.index] = new value after adding sect
s = []  # global list of sects; each sect's index 
        # MUST line up with the bids in each UBids.sect_bids


load_ub(semester)
load_sects(semester)
test_db_load()
order = orderer(len(ub))
for o in order:
    o.extend(o[::-1])   # adds a reversed copy of o to o
    o.extend(o)         # doubles o
    o.extend(o)         # again
    o.extend(o)         # again; o is long enough for 16 choices

adjuncts_knocked = 0  # for testing

for o in order:
    done = 0  # count of USchedOpts in r that are done
    nv = [[None for b in ub] for sect in s]
    r = [USchedOpt(i) for i in range(len(ub))]
    for m in range(len(s)):
        for n in range(len(ub)):
            nv[m][n] = r[n].eval_if_added(m)
    for i in o:  # for each faculty in order, get sect with max new value
        if not r[i].done:
            if r[i].unit_total < ub[i].min_acc_units:
                mode = 0  # definitely add a class!
            elif r[i].unit_total < ub[i].min_des_units:
                mode = 1  # only add a class if it increases value
            elif r[i].unit_total <= ub[i].max_des_units:
                mode = 2  # only add a class if it increases value by more than 1?
            all_nv_are_none = True
            max_nv = -20
            for m in range(len(s)):  # get sect w/ maximum new value
                if nv[m][i] is not None:
                    all_nv_are_none = False
                    if nv[m][i] > max_nv:
                        if ( mode == 0 or (mode == 1 and nv[m][i] > r[i].total_bid) or
                             (mode == 2 and nv[m][i] > (r[i].total_bid + 1)) ):
                            max_nv = nv[m][i]
                            max_sec = m
            if all_nv_are_none or max_nv == -20:
                # there is no section that can legally and gainfully be added
                r[i].done = True
            else:
                r[i].add(max_sec)
                if s[max_sec].taken_by is not '':
                    adjuncts_knocked += 1
                for n in range(len(ub)):
                    nv[max_sec][n] = None
                for m in range(len(s)):
                    if nv[m][i] is not None:  # only eval legal sects
                        nv[m][i] = r[i].eval_if_added(m)
            if r[i].done:
                done += 1
        if done == len(r):
            break
    results.append(r)

totals = [0 for i in range(len(results))]
for i in range(len(results)):
    for j in range(len(results[i])):
        totals[i] += results[i][j].total_bid
    totals[i] = totals[i]/len(results[i])
sumi = 0
for i in totals:
    sumi += i
print('Averages of each schedule: ', totals)
print('Average pre-trade bid in schedules: ', str(sumi/len(totals)))
print('Average number of adjuncts knocked: ', str(adjuncts_knocked/len(results)))

test_results_strs = []
for i in range(len(results[13])):
    test_results_strs.append(str(results[13][i]))

for z in range(1):
    wtables = []  # list of want tables, one for each r in results. Each want table is
                  # a list, indexed like s, of wants. Each want
                  # is a list of tuples, (wanted sect, how much it's wanted)
    for r in results:
        wt = [[] for m in range(len(s))]
        claimed = []  # list of si's claimed by non-adjunct faculty
        unclaimed = []  # list of si's claimed by noone
        adjuncts = []  # list of si's claimed by adjuncts; blocked from trades
        owners = [None for si in range(len(s))]
        for m in range(len(s)):
            owner = find_owner(r=r, si=m)
            owners[m] = owner
            if owner is None:
                unclaimed.append(m)
            elif owner == -1:
                adjuncts.append(m)
            else:
                claimed.append(m)
        for m in range(len(s)):
            if owners[m] is None:  # un-owned classes can be traded, w/ 0 AV to non-owner
                for c in claimed:
                    wt[m].append((c, 0))
            elif owners[m] != -1:  # si[m] is claimed; find and sort trades
                for n in range(len(s)):
                    if owners[n] != -1:  # no offers for adjuncts' classes
                        av = r[owners[m]].eval_trade(si_old=m, si_new=n)
                        if av is not None:
                            if av >= 0:
                                wt[m].append((n, av))
                for x in range(len(wt[m])):  # selection sort
                    index_of_max = x
                    for y in range(x + 1, len(wt[m])):
                        if wt[m][y][1] > wt[m][x][1]:
                            index_of_max = y
                    temp = wt[m][x]
                    wt[m][x] = wt[m][index_of_max]
                    wt[m][index_of_max] = temp
        wtables.append(wt)
        disjoint_sets = cycler.cycler(wt)
        max_improvement = 0
        max_index = None
        for ds in range(len(disjoint_sets)):  # TODO: move this code into cycler for abstraction
            improvement = 0
            for cyc in disjoint_sets[ds]:
                improvement += cyc.value
            if improvement > max_improvement:
                max_improvement = improvement
                max_index = ds
        if max_index is not None:
            for cyc in disjoint_sets[max_index]:
                if owners[cyc.end.data] is not None:
                    r[owners[cyc.end.data]].add(cyc.start.data)
                    r[owners[cyc.end.data]].remove(cyc.end.data)
                current = cyc.end
                # give end's owner section owned by start
                while current.prev_node is not None:  # while current != start
                    # give current.prev's owner current's section
                    if owners[current.prev_node.data] is not None:
                        r[owners[current.prev_node.data]].add(current.data)
                        r[owners[current.prev_node.data]].remove(current.prev_node.data)
                    current = current.prev_node
    totals = [0 for i in range(len(results))]
    for i in range(len(results)):
        for j in range(len(results[i])):
            totals[i] += results[i][j].total_bid
        totals[i] = totals[i]/len(results[i])
    sumi = 0
    for i in totals:
        sumi += i
    print('Averages of each schedule: ', totals)
    print('Average bid after trading {} time in schedules: '.format(z+1), str(sumi/len(totals)))

#TESTING TRADES
# Note this test doesn't work! it prints the POST-TRADE wants instead of pre-trade wants.
# Fix later by making separate results list to compare before/after
test_wt_strs = ['' for m in range(len(results[13]))]
for m in range(len(results[13])):
    print(ub[m])
    print(test_results_strs[m])
    for i in range(len(results[13][m].s)):
        test_wt_strs[m] += 'si ' + str(results[13][m].s[i]) + ' wants: ' + str(wtables[13][results[13][m].s[i]]) + '\n'
    print(test_wt_strs[m])
    print(results[13][m])





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


