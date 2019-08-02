from scheduleer import db, User, Post, Section, SectionBid, UserBids

'''test_users = [('smithbt', 'smithbt@piercecollege.edu'),
              ('caincd', 'caincd@piercecollege.edu'),
              ('martinje', 'martinje@piercecollege.edu'),
              ('chowsz', 'chowsz@piercecollege.edu'),
              ('putnamtc', 'putnamtc@piercecollege.edu'),
              ('navabm', 'navabm@piercecollege.edu'),
              ('lehavisa', 'lehavisa@piercecollege.edu'),
              ('rashidmm', 'rashidmm@piercecollege.edu'),
              ('tabataz', 'tabataz@piercecollege.edu'),
              ('forkeoaa', 'forkeoaa@piercecollege.edu'),
              ('johnsotm', 'johnsotm@piercecollege.edu'),
              ('tchertea', 'tchertea@piercecollege.edu'),
              ('lamd', 'lamd@piercecollege.edu'),
              ('furmulr', 'furmulr@piercecollege.edu'),
              ('phamp', 'phamp@piercecollege.edu'),
              ('pearsasa', 'pearsasa@piercecollege.edu'),
              ('pumarmd', 'pumarmd@piercecollege.edu'),
              ('schweshr', 'schweshr@piercecollege.edu'),
              ('sotode2', 'sotode2@piercecollege.edu'),
              ('khasane', 'khasane@piercecollege.edu'),
              ('semerdy', 'semerdy@piercecollege.edu')
              ('veigajr', 'veigajr@piercecollege.edu')
              ]

for row in test_users:
    db.session.add(Userdb(username=row[0], email=row[1]))
db.session.commit()'''

# db.session.add(Userdb(username='veigajr', email='veigajr@piercecollege.edu'))

users = User.query.all()
for u in users:
    print(u.id, u.username, u.email)