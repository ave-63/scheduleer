from scheduleer import db, User, Post, Section, SectionBid, UserBids

sects = Section.query.all()
for s in sects:
    print(s.choice_num, s.course, s.start_time, s.end_time, s.mon_wed,
        s.tue_thu, s.mtwth, s.room, s.units, s.semester, s.taken_by)