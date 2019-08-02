import datetime
from scheduleer import UBids

b = []
b.append(UBids(user='smithbt', semester='Fa2019', timestamp=datetime.datetime.now()))
b[0].bid_1_prep = 4
b[0].bid_2_prep = 5
b[0].bid_3_prep = 0
b[0].bid_4_prep = -2
b[0].bid_5_prep = -5
b[0].min_acc_units = 13
b[0].max_acc_units = 17
b[0].min_des_units = 14
b[0].max_des_units = 16
b[0].sect_bids.append((1, -5))  # 110 8:00 am MTWTh adj
b[0].sect_bids.append((2, -5))  # 110 9:35 am MTWTh adj 
b[0].sect_bids.append((3, -5))  # 110 4:10 PM MW adj
b[0].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[0].sect_bids.append((5, -5))  # 110 8:00 AM MTWTh adj
b[0].sect_bids.append((6, 0))  # 115 8:00 AM MTWTh 
b[0].sect_bids.append((7, 0))  # 115 11:10 AM MTWTh
b[0].sect_bids.append((8, 0))  # 115 12:45 PM MW
b[0].sect_bids.append((9, 0))  # 115 12:45 PM TTh
b[0].sect_bids.append((10, -5))  # 115 4:10 PM TTh
b[0].sect_bids.append((11, -5))  # 134 8:00 AM MTWTh LEHAVI
b[0].sect_bids.append((12, 3))  # 134 8:00 AM MTWTh
b[0].sect_bids.append((13, 3))  # 134 8:00 AM MTWTh
b[0].sect_bids.append((14, 4))  # 134 9:35 AM MTWTh
b[0].sect_bids.append((15, 4))  # 134 9:35 AM MTWTh
b[0].sect_bids.append((16, 4))  # 134 11:10 AM MTWTh
b[0].sect_bids.append((17, -5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[0].sect_bids.append((18, -2)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[0].sect_bids.append((19, -2)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[0].sect_bids.append((20, 1))  # 134 12:45 PM 3:55 PM MW 
b[0].sect_bids.append((21, -4))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[0].sect_bids.append((22, 2))  # 134 3:30 PM 6:40 PM MW Le 
b[0].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[0].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[0].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[0].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[0].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[0].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[0].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[0].sect_bids.append((30, 1))  # 227 8:00 AM 8:50 AM MTWTh
b[0].sect_bids.append((31, 1))  # 227 8:00 AM 10:05 AM MW
b[0].sect_bids.append((32, 1))  # 227 8:00 AM 10:05 AM TTh
b[0].sect_bids.append((33, 1))  # 227 9:35 AM 10:25 AM MTWTh
b[0].sect_bids.append((34, 1))  # 227 9:35 AM 11:40 AM MW 
b[0].sect_bids.append((35, -5))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[0].sect_bids.append((36, 1))  # 227 10:10 AM 11:00 AM MTWTh
b[0].sect_bids.append((37, 1))  # 227 10:10 AM 11:00 AM MTWTh
b[0].sect_bids.append((38, 1))  # 227 10:30 AM 12:35 PM MW 
b[0].sect_bids.append((39, 1))  # 227 10:30 AM 12:35 PM TTh
b[0].sect_bids.append((40, 1))  # 227 11:10 AM 1:15 PM MW
b[0].sect_bids.append((41, 1))  # 227 11:10 AM 1:15 PM TTh
b[0].sect_bids.append((42, 1))  # 227 11:45 AM 12:35 PM MTWTh
b[0].sect_bids.append((43, 1))  # 227 11:45 AM 12:35 PM MTWTh
b[0].sect_bids.append((44, 1))  # 227 12:45 PM 2:50 PM MW
b[0].sect_bids.append((45, 1))  # 227 12:45 PM 2:50 PM MW
b[0].sect_bids.append((46, 1))  # 227 12:45 PM 2:50 PM TTh
b[0].sect_bids.append((47, -2)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[0].sect_bids.append((48, -2))  # 227 4:35 PM 6:40 PM MW
b[0].sect_bids.append((49, -2))  # 227 4:35 PM 6:40 PM TTh
b[0].sect_bids.append((50, -2))  # 227 7:00 PM 9:05 PM MW
b[0].sect_bids.append((51, -4))  # 227 7:00 PM 9:05 PM MW
b[0].sect_bids.append((52, -4))  # 227 7:00 PM 9:05 PM TTh
b[0].sect_bids.append((53, -4))  # 227 7:00 PM 9:05 PM TTh
b[0].sect_bids.append((54, -1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[0].sect_bids.append((55, -1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[0].sect_bids.append((56, 1))  # 228A 8:00 AM 9:10 AM MTWTh
b[0].sect_bids.append((57, 1))  # 228A 12:45 PM 3:15 PM MW
b[0].sect_bids.append((58, 1))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[0].sect_bids.append((59, 1))  # 228A 7:00 PM 9:30 PM MW
b[0].sect_bids.append((60, 1))  # 228A 7:00 PM 9:30 PM TTh 
b[0].sect_bids.append((61, 1))  # 228B 8:00 AM 9:10 AM MTWTh
b[0].sect_bids.append((62, 1))  # 228B 12:45 PM 3:15 PM MW 
b[0].sect_bids.append((63, 1))  # 228B 4:10 PM 6:40 PM MW
b[0].sect_bids.append((64, 1))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[0].sect_bids.append((65, -2))  # 238 8:00 AM 9:10 AM MTWTh
b[0].sect_bids.append((66, -2))  # 238 9:35 AM 10:45 AM MTWTh
b[0].sect_bids.append((67, -2))  # 238 11:10 AM 12:20 PM MTWTh
b[0].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[0].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[0].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[0].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[0].sect_bids.append((72, 1))  # 240 8:00 AM 9:25 AM MW
b[0].sect_bids.append((73, 1))  # 240 8:00 AM 9:25 AM TTh
b[0].sect_bids.append((74, 2))  # 240 9:35 AM 11:00 AM MW
b[0].sect_bids.append((75, 2))  # 240 9:35 AM 11:00 AM TTh
b[0].sect_bids.append((76, 2))  # 240 11:10 AM 12:35 PM MW 
b[0].sect_bids.append((77, 2))  # 240 11:10 AM 12:35 PM TTh 
b[0].sect_bids.append((78, 2))  # 240 12:45 PM 2:10 PM MW
b[0].sect_bids.append((79, 2))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[0].sect_bids.append((80, 2))  # 240 12:45 PM 2:10 PM MW
b[0].sect_bids.append((81, 0))  # 240 3:40 PM 5:05 PM TTh
b[0].sect_bids.append((82, 0))  # 240 3:40 PM 5:05 PM MW
b[0].sect_bids.append((83, 0))  # 240 5:15 PM 6:40 PM TTh
b[0].sect_bids.append((84, 0))  # 240 5:15 PM 6:40 PM MW Harandian
b[0].sect_bids.append((85, 0))  # 240 7:00 PM 8:25 PM MW
b[0].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[0].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[0].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[0].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[0].sect_bids.append((90, 3))  # 260 8:00 AM 9:10 AM MTWTh
b[0].sect_bids.append((91, 3))  # 260 9:35 AM 10:45 AM MTWTh
b[0].sect_bids.append((92, 3))  # 260 11:10 AM 12:20 PM MTWTh
b[0].sect_bids.append((93, 3))  # 260 12:45 PM 1:55 PM MTWTh
b[0].sect_bids.append((94, 3))  # 260 12:45 PM 3:15 PM MW
b[0].sect_bids.append((95, 2))  # 260 2:25 PM 3:35 PM MTWTh
b[0].sect_bids.append((96, 2))  # 260 2:25 PM 3:35 PM MTWTh
b[0].sect_bids.append((97, 0))  # 260 4:10 PM 6:40 PM MW
b[0].sect_bids.append((98, 0))  # 260 4:10 PM 6:40 PM TTh
b[0].sect_bids.append((99, -2))  # 260 7:00 PM 9:30 PM MW
b[0].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[0].sect_bids.append((101, 4))  # 261 8:00 AM 9:10 AM MTWTh
b[0].sect_bids.append((102, 4))  # 261 8:00 AM 9:10 AM MTWTh
b[0].sect_bids.append((103, 4))  # 261 9:35 AM 10:45 AM MTWTh
b[0].sect_bids.append((104, 4))  # 261 9:35 AM 10:45 AM MTWTh
b[0].sect_bids.append((105, 4))  # 261 11:10 AM 12:20 PM MTWTh
b[0].sect_bids.append((106, 3))  # 261 12:45 PM 3:15 PM MW
b[0].sect_bids.append((107, 3))  # 261 2:25 PM 3:35 PM MTWTh
b[0].sect_bids.append((108, 1))  # 261 4:10 PM 6:40 PM MW Martinez
b[0].sect_bids.append((109, 0))  # 261 4:10 PM 6:40 PM TTh
b[0].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[0].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[0].sect_bids.append((112, 1))  # 262 8:00 AM 9:10 AM MTWTh
b[0].sect_bids.append((113, 1))  # 262 9:35 AM 10:45 AM MTWTh
b[0].sect_bids.append((114, 1))  # 262 11:10 AM 12:20 PM MTWTh
b[0].sect_bids.append((115, 1))  # 262 11:10 AM 12:20 PM MTWTh
b[0].sect_bids.append((116, -2))  # 262 4:10 PM 6:40 PM TTh
b[0].sect_bids.append((117, -2))  # 262 7:00 PM 9:30 PM MW
b[0].sect_bids.append((118, -2))  # 262 7:00 PM 9:30 PM TTh
b[0].sect_bids.append((119, 4))  # 263 8:00 AM 9:10 AM MTWTh
b[0].sect_bids.append((120, 4))  # 263 9:35 AM 10:45 AM MTWTh
b[0].sect_bids.append((121, 4))  # 263 11:10 AM 12:20 PM MTWT
b[0].sect_bids.append((122, -2))  # 263 7:00 PM 9:30 PM TTh
b[0].sect_bids.append((123, 4))  # 270 8:00 AM 9:25 AM MW
b[0].sect_bids.append((124, 4))  # 270 12:45 PM 2:10 PM MW
b[0].sect_bids.append((125, -2))  # 270 5:15 PM 6:40 PM TTh
b[0].sect_bids.append((126, -2))  # 275 9:35 AM 11:00 AM TTh
b[0].sect_bids.append((127, -2))  # 275 3:40 PM 5:05 PM MW

b.append(UBids(user='caincd', semester='Fa2019', timestamp=datetime.datetime.now()))
b[1].bid_1_prep = 4
b[1].bid_2_prep = 5
b[1].bid_3_prep = 0
b[1].bid_4_prep = -2
b[1].bid_5_prep = -5
b[1].min_acc_units = 13
b[1].max_acc_units = 17
b[1].min_des_units = 14
b[1].max_des_units = 16
b[1].sect_bids.append((1, -2))  # 110 8:00 am MTWTh adj
b[1].sect_bids.append((2, -2))  # 110 9:35 am MTWTh adj 
b[1].sect_bids.append((3, -2))  # 110 4:10 PM MW adj
b[1].sect_bids.append((4, -2))  # 110 7:00 PM TTh
b[1].sect_bids.append((5, -2))  # 110 8:00 AM MTWTh adj
b[1].sect_bids.append((6, 3))  # 115 8:00 AM MTWTh 
b[1].sect_bids.append((7, 3))  # 115 11:10 AM MTWTh
b[1].sect_bids.append((8, 3))  # 115 12:45 PM MW
b[1].sect_bids.append((9, 3))  # 115 12:45 PM TTh
b[1].sect_bids.append((10, 1))  # 115 4:10 PM TTh
b[1].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[1].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[1].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[1].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[1].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[1].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[1].sect_bids.append((17, -2)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[1].sect_bids.append((18, -2)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[1].sect_bids.append((19, -2)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[1].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[1].sect_bids.append((21, -2))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[1].sect_bids.append((22, -2))  # 134 3:30 PM 6:40 PM MW Le 
b[1].sect_bids.append((23, -2))  # 134 6:50 PM 10:00 PM MW Grigoryan 
b[1].sect_bids.append((24, -2))  # 134 6:50 PM 10:00 PM MW
b[1].sect_bids.append((25, -2))  # 134 6:50 PM 10:00 PM TTh 
b[1].sect_bids.append((26, -2))  # 134 6:50 PM 10:00 PM TTh
b[1].sect_bids.append((27, -2))  # 215 5:15 PM 6:40 PM MW
b[1].sect_bids.append((28, -2))  # 215 3:40 PM 5:05 PM TTh 
b[1].sect_bids.append((29, -3))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[1].sect_bids.append((30, -1))  # 227 8:00 AM 8:50 AM MTWTh
b[1].sect_bids.append((31, -1))  # 227 8:00 AM 10:05 AM MW
b[1].sect_bids.append((32, -1))  # 227 8:00 AM 10:05 AM TTh
b[1].sect_bids.append((33, -1))  # 227 9:35 AM 10:25 AM MTWTh
b[1].sect_bids.append((34, -1))  # 227 9:35 AM 11:40 AM MW 
b[1].sect_bids.append((35, -1))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[1].sect_bids.append((36, -1))  # 227 10:10 AM 11:00 AM MTWTh
b[1].sect_bids.append((37, -1))  # 227 10:10 AM 11:00 AM MTWTh
b[1].sect_bids.append((38, -1))  # 227 10:30 AM 12:35 PM MW 
b[1].sect_bids.append((39, -1))  # 227 10:30 AM 12:35 PM TTh
b[1].sect_bids.append((40, -1))  # 227 11:10 AM 1:15 PM MW
b[1].sect_bids.append((41, -1))  # 227 11:10 AM 1:15 PM TTh
b[1].sect_bids.append((42, -1))  # 227 11:45 AM 12:35 PM MTWTh
b[1].sect_bids.append((43, -1))  # 227 11:45 AM 12:35 PM MTWTh
b[1].sect_bids.append((44, -1))  # 227 12:45 PM 2:50 PM MW
b[1].sect_bids.append((45, -1))  # 227 12:45 PM 2:50 PM MW
b[1].sect_bids.append((46, -1))  # 227 12:45 PM 2:50 PM TTh
b[1].sect_bids.append((47, -1)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[1].sect_bids.append((48, -4))  # 227 4:35 PM 6:40 PM MW
b[1].sect_bids.append((49, -4))  # 227 4:35 PM 6:40 PM TTh
b[1].sect_bids.append((50, -4))  # 227 7:00 PM 9:05 PM MW
b[1].sect_bids.append((51, -4))  # 227 7:00 PM 9:05 PM MW
b[1].sect_bids.append((52, -4))  # 227 7:00 PM 9:05 PM TTh
b[1].sect_bids.append((53, -4))  # 227 7:00 PM 9:05 PM TTh
b[1].sect_bids.append((54, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[1].sect_bids.append((55, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[1].sect_bids.append((56, 1))  # 228A 8:00 AM 9:10 AM MTWTh
b[1].sect_bids.append((57, 1))  # 228A 12:45 PM 3:15 PM MW
b[1].sect_bids.append((58, 1))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[1].sect_bids.append((59, 1))  # 228A 7:00 PM 9:30 PM MW
b[1].sect_bids.append((60, 1))  # 228A 7:00 PM 9:30 PM TTh 
b[1].sect_bids.append((61, 1))  # 228B 8:00 AM 9:10 AM MTWTh
b[1].sect_bids.append((62, 1))  # 228B 12:45 PM 3:15 PM MW 
b[1].sect_bids.append((63, 1))  # 228B 4:10 PM 6:40 PM MW
b[1].sect_bids.append((64, 1))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[1].sect_bids.append((65, 3))  # 238 8:00 AM 9:10 AM MTWTh
b[1].sect_bids.append((66, 3))  # 238 9:35 AM 10:45 AM MTWTh
b[1].sect_bids.append((67, 3))  # 238 11:10 AM 12:20 PM MTWTh
b[1].sect_bids.append((68, 3))  # 238 4:10 PM 6:40 PM MW 
b[1].sect_bids.append((69, 3))  # 238 4:10 PM 6:40 PM TTh
b[1].sect_bids.append((70, 0))  # 238 7:00 PM 9:30 PM MW
b[1].sect_bids.append((71, 0))  # 238 7:00 PM 9:30 PM TTh New
b[1].sect_bids.append((72, -2))  # 240 8:00 AM 9:25 AM MW
b[1].sect_bids.append((73, -1))  # 240 8:00 AM 9:25 AM TTh
b[1].sect_bids.append((74, -1))  # 240 9:35 AM 11:00 AM MW
b[1].sect_bids.append((75, -1))  # 240 9:35 AM 11:00 AM TTh
b[1].sect_bids.append((76, -1))  # 240 11:10 AM 12:35 PM MW 
b[1].sect_bids.append((77, -1))  # 240 11:10 AM 12:35 PM TTh 
b[1].sect_bids.append((78, -1))  # 240 12:45 PM 2:10 PM MW
b[1].sect_bids.append((79, -1))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[1].sect_bids.append((80, -1))  # 240 12:45 PM 2:10 PM MW
b[1].sect_bids.append((81, -1))  # 240 3:40 PM 5:05 PM TTh
b[1].sect_bids.append((82, -1))  # 240 3:40 PM 5:05 PM MW
b[1].sect_bids.append((83, -1))  # 240 5:15 PM 6:40 PM TTh
b[1].sect_bids.append((84, -1))  # 240 5:15 PM 6:40 PM MW Harandian
b[1].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[1].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[1].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[1].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[1].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[1].sect_bids.append((90, 0))  # 260 8:00 AM 9:10 AM MTWTh
b[1].sect_bids.append((91, 0))  # 260 9:35 AM 10:45 AM MTWTh
b[1].sect_bids.append((92, 0))  # 260 11:10 AM 12:20 PM MTWTh
b[1].sect_bids.append((93, 0))  # 260 12:45 PM 1:55 PM MTWTh
b[1].sect_bids.append((94, 0))  # 260 12:45 PM 3:15 PM MW
b[1].sect_bids.append((95, 0))  # 260 2:25 PM 3:35 PM MTWTh
b[1].sect_bids.append((96, 0))  # 260 2:25 PM 3:35 PM MTWTh
b[1].sect_bids.append((97, -5))  # 260 4:10 PM 6:40 PM MW
b[1].sect_bids.append((98, -5))  # 260 4:10 PM 6:40 PM TTh
b[1].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[1].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[1].sect_bids.append((101, 4))  # 261 8:00 AM 9:10 AM MTWTh
b[1].sect_bids.append((102, 4))  # 261 8:00 AM 9:10 AM MTWTh
b[1].sect_bids.append((103, 4))  # 261 9:35 AM 10:45 AM MTWTh
b[1].sect_bids.append((104, 4))  # 261 9:35 AM 10:45 AM MTWTh
b[1].sect_bids.append((105, 4))  # 261 11:10 AM 12:20 PM MTWTh
b[1].sect_bids.append((106, 4))  # 261 12:45 PM 3:15 PM MW
b[1].sect_bids.append((107, 4))  # 261 2:25 PM 3:35 PM MTWTh
b[1].sect_bids.append((108, -2))  # 261 4:10 PM 6:40 PM MW Martinez
b[1].sect_bids.append((109, 0))  # 261 4:10 PM 6:40 PM TTh
b[1].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[1].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[1].sect_bids.append((112, 0))  # 262 8:00 AM 9:10 AM MTWTh
b[1].sect_bids.append((113, 0))  # 262 9:35 AM 10:45 AM MTWTh
b[1].sect_bids.append((114, 0))  # 262 11:10 AM 12:20 PM MTWTh
b[1].sect_bids.append((115, 0))  # 262 11:10 AM 12:20 PM MTWTh
b[1].sect_bids.append((116, 0))  # 262 4:10 PM 6:40 PM TTh
b[1].sect_bids.append((117, -2))  # 262 7:00 PM 9:30 PM MW
b[1].sect_bids.append((118, -2))  # 262 7:00 PM 9:30 PM TTh
b[1].sect_bids.append((119, -1))  # 263 8:00 AM 9:10 AM MTWTh
b[1].sect_bids.append((120, -1))  # 263 9:35 AM 10:45 AM MTWTh
b[1].sect_bids.append((121, -1))  # 263 11:10 AM 12:20 PM MTWT
b[1].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[1].sect_bids.append((123, -1))  # 270 8:00 AM 9:25 AM MW
b[1].sect_bids.append((124, -1))  # 270 12:45 PM 2:10 PM MW
b[1].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[1].sect_bids.append((126, -1))  # 275 9:35 AM 11:00 AM TTh
b[1].sect_bids.append((127, -3))  # 275 3:40 PM 5:05 PM MW



b.append(UBids(user='chowsz', semester='Fa2019', timestamp=datetime.datetime.now()))
b[2].bid_1_prep = 4
b[2].bid_2_prep = 5
b[2].bid_3_prep = 0
b[2].bid_4_prep = -2
b[2].bid_5_prep = -5
b[2].min_acc_units = 14
b[2].max_acc_units = 18
b[2].min_des_units = 15
b[2].max_des_units = 16
b[2].sect_bids.append((1, -4))  # 110 8:00 am MTWTh adj
b[2].sect_bids.append((2, -4))  # 110 9:35 am MTWTh adj 
b[2].sect_bids.append((3, -4))  # 110 4:10 PM MW adj
b[2].sect_bids.append((4, -4))  # 110 7:00 PM TTh
b[2].sect_bids.append((5, -4))  # 110 8:00 AM MTWTh adj
b[2].sect_bids.append((6, -4))  # 115 8:00 AM MTWTh 
b[2].sect_bids.append((7, -4))  # 115 11:10 AM MTWTh
b[2].sect_bids.append((8, -4))  # 115 12:45 PM MW
b[2].sect_bids.append((9, -4))  # 115 12:45 PM TTh
b[2].sect_bids.append((10, -4))  # 115 4:10 PM TTh
b[2].sect_bids.append((11, 1))  # 134 8:00 AM MTWTh LEHAVI
b[2].sect_bids.append((12, 1))  # 134 8:00 AM MTWTh
b[2].sect_bids.append((13, 1))  # 134 8:00 AM MTWTh
b[2].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[2].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[2].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[2].sect_bids.append((17, -2)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[2].sect_bids.append((18, -2)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[2].sect_bids.append((19, -2)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[2].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[2].sect_bids.append((21, -2))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[2].sect_bids.append((22, 5))  # 134 3:30 PM 6:40 PM MW Le 
b[2].sect_bids.append((23, 4))  # 6:50 PM 10:00 PM MW Grigoryan 
b[2].sect_bids.append((24, 4))  # 134 6:50 PM 10:00 PM MW
b[2].sect_bids.append((25, 4))  # 134 6:50 PM 10:00 PM TTh 
b[2].sect_bids.append((26, 4))  # 134 6:50 PM 10:00 PM TTh
b[2].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[2].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[2].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[2].sect_bids.append((30, -5))  # 227 8:00 AM 8:50 AM MTWTh
b[2].sect_bids.append((31, -5))  # 227 8:00 AM 10:05 AM MW
b[2].sect_bids.append((32, -5))  # 227 8:00 AM 10:05 AM TTh
b[2].sect_bids.append((33, -5))  # 227 9:35 AM 10:25 AM MTWTh
b[2].sect_bids.append((34, -5))  # 227 9:35 AM 11:40 AM MW 
b[2].sect_bids.append((35, -5))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[2].sect_bids.append((36, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[2].sect_bids.append((37, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[2].sect_bids.append((38, -5))  # 227 10:30 AM 12:35 PM MW 
b[2].sect_bids.append((39, -5))  # 227 10:30 AM 12:35 PM TTh
b[2].sect_bids.append((40, -5))  # 227 11:10 AM 1:15 PM MW
b[2].sect_bids.append((41, -5))  # 227 11:10 AM 1:15 PM TTh
b[2].sect_bids.append((42, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[2].sect_bids.append((43, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[2].sect_bids.append((44, -5))  # 227 12:45 PM 2:50 PM MW
b[2].sect_bids.append((45, -5))  # 227 12:45 PM 2:50 PM MW
b[2].sect_bids.append((46, -5))  # 227 12:45 PM 2:50 PM TTh
b[2].sect_bids.append((47, -5)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[2].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[2].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[2].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[2].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[2].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[2].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[2].sect_bids.append((54, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[2].sect_bids.append((55, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[2].sect_bids.append((56, -5))  # 228A 8:00 AM 9:10 AM MTWTh
b[2].sect_bids.append((57, -5))  # 228A 12:45 PM 3:15 PM MW
b[2].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[2].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[2].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[2].sect_bids.append((61, -5))  # 228B 8:00 AM 9:10 AM MTWTh
b[2].sect_bids.append((62, -5))  # 228B 12:45 PM 3:15 PM MW 
b[2].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[2].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[2].sect_bids.append((65, -5))  # 238 8:00 AM 9:10 AM MTWTh
b[2].sect_bids.append((66, -5))  # 238 9:35 AM 10:45 AM MTWTh
b[2].sect_bids.append((67, -5))  # 238 11:10 AM 12:20 PM MTWTh
b[2].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[2].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[2].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[2].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[2].sect_bids.append((72, -5))  # 240 8:00 AM 9:25 AM MW
b[2].sect_bids.append((73, -5))  # 240 8:00 AM 9:25 AM TTh
b[2].sect_bids.append((74, 1))  # 240 9:35 AM 11:00 AM MW
b[2].sect_bids.append((75, 1))  # 240 9:35 AM 11:00 AM TTh
b[2].sect_bids.append((76, 1))  # 240 11:10 AM 12:35 PM MW 
b[2].sect_bids.append((77, 1))  # 240 11:10 AM 12:35 PM TTh 
b[2].sect_bids.append((78, 1))  # 240 12:45 PM 2:10 PM MW
b[2].sect_bids.append((79, 1))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[2].sect_bids.append((80, 1))  # 240 12:45 PM 2:10 PM MW
b[2].sect_bids.append((81, 1))  # 240 3:40 PM 5:05 PM TTh
b[2].sect_bids.append((82, 1))  # 240 3:40 PM 5:05 PM MW
b[2].sect_bids.append((83, 1))  # 240 5:15 PM 6:40 PM TTh
b[2].sect_bids.append((84, 1))  # 240 5:15 PM 6:40 PM MW Harandian
b[2].sect_bids.append((85, 1))  # 240 7:00 PM 8:25 PM MW
b[2].sect_bids.append((86, 1))  # 240 7:00 PM 8:25 PM TTh
b[2].sect_bids.append((87, 1))  # 240 7:00 PM 8:25 PM TTh
b[2].sect_bids.append((88, 1))  # 240 8:35 PM 10:00 PM MW 
b[2].sect_bids.append((89, 1))  # 240 8:35 PM 10:00 PM TTh 
b[2].sect_bids.append((90, -3))  # 260 8:00 AM 9:10 AM MTWTh
b[2].sect_bids.append((91, 1))  # 260 9:35 AM 10:45 AM MTWTh
b[2].sect_bids.append((92, 1))  # 260 11:10 AM 12:20 PM MTWTh
b[2].sect_bids.append((93, 1))  # 260 12:45 PM 1:55 PM MTWTh
b[2].sect_bids.append((94, 1))  # 260 12:45 PM 3:15 PM MW
b[2].sect_bids.append((95, 1))  # 260 2:25 PM 3:35 PM MTWTh
b[2].sect_bids.append((96, 1))  # 260 2:25 PM 3:35 PM MTWTh
b[2].sect_bids.append((97, 1))  # 260 4:10 PM 6:40 PM MW
b[2].sect_bids.append((98, 1))  # 260 4:10 PM 6:40 PM TTh
b[2].sect_bids.append((99, 1))  # 260 7:00 PM 9:30 PM MW
b[2].sect_bids.append((100, 1))  # 260 7:00 PM 9:30 PM TTh
b[2].sect_bids.append((101, -2))  # 261 8:00 AM 9:10 AM MTWTh
b[2].sect_bids.append((102, -2))  # 261 8:00 AM 9:10 AM MTWTh
b[2].sect_bids.append((103, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[2].sect_bids.append((104, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[2].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[2].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[2].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[2].sect_bids.append((108, -2))  # 261 4:10 PM 6:40 PM MW Martinez
b[2].sect_bids.append((109, 5))  # 261 4:10 PM 6:40 PM TTh
b[2].sect_bids.append((110, -2))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[2].sect_bids.append((111, -2))  # 261 7:00 PM 9:30 PM TTh Lin
b[2].sect_bids.append((112, -1))  # 262 8:00 AM 9:10 AM MTWTh
b[2].sect_bids.append((113, 5))  # 262 9:35 AM 10:45 AM MTWTh
b[2].sect_bids.append((114, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[2].sect_bids.append((115, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[2].sect_bids.append((116, 5))  # 262 4:10 PM 6:40 PM TTh
b[2].sect_bids.append((117, 5))  # 262 7:00 PM 9:30 PM MW
b[2].sect_bids.append((118, 5))  # 262 7:00 PM 9:30 PM TTh
b[2].sect_bids.append((119, -2))  # 263 8:00 AM 9:10 AM MTWTh
b[2].sect_bids.append((120, 2))  # 263 9:35 AM 10:45 AM MTWTh
b[2].sect_bids.append((121, 2))  # 263 11:10 AM 12:20 PM MTWT
b[2].sect_bids.append((122, 2))  # 263 7:00 PM 9:30 PM TTh
b[2].sect_bids.append((123, -2))  # 270 8:00 AM 9:25 AM MW
b[2].sect_bids.append((124, -2))  # 270 12:45 PM 2:10 PM MW
b[2].sect_bids.append((125, -2))  # 270 5:15 PM 6:40 PM TTh
b[2].sect_bids.append((126, -2))  # 275 9:35 AM 11:00 AM TTh
b[2].sect_bids.append((127, -2))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='furmulr', semester='Fa2019', timestamp=datetime.datetime.now()))
b[3].bid_1_prep = 4
b[3].bid_2_prep = 5
b[3].bid_3_prep = 0
b[3].bid_4_prep = -2
b[3].bid_5_prep = -5
b[3].min_acc_units = 13
b[3].max_acc_units = 17
b[3].min_des_units = 14
b[3].max_des_units = 16
b[3].sect_bids.append((1, -5))  # 110 8:00 am MTWTh adj
b[3].sect_bids.append((2, -3))  # 110 9:35 am MTWTh adj 
b[3].sect_bids.append((3, 1))  # 110 4:10 PM MW adj
b[3].sect_bids.append((4, 1))  # 110 7:00 PM TTh
b[3].sect_bids.append((5, 1))  # 110 8:00 AM MTWTh adj
b[3].sect_bids.append((6, 1))  # 115 8:00 AM MTWTh 
b[3].sect_bids.append((7, 3))  # 115 11:10 AM MTWTh
b[3].sect_bids.append((8, 3))  # 115 12:45 PM MW
b[3].sect_bids.append((9, 3))  # 115 12:45 PM TTh
b[3].sect_bids.append((10, 3))  # 115 4:10 PM TTh
b[3].sect_bids.append((11, -5))  # 134 8:00 AM MTWTh LEHAVI
b[3].sect_bids.append((12, -5))  # 134 8:00 AM MTWTh
b[3].sect_bids.append((13, -5))  # 134 8:00 AM MTWTh
b[3].sect_bids.append((14, -2))  # 134 9:35 AM MTWTh
b[3].sect_bids.append((15, -2))  # 134 9:35 AM MTWTh
b[3].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[3].sect_bids.append((17, -1)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[3].sect_bids.append((18, -1)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[3].sect_bids.append((19, -1)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[3].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[3].sect_bids.append((21, 3))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[3].sect_bids.append((22, 3))  # 134 3:30 PM 6:40 PM MW Le 
b[3].sect_bids.append((23, 3))  # 6:50 PM 10:00 PM MW Grigoryan 
b[3].sect_bids.append((24, 1))  # 134 6:50 PM 10:00 PM MW
b[3].sect_bids.append((25, 1))  # 134 6:50 PM 10:00 PM TTh 
b[3].sect_bids.append((26, 1))  # 134 6:50 PM 10:00 PM TTh
b[3].sect_bids.append((27, 0))  # 215 5:15 PM 6:40 PM MW
b[3].sect_bids.append((28, 0))  # 215 3:40 PM 5:05 PM TTh 
b[3].sect_bids.append((29, -3))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[3].sect_bids.append((30, -3))  # 227 8:00 AM 8:50 AM MTWTh
b[3].sect_bids.append((31, -2))  # 227 8:00 AM 10:05 AM MW
b[3].sect_bids.append((32, -2))  # 227 8:00 AM 10:05 AM TTh
b[3].sect_bids.append((33, -2))  # 227 9:35 AM 10:25 AM MTWTh
b[3].sect_bids.append((34, -2))  # 227 9:35 AM 11:40 AM MW 
b[3].sect_bids.append((35, -2))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[3].sect_bids.append((36, -2))  # 227 10:10 AM 11:00 AM MTWTh
b[3].sect_bids.append((37, -2))  # 227 10:10 AM 11:00 AM MTWTh
b[3].sect_bids.append((38, -2))  # 227 10:30 AM 12:35 PM MW 
b[3].sect_bids.append((39, -2))  # 227 10:30 AM 12:35 PM TTh
b[3].sect_bids.append((40, -2))  # 227 11:10 AM 1:15 PM MW
b[3].sect_bids.append((41, -2))  # 227 11:10 AM 1:15 PM TTh
b[3].sect_bids.append((42, -2))  # 227 11:45 AM 12:35 PM MTWTh
b[3].sect_bids.append((43, -2))  # 227 11:45 AM 12:35 PM MTWTh
b[3].sect_bids.append((44, -2))  # 227 12:45 PM 2:50 PM MW
b[3].sect_bids.append((45, -2))  # 227 12:45 PM 2:50 PM MW
b[3].sect_bids.append((46, -2))  # 227 12:45 PM 2:50 PM TTh
b[3].sect_bids.append((47, -2)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[3].sect_bids.append((48, -2))  # 227 4:35 PM 6:40 PM MW
b[3].sect_bids.append((49, -2))  # 227 4:35 PM 6:40 PM TTh
b[3].sect_bids.append((50, -2))  # 227 7:00 PM 9:05 PM MW
b[3].sect_bids.append((51, -2))  # 227 7:00 PM 9:05 PM MW
b[3].sect_bids.append((52, -2))  # 227 7:00 PM 9:05 PM TTh
b[3].sect_bids.append((53, -2))  # 227 7:00 PM 9:05 PM TTh
b[3].sect_bids.append((54, -2))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[3].sect_bids.append((55, -2))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[3].sect_bids.append((56, -2))  # 228A 8:00 AM 9:10 AM MTWTh
b[3].sect_bids.append((57, -2))  # 228A 12:45 PM 3:15 PM MW
b[3].sect_bids.append((58, -2))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[3].sect_bids.append((59, -2))  # 228A 7:00 PM 9:30 PM MW
b[3].sect_bids.append((60, -2))  # 228A 7:00 PM 9:30 PM TTh 
b[3].sect_bids.append((61, -2))  # 228B 8:00 AM 9:10 AM MTWTh
b[3].sect_bids.append((62, -2))  # 228B 12:45 PM 3:15 PM MW 
b[3].sect_bids.append((63, -2))  # 228B 4:10 PM 6:40 PM MW
b[3].sect_bids.append((64, -2))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[3].sect_bids.append((65, -2))  # 238 8:00 AM 9:10 AM MTWTh
b[3].sect_bids.append((66, -2))  # 238 9:35 AM 10:45 AM MTWTh
b[3].sect_bids.append((67, -2))  # 238 11:10 AM 12:20 PM MTWTh
b[3].sect_bids.append((68, -2))  # 238 4:10 PM 6:40 PM MW 
b[3].sect_bids.append((69, -2))  # 238 4:10 PM 6:40 PM TTh
b[3].sect_bids.append((70, -2))  # 238 7:00 PM 9:30 PM MW
b[3].sect_bids.append((71, -2))  # 238 7:00 PM 9:30 PM TTh New
b[3].sect_bids.append((72, -5))  # 240 8:00 AM 9:25 AM MW
b[3].sect_bids.append((73, -5))  # 240 8:00 AM 9:25 AM TTh
b[3].sect_bids.append((74, -3))  # 240 9:35 AM 11:00 AM MW
b[3].sect_bids.append((75, -3))  # 240 9:35 AM 11:00 AM TTh
b[3].sect_bids.append((76, 1))  # 240 11:10 AM 12:35 PM MW 
b[3].sect_bids.append((77, 1))  # 240 11:10 AM 12:35 PM TTh 
b[3].sect_bids.append((78, 1))  # 240 12:45 PM 2:10 PM MW
b[3].sect_bids.append((79, 1))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[3].sect_bids.append((80, 1))  # 240 12:45 PM 2:10 PM MW
b[3].sect_bids.append((81, 1))  # 240 3:40 PM 5:05 PM TTh
b[3].sect_bids.append((82, 1))  # 240 3:40 PM 5:05 PM MW
b[3].sect_bids.append((83, 1))  # 240 5:15 PM 6:40 PM TTh
b[3].sect_bids.append((84, 1))  # 240 5:15 PM 6:40 PM MW Harandian
b[3].sect_bids.append((85, 1))  # 240 7:00 PM 8:25 PM MW
b[3].sect_bids.append((86, 1))  # 240 7:00 PM 8:25 PM TTh
b[3].sect_bids.append((87, 1))  # 240 7:00 PM 8:25 PM TTh
b[3].sect_bids.append((88, 1))  # 240 8:35 PM 10:00 PM MW 
b[3].sect_bids.append((89, 1))  # 240 8:35 PM 10:00 PM TTh 
b[3].sect_bids.append((90, -3))  # 260 8:00 AM 9:10 AM MTWTh
b[3].sect_bids.append((91, -3))  # 260 9:35 AM 10:45 AM MTWTh
b[3].sect_bids.append((92, 1))  # 260 11:10 AM 12:20 PM MTWTh
b[3].sect_bids.append((93, 1))  # 260 12:45 PM 1:55 PM MTWTh
b[3].sect_bids.append((94, 1))  # 260 12:45 PM 3:15 PM MW
b[3].sect_bids.append((95, 1))  # 260 2:25 PM 3:35 PM MTWTh
b[3].sect_bids.append((96, 1))  # 260 2:25 PM 3:35 PM MTWTh
b[3].sect_bids.append((97, 1))  # 260 4:10 PM 6:40 PM MW
b[3].sect_bids.append((98, 1))  # 260 4:10 PM 6:40 PM TTh
b[3].sect_bids.append((99, -1))  # 260 7:00 PM 9:30 PM MW
b[3].sect_bids.append((100, -1))  # 260 7:00 PM 9:30 PM TTh
b[3].sect_bids.append((101, -3))  # 261 8:00 AM 9:10 AM MTWTh
b[3].sect_bids.append((102, -3))  # 261 8:00 AM 9:10 AM MTWTh
b[3].sect_bids.append((103, 0))  # 261 9:35 AM 10:45 AM MTWTh
b[3].sect_bids.append((104, 0))  # 261 9:35 AM 10:45 AM MTWTh
b[3].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[3].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[3].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[3].sect_bids.append((108, 5))  # 261 4:10 PM 6:40 PM MW Martinez
b[3].sect_bids.append((109, 5))  # 261 4:10 PM 6:40 PM TTh
b[3].sect_bids.append((110, 1))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[3].sect_bids.append((111, 1))  # 261 7:00 PM 9:30 PM TTh Lin
b[3].sect_bids.append((112, -5))  # 262 8:00 AM 9:10 AM MTWTh
b[3].sect_bids.append((113, -3))  # 262 9:35 AM 10:45 AM MTWTh
b[3].sect_bids.append((114, 3))  # 262 11:10 AM 12:20 PM MTWTh
b[3].sect_bids.append((115, 3))  # 262 11:10 AM 12:20 PM MTWTh
b[3].sect_bids.append((116, 3))  # 262 4:10 PM 6:40 PM TTh
b[3].sect_bids.append((117, 0))  # 262 7:00 PM 9:30 PM MW
b[3].sect_bids.append((118, 0))  # 262 7:00 PM 9:30 PM TTh
b[3].sect_bids.append((119, -3))  # 263 8:00 AM 9:10 AM MTWTh
b[3].sect_bids.append((120, -3))  # 263 9:35 AM 10:45 AM MTWTh
b[3].sect_bids.append((121, 5))  # 263 11:10 AM 12:20 PM MTWT
b[3].sect_bids.append((122, 3))  # 263 7:00 PM 9:30 PM TTh
b[3].sect_bids.append((123, -4))  # 270 8:00 AM 9:25 AM MW
b[3].sect_bids.append((124, -4))  # 270 12:45 PM 2:10 PM MW
b[3].sect_bids.append((125, -4))  # 270 5:15 PM 6:40 PM TTh
b[3].sect_bids.append((126, -4))  # 275 9:35 AM 11:00 AM TTh
b[3].sect_bids.append((127, -4))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='forkeoaa', semester='Fa2019', timestamp=datetime.datetime.now()))
b[4].bid_1_prep = 4
b[4].bid_2_prep = 5
b[4].bid_3_prep = 0
b[4].bid_4_prep = -2
b[4].bid_5_prep = -5
b[4].min_acc_units = 13
b[4].max_acc_units = 17
b[4].min_des_units = 14
b[4].max_des_units = 16
b[4].sect_bids.append((1, -3))  # 110 8:00 am MTWTh adj
b[4].sect_bids.append((2, -3))  # 110 9:35 am MTWTh adj 
b[4].sect_bids.append((3, 1))  # 110 4:10 PM MW adj
b[4].sect_bids.append((4, 1))  # 110 7:00 PM TTh
b[4].sect_bids.append((5, 0))  # 110 8:00 AM MTWTh adj
b[4].sect_bids.append((6, -3))  # 115 8:00 AM MTWTh 
b[4].sect_bids.append((7, 1))  # 115 11:10 AM MTWTh
b[4].sect_bids.append((8, 1))  # 115 12:45 PM MW
b[4].sect_bids.append((9, 1))  # 115 12:45 PM TTh
b[4].sect_bids.append((10, 1))  # 115 4:10 PM TTh
b[4].sect_bids.append((11, -4))  # 134 8:00 AM MTWTh LEHAVI
b[4].sect_bids.append((12, -4))  # 134 8:00 AM MTWTh
b[4].sect_bids.append((13, -2))  # 134 8:00 AM MTWTh
b[4].sect_bids.append((14, -2))  # 134 9:35 AM MTWTh
b[4].sect_bids.append((15, -2))  # 134 9:35 AM MTWTh
b[4].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[4].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[4].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[4].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[4].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[4].sect_bids.append((21, 5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[4].sect_bids.append((22, 5))  # 134 3:30 PM 6:40 PM MW Le 
b[4].sect_bids.append((23, 5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[4].sect_bids.append((24, 5))  # 134 6:50 PM 10:00 PM MW
b[4].sect_bids.append((25, 5))  # 134 6:50 PM 10:00 PM TTh 
b[4].sect_bids.append((26, 5))  # 134 6:50 PM 10:00 PM TTh
b[4].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[4].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[4].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[4].sect_bids.append((30, -5))  # 227 8:00 AM 8:50 AM MTWTh
b[4].sect_bids.append((31, -5))  # 227 8:00 AM 10:05 AM MW
b[4].sect_bids.append((32, -5))  # 227 8:00 AM 10:05 AM TTh
b[4].sect_bids.append((33, -5))  # 227 9:35 AM 10:25 AM MTWTh
b[4].sect_bids.append((34, -5))  # 227 9:35 AM 11:40 AM MW 
b[4].sect_bids.append((35, -5))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[4].sect_bids.append((36, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[4].sect_bids.append((37, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[4].sect_bids.append((38, -5))  # 227 10:30 AM 12:35 PM MW 
b[4].sect_bids.append((39, -5))  # 227 10:30 AM 12:35 PM TTh
b[4].sect_bids.append((40, -5))  # 227 11:10 AM 1:15 PM MW
b[4].sect_bids.append((41, -5))  # 227 11:10 AM 1:15 PM TTh
b[4].sect_bids.append((42, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[4].sect_bids.append((43, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[4].sect_bids.append((44, -5))  # 227 12:45 PM 2:50 PM MW
b[4].sect_bids.append((45, -5))  # 227 12:45 PM 2:50 PM MW
b[4].sect_bids.append((46, -5))  # 227 12:45 PM 2:50 PM TTh
b[4].sect_bids.append((47, -5)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[4].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[4].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[4].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[4].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[4].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[4].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[4].sect_bids.append((54, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[4].sect_bids.append((55, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[4].sect_bids.append((56, -5))  # 228A 8:00 AM 9:10 AM MTWTh
b[4].sect_bids.append((57, -5))  # 228A 12:45 PM 3:15 PM MW
b[4].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[4].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[4].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[4].sect_bids.append((61, -5))  # 228B 8:00 AM 9:10 AM MTWTh
b[4].sect_bids.append((62, -5))  # 228B 12:45 PM 3:15 PM MW 
b[4].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[4].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[4].sect_bids.append((65, -3))  # 238 8:00 AM 9:10 AM MTWTh
b[4].sect_bids.append((66, -3))  # 238 9:35 AM 10:45 AM MTWTh
b[4].sect_bids.append((67, 5))  # 238 11:10 AM 12:20 PM MTWTh
b[4].sect_bids.append((68, 5))  # 238 4:10 PM 6:40 PM MW 
b[4].sect_bids.append((69, 5))  # 238 4:10 PM 6:40 PM TTh
b[4].sect_bids.append((70, 5))  # 238 7:00 PM 9:30 PM MW
b[4].sect_bids.append((71, 5))  # 238 7:00 PM 9:30 PM TTh New
b[4].sect_bids.append((72, -5))  # 240 8:00 AM 9:25 AM MW
b[4].sect_bids.append((73, -5))  # 240 8:00 AM 9:25 AM TTh
b[4].sect_bids.append((74, -5))  # 240 9:35 AM 11:00 AM MW
b[4].sect_bids.append((75, -5))  # 240 9:35 AM 11:00 AM TTh
b[4].sect_bids.append((76, 0))  # 240 11:10 AM 12:35 PM MW 
b[4].sect_bids.append((77, 0))  # 240 11:10 AM 12:35 PM TTh 
b[4].sect_bids.append((78, 0))  # 240 12:45 PM 2:10 PM MW
b[4].sect_bids.append((79, 0))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[4].sect_bids.append((80, 0))  # 240 12:45 PM 2:10 PM MW
b[4].sect_bids.append((81, 0))  # 240 3:40 PM 5:05 PM TTh
b[4].sect_bids.append((82, 0))  # 240 3:40 PM 5:05 PM MW
b[4].sect_bids.append((83, 0))  # 240 5:15 PM 6:40 PM TTh
b[4].sect_bids.append((84, 0))  # 240 5:15 PM 6:40 PM MW Harandian
b[4].sect_bids.append((85, 0))  # 240 7:00 PM 8:25 PM MW
b[4].sect_bids.append((86, 0))  # 240 7:00 PM 8:25 PM TTh
b[4].sect_bids.append((87, 0))  # 240 7:00 PM 8:25 PM TTh
b[4].sect_bids.append((88, 0))  # 240 8:35 PM 10:00 PM MW 
b[4].sect_bids.append((89, 0))  # 240 8:35 PM 10:00 PM TTh 
b[4].sect_bids.append((90, -5))  # 260 8:00 AM 9:10 AM MTWTh
b[4].sect_bids.append((91, -5))  # 260 9:35 AM 10:45 AM MTWTh
b[4].sect_bids.append((92, 4))  # 260 11:10 AM 12:20 PM MTWTh
b[4].sect_bids.append((93, 4))  # 260 12:45 PM 1:55 PM MTWTh
b[4].sect_bids.append((94, 4))  # 260 12:45 PM 3:15 PM MW
b[4].sect_bids.append((95, 4))  # 260 2:25 PM 3:35 PM MTWTh
b[4].sect_bids.append((96, 4))  # 260 2:25 PM 3:35 PM MTWTh
b[4].sect_bids.append((97, 4))  # 260 4:10 PM 6:40 PM MW
b[4].sect_bids.append((98, 4))  # 260 4:10 PM 6:40 PM TTh
b[4].sect_bids.append((99, 4))  # 260 7:00 PM 9:30 PM MW
b[4].sect_bids.append((100, 4))  # 260 7:00 PM 9:30 PM TTh
b[4].sect_bids.append((101, -2))  # 261 8:00 AM 9:10 AM MTWTh
b[4].sect_bids.append((102, -2))  # 261 8:00 AM 9:10 AM MTWTh
b[4].sect_bids.append((103, -2))  # 261 9:35 AM 10:45 AM MTWTh
b[4].sect_bids.append((104, -2))  # 261 9:35 AM 10:45 AM MTWTh
b[4].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[4].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[4].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[4].sect_bids.append((108, 5))  # 261 4:10 PM 6:40 PM MW Martinez
b[4].sect_bids.append((109, 5))  # 261 4:10 PM 6:40 PM TTh
b[4].sect_bids.append((110, 5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[4].sect_bids.append((111, 5))  # 261 7:00 PM 9:30 PM TTh Lin
b[4].sect_bids.append((112, -5))  # 262 8:00 AM 9:10 AM MTWTh
b[4].sect_bids.append((113, -5))  # 262 9:35 AM 10:45 AM MTWTh
b[4].sect_bids.append((114, 2))  # 262 11:10 AM 12:20 PM MTWTh
b[4].sect_bids.append((115, 2))  # 262 11:10 AM 12:20 PM MTWTh
b[4].sect_bids.append((116, 2))  # 262 4:10 PM 6:40 PM TTh
b[4].sect_bids.append((117, 2))  # 262 7:00 PM 9:30 PM MW
b[4].sect_bids.append((118, 2))  # 262 7:00 PM 9:30 PM TTh
b[4].sect_bids.append((119, -5))  # 263 8:00 AM 9:10 AM MTWTh
b[4].sect_bids.append((120, -5))  # 263 9:35 AM 10:45 AM MTWTh
b[4].sect_bids.append((121, 2))  # 263 11:10 AM 12:20 PM MTWT
b[4].sect_bids.append((122, 2))  # 263 7:00 PM 9:30 PM TTh
b[4].sect_bids.append((123, -5))  # 270 8:00 AM 9:25 AM MW
b[4].sect_bids.append((124, -5))  # 270 12:45 PM 2:10 PM MW
b[4].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[4].sect_bids.append((126, -5))  # 275 9:35 AM 11:00 AM TTh
b[4].sect_bids.append((127, -5))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='johnsotm', semester='Fa2019', timestamp=datetime.datetime.now()))
b[5].bid_1_prep = 4
b[5].bid_2_prep = 5
b[5].bid_3_prep = 0
b[5].bid_4_prep = -2
b[5].bid_5_prep = -5
b[5].min_acc_units = 14
b[5].max_acc_units = 17
b[5].min_des_units = 15
b[5].max_des_units = 16
b[5].sect_bids.append((1, 1))  # 110 8:00 am MTWTh adj
b[5].sect_bids.append((2, 1))  # 110 9:35 am MTWTh adj 
b[5].sect_bids.append((3, 1))  # 110 4:10 PM MW adj
b[5].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[5].sect_bids.append((5, 1))  # 110 8:00 AM MTWTh adj
b[5].sect_bids.append((6, 4))  # 115 8:00 AM MTWTh 
b[5].sect_bids.append((7, 4))  # 115 11:10 AM MTWTh
b[5].sect_bids.append((8, 4))  # 115 12:45 PM MW
b[5].sect_bids.append((9, 4))  # 115 12:45 PM TTh
b[5].sect_bids.append((10, 4))  # 115 4:10 PM TTh
b[5].sect_bids.append((11, 1))  # 134 8:00 AM MTWTh LEHAVI
b[5].sect_bids.append((12, 1))  # 134 8:00 AM MTWTh
b[5].sect_bids.append((13, 1))  # 134 8:00 AM MTWTh
b[5].sect_bids.append((14, 1))  # 134 9:35 AM MTWTh
b[5].sect_bids.append((15, 1))  # 134 9:35 AM MTWTh
b[5].sect_bids.append((16, 1))  # 134 11:10 AM MTWTh
b[5].sect_bids.append((17, 1)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[5].sect_bids.append((18, 1)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[5].sect_bids.append((19, 1)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[5].sect_bids.append((20, 1))  # 134 12:45 PM 3:55 PM MW 
b[5].sect_bids.append((21, 1))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[5].sect_bids.append((22, 1))  # 134 3:30 PM 6:40 PM MW Le 
b[5].sect_bids.append((23, 1))  # 6:50 PM 10:00 PM MW Grigoryan 
b[5].sect_bids.append((24, -4))  # 134 6:50 PM 10:00 PM MW
b[5].sect_bids.append((25, -4))  # 134 6:50 PM 10:00 PM TTh 
b[5].sect_bids.append((26, -4))  # 134 6:50 PM 10:00 PM TTh
b[5].sect_bids.append((27, 2))  # 215 5:15 PM 6:40 PM MW
b[5].sect_bids.append((28, 2))  # 215 3:40 PM 5:05 PM TTh 
b[5].sect_bids.append((29, -2))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[5].sect_bids.append((30, 1))  # 227 8:00 AM 8:50 AM MTWTh
b[5].sect_bids.append((31, 1))  # 227 8:00 AM 10:05 AM MW
b[5].sect_bids.append((32, 1))  # 227 8:00 AM 10:05 AM TTh
b[5].sect_bids.append((33, 1))  # 227 9:35 AM 10:25 AM MTWTh
b[5].sect_bids.append((34, 1))  # 227 9:35 AM 11:40 AM MW 
b[5].sect_bids.append((35, 1))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[5].sect_bids.append((36, 1))  # 227 10:10 AM 11:00 AM MTWTh
b[5].sect_bids.append((37, 1))  # 227 10:10 AM 11:00 AM MTWTh
b[5].sect_bids.append((38, 1))  # 227 10:30 AM 12:35 PM MW 
b[5].sect_bids.append((39, 1))  # 227 10:30 AM 12:35 PM TTh
b[5].sect_bids.append((40, 1))  # 227 11:10 AM 1:15 PM MW
b[5].sect_bids.append((41, 1))  # 227 11:10 AM 1:15 PM TTh
b[5].sect_bids.append((42, 1))  # 227 11:45 AM 12:35 PM MTWTh
b[5].sect_bids.append((43, 1))  # 227 11:45 AM 12:35 PM MTWTh
b[5].sect_bids.append((44, 1))  # 227 12:45 PM 2:50 PM MW
b[5].sect_bids.append((45, 1))  # 227 12:45 PM 2:50 PM MW
b[5].sect_bids.append((46, 1))  # 227 12:45 PM 2:50 PM TTh
b[5].sect_bids.append((47, 1)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[5].sect_bids.append((48, 1))  # 227 4:35 PM 6:40 PM MW
b[5].sect_bids.append((49, 1))  # 227 4:35 PM 6:40 PM TTh
b[5].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[5].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[5].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[5].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[5].sect_bids.append((54, 3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[5].sect_bids.append((55, 3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[5].sect_bids.append((56, 3))  # 228A 8:00 AM 9:10 AM MTWTh
b[5].sect_bids.append((57, 3))  # 228A 12:45 PM 3:15 PM MW
b[5].sect_bids.append((58, 3))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[5].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[5].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[5].sect_bids.append((61, 3))  # 228B 8:00 AM 9:10 AM MTWTh
b[5].sect_bids.append((62, 3))  # 228B 12:45 PM 3:15 PM MW 
b[5].sect_bids.append((63, 3))  # 228B 4:10 PM 6:40 PM MW
b[5].sect_bids.append((64, 3))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[5].sect_bids.append((65, -5))  # 238 8:00 AM 9:10 AM MTWTh
b[5].sect_bids.append((66, -5))  # 238 9:35 AM 10:45 AM MTWTh
b[5].sect_bids.append((67, -5))  # 238 11:10 AM 12:20 PM MTWTh
b[5].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[5].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[5].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[5].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[5].sect_bids.append((72, 2))  # 240 8:00 AM 9:25 AM MW
b[5].sect_bids.append((73, 2))  # 240 8:00 AM 9:25 AM TTh
b[5].sect_bids.append((74, 2))  # 240 9:35 AM 11:00 AM MW
b[5].sect_bids.append((75, 2))  # 240 9:35 AM 11:00 AM TTh
b[5].sect_bids.append((76, 2))  # 240 11:10 AM 12:35 PM MW 
b[5].sect_bids.append((77, 2))  # 240 11:10 AM 12:35 PM TTh 
b[5].sect_bids.append((78, 2))  # 240 12:45 PM 2:10 PM MW
b[5].sect_bids.append((79, 2))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[5].sect_bids.append((80, 2))  # 240 12:45 PM 2:10 PM MW
b[5].sect_bids.append((81, 2))  # 240 3:40 PM 5:05 PM TTh
b[5].sect_bids.append((82, 2))  # 240 3:40 PM 5:05 PM MW
b[5].sect_bids.append((83, 2))  # 240 5:15 PM 6:40 PM TTh
b[5].sect_bids.append((84, 2))  # 240 5:15 PM 6:40 PM MW Harandian
b[5].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[5].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[5].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[5].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[5].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[5].sect_bids.append((90, 4))  # 260 8:00 AM 9:10 AM MTWTh
b[5].sect_bids.append((91, 4))  # 260 9:35 AM 10:45 AM MTWTh
b[5].sect_bids.append((92, 4))  # 260 11:10 AM 12:20 PM MTWTh
b[5].sect_bids.append((93, 4))  # 260 12:45 PM 1:55 PM MTWTh
b[5].sect_bids.append((94, 4))  # 260 12:45 PM 3:15 PM MW
b[5].sect_bids.append((95, 4))  # 260 2:25 PM 3:35 PM MTWTh
b[5].sect_bids.append((96, 4))  # 260 2:25 PM 3:35 PM MTWTh
b[5].sect_bids.append((97, 4))  # 260 4:10 PM 6:40 PM MW
b[5].sect_bids.append((98, 4))  # 260 4:10 PM 6:40 PM TTh
b[5].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[5].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[5].sect_bids.append((101, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[5].sect_bids.append((102, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[5].sect_bids.append((103, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[5].sect_bids.append((104, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[5].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[5].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[5].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[5].sect_bids.append((108, 5))  # 261 4:10 PM 6:40 PM MW Martinez
b[5].sect_bids.append((109, 5))  # 261 4:10 PM 6:40 PM TTh
b[5].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[5].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[5].sect_bids.append((112, 5))  # 262 8:00 AM 9:10 AM MTWTh
b[5].sect_bids.append((113, 5))  # 262 9:35 AM 10:45 AM MTWTh
b[5].sect_bids.append((114, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[5].sect_bids.append((115, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[5].sect_bids.append((116, 5))  # 262 4:10 PM 6:40 PM TTh
b[5].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[5].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[5].sect_bids.append((119, 2))  # 263 8:00 AM 9:10 AM MTWTh
b[5].sect_bids.append((120, 2))  # 263 9:35 AM 10:45 AM MTWTh
b[5].sect_bids.append((121, 2))  # 263 11:10 AM 12:20 PM MTWT
b[5].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[5].sect_bids.append((123, 1))  # 270 8:00 AM 9:25 AM MW
b[5].sect_bids.append((124, 1))  # 270 12:45 PM 2:10 PM MW
b[5].sect_bids.append((125, 1))  # 270 5:15 PM 6:40 PM TTh
b[5].sect_bids.append((126, 1))  # 275 9:35 AM 11:00 AM TTh
b[5].sect_bids.append((127, 1))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='khasane', semester='Fa2019', timestamp=datetime.datetime.now()))
b[6].bid_1_prep = 4
b[6].bid_2_prep = 5
b[6].bid_3_prep = 0
b[6].bid_4_prep = -2
b[6].bid_5_prep = -5
b[6].min_acc_units = 14
b[6].max_acc_units = 17
b[6].min_des_units = 15
b[6].max_des_units = 16
b[6].sect_bids.append((1, 0))  # 110 8:00 am MTWTh adj
b[6].sect_bids.append((2, 0))  # 110 9:35 am MTWTh adj 
b[6].sect_bids.append((3, -2))  # 110 4:10 PM MW adj
b[6].sect_bids.append((4, -2))  # 110 7:00 PM TTh
b[6].sect_bids.append((5, -2))  # 110 8:00 AM MTWTh adj
b[6].sect_bids.append((6, 4))  # 115 8:00 AM MTWTh 
b[6].sect_bids.append((7, 4))  # 115 11:10 AM MTWTh
b[6].sect_bids.append((8, 4))  # 115 12:45 PM MW
b[6].sect_bids.append((9, 4))  # 115 12:45 PM TTh
b[6].sect_bids.append((10, -5))  # 115 4:10 PM TTh
b[6].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[6].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[6].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[6].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[6].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[6].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[6].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[6].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[6].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[6].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[6].sect_bids.append((21, -5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[6].sect_bids.append((22, -5))  # 134 3:30 PM 6:40 PM MW Le 
b[6].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[6].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[6].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[6].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[6].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[6].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[6].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[6].sect_bids.append((30, 4))  # 227 8:00 AM 8:50 AM MTWTh
b[6].sect_bids.append((31, 4))  # 227 8:00 AM 10:05 AM MW
b[6].sect_bids.append((32, 4))  # 227 8:00 AM 10:05 AM TTh
b[6].sect_bids.append((33, 4))  # 227 9:35 AM 10:25 AM MTWTh
b[6].sect_bids.append((34, 4))  # 227 9:35 AM 11:40 AM MW 
b[6].sect_bids.append((35, 4))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[6].sect_bids.append((36, 4))  # 227 10:10 AM 11:00 AM MTWTh
b[6].sect_bids.append((37, 4))  # 227 10:10 AM 11:00 AM MTWTh
b[6].sect_bids.append((38, 4))  # 227 10:30 AM 12:35 PM MW 
b[6].sect_bids.append((39, 4))  # 227 10:30 AM 12:35 PM TTh
b[6].sect_bids.append((40, 4))  # 227 11:10 AM 1:15 PM MW
b[6].sect_bids.append((41, 4))  # 227 11:10 AM 1:15 PM TTh
b[6].sect_bids.append((42, 4))  # 227 11:45 AM 12:35 PM MTWTh
b[6].sect_bids.append((43, 4))  # 227 11:45 AM 12:35 PM MTWTh
b[6].sect_bids.append((44, 4))  # 227 12:45 PM 2:50 PM MW
b[6].sect_bids.append((45, 4))  # 227 12:45 PM 2:50 PM MW
b[6].sect_bids.append((46, 4))  # 227 12:45 PM 2:50 PM TTh
b[6].sect_bids.append((47, 4)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[6].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[6].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[6].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[6].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[6].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[6].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[6].sect_bids.append((54, 4))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[6].sect_bids.append((55, 4))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[6].sect_bids.append((56, 4))  # 228A 8:00 AM 9:10 AM MTWTh
b[6].sect_bids.append((57, 4))  # 228A 12:45 PM 3:15 PM MW
b[6].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[6].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[6].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[6].sect_bids.append((61, 4))  # 228B 8:00 AM 9:10 AM MTWTh
b[6].sect_bids.append((62, 4))  # 228B 12:45 PM 3:15 PM MW 
b[6].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[6].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[6].sect_bids.append((65, -2))  # 238 8:00 AM 9:10 AM MTWTh
b[6].sect_bids.append((66, -2))  # 238 9:35 AM 10:45 AM MTWTh
b[6].sect_bids.append((67, -2))  # 238 11:10 AM 12:20 PM MTWTh
b[6].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[6].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[6].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[6].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[6].sect_bids.append((72, 4))  # 240 8:00 AM 9:25 AM MW
b[6].sect_bids.append((73, 4))  # 240 8:00 AM 9:25 AM TTh
b[6].sect_bids.append((74, 4))  # 240 9:35 AM 11:00 AM MW
b[6].sect_bids.append((75, 4))  # 240 9:35 AM 11:00 AM TTh
b[6].sect_bids.append((76, 4))  # 240 11:10 AM 12:35 PM MW 
b[6].sect_bids.append((77, 4))  # 240 11:10 AM 12:35 PM TTh 
b[6].sect_bids.append((78, 4))  # 240 12:45 PM 2:10 PM MW
b[6].sect_bids.append((79, 4))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[6].sect_bids.append((80, 4))  # 240 12:45 PM 2:10 PM MW
b[6].sect_bids.append((81, -5))  # 240 3:40 PM 5:05 PM TTh
b[6].sect_bids.append((82, -5))  # 240 3:40 PM 5:05 PM MW
b[6].sect_bids.append((83, -5))  # 240 5:15 PM 6:40 PM TTh
b[6].sect_bids.append((84, -5))  # 240 5:15 PM 6:40 PM MW Harandian
b[6].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[6].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[6].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[6].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[6].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[6].sect_bids.append((90, 3))  # 260 8:00 AM 9:10 AM MTWTh
b[6].sect_bids.append((91, 3))  # 260 9:35 AM 10:45 AM MTWTh
b[6].sect_bids.append((92, 3))  # 260 11:10 AM 12:20 PM MTWTh
b[6].sect_bids.append((93, 3))  # 260 12:45 PM 1:55 PM MTWTh
b[6].sect_bids.append((94, 3))  # 260 12:45 PM 3:15 PM MW
b[6].sect_bids.append((95, 3))  # 260 2:25 PM 3:35 PM MTWTh
b[6].sect_bids.append((96, 3))  # 260 2:25 PM 3:35 PM MTWTh
b[6].sect_bids.append((97, -5))  # 260 4:10 PM 6:40 PM MW
b[6].sect_bids.append((98, -5))  # 260 4:10 PM 6:40 PM TTh
b[6].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[6].sect_bids.append((100, 0))  # 260 7:00 PM 9:30 PM TTh
b[6].sect_bids.append((101, 0))  # 261 8:00 AM 9:10 AM MTWTh
b[6].sect_bids.append((102, 0))  # 261 8:00 AM 9:10 AM MTWTh
b[6].sect_bids.append((103, 0))  # 261 9:35 AM 10:45 AM MTWTh
b[6].sect_bids.append((104, 0))  # 261 9:35 AM 10:45 AM MTWTh
b[6].sect_bids.append((105, 0))  # 261 11:10 AM 12:20 PM MTWTh
b[6].sect_bids.append((106, 0))  # 261 12:45 PM 3:15 PM MW
b[6].sect_bids.append((107, 0))  # 261 2:25 PM 3:35 PM MTWTh
b[6].sect_bids.append((108, 0))  # 261 4:10 PM 6:40 PM MW Martinez
b[6].sect_bids.append((109, 0))  # 261 4:10 PM 6:40 PM TTh
b[6].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[6].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[6].sect_bids.append((112, 0))  # 262 8:00 AM 9:10 AM MTWTh
b[6].sect_bids.append((113, 0))  # 262 9:35 AM 10:45 AM MTWTh
b[6].sect_bids.append((114, 0))  # 262 11:10 AM 12:20 PM MTWTh
b[6].sect_bids.append((115, 0))  # 262 11:10 AM 12:20 PM MTWTh
b[6].sect_bids.append((116, -5))  # 262 4:10 PM 6:40 PM TTh
b[6].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[6].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[6].sect_bids.append((119, -2))  # 263 8:00 AM 9:10 AM MTWTh
b[6].sect_bids.append((120, -2))  # 263 9:35 AM 10:45 AM MTWTh
b[6].sect_bids.append((121, -2))  # 263 11:10 AM 12:20 PM MTWT
b[6].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[6].sect_bids.append((123, -5))  # 270 8:00 AM 9:25 AM MW
b[6].sect_bids.append((124, -5))  # 270 12:45 PM 2:10 PM MW
b[6].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[6].sect_bids.append((126, -5))  # 275 9:35 AM 11:00 AM TTh
b[6].sect_bids.append((127, -5))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='lamd', semester='Fa2019', timestamp=datetime.datetime.now()))
b[7].bid_1_prep = 4
b[7].bid_2_prep = 5
b[7].bid_3_prep = 0
b[7].bid_4_prep = -2
b[7].bid_5_prep = -5
b[7].min_acc_units = 12
b[7].max_acc_units = 16
b[7].min_des_units = 14
b[7].max_des_units = 15
b[7].sect_bids.append((1, 1))  # 110 8:00 am MTWTh adj
b[7].sect_bids.append((2, 1))  # 110 9:35 am MTWTh adj 
b[7].sect_bids.append((3, 1))  # 110 4:10 PM MW adj
b[7].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[7].sect_bids.append((5, 5))  # 110 8:00 AM MTWTh adj
b[7].sect_bids.append((6, 5))  # 115 8:00 AM MTWTh 
b[7].sect_bids.append((7, 5))  # 115 11:10 AM MTWTh
b[7].sect_bids.append((8, 5))  # 115 12:45 PM MW
b[7].sect_bids.append((9, 5))  # 115 12:45 PM TTh
b[7].sect_bids.append((10, 5))  # 115 4:10 PM TTh
b[7].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[7].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[7].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[7].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[7].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[7].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[7].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[7].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[7].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[7].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[7].sect_bids.append((21, -4))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[7].sect_bids.append((22, -4))  # 134 3:30 PM 6:40 PM MW Le 
b[7].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[7].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[7].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[7].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[7].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[7].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[7].sect_bids.append((29, 5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[7].sect_bids.append((30, 5))  # 227 8:00 AM 8:50 AM MTWTh
b[7].sect_bids.append((31, 5))  # 227 8:00 AM 10:05 AM MW
b[7].sect_bids.append((32, 5))  # 227 8:00 AM 10:05 AM TTh
b[7].sect_bids.append((33, 5))  # 227 9:35 AM 10:25 AM MTWTh
b[7].sect_bids.append((34, 5))  # 227 9:35 AM 11:40 AM MW 
b[7].sect_bids.append((35, 5))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[7].sect_bids.append((36, 5))  # 227 10:10 AM 11:00 AM MTWTh
b[7].sect_bids.append((37, 5))  # 227 10:10 AM 11:00 AM MTWTh
b[7].sect_bids.append((38, 5))  # 227 10:30 AM 12:35 PM MW 
b[7].sect_bids.append((39, 5))  # 227 10:30 AM 12:35 PM TTh
b[7].sect_bids.append((40, 5))  # 227 11:10 AM 1:15 PM MW
b[7].sect_bids.append((41, 5))  # 227 11:10 AM 1:15 PM TTh
b[7].sect_bids.append((42, 5))  # 227 11:45 AM 12:35 PM MTWTh
b[7].sect_bids.append((43, 5))  # 227 11:45 AM 12:35 PM MTWTh
b[7].sect_bids.append((44, 5))  # 227 12:45 PM 2:50 PM MW
b[7].sect_bids.append((45, 5))  # 227 12:45 PM 2:50 PM MW
b[7].sect_bids.append((46, 5))  # 227 12:45 PM 2:50 PM TTh
b[7].sect_bids.append((47, 5)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[7].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[7].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[7].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[7].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[7].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[7].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[7].sect_bids.append((54, 5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[7].sect_bids.append((55, 5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[7].sect_bids.append((56, 5))  # 228A 8:00 AM 9:10 AM MTWTh
b[7].sect_bids.append((57, 5))  # 228A 12:45 PM 3:15 PM MW
b[7].sect_bids.append((58, 5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[7].sect_bids.append((59, 5))  # 228A 7:00 PM 9:30 PM MW
b[7].sect_bids.append((60, 5))  # 228A 7:00 PM 9:30 PM TTh 
b[7].sect_bids.append((61, 5))  # 228B 8:00 AM 9:10 AM MTWTh
b[7].sect_bids.append((62, -5))  # 228B 12:45 PM 3:15 PM MW 
b[7].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[7].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[7].sect_bids.append((65, 3))  # 238 8:00 AM 9:10 AM MTWTh
b[7].sect_bids.append((66, 3))  # 238 9:35 AM 10:45 AM MTWTh
b[7].sect_bids.append((67, 3))  # 238 11:10 AM 12:20 PM MTWTh
b[7].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[7].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[7].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[7].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[7].sect_bids.append((72, 2))  # 240 8:00 AM 9:25 AM MW
b[7].sect_bids.append((73, 2))  # 240 8:00 AM 9:25 AM TTh
b[7].sect_bids.append((74, 2))  # 240 9:35 AM 11:00 AM MW
b[7].sect_bids.append((75, 2))  # 240 9:35 AM 11:00 AM TTh
b[7].sect_bids.append((76, 2))  # 240 11:10 AM 12:35 PM MW 
b[7].sect_bids.append((77, 2))  # 240 11:10 AM 12:35 PM TTh 
b[7].sect_bids.append((78, 2))  # 240 12:45 PM 2:10 PM MW
b[7].sect_bids.append((79, 2))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[7].sect_bids.append((80, 2))  # 240 12:45 PM 2:10 PM MW
b[7].sect_bids.append((81, -5))  # 240 3:40 PM 5:05 PM TTh
b[7].sect_bids.append((82, -5))  # 240 3:40 PM 5:05 PM MW
b[7].sect_bids.append((83, -5))  # 240 5:15 PM 6:40 PM TTh
b[7].sect_bids.append((84, -5))  # 240 5:15 PM 6:40 PM MW Harandian
b[7].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[7].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[7].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[7].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[7].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[7].sect_bids.append((90, 2))  # 260 8:00 AM 9:10 AM MTWTh
b[7].sect_bids.append((91, 2))  # 260 9:35 AM 10:45 AM MTWTh
b[7].sect_bids.append((92, 2))  # 260 11:10 AM 12:20 PM MTWTh
b[7].sect_bids.append((93, 2))  # 260 12:45 PM 1:55 PM MTWTh
b[7].sect_bids.append((94, 2))  # 260 12:45 PM 3:15 PM MW
b[7].sect_bids.append((95, 2))  # 260 2:25 PM 3:35 PM MTWTh
b[7].sect_bids.append((96, 2))  # 260 2:25 PM 3:35 PM MTWTh
b[7].sect_bids.append((97, -5))  # 260 4:10 PM 6:40 PM MW
b[7].sect_bids.append((98, -5))  # 260 4:10 PM 6:40 PM TTh
b[7].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[7].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[7].sect_bids.append((101, 2))  # 261 8:00 AM 9:10 AM MTWTh
b[7].sect_bids.append((102, 2))  # 261 8:00 AM 9:10 AM MTWTh
b[7].sect_bids.append((103, 2))  # 261 9:35 AM 10:45 AM MTWTh
b[7].sect_bids.append((104, 2))  # 261 9:35 AM 10:45 AM MTWTh
b[7].sect_bids.append((105, 2))  # 261 11:10 AM 12:20 PM MTWTh
b[7].sect_bids.append((106, 2))  # 261 12:45 PM 3:15 PM MW
b[7].sect_bids.append((107, 2))  # 261 2:25 PM 3:35 PM MTWTh
b[7].sect_bids.append((108, -5))  # 261 4:10 PM 6:40 PM MW Martinez
b[7].sect_bids.append((109, -5))  # 261 4:10 PM 6:40 PM TTh
b[7].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[7].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[7].sect_bids.append((112, 2))  # 262 8:00 AM 9:10 AM MTWTh
b[7].sect_bids.append((113, 2))  # 262 9:35 AM 10:45 AM MTWTh
b[7].sect_bids.append((114, 2))  # 262 11:10 AM 12:20 PM MTWTh
b[7].sect_bids.append((115, 2))  # 262 11:10 AM 12:20 PM MTWTh
b[7].sect_bids.append((116, -5))  # 262 4:10 PM 6:40 PM TTh
b[7].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[7].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[7].sect_bids.append((119, 2))  # 263 8:00 AM 9:10 AM MTWTh
b[7].sect_bids.append((120, 2))  # 263 9:35 AM 10:45 AM MTWTh
b[7].sect_bids.append((121, 2))  # 263 11:10 AM 12:20 PM MTWT
b[7].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[7].sect_bids.append((123, -5))  # 270 8:00 AM 9:25 AM MW
b[7].sect_bids.append((124, -5))  # 270 12:45 PM 2:10 PM MW
b[7].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[7].sect_bids.append((126, -5))  # 275 9:35 AM 11:00 AM TTh
b[7].sect_bids.append((127, -5))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='martinje', semester='Fa2019', timestamp=datetime.datetime.now()))
b[8].bid_1_prep = 4
b[8].bid_2_prep = 5
b[8].bid_3_prep = 0
b[8].bid_4_prep = -2
b[8].bid_5_prep = -5
b[8].min_acc_units = 14
b[8].max_acc_units = 17
b[8].min_des_units = 14
b[8].max_des_units = 16
b[8].sect_bids.append((1, 0))  # 110 8:00 am MTWTh adj
b[8].sect_bids.append((2, 0))  # 110 9:35 am MTWTh adj 
b[8].sect_bids.append((3, 0))  # 110 4:10 PM MW adj
b[8].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[8].sect_bids.append((5, 0))  # 110 8:00 AM MTWTh adj
b[8].sect_bids.append((6, 2))  # 115 8:00 AM MTWTh 
b[8].sect_bids.append((7, 2))  # 115 11:10 AM MTWTh
b[8].sect_bids.append((8, 2))  # 115 12:45 PM MW
b[8].sect_bids.append((9, 2))  # 115 12:45 PM TTh
b[8].sect_bids.append((10, -5))  # 115 4:10 PM TTh
b[8].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[8].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[8].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[8].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[8].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[8].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[8].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[8].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[8].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[8].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[8].sect_bids.append((21, -5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[8].sect_bids.append((22, -5))  # 134 3:30 PM 6:40 PM MW Le 
b[8].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[8].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[8].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[8].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[8].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[8].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[8].sect_bids.append((29, 1))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[8].sect_bids.append((30, 1))  # 227 8:00 AM 8:50 AM MTWTh
b[8].sect_bids.append((31, 1))  # 227 8:00 AM 10:05 AM MW
b[8].sect_bids.append((32, 1))  # 227 8:00 AM 10:05 AM TTh
b[8].sect_bids.append((33, 1))  # 227 9:35 AM 10:25 AM MTWTh
b[8].sect_bids.append((34, 1))  # 227 9:35 AM 11:40 AM MW 
b[8].sect_bids.append((35, 1))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[8].sect_bids.append((36, 1))  # 227 10:10 AM 11:00 AM MTWTh
b[8].sect_bids.append((37, 1))  # 227 10:10 AM 11:00 AM MTWTh
b[8].sect_bids.append((38, 1))  # 227 10:30 AM 12:35 PM MW 
b[8].sect_bids.append((39, 1))  # 227 10:30 AM 12:35 PM TTh
b[8].sect_bids.append((40, 1))  # 227 11:10 AM 1:15 PM MW
b[8].sect_bids.append((41, 1))  # 227 11:10 AM 1:15 PM TTh
b[8].sect_bids.append((42, 1))  # 227 11:45 AM 12:35 PM MTWTh
b[8].sect_bids.append((43, 1))  # 227 11:45 AM 12:35 PM MTWTh
b[8].sect_bids.append((44, 1))  # 227 12:45 PM 2:50 PM MW
b[8].sect_bids.append((45, 1))  # 227 12:45 PM 2:50 PM MW
b[8].sect_bids.append((46, 1))  # 227 12:45 PM 2:50 PM TTh
b[8].sect_bids.append((47, 1)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[8].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[8].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[8].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[8].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[8].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[8].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[8].sect_bids.append((54, 3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[8].sect_bids.append((55, 3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[8].sect_bids.append((56, 3))  # 228A 8:00 AM 9:10 AM MTWTh
b[8].sect_bids.append((57, 3))  # 228A 12:45 PM 3:15 PM MW
b[8].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[8].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[8].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[8].sect_bids.append((61, 1))  # 228B 8:00 AM 9:10 AM MTWTh
b[8].sect_bids.append((62, 1))  # 228B 12:45 PM 3:15 PM MW 
b[8].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[8].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[8].sect_bids.append((65, -2))  # 238 8:00 AM 9:10 AM MTWTh
b[8].sect_bids.append((66, -2))  # 238 9:35 AM 10:45 AM MTWTh
b[8].sect_bids.append((67, -2))  # 238 11:10 AM 12:20 PM MTWTh
b[8].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[8].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[8].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[8].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[8].sect_bids.append((72, 4))  # 240 8:00 AM 9:25 AM MW
b[8].sect_bids.append((73, 4))  # 240 8:00 AM 9:25 AM TTh
b[8].sect_bids.append((74, 4))  # 240 9:35 AM 11:00 AM MW
b[8].sect_bids.append((75, 4))  # 240 9:35 AM 11:00 AM TTh
b[8].sect_bids.append((76, 4))  # 240 11:10 AM 12:35 PM MW 
b[8].sect_bids.append((77, 4))  # 240 11:10 AM 12:35 PM TTh 
b[8].sect_bids.append((78, 4))  # 240 12:45 PM 2:10 PM MW
b[8].sect_bids.append((79, 4))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[8].sect_bids.append((80, 4))  # 240 12:45 PM 2:10 PM MW
b[8].sect_bids.append((81, -5))  # 240 3:40 PM 5:05 PM TTh
b[8].sect_bids.append((82, -5))  # 240 3:40 PM 5:05 PM MW
b[8].sect_bids.append((83, -5))  # 240 5:15 PM 6:40 PM TTh
b[8].sect_bids.append((84, -5))  # 240 5:15 PM 6:40 PM MW Harandian
b[8].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[8].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[8].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[8].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[8].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[8].sect_bids.append((90, 0))  # 260 8:00 AM 9:10 AM MTWTh
b[8].sect_bids.append((91, 0))  # 260 9:35 AM 10:45 AM MTWTh
b[8].sect_bids.append((92, 0))  # 260 11:10 AM 12:20 PM MTWTh
b[8].sect_bids.append((93, 0))  # 260 12:45 PM 1:55 PM MTWTh
b[8].sect_bids.append((94, 0))  # 260 12:45 PM 3:15 PM MW
b[8].sect_bids.append((95, 0))  # 260 2:25 PM 3:35 PM MTWTh
b[8].sect_bids.append((96, 0))  # 260 2:25 PM 3:35 PM MTWTh
b[8].sect_bids.append((97, -5))  # 260 4:10 PM 6:40 PM MW
b[8].sect_bids.append((98, -5))  # 260 4:10 PM 6:40 PM TTh
b[8].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[8].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[8].sect_bids.append((101, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[8].sect_bids.append((102, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[8].sect_bids.append((103, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[8].sect_bids.append((104, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[8].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[8].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[8].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[8].sect_bids.append((108, -5))  # 261 4:10 PM 6:40 PM MW Martinez
b[8].sect_bids.append((109, -5))  # 261 4:10 PM 6:40 PM TTh
b[8].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[8].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[8].sect_bids.append((112, 3))  # 262 8:00 AM 9:10 AM MTWTh
b[8].sect_bids.append((113, 3))  # 262 9:35 AM 10:45 AM MTWTh
b[8].sect_bids.append((114, 3))  # 262 11:10 AM 12:20 PM MTWTh
b[8].sect_bids.append((115, 3))  # 262 11:10 AM 12:20 PM MTWTh
b[8].sect_bids.append((116, -5))  # 262 4:10 PM 6:40 PM TTh
b[8].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[8].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[8].sect_bids.append((119, 2))  # 263 8:00 AM 9:10 AM MTWTh
b[8].sect_bids.append((120, 2))  # 263 9:35 AM 10:45 AM MTWTh
b[8].sect_bids.append((121, 2))  # 263 11:10 AM 12:20 PM MTWT
b[8].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[8].sect_bids.append((123, 4))  # 270 8:00 AM 9:25 AM MW
b[8].sect_bids.append((124, 4))  # 270 12:45 PM 2:10 PM MW
b[8].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[8].sect_bids.append((126, 0))  # 275 9:35 AM 11:00 AM TTh
b[8].sect_bids.append((127, 0))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='navabm', semester='Fa2019', timestamp=datetime.datetime.now()))
b[9].bid_1_prep = 4
b[9].bid_2_prep = 5
b[9].bid_3_prep = 0
b[9].bid_4_prep = -2
b[9].bid_5_prep = -5
b[9].min_acc_units = 13
b[9].max_acc_units = 17
b[9].min_des_units = 14
b[9].max_des_units = 16
b[9].sect_bids.append((1, -3))  # 110 8:00 am MTWTh adj
b[9].sect_bids.append((2, -3))  # 110 9:35 am MTWTh adj 
b[9].sect_bids.append((3, -3))  # 110 4:10 PM MW adj
b[9].sect_bids.append((4, -3))  # 110 7:00 PM TTh
b[9].sect_bids.append((5, -3))  # 110 8:00 AM MTWTh adj
b[9].sect_bids.append((6, 4))  # 115 8:00 AM MTWTh 
b[9].sect_bids.append((7, 4))  # 115 11:10 AM MTWTh
b[9].sect_bids.append((8, 4))  # 115 12:45 PM MW
b[9].sect_bids.append((9, 4))  # 115 12:45 PM TTh
b[9].sect_bids.append((10, -3))  # 115 4:10 PM TTh
b[9].sect_bids.append((11, 4))  # 134 8:00 AM MTWTh LEHAVI
b[9].sect_bids.append((12, 4))  # 134 8:00 AM MTWTh
b[9].sect_bids.append((13, 4))  # 134 8:00 AM MTWTh
b[9].sect_bids.append((14, 4))  # 134 9:35 AM MTWTh
b[9].sect_bids.append((15, 4))  # 134 9:35 AM MTWTh
b[9].sect_bids.append((16, 4))  # 134 11:10 AM MTWTh
b[9].sect_bids.append((17, 4)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[9].sect_bids.append((18, 4)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[9].sect_bids.append((19, 4)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[9].sect_bids.append((20, 4))  # 134 12:45 PM 3:55 PM MW 
b[9].sect_bids.append((21, -3))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[9].sect_bids.append((22, -3))  # 134 3:30 PM 6:40 PM MW Le 
b[9].sect_bids.append((23, -3))  # 6:50 PM 10:00 PM MW Grigoryan 
b[9].sect_bids.append((24, -3))  # 134 6:50 PM 10:00 PM MW
b[9].sect_bids.append((25, -3))  # 134 6:50 PM 10:00 PM TTh 
b[9].sect_bids.append((26, -3))  # 134 6:50 PM 10:00 PM TTh
b[9].sect_bids.append((27, 0))  # 215 5:15 PM 6:40 PM MW
b[9].sect_bids.append((28, 0))  # 215 3:40 PM 5:05 PM TTh 
b[9].sect_bids.append((29, 0))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[9].sect_bids.append((30, 0))  # 227 8:00 AM 8:50 AM MTWTh
b[9].sect_bids.append((31, 0))  # 227 8:00 AM 10:05 AM MW
b[9].sect_bids.append((32, 0))  # 227 8:00 AM 10:05 AM TTh
b[9].sect_bids.append((33, 0))  # 227 9:35 AM 10:25 AM MTWTh
b[9].sect_bids.append((34, 0))  # 227 9:35 AM 11:40 AM MW 
b[9].sect_bids.append((35, 0))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[9].sect_bids.append((36, 0))  # 227 10:10 AM 11:00 AM MTWTh
b[9].sect_bids.append((37, 0))  # 227 10:10 AM 11:00 AM MTWTh
b[9].sect_bids.append((38, 0))  # 227 10:30 AM 12:35 PM MW 
b[9].sect_bids.append((39, 0))  # 227 10:30 AM 12:35 PM TTh
b[9].sect_bids.append((40, 0))  # 227 11:10 AM 1:15 PM MW
b[9].sect_bids.append((41, 0))  # 227 11:10 AM 1:15 PM TTh
b[9].sect_bids.append((42, 0))  # 227 11:45 AM 12:35 PM MTWTh
b[9].sect_bids.append((43, 0))  # 227 11:45 AM 12:35 PM MTWTh
b[9].sect_bids.append((44, 0))  # 227 12:45 PM 2:50 PM MW
b[9].sect_bids.append((45, 0))  # 227 12:45 PM 2:50 PM MW
b[9].sect_bids.append((46, 0))  # 227 12:45 PM 2:50 PM TTh
b[9].sect_bids.append((47, 0)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[9].sect_bids.append((48, 0))  # 227 4:35 PM 6:40 PM MW
b[9].sect_bids.append((49, 0))  # 227 4:35 PM 6:40 PM TTh
b[9].sect_bids.append((50, -3))  # 227 7:00 PM 9:05 PM MW
b[9].sect_bids.append((51, -3))  # 227 7:00 PM 9:05 PM MW
b[9].sect_bids.append((52, -3))  # 227 7:00 PM 9:05 PM TTh
b[9].sect_bids.append((53, -3))  # 227 7:00 PM 9:05 PM TTh
b[9].sect_bids.append((54, 3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[9].sect_bids.append((55, 3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[9].sect_bids.append((56, 3))  # 228A 8:00 AM 9:10 AM MTWTh
b[9].sect_bids.append((57, 3))  # 228A 12:45 PM 3:15 PM MW
b[9].sect_bids.append((58, -3))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[9].sect_bids.append((59, -3))  # 228A 7:00 PM 9:30 PM MW
b[9].sect_bids.append((60, -3))  # 228A 7:00 PM 9:30 PM TTh 
b[9].sect_bids.append((61, 4))  # 228B 8:00 AM 9:10 AM MTWTh
b[9].sect_bids.append((62, 4))  # 228B 12:45 PM 3:15 PM MW 
b[9].sect_bids.append((63, -3))  # 228B 4:10 PM 6:40 PM MW
b[9].sect_bids.append((64, -3))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[9].sect_bids.append((65, -2))  # 238 8:00 AM 9:10 AM MTWTh
b[9].sect_bids.append((66, -2))  # 238 9:35 AM 10:45 AM MTWTh
b[9].sect_bids.append((67, -2))  # 238 11:10 AM 12:20 PM MTWTh
b[9].sect_bids.append((68, -3))  # 238 4:10 PM 6:40 PM MW 
b[9].sect_bids.append((69, -3))  # 238 4:10 PM 6:40 PM TTh
b[9].sect_bids.append((70, -2))  # 238 7:00 PM 9:30 PM MW
b[9].sect_bids.append((71, -2))  # 238 7:00 PM 9:30 PM TTh New
b[9].sect_bids.append((72, 2))  # 240 8:00 AM 9:25 AM MW
b[9].sect_bids.append((73, 2))  # 240 8:00 AM 9:25 AM TTh
b[9].sect_bids.append((74, 2))  # 240 9:35 AM 11:00 AM MW
b[9].sect_bids.append((75, 2))  # 240 9:35 AM 11:00 AM TTh
b[9].sect_bids.append((76, 2))  # 240 11:10 AM 12:35 PM MW 
b[9].sect_bids.append((77, 2))  # 240 11:10 AM 12:35 PM TTh 
b[9].sect_bids.append((78, 2))  # 240 12:45 PM 2:10 PM MW
b[9].sect_bids.append((79, 2))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[9].sect_bids.append((80, 2))  # 240 12:45 PM 2:10 PM MW
b[9].sect_bids.append((81, -3))  # 240 3:40 PM 5:05 PM TTh
b[9].sect_bids.append((82, -3))  # 240 3:40 PM 5:05 PM MW
b[9].sect_bids.append((83, -3))  # 240 5:15 PM 6:40 PM TTh
b[9].sect_bids.append((84, -3))  # 240 5:15 PM 6:40 PM MW Harandian
b[9].sect_bids.append((85, -3))  # 240 7:00 PM 8:25 PM MW
b[9].sect_bids.append((86, -3))  # 240 7:00 PM 8:25 PM TTh
b[9].sect_bids.append((87, -3))  # 240 7:00 PM 8:25 PM TTh
b[9].sect_bids.append((88, -3))  # 240 8:35 PM 10:00 PM MW 
b[9].sect_bids.append((89, -3))  # 240 8:35 PM 10:00 PM TTh 
b[9].sect_bids.append((90, 5))  # 260 8:00 AM 9:10 AM MTWTh
b[9].sect_bids.append((91, 5))  # 260 9:35 AM 10:45 AM MTWTh
b[9].sect_bids.append((92, 5))  # 260 11:10 AM 12:20 PM MTWTh
b[9].sect_bids.append((93, 5))  # 260 12:45 PM 1:55 PM MTWTh
b[9].sect_bids.append((94, 5))  # 260 12:45 PM 3:15 PM MW
b[9].sect_bids.append((95, 5))  # 260 2:25 PM 3:35 PM MTWTh
b[9].sect_bids.append((96, 5))  # 260 2:25 PM 3:35 PM MTWTh
b[9].sect_bids.append((97, -3))  # 260 4:10 PM 6:40 PM MW
b[9].sect_bids.append((98, -3))  # 260 4:10 PM 6:40 PM TTh
b[9].sect_bids.append((99, -3))  # 260 7:00 PM 9:30 PM MW
b[9].sect_bids.append((100, -3))  # 260 7:00 PM 9:30 PM TTh
b[9].sect_bids.append((101, 4))  # 261 8:00 AM 9:10 AM MTWTh
b[9].sect_bids.append((102, 4))  # 261 8:00 AM 9:10 AM MTWTh
b[9].sect_bids.append((103, 4))  # 261 9:35 AM 10:45 AM MTWTh
b[9].sect_bids.append((104, 4))  # 261 9:35 AM 10:45 AM MTWTh
b[9].sect_bids.append((105, 4))  # 261 11:10 AM 12:20 PM MTWTh
b[9].sect_bids.append((106, 4))  # 261 12:45 PM 3:15 PM MW
b[9].sect_bids.append((107, -3))  # 261 2:25 PM 3:35 PM MTWTh
b[9].sect_bids.append((108, -3))  # 261 4:10 PM 6:40 PM MW Martinez
b[9].sect_bids.append((109, -3))  # 261 4:10 PM 6:40 PM TTh
b[9].sect_bids.append((110, -3))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[9].sect_bids.append((111, -3))  # 261 7:00 PM 9:30 PM TTh Lin
b[9].sect_bids.append((112, 2))  # 262 8:00 AM 9:10 AM MTWTh
b[9].sect_bids.append((113, 2))  # 262 9:35 AM 10:45 AM MTWTh
b[9].sect_bids.append((114, 2))  # 262 11:10 AM 12:20 PM MTWTh
b[9].sect_bids.append((115, 2))  # 262 11:10 AM 12:20 PM MTWTh
b[9].sect_bids.append((116, -3))  # 262 4:10 PM 6:40 PM TTh
b[9].sect_bids.append((117, -3))  # 262 7:00 PM 9:30 PM MW
b[9].sect_bids.append((118, -3))  # 262 7:00 PM 9:30 PM TTh
b[9].sect_bids.append((119, 0))  # 263 8:00 AM 9:10 AM MTWTh
b[9].sect_bids.append((120, 0))  # 263 9:35 AM 10:45 AM MTWTh
b[9].sect_bids.append((121, 0))  # 263 11:10 AM 12:20 PM MTWT
b[9].sect_bids.append((122, -3))  # 263 7:00 PM 9:30 PM TTh
b[9].sect_bids.append((123, -3))  # 270 8:00 AM 9:25 AM MW
b[9].sect_bids.append((124, -3))  # 270 12:45 PM 2:10 PM MW
b[9].sect_bids.append((125, -3))  # 270 5:15 PM 6:40 PM TTh
b[9].sect_bids.append((126, -3))  # 275 9:35 AM 11:00 AM TTh
b[9].sect_bids.append((127, -3))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='pearsasa', semester='Fa2019', timestamp=datetime.datetime.now()))
b[10].bid_1_prep = 4
b[10].bid_2_prep = 5
b[10].bid_3_prep = 2
b[10].bid_4_prep = -2
b[10].bid_5_prep = -5
b[10].min_acc_units = 18
b[10].max_acc_units = 27
b[10].min_des_units = 20
b[10].max_des_units = 23
b[10].sect_bids.append((1, -5))  # 110 8:00 am MTWTh adj
b[10].sect_bids.append((2, -5))  # 110 9:35 am MTWTh adj 
b[10].sect_bids.append((3, -5))  # 110 4:10 PM MW adj
b[10].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[10].sect_bids.append((5, -5))  # 110 8:00 AM MTWTh adj
b[10].sect_bids.append((6, -5))  # 115 8:00 AM MTWTh 
b[10].sect_bids.append((7, -5))  # 115 11:10 AM MTWTh
b[10].sect_bids.append((8, -5))  # 115 12:45 PM MW
b[10].sect_bids.append((9, -5))  # 115 12:45 PM TTh
b[10].sect_bids.append((10, -5))  # 115 4:10 PM TTh
b[10].sect_bids.append((11, -5))  # 134 8:00 AM MTWTh LEHAVI
b[10].sect_bids.append((12, -5))  # 134 8:00 AM MTWTh
b[10].sect_bids.append((13, -5))  # 134 8:00 AM MTWTh
b[10].sect_bids.append((14, -5))  # 134 9:35 AM MTWTh
b[10].sect_bids.append((15, -5))  # 134 9:35 AM MTWTh
b[10].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[10].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[10].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[10].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[10].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[10].sect_bids.append((21, 5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[10].sect_bids.append((22, 5))  # 134 3:30 PM 6:40 PM MW Le 
b[10].sect_bids.append((23, 5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[10].sect_bids.append((24, 5))  # 134 6:50 PM 10:00 PM MW
b[10].sect_bids.append((25, 5))  # 134 6:50 PM 10:00 PM TTh 
b[10].sect_bids.append((26, 5))  # 134 6:50 PM 10:00 PM TTh
b[10].sect_bids.append((27, 5))  # 215 5:15 PM 6:40 PM MW
b[10].sect_bids.append((28, 5))  # 215 3:40 PM 5:05 PM TTh 
b[10].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[10].sect_bids.append((30, -5))  # 227 8:00 AM 8:50 AM MTWTh
b[10].sect_bids.append((31, -5))  # 227 8:00 AM 10:05 AM MW
b[10].sect_bids.append((32, -5))  # 227 8:00 AM 10:05 AM TTh
b[10].sect_bids.append((33, -5))  # 227 9:35 AM 10:25 AM MTWTh
b[10].sect_bids.append((34, -5))  # 227 9:35 AM 11:40 AM MW 
b[10].sect_bids.append((35, -5))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[10].sect_bids.append((36, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[10].sect_bids.append((37, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[10].sect_bids.append((38, -5))  # 227 10:30 AM 12:35 PM MW 
b[10].sect_bids.append((39, -5))  # 227 10:30 AM 12:35 PM TTh
b[10].sect_bids.append((40, -5))  # 227 11:10 AM 1:15 PM MW
b[10].sect_bids.append((41, -5))  # 227 11:10 AM 1:15 PM TTh
b[10].sect_bids.append((42, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[10].sect_bids.append((43, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[10].sect_bids.append((44, -5))  # 227 12:45 PM 2:50 PM MW
b[10].sect_bids.append((45, -5))  # 227 12:45 PM 2:50 PM MW
b[10].sect_bids.append((46, -5))  # 227 12:45 PM 2:50 PM TTh
b[10].sect_bids.append((47, -5)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[10].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[10].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[10].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[10].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[10].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[10].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[10].sect_bids.append((54, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[10].sect_bids.append((55, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[10].sect_bids.append((56, -5))  # 228A 8:00 AM 9:10 AM MTWTh
b[10].sect_bids.append((57, -5))  # 228A 12:45 PM 3:15 PM MW
b[10].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[10].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[10].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[10].sect_bids.append((61, -5))  # 228B 8:00 AM 9:10 AM MTWTh
b[10].sect_bids.append((62, -5))  # 228B 12:45 PM 3:15 PM MW 
b[10].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[10].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[10].sect_bids.append((65, -3))  # 238 8:00 AM 9:10 AM MTWTh
b[10].sect_bids.append((66, -3))  # 238 9:35 AM 10:45 AM MTWTh
b[10].sect_bids.append((67, -3))  # 238 11:10 AM 12:20 PM MTWTh
b[10].sect_bids.append((68, 3))  # 238 4:10 PM 6:40 PM MW 
b[10].sect_bids.append((69, 3))  # 238 4:10 PM 6:40 PM TTh
b[10].sect_bids.append((70, 3))  # 238 7:00 PM 9:30 PM MW
b[10].sect_bids.append((71, 3))  # 238 7:00 PM 9:30 PM TTh New
b[10].sect_bids.append((72, -3))  # 240 8:00 AM 9:25 AM MW
b[10].sect_bids.append((73, -3))  # 240 8:00 AM 9:25 AM TTh
b[10].sect_bids.append((74, -3))  # 240 9:35 AM 11:00 AM MW
b[10].sect_bids.append((75, -3))  # 240 9:35 AM 11:00 AM TTh
b[10].sect_bids.append((76, 3))  # 240 11:10 AM 12:35 PM MW 
b[10].sect_bids.append((77, 3))  # 240 11:10 AM 12:35 PM TTh 
b[10].sect_bids.append((78, 3))  # 240 12:45 PM 2:10 PM MW
b[10].sect_bids.append((79, 3))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[10].sect_bids.append((80, 3))  # 240 12:45 PM 2:10 PM MW
b[10].sect_bids.append((81, 3))  # 240 3:40 PM 5:05 PM TTh
b[10].sect_bids.append((82, 3))  # 240 3:40 PM 5:05 PM MW
b[10].sect_bids.append((83, 3))  # 240 5:15 PM 6:40 PM TTh
b[10].sect_bids.append((84, 3))  # 240 5:15 PM 6:40 PM MW Harandian
b[10].sect_bids.append((85, 3))  # 240 7:00 PM 8:25 PM MW
b[10].sect_bids.append((86, 3))  # 240 7:00 PM 8:25 PM TTh
b[10].sect_bids.append((87, 3))  # 240 7:00 PM 8:25 PM TTh
b[10].sect_bids.append((88, 3))  # 240 8:35 PM 10:00 PM MW 
b[10].sect_bids.append((89, 3))  # 240 8:35 PM 10:00 PM TTh 
b[10].sect_bids.append((90, -3))  # 260 8:00 AM 9:10 AM MTWTh
b[10].sect_bids.append((91, -3))  # 260 9:35 AM 10:45 AM MTWTh
b[10].sect_bids.append((92, 3))  # 260 11:10 AM 12:20 PM MTWTh
b[10].sect_bids.append((93, 3))  # 260 12:45 PM 1:55 PM MTWTh
b[10].sect_bids.append((94, 3))  # 260 12:45 PM 3:15 PM MW
b[10].sect_bids.append((95, 3))  # 260 2:25 PM 3:35 PM MTWTh
b[10].sect_bids.append((96, 3))  # 260 2:25 PM 3:35 PM MTWTh
b[10].sect_bids.append((97, 3))  # 260 4:10 PM 6:40 PM MW
b[10].sect_bids.append((98, 3))  # 260 4:10 PM 6:40 PM TTh
b[10].sect_bids.append((99, 3))  # 260 7:00 PM 9:30 PM MW
b[10].sect_bids.append((100, 3))  # 260 7:00 PM 9:30 PM TTh
b[10].sect_bids.append((101, -3))  # 261 8:00 AM 9:10 AM MTWTh
b[10].sect_bids.append((102, -3))  # 261 8:00 AM 9:10 AM MTWTh
b[10].sect_bids.append((103, -3))  # 261 9:35 AM 10:45 AM MTWTh
b[10].sect_bids.append((104, -3))  # 261 9:35 AM 10:45 AM MTWTh
b[10].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[10].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[10].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[10].sect_bids.append((108, 5))  # 261 4:10 PM 6:40 PM MW Martinez
b[10].sect_bids.append((109, 5))  # 261 4:10 PM 6:40 PM TTh
b[10].sect_bids.append((110, 5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[10].sect_bids.append((111, 5))  # 261 7:00 PM 9:30 PM TTh Lin
b[10].sect_bids.append((112, -2))  # 262 8:00 AM 9:10 AM MTWTh
b[10].sect_bids.append((113, -2))  # 262 9:35 AM 10:45 AM MTWTh
b[10].sect_bids.append((114, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[10].sect_bids.append((115, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[10].sect_bids.append((116, 5))  # 262 4:10 PM 6:40 PM TTh
b[10].sect_bids.append((117, 5))  # 262 7:00 PM 9:30 PM MW
b[10].sect_bids.append((118, 5))  # 262 7:00 PM 9:30 PM TTh
b[10].sect_bids.append((119, -3))  # 263 8:00 AM 9:10 AM MTWTh
b[10].sect_bids.append((120, -3))  # 263 9:35 AM 10:45 AM MTWTh
b[10].sect_bids.append((121, 5))  # 263 11:10 AM 12:20 PM MTWT
b[10].sect_bids.append((122, 5))  # 263 7:00 PM 9:30 PM TTh
b[10].sect_bids.append((123, -5))  # 270 8:00 AM 9:25 AM MW
b[10].sect_bids.append((124, 5))  # 270 12:45 PM 2:10 PM MW
b[10].sect_bids.append((125, 5))  # 270 5:15 PM 6:40 PM TTh
b[10].sect_bids.append((126, -5))  # 275 9:35 AM 11:00 AM TTh
b[10].sect_bids.append((127, 5))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='phamp', semester='Fa2019', timestamp=datetime.datetime.now()))
b[11].bid_1_prep = 4
b[11].bid_2_prep = 5
b[11].bid_3_prep = 0
b[11].bid_4_prep = -2
b[11].bid_5_prep = -5
b[11].min_acc_units = 12
b[11].max_acc_units = 16
b[11].min_des_units = 14
b[11].max_des_units = 15
b[11].sect_bids.append((1, 0))  # 110 8:00 am MTWTh adj
b[11].sect_bids.append((2, 0))  # 110 9:35 am MTWTh adj 
b[11].sect_bids.append((3, 0))  # 110 4:10 PM MW adj
b[11].sect_bids.append((4, 0))  # 110 7:00 PM TTh
b[11].sect_bids.append((5, 0))  # 110 8:00 AM MTWTh adj
b[11].sect_bids.append((6, 4))  # 115 8:00 AM MTWTh 
b[11].sect_bids.append((7, 4))  # 115 11:10 AM MTWTh
b[11].sect_bids.append((8, 4))  # 115 12:45 PM MW
b[11].sect_bids.append((9, 4))  # 115 12:45 PM TTh
b[11].sect_bids.append((10, -5))  # 115 4:10 PM TTh
b[11].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[11].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[11].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[11].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[11].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[11].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[11].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[11].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[11].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[11].sect_bids.append((20, -5))  # 134 12:45 PM 3:55 PM MW 
b[11].sect_bids.append((21, -5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[11].sect_bids.append((22, -5))  # 134 3:30 PM 6:40 PM MW Le 
b[11].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[11].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[11].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[11].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[11].sect_bids.append((27, -2))  # 215 5:15 PM 6:40 PM MW
b[11].sect_bids.append((28, -2))  # 215 3:40 PM 5:05 PM TTh 
b[11].sect_bids.append((29, 4))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[11].sect_bids.append((30, 4))  # 227 8:00 AM 8:50 AM MTWTh
b[11].sect_bids.append((31, 4))  # 227 8:00 AM 10:05 AM MW
b[11].sect_bids.append((32, 4))  # 227 8:00 AM 10:05 AM TTh
b[11].sect_bids.append((33, 4))  # 227 9:35 AM 10:25 AM MTWTh
b[11].sect_bids.append((34, 4))  # 227 9:35 AM 11:40 AM MW 
b[11].sect_bids.append((35, 4))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[11].sect_bids.append((36, 4))  # 227 10:10 AM 11:00 AM MTWTh
b[11].sect_bids.append((37, 4))  # 227 10:10 AM 11:00 AM MTWTh
b[11].sect_bids.append((38, 4))  # 227 10:30 AM 12:35 PM MW 
b[11].sect_bids.append((39, 4))  # 227 10:30 AM 12:35 PM TTh
b[11].sect_bids.append((40, 4))  # 227 11:10 AM 1:15 PM MW
b[11].sect_bids.append((41, 4))  # 227 11:10 AM 1:15 PM TTh
b[11].sect_bids.append((42, 4))  # 227 11:45 AM 12:35 PM MTWTh
b[11].sect_bids.append((43, 4))  # 227 11:45 AM 12:35 PM MTWTh
b[11].sect_bids.append((44, 4))  # 227 12:45 PM 2:50 PM MW
b[11].sect_bids.append((45, 4))  # 227 12:45 PM 2:50 PM MW
b[11].sect_bids.append((46, 4))  # 227 12:45 PM 2:50 PM TTh
b[11].sect_bids.append((47, 4)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[11].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[11].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[11].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[11].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[11].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[11].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[11].sect_bids.append((54, 3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[11].sect_bids.append((55, 3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[11].sect_bids.append((56, 3))  # 228A 8:00 AM 9:10 AM MTWTh
b[11].sect_bids.append((57, 3))  # 228A 12:45 PM 3:15 PM MW
b[11].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[11].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[11].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[11].sect_bids.append((61, 3))  # 228B 8:00 AM 9:10 AM MTWTh
b[11].sect_bids.append((62, 3))  # 228B 12:45 PM 3:15 PM MW 
b[11].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[11].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[11].sect_bids.append((65, -5))  # 238 8:00 AM 9:10 AM MTWTh
b[11].sect_bids.append((66, -5))  # 238 9:35 AM 10:45 AM MTWTh
b[11].sect_bids.append((67, -5))  # 238 11:10 AM 12:20 PM MTWTh
b[11].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[11].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[11].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[11].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[11].sect_bids.append((72, 2))  # 240 8:00 AM 9:25 AM MW
b[11].sect_bids.append((73, 2))  # 240 8:00 AM 9:25 AM TTh
b[11].sect_bids.append((74, 2))  # 240 9:35 AM 11:00 AM MW
b[11].sect_bids.append((75, 2))  # 240 9:35 AM 11:00 AM TTh
b[11].sect_bids.append((76, 2))  # 240 11:10 AM 12:35 PM MW 
b[11].sect_bids.append((77, 2))  # 240 11:10 AM 12:35 PM TTh 
b[11].sect_bids.append((78, 2))  # 240 12:45 PM 2:10 PM MW
b[11].sect_bids.append((79, 2))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[11].sect_bids.append((80, 2))  # 240 12:45 PM 2:10 PM MW
b[11].sect_bids.append((81, -5))  # 240 3:40 PM 5:05 PM TTh
b[11].sect_bids.append((82, -5))  # 240 3:40 PM 5:05 PM MW
b[11].sect_bids.append((83, -5))  # 240 5:15 PM 6:40 PM TTh
b[11].sect_bids.append((84, -5))  # 240 5:15 PM 6:40 PM MW Harandian
b[11].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[11].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[11].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[11].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[11].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[11].sect_bids.append((90, 4))  # 260 8:00 AM 9:10 AM MTWTh
b[11].sect_bids.append((91, 4))  # 260 9:35 AM 10:45 AM MTWTh
b[11].sect_bids.append((92, 4))  # 260 11:10 AM 12:20 PM MTWTh
b[11].sect_bids.append((93, 4))  # 260 12:45 PM 1:55 PM MTWTh
b[11].sect_bids.append((94, 4))  # 260 12:45 PM 3:15 PM MW
b[11].sect_bids.append((95, 4))  # 260 2:25 PM 3:35 PM MTWTh
b[11].sect_bids.append((96, 4))  # 260 2:25 PM 3:35 PM MTWTh
b[11].sect_bids.append((97, -5))  # 260 4:10 PM 6:40 PM MW
b[11].sect_bids.append((98, -5))  # 260 4:10 PM 6:40 PM TTh
b[11].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[11].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[11].sect_bids.append((101, 1))  # 261 8:00 AM 9:10 AM MTWTh
b[11].sect_bids.append((102, 1))  # 261 8:00 AM 9:10 AM MTWTh
b[11].sect_bids.append((103, 1))  # 261 9:35 AM 10:45 AM MTWTh
b[11].sect_bids.append((104, 1))  # 261 9:35 AM 10:45 AM MTWTh
b[11].sect_bids.append((105, 1))  # 261 11:10 AM 12:20 PM MTWTh
b[11].sect_bids.append((106, 1))  # 261 12:45 PM 3:15 PM MW
b[11].sect_bids.append((107, -5))  # 261 2:25 PM 3:35 PM MTWTh
b[11].sect_bids.append((108, -5))  # 261 4:10 PM 6:40 PM MW Martinez
b[11].sect_bids.append((109, -5))  # 261 4:10 PM 6:40 PM TTh
b[11].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[11].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[11].sect_bids.append((112, 0))  # 262 8:00 AM 9:10 AM MTWTh
b[11].sect_bids.append((113, 0))  # 262 9:35 AM 10:45 AM MTWTh
b[11].sect_bids.append((114, 0))  # 262 11:10 AM 12:20 PM MTWTh
b[11].sect_bids.append((115, 0))  # 262 11:10 AM 12:20 PM MTWTh
b[11].sect_bids.append((116, -5))  # 262 4:10 PM 6:40 PM TTh
b[11].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[11].sect_bids.append((118, 0))  # 262 7:00 PM 9:30 PM TTh
b[11].sect_bids.append((119, 0))  # 263 8:00 AM 9:10 AM MTWTh
b[11].sect_bids.append((120, 0))  # 263 9:35 AM 10:45 AM MTWTh
b[11].sect_bids.append((121, 0))  # 263 11:10 AM 12:20 PM MTWT
b[11].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[11].sect_bids.append((123, -4))  # 270 8:00 AM 9:25 AM MW
b[11].sect_bids.append((124, -4))  # 270 12:45 PM 2:10 PM MW
b[11].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[11].sect_bids.append((126, -4))  # 275 9:35 AM 11:00 AM Th
b[11].sect_bids.append((127, -5))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='pumarmd', semester='Fa2019', timestamp=datetime.datetime.now()))
b[12].bid_1_prep = 4
b[12].bid_2_prep = 5
b[12].bid_3_prep = 0
b[12].bid_4_prep = -2
b[12].bid_5_prep = -5
b[12].min_acc_units = 16
b[12].max_acc_units = 24
b[12].min_des_units = 19
b[12].max_des_units = 20
b[12].sect_bids.append((1, 0))  # 110 8:00 am MTWTh adj
b[12].sect_bids.append((2, 0))  # 110 9:35 am MTWTh adj 
b[12].sect_bids.append((3, 0))  # 110 4:10 PM MW adj
b[12].sect_bids.append((4, 0))  # 110 7:00 PM TTh
b[12].sect_bids.append((5, 0))  # 110 8:00 AM MTWTh adj
b[12].sect_bids.append((6, 1))  # 115 8:00 AM MTWTh 
b[12].sect_bids.append((7, 1))  # 115 11:10 AM MTWTh
b[12].sect_bids.append((8, 1))  # 115 12:45 PM MW
b[12].sect_bids.append((9, 1))  # 115 12:45 PM TTh
b[12].sect_bids.append((10, 1))  # 115 4:10 PM TTh
b[12].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[12].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[12].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[12].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[12].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[12].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[12].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[12].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[12].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[12].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[12].sect_bids.append((21, -3))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[12].sect_bids.append((22, -3))  # 134 3:30 PM 6:40 PM MW Le 
b[12].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[12].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[12].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[12].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[12].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[12].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[12].sect_bids.append((29, 2))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[12].sect_bids.append((30, 2))  # 227 8:00 AM 8:50 AM MTWTh
b[12].sect_bids.append((31, 2))  # 227 8:00 AM 10:05 AM MW
b[12].sect_bids.append((32, 2))  # 227 8:00 AM 10:05 AM TTh
b[12].sect_bids.append((33, 2))  # 227 9:35 AM 10:25 AM MTWTh
b[12].sect_bids.append((34, 2))  # 227 9:35 AM 11:40 AM MW 
b[12].sect_bids.append((35, 2))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[12].sect_bids.append((36, 2))  # 227 10:10 AM 11:00 AM MTWTh
b[12].sect_bids.append((37, 2))  # 227 10:10 AM 11:00 AM MTWTh
b[12].sect_bids.append((38, 2))  # 227 10:30 AM 12:35 PM MW 
b[12].sect_bids.append((39, 2))  # 227 10:30 AM 12:35 PM TTh
b[12].sect_bids.append((40, 2))  # 227 11:10 AM 1:15 PM MW
b[12].sect_bids.append((41, 2))  # 227 11:10 AM 1:15 PM TTh
b[12].sect_bids.append((42, 2))  # 227 11:45 AM 12:35 PM MTWTh
b[12].sect_bids.append((43, 2))  # 227 11:45 AM 12:35 PM MTWTh
b[12].sect_bids.append((44, 2))  # 227 12:45 PM 2:50 PM MW
b[12].sect_bids.append((45, 2))  # 227 12:45 PM 2:50 PM MW
b[12].sect_bids.append((46, 2))  # 227 12:45 PM 2:50 PM TTh
b[12].sect_bids.append((47, 2)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[12].sect_bids.append((48, -1))  # 227 4:35 PM 6:40 PM MW
b[12].sect_bids.append((49, -1))  # 227 4:35 PM 6:40 PM TTh
b[12].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[12].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[12].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[12].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[12].sect_bids.append((54, 1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[12].sect_bids.append((55, 1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[12].sect_bids.append((56, 1))  # 228A 8:00 AM 9:10 AM MTWTh
b[12].sect_bids.append((57, 1))  # 228A 12:45 PM 3:15 PM MW
b[12].sect_bids.append((58, 1))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[12].sect_bids.append((59, 1))  # 228A 7:00 PM 9:30 PM MW
b[12].sect_bids.append((60, 1))  # 228A 7:00 PM 9:30 PM TTh 
b[12].sect_bids.append((61, 1))  # 228B 8:00 AM 9:10 AM MTWTh
b[12].sect_bids.append((62, 1))  # 228B 12:45 PM 3:15 PM MW 
b[12].sect_bids.append((63, -1))  # 228B 4:10 PM 6:40 PM MW
b[12].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[12].sect_bids.append((65, 0))  # 238 8:00 AM 9:10 AM MTWTh
b[12].sect_bids.append((66, 0))  # 238 9:35 AM 10:45 AM MTWTh
b[12].sect_bids.append((67, 0))  # 238 11:10 AM 12:20 PM MTWTh
b[12].sect_bids.append((68, -2))  # 238 4:10 PM 6:40 PM MW 
b[12].sect_bids.append((69, -2))  # 238 4:10 PM 6:40 PM TTh
b[12].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[12].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[12].sect_bids.append((72, 2))  # 240 8:00 AM 9:25 AM MW
b[12].sect_bids.append((73, 2))  # 240 8:00 AM 9:25 AM TTh
b[12].sect_bids.append((74, 2))  # 240 9:35 AM 11:00 AM MW
b[12].sect_bids.append((75, 2))  # 240 9:35 AM 11:00 AM TTh
b[12].sect_bids.append((76, 2))  # 240 11:10 AM 12:35 PM MW 
b[12].sect_bids.append((77, 2))  # 240 11:10 AM 12:35 PM TTh 
b[12].sect_bids.append((78, 2))  # 240 12:45 PM 2:10 PM MW
b[12].sect_bids.append((79, 2))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[12].sect_bids.append((80, 2))  # 240 12:45 PM 2:10 PM MW
b[12].sect_bids.append((81, 2))  # 240 3:40 PM 5:05 PM TTh
b[12].sect_bids.append((82, 2))  # 240 3:40 PM 5:05 PM MW
b[12].sect_bids.append((83, -1))  # 240 5:15 PM 6:40 PM TTh
b[12].sect_bids.append((84, -1))  # 240 5:15 PM 6:40 PM MW Harandian
b[12].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[12].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[12].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[12].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[12].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[12].sect_bids.append((90, 4))  # 260 8:00 AM 9:10 AM MTWTh
b[12].sect_bids.append((91, 4))  # 260 9:35 AM 10:45 AM MTWTh
b[12].sect_bids.append((92, 4))  # 260 11:10 AM 12:20 PM MTWTh
b[12].sect_bids.append((93, 4))  # 260 12:45 PM 1:55 PM MTWTh
b[12].sect_bids.append((94, 4))  # 260 12:45 PM 3:15 PM MW
b[12].sect_bids.append((95, 4))  # 260 2:25 PM 3:35 PM MTWTh
b[12].sect_bids.append((96, 4))  # 260 2:25 PM 3:35 PM MTWTh
b[12].sect_bids.append((97, -1))  # 260 4:10 PM 6:40 PM MW
b[12].sect_bids.append((98, -1))  # 260 4:10 PM 6:40 PM TTh
b[12].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[12].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[12].sect_bids.append((101, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[12].sect_bids.append((102, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[12].sect_bids.append((103, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[12].sect_bids.append((104, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[12].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[12].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[12].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[12].sect_bids.append((108, -1))  # 261 4:10 PM 6:40 PM MW Martinez
b[12].sect_bids.append((109, -1))  # 261 4:10 PM 6:40 PM TTh
b[12].sect_bids.append((110, -3))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[12].sect_bids.append((111, -3))  # 261 7:00 PM 9:30 PM TTh Lin
b[12].sect_bids.append((112, 2))  # 262 8:00 AM 9:10 AM MTWTh
b[12].sect_bids.append((113, 2))  # 262 9:35 AM 10:45 AM MTWTh
b[12].sect_bids.append((114, 2))  # 262 11:10 AM 12:20 PM MTWTh
b[12].sect_bids.append((115, 2))  # 262 11:10 AM 12:20 PM MTWTh
b[12].sect_bids.append((116, -1))  # 262 4:10 PM 6:40 PM TTh
b[12].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[12].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[12].sect_bids.append((119, 2))  # 263 8:00 AM 9:10 AM MTWTh
b[12].sect_bids.append((120, 2))  # 263 9:35 AM 10:45 AM MTWTh
b[12].sect_bids.append((121, 2))  # 263 11:10 AM 12:20 PM MTWT
b[12].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[12].sect_bids.append((123, 2))  # 270 8:00 AM 9:25 AM MW
b[12].sect_bids.append((124, 2))  # 270 12:45 PM 2:10 PM MW
b[12].sect_bids.append((125, -1))  # 270 5:15 PM 6:40 PM TTh
b[12].sect_bids.append((126, 0))  # 275 9:35 AM 11:00 AM TTh
b[12].sect_bids.append((127, 0))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='putnamtc', semester='Fa2019', timestamp=datetime.datetime.now()))
b[13].bid_1_prep = 4
b[13].bid_2_prep = 5
b[13].bid_3_prep = 0
b[13].bid_4_prep = -2
b[13].bid_5_prep = -5
b[13].min_acc_units = 14
b[13].max_acc_units = 16
b[13].min_des_units = 14
b[13].max_des_units = 15
b[13].sect_bids.append((1, -5))  # 110 8:00 am MTWTh adj
b[13].sect_bids.append((2, -5))  # 110 9:35 am MTWTh adj 
b[13].sect_bids.append((3, -5))  # 110 4:10 PM MW adj
b[13].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[13].sect_bids.append((5, -5))  # 110 8:00 AM MTWTh adj
b[13].sect_bids.append((6, -5))  # 115 8:00 AM MTWTh 
b[13].sect_bids.append((7, -5))  # 115 11:10 AM MTWTh
b[13].sect_bids.append((8, -5))  # 115 12:45 PM MW
b[13].sect_bids.append((9, -5))  # 115 12:45 PM TTh
b[13].sect_bids.append((10, -5))  # 115 4:10 PM TTh
b[13].sect_bids.append((11, 4))  # 134 8:00 AM MTWTh LEHAVI
b[13].sect_bids.append((12, 4))  # 134 8:00 AM MTWTh
b[13].sect_bids.append((13, 4))  # 134 8:00 AM MTWTh
b[13].sect_bids.append((14, 4))  # 134 9:35 AM MTWTh
b[13].sect_bids.append((15, 4))  # 134 9:35 AM MTWTh
b[13].sect_bids.append((16, 4))  # 134 11:10 AM MTWTh
b[13].sect_bids.append((17, 4)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[13].sect_bids.append((18, 4)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[13].sect_bids.append((19, 4)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[13].sect_bids.append((20, 4))  # 134 12:45 PM 3:55 PM MW 
b[13].sect_bids.append((21, 4))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[13].sect_bids.append((22, 4))  # 134 3:30 PM 6:40 PM MW Le 
b[13].sect_bids.append((23, 2))  # 6:50 PM 10:00 PM MW Grigoryan 
b[13].sect_bids.append((24, 2))  # 134 6:50 PM 10:00 PM MW
b[13].sect_bids.append((25, 2))  # 134 6:50 PM 10:00 PM TTh 
b[13].sect_bids.append((26, 2))  # 134 6:50 PM 10:00 PM TTh
b[13].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[13].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[13].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[13].sect_bids.append((30, -5))  # 227 8:00 AM 8:50 AM MTWTh
b[13].sect_bids.append((31, -5))  # 227 8:00 AM 10:05 AM MW
b[13].sect_bids.append((32, -5))  # 227 8:00 AM 10:05 AM TTh
b[13].sect_bids.append((33, -5))  # 227 9:35 AM 10:25 AM MTWTh
b[13].sect_bids.append((34, -5))  # 227 9:35 AM 11:40 AM MW 
b[13].sect_bids.append((35, -5))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[13].sect_bids.append((36, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[13].sect_bids.append((37, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[13].sect_bids.append((38, -5))  # 227 10:30 AM 12:35 PM MW 
b[13].sect_bids.append((39, -5))  # 227 10:30 AM 12:35 PM TTh
b[13].sect_bids.append((40, -5))  # 227 11:10 AM 1:15 PM MW
b[13].sect_bids.append((41, -5))  # 227 11:10 AM 1:15 PM TTh
b[13].sect_bids.append((42, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[13].sect_bids.append((43, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[13].sect_bids.append((44, -5))  # 227 12:45 PM 2:50 PM MW
b[13].sect_bids.append((45, -5))  # 227 12:45 PM 2:50 PM MW
b[13].sect_bids.append((46, -5))  # 227 12:45 PM 2:50 PM TTh
b[13].sect_bids.append((47, -5)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[13].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[13].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[13].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[13].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[13].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[13].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[13].sect_bids.append((54, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[13].sect_bids.append((55, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[13].sect_bids.append((56, -5))  # 228A 8:00 AM 9:10 AM MTWTh
b[13].sect_bids.append((57, -5))  # 228A 12:45 PM 3:15 PM MW
b[13].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[13].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[13].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[13].sect_bids.append((61, -5))  # 228B 8:00 AM 9:10 AM MTWTh
b[13].sect_bids.append((62, -5))  # 228B 12:45 PM 3:15 PM MW 
b[13].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[13].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[13].sect_bids.append((65, -5))  # 238 8:00 AM 9:10 AM MTWTh
b[13].sect_bids.append((66, -5))  # 238 9:35 AM 10:45 AM MTWTh
b[13].sect_bids.append((67, -5))  # 238 11:10 AM 12:20 PM MTWTh
b[13].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[13].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[13].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[13].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[13].sect_bids.append((72, -5))  # 240 8:00 AM 9:25 AM MW
b[13].sect_bids.append((73, -5))  # 240 8:00 AM 9:25 AM TTh
b[13].sect_bids.append((74, -5))  # 240 9:35 AM 11:00 AM MW
b[13].sect_bids.append((75, -5))  # 240 9:35 AM 11:00 AM TTh
b[13].sect_bids.append((76, -5))  # 240 11:10 AM 12:35 PM MW 
b[13].sect_bids.append((77, -5))  # 240 11:10 AM 12:35 PM TTh 
b[13].sect_bids.append((78, -5))  # 240 12:45 PM 2:10 PM MW
b[13].sect_bids.append((79, -5))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[13].sect_bids.append((80, -5))  # 240 12:45 PM 2:10 PM MW
b[13].sect_bids.append((81, -5))  # 240 3:40 PM 5:05 PM TTh
b[13].sect_bids.append((82, -5))  # 240 3:40 PM 5:05 PM MW
b[13].sect_bids.append((83, -5))  # 240 5:15 PM 6:40 PM TTh
b[13].sect_bids.append((84, -5))  # 240 5:15 PM 6:40 PM MW Harandian
b[13].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[13].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[13].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[13].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[13].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[13].sect_bids.append((90, 5))  # 260 8:00 AM 9:10 AM MTWTh
b[13].sect_bids.append((91, 5))  # 260 9:35 AM 10:45 AM MTWTh
b[13].sect_bids.append((92, 5))  # 260 11:10 AM 12:20 PM MTWTh
b[13].sect_bids.append((93, 5))  # 260 12:45 PM 1:55 PM MTWTh
b[13].sect_bids.append((94, 5))  # 260 12:45 PM 3:15 PM MW
b[13].sect_bids.append((95, 5))  # 260 2:25 PM 3:35 PM MTWTh
b[13].sect_bids.append((96, 5))  # 260 2:25 PM 3:35 PM MTWTh
b[13].sect_bids.append((97, 5))  # 260 4:10 PM 6:40 PM MW
b[13].sect_bids.append((98, 5))  # 260 4:10 PM 6:40 PM TTh
b[13].sect_bids.append((99, 4))  # 260 7:00 PM 9:30 PM MW
b[13].sect_bids.append((100, 3))  # 260 7:00 PM 9:30 PM TTh
b[13].sect_bids.append((101, -5))  # 261 8:00 AM 9:10 AM MTWTh
b[13].sect_bids.append((102, -5))  # 261 8:00 AM 9:10 AM MTWTh
b[13].sect_bids.append((103, -5))  # 261 9:35 AM 10:45 AM MTWTh
b[13].sect_bids.append((104, -5))  # 261 9:35 AM 10:45 AM MTWTh
b[13].sect_bids.append((105, -5))  # 261 11:10 AM 12:20 PM MTWTh
b[13].sect_bids.append((106, -5))  # 261 12:45 PM 3:15 PM MW
b[13].sect_bids.append((107, -5))  # 261 2:25 PM 3:35 PM MTWTh
b[13].sect_bids.append((108, -5))  # 261 4:10 PM 6:40 PM MW Martinez
b[13].sect_bids.append((109, -5))  # 261 4:10 PM 6:40 PM TTh
b[13].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[13].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[13].sect_bids.append((112, -5))  # 262 8:00 AM 9:10 AM MTWTh
b[13].sect_bids.append((113, -5))  # 262 9:35 AM 10:45 AM MTWTh
b[13].sect_bids.append((114, -5))  # 262 11:10 AM 12:20 PM MTWTh
b[13].sect_bids.append((115, -5))  # 262 11:10 AM 12:20 PM MTWTh
b[13].sect_bids.append((116, -5))  # 262 4:10 PM 6:40 PM TTh
b[13].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[13].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[13].sect_bids.append((119, -5))  # 263 8:00 AM 9:10 AM MTWTh
b[13].sect_bids.append((120, -5))  # 263 9:35 AM 10:45 AM MTWTh
b[13].sect_bids.append((121, -5))  # 263 11:10 AM 12:20 PM MTWT
b[13].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[13].sect_bids.append((123, -5))  # 270 8:00 AM 9:25 AM MW
b[13].sect_bids.append((124, -5))  # 270 12:45 PM 2:10 PM MW
b[13].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[13].sect_bids.append((126, -5))  # 275 9:35 AM 11:00 AM TTh
b[13].sect_bids.append((127, -5))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='rashidmm', semester='Fa2019', timestamp=datetime.datetime.now()))
b[14].bid_1_prep = 4
b[14].bid_2_prep = 5
b[14].bid_3_prep = 0
b[14].bid_4_prep = -2
b[14].bid_5_prep = -5
b[14].min_acc_units = 13
b[14].max_acc_units = 17
b[14].min_des_units = 14
b[14].max_des_units = 16
b[14].sect_bids.append((1, -2))  # 110 8:00 am MTWTh adj
b[14].sect_bids.append((2, -2))  # 110 9:35 am MTWTh adj 
b[14].sect_bids.append((3, -5))  # 110 4:10 PM MW adj
b[14].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[14].sect_bids.append((5, -2))  # 110 8:00 AM MTWTh adj
b[14].sect_bids.append((6, 4))  # 115 8:00 AM MTWTh 
b[14].sect_bids.append((7, 4))  # 115 11:10 AM MTWTh
b[14].sect_bids.append((8, 4))  # 115 12:45 PM MW
b[14].sect_bids.append((9, 4))  # 115 12:45 PM TTh
b[14].sect_bids.append((10, -5))  # 115 4:10 PM TTh
b[14].sect_bids.append((11, 4))  # 134 8:00 AM MTWTh LEHAVI
b[14].sect_bids.append((12, 4))  # 134 8:00 AM MTWTh
b[14].sect_bids.append((13, 4))  # 134 8:00 AM MTWTh
b[14].sect_bids.append((14, 4))  # 134 9:35 AM MTWTh
b[14].sect_bids.append((15, 4))  # 134 9:35 AM MTWTh
b[14].sect_bids.append((16, 4))  # 134 11:10 AM MTWTh
b[14].sect_bids.append((17, 4)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[14].sect_bids.append((18, 4)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[14].sect_bids.append((19, 4)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[14].sect_bids.append((20, -3))  # 134 12:45 PM 3:55 PM MW 
b[14].sect_bids.append((21, -5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[14].sect_bids.append((22, -5))  # 134 3:30 PM 6:40 PM MW Le 
b[14].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[14].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[14].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[14].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[14].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[14].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[14].sect_bids.append((29, 3))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[14].sect_bids.append((30, 3))  # 227 8:00 AM 8:50 AM MTWTh
b[14].sect_bids.append((31, 3))  # 227 8:00 AM 10:05 AM MW
b[14].sect_bids.append((32, 3))  # 227 8:00 AM 10:05 AM TTh
b[14].sect_bids.append((33, 3))  # 227 9:35 AM 10:25 AM MTWTh
b[14].sect_bids.append((34, 3))  # 227 9:35 AM 11:40 AM MW 
b[14].sect_bids.append((35, 3))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[14].sect_bids.append((36, 3))  # 227 10:10 AM 11:00 AM MTWTh
b[14].sect_bids.append((37, 3))  # 227 10:10 AM 11:00 AM MTWTh
b[14].sect_bids.append((38, 3))  # 227 10:30 AM 12:35 PM MW 
b[14].sect_bids.append((39, 3))  # 227 10:30 AM 12:35 PM TTh
b[14].sect_bids.append((40, 3))  # 227 11:10 AM 1:15 PM MW
b[14].sect_bids.append((41, 3))  # 227 11:10 AM 1:15 PM TTh
b[14].sect_bids.append((42, 3))  # 227 11:45 AM 12:35 PM MTWTh
b[14].sect_bids.append((43, 3))  # 227 11:45 AM 12:35 PM MTWTh
b[14].sect_bids.append((44, 3))  # 227 12:45 PM 2:50 PM MW
b[14].sect_bids.append((45, 3))  # 227 12:45 PM 2:50 PM MW
b[14].sect_bids.append((46, 3))  # 227 12:45 PM 2:50 PM TTh
b[14].sect_bids.append((47, 3)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[14].sect_bids.append((48, -3))  # 227 4:35 PM 6:40 PM MW
b[14].sect_bids.append((49, -3))  # 227 4:35 PM 6:40 PM TTh
b[14].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[14].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[14].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[14].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[14].sect_bids.append((54, 1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[14].sect_bids.append((55, 1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[14].sect_bids.append((56, 1))  # 228A 8:00 AM 9:10 AM MTWTh
b[14].sect_bids.append((57, 1))  # 228A 12:45 PM 3:15 PM MW
b[14].sect_bids.append((58, 1))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[14].sect_bids.append((59, 1))  # 228A 7:00 PM 9:30 PM MW
b[14].sect_bids.append((60, 1))  # 228A 7:00 PM 9:30 PM TTh 
b[14].sect_bids.append((61, 1))  # 228B 8:00 AM 9:10 AM MTWTh
b[14].sect_bids.append((62, 1))  # 228B 12:45 PM 3:15 PM MW 
b[14].sect_bids.append((63, 1))  # 228B 4:10 PM 6:40 PM MW
b[14].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[14].sect_bids.append((65, 0))  # 238 8:00 AM 9:10 AM MTWTh
b[14].sect_bids.append((66, 0))  # 238 9:35 AM 10:45 AM MTWTh
b[14].sect_bids.append((67, 0))  # 238 11:10 AM 12:20 PM MTWTh
b[14].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[14].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[14].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[14].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[14].sect_bids.append((72, -2))  # 240 8:00 AM 9:25 AM MW
b[14].sect_bids.append((73, -2))  # 240 8:00 AM 9:25 AM TTh
b[14].sect_bids.append((74, -2))  # 240 9:35 AM 11:00 AM MW
b[14].sect_bids.append((75, -2))  # 240 9:35 AM 11:00 AM TTh
b[14].sect_bids.append((76, -2))  # 240 11:10 AM 12:35 PM MW 
b[14].sect_bids.append((77, -2))  # 240 11:10 AM 12:35 PM TTh 
b[14].sect_bids.append((78, -2))  # 240 12:45 PM 2:10 PM MW
b[14].sect_bids.append((79, -2))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[14].sect_bids.append((80, -2))  # 240 12:45 PM 2:10 PM MW
b[14].sect_bids.append((81, -3))  # 240 3:40 PM 5:05 PM TTh
b[14].sect_bids.append((82, -3))  # 240 3:40 PM 5:05 PM MW
b[14].sect_bids.append((83, -5))  # 240 5:15 PM 6:40 PM TTh
b[14].sect_bids.append((84, -5))  # 240 5:15 PM 6:40 PM MW Harandian
b[14].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[14].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[14].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[14].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[14].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[14].sect_bids.append((90, 1))  # 260 8:00 AM 9:10 AM MTWTh
b[14].sect_bids.append((91, 1))  # 260 9:35 AM 10:45 AM MTWTh
b[14].sect_bids.append((92, 1))  # 260 11:10 AM 12:20 PM MTWTh
b[14].sect_bids.append((93, 1))  # 260 12:45 PM 1:55 PM MTWTh
b[14].sect_bids.append((94, 1))  # 260 12:45 PM 3:15 PM MW
b[14].sect_bids.append((95, 1))  # 260 2:25 PM 3:35 PM MTWTh
b[14].sect_bids.append((96, 1))  # 260 2:25 PM 3:35 PM MTWTh
b[14].sect_bids.append((97, -3))  # 260 4:10 PM 6:40 PM MW
b[14].sect_bids.append((98, -3))  # 260 4:10 PM 6:40 PM TTh
b[14].sect_bids.append((99, -3))  # 260 7:00 PM 9:30 PM MW
b[14].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[14].sect_bids.append((101, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[14].sect_bids.append((102, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[14].sect_bids.append((103, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[14].sect_bids.append((104, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[14].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[14].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[14].sect_bids.append((107, 0))  # 261 2:25 PM 3:35 PM MTWTh
b[14].sect_bids.append((108, -3))  # 261 4:10 PM 6:40 PM MW Martinez
b[14].sect_bids.append((109, -3))  # 261 4:10 PM 6:40 PM TTh
b[14].sect_bids.append((110, -4))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[14].sect_bids.append((111, -4))  # 261 7:00 PM 9:30 PM TTh Lin
b[14].sect_bids.append((112, 5))  # 262 8:00 AM 9:10 AM MTWTh
b[14].sect_bids.append((113, 5))  # 262 9:35 AM 10:45 AM MTWTh
b[14].sect_bids.append((114, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[14].sect_bids.append((115, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[14].sect_bids.append((116, -4))  # 262 4:10 PM 6:40 PM TTh
b[14].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[14].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[14].sect_bids.append((119, 3))  # 263 8:00 AM 9:10 AM MTWTh
b[14].sect_bids.append((120, 3))  # 263 9:35 AM 10:45 AM MTWTh
b[14].sect_bids.append((121, 3))  # 263 11:10 AM 12:20 PM MTWT
b[14].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[14].sect_bids.append((123, 0))  # 270 8:00 AM 9:25 AM MW
b[14].sect_bids.append((124, 0))  # 270 12:45 PM 2:10 PM MW
b[14].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[14].sect_bids.append((126, -1))  # 275 9:35 AM 11:00 AM TTh
b[14].sect_bids.append((127, -1))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='schweshr', semester='Fa2019', timestamp=datetime.datetime.now()))
b[15].bid_1_prep = 4
b[15].bid_2_prep = 5
b[15].bid_3_prep = 2
b[15].bid_4_prep = -1
b[15].bid_5_prep = -2
b[15].min_acc_units = 15
b[15].max_acc_units = 20
b[15].min_des_units = 17
b[15].max_des_units = 18
b[15].sect_bids.append((1, -5))  # 110 8:00 am MTWTh adj
b[15].sect_bids.append((2, -5))  # 110 9:35 am MTWTh adj 
b[15].sect_bids.append((3, -5))  # 110 4:10 PM MW adj
b[15].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[15].sect_bids.append((5, -5))  # 110 8:00 AM MTWTh adj
b[15].sect_bids.append((6, -5))  # 115 8:00 AM MTWTh 
b[15].sect_bids.append((7, 1))  # 115 11:10 AM MTWTh
b[15].sect_bids.append((8, 1))  # 115 12:45 PM MW
b[15].sect_bids.append((9, 1))  # 115 12:45 PM TTh
b[15].sect_bids.append((10, 1))  # 115 4:10 PM TTh
b[15].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[15].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[15].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[15].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[15].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[15].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[15].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[15].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[15].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[15].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[15].sect_bids.append((21, 5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[15].sect_bids.append((22, 5))  # 134 3:30 PM 6:40 PM MW Le 
b[15].sect_bids.append((23, -3))  # 6:50 PM 10:00 PM MW Grigoryan 
b[15].sect_bids.append((24, -3))  # 134 6:50 PM 10:00 PM MW
b[15].sect_bids.append((25, -3))  # 134 6:50 PM 10:00 PM TTh 
b[15].sect_bids.append((26, -3))  # 134 6:50 PM 10:00 PM TTh
b[15].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[15].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[15].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[15].sect_bids.append((30, -5))  # 227 8:00 AM 8:50 AM MTWTh
b[15].sect_bids.append((31, -5))  # 227 8:00 AM 10:05 AM MW
b[15].sect_bids.append((32, -5))  # 227 8:00 AM 10:05 AM TTh
b[15].sect_bids.append((33, -5))  # 227 9:35 AM 10:25 AM MTWTh
b[15].sect_bids.append((34, -5))  # 227 9:35 AM 11:40 AM MW 
b[15].sect_bids.append((35, -5))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[15].sect_bids.append((36, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[15].sect_bids.append((37, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[15].sect_bids.append((38, -5))  # 227 10:30 AM 12:35 PM MW 
b[15].sect_bids.append((39, -5))  # 227 10:30 AM 12:35 PM TTh
b[15].sect_bids.append((40, -5))  # 227 11:10 AM 1:15 PM MW
b[15].sect_bids.append((41, -5))  # 227 11:10 AM 1:15 PM TTh
b[15].sect_bids.append((42, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[15].sect_bids.append((43, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[15].sect_bids.append((44, -5))  # 227 12:45 PM 2:50 PM MW
b[15].sect_bids.append((45, -5))  # 227 12:45 PM 2:50 PM MW
b[15].sect_bids.append((46, -5))  # 227 12:45 PM 2:50 PM TTh
b[15].sect_bids.append((47, -5)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[15].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[15].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[15].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[15].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[15].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[15].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[15].sect_bids.append((54, 2))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[15].sect_bids.append((55, 2))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[15].sect_bids.append((56, -5))  # 228A 8:00 AM 9:10 AM MTWTh
b[15].sect_bids.append((57, 2))  # 228A 12:45 PM 3:15 PM MW
b[15].sect_bids.append((58, 2))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[15].sect_bids.append((59, -3))  # 228A 7:00 PM 9:30 PM MW
b[15].sect_bids.append((60, -3))  # 228A 7:00 PM 9:30 PM TTh 
b[15].sect_bids.append((61, -5))  # 228B 8:00 AM 9:10 AM MTWTh
b[15].sect_bids.append((62, 2))  # 228B 12:45 PM 3:15 PM MW 
b[15].sect_bids.append((63, 2))  # 228B 4:10 PM 6:40 PM MW
b[15].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[15].sect_bids.append((65, -5))  # 238 8:00 AM 9:10 AM MTWTh
b[15].sect_bids.append((66, -5))  # 238 9:35 AM 10:45 AM MTWTh
b[15].sect_bids.append((67, -5))  # 238 11:10 AM 12:20 PM MTWTh
b[15].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[15].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[15].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[15].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[15].sect_bids.append((72, -3))  # 240 8:00 AM 9:25 AM MW
b[15].sect_bids.append((73, -3))  # 240 8:00 AM 9:25 AM TTh
b[15].sect_bids.append((74, 5))  # 240 9:35 AM 11:00 AM MW
b[15].sect_bids.append((75, 5))  # 240 9:35 AM 11:00 AM TTh
b[15].sect_bids.append((76, 5))  # 240 11:10 AM 12:35 PM MW 
b[15].sect_bids.append((77, 5))  # 240 11:10 AM 12:35 PM TTh 
b[15].sect_bids.append((78, 5))  # 240 12:45 PM 2:10 PM MW
b[15].sect_bids.append((79, 5))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[15].sect_bids.append((80, 5))  # 240 12:45 PM 2:10 PM MW
b[15].sect_bids.append((81, 5))  # 240 3:40 PM 5:05 PM TTh
b[15].sect_bids.append((82, 5))  # 240 3:40 PM 5:05 PM MW
b[15].sect_bids.append((83, 5))  # 240 5:15 PM 6:40 PM TTh
b[15].sect_bids.append((84, 5))  # 240 5:15 PM 6:40 PM MW Harandian
b[15].sect_bids.append((85, 5))  # 240 7:00 PM 8:25 PM MW
b[15].sect_bids.append((86, 5))  # 240 7:00 PM 8:25 PM TTh
b[15].sect_bids.append((87, 5))  # 240 7:00 PM 8:25 PM TTh
b[15].sect_bids.append((88, -4))  # 240 8:35 PM 10:00 PM MW 
b[15].sect_bids.append((89, -4))  # 240 8:35 PM 10:00 PM TTh 
b[15].sect_bids.append((90, 3))  # 260 8:00 AM 9:10 AM MTWTh
b[15].sect_bids.append((91, 3))  # 260 9:35 AM 10:45 AM MTWTh
b[15].sect_bids.append((92, 3))  # 260 11:10 AM 12:20 PM MTWTh
b[15].sect_bids.append((93, 3))  # 260 12:45 PM 1:55 PM MTWTh
b[15].sect_bids.append((94, 3))  # 260 12:45 PM 3:15 PM MW
b[15].sect_bids.append((95, 3))  # 260 2:25 PM 3:35 PM MTWTh
b[15].sect_bids.append((96, 3))  # 260 2:25 PM 3:35 PM MTWTh
b[15].sect_bids.append((97, 3))  # 260 4:10 PM 6:40 PM MW
b[15].sect_bids.append((98, 3))  # 260 4:10 PM 6:40 PM TTh
b[15].sect_bids.append((99, -3))  # 260 7:00 PM 9:30 PM MW
b[15].sect_bids.append((100,-3 ))  # 260 7:00 PM 9:30 PM TTh
b[15].sect_bids.append((101, -1))  # 261 8:00 AM 9:10 AM MTWTh
b[15].sect_bids.append((102, -1))  # 261 8:00 AM 9:10 AM MTWTh
b[15].sect_bids.append((103, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[15].sect_bids.append((104, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[15].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[15].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[15].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[15].sect_bids.append((108, 5))  # 261 4:10 PM 6:40 PM MW Martinez
b[15].sect_bids.append((109, 5))  # 261 4:10 PM 6:40 PM TTh
b[15].sect_bids.append((110, -1))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[15].sect_bids.append((111, -1))  # 261 7:00 PM 9:30 PM TTh Lin
b[15].sect_bids.append((112, -1))  # 262 8:00 AM 9:10 AM MTWTh
b[15].sect_bids.append((113, 5))  # 262 9:35 AM 10:45 AM MTWTh
b[15].sect_bids.append((114, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[15].sect_bids.append((115, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[15].sect_bids.append((116, 5))  # 262 4:10 PM 6:40 PM TTh
b[15].sect_bids.append((117, -1))  # 262 7:00 PM 9:30 PM MW
b[15].sect_bids.append((118, -1))  # 262 7:00 PM 9:30 PM TTh
b[15].sect_bids.append((119, -1))  # 263 8:00 AM 9:10 AM MTWTh
b[15].sect_bids.append((120, 5))  # 263 9:35 AM 10:45 AM MTWTh
b[15].sect_bids.append((121, 5))  # 263 11:10 AM 12:20 PM MTWT
b[15].sect_bids.append((122, 5))  # 263 7:00 PM 9:30 PM TTh
b[15].sect_bids.append((123, -1))  # 270 8:00 AM 9:25 AM MW
b[15].sect_bids.append((124, 4))  # 270 12:45 PM 2:10 PM MW
b[15].sect_bids.append((125, 4))  # 270 5:15 PM 6:40 PM TTh
b[15].sect_bids.append((126, 4))  # 275 9:35 AM 11:00 AM TTh
b[15].sect_bids.append((127, 4))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='semerdy', semester='Fa2019', timestamp=datetime.datetime.now()))
b[16].bid_1_prep = 4
b[16].bid_2_prep = 5
b[16].bid_3_prep = 0
b[16].bid_4_prep = -2
b[16].bid_5_prep = -5
b[16].min_acc_units = 15
b[16].max_acc_units = 17
b[16].min_des_units = 15
b[16].max_des_units = 16
b[16].sect_bids.append((1, -5))  # 110 8:00 am MTWTh adj
b[16].sect_bids.append((2, -5))  # 110 9:35 am MTWTh adj 
b[16].sect_bids.append((3, -5))  # 110 4:10 PM MW adj
b[16].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[16].sect_bids.append((5, -5))  # 110 8:00 AM MTWTh adj
b[16].sect_bids.append((6, 5))  # 115 8:00 AM MTWTh 
b[16].sect_bids.append((7, 5))  # 115 11:10 AM MTWTh
b[16].sect_bids.append((8, 5))  # 115 12:45 PM MW
b[16].sect_bids.append((9, 5))  # 115 12:45 PM TTh
b[16].sect_bids.append((10, 5))  # 115 4:10 PM TTh
b[16].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[16].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[16].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[16].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[16].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[16].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[16].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[16].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[16].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[16].sect_bids.append((20, 2))  # 134 12:45 PM 3:55 PM MW 
b[16].sect_bids.append((21, -5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[16].sect_bids.append((22, -5))  # 134 3:30 PM 6:40 PM MW Le 
b[16].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[16].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[16].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[16].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[16].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[16].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[16].sect_bids.append((29, -3))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[16].sect_bids.append((30, -3))  # 227 8:00 AM 8:50 AM MTWTh
b[16].sect_bids.append((31, -3))  # 227 8:00 AM 10:05 AM MW
b[16].sect_bids.append((32, -3))  # 227 8:00 AM 10:05 AM TTh
b[16].sect_bids.append((33, -3))  # 227 9:35 AM 10:25 AM MTWTh
b[16].sect_bids.append((34, -3))  # 227 9:35 AM 11:40 AM MW 
b[16].sect_bids.append((35, -3))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[16].sect_bids.append((36, -3))  # 227 10:10 AM 11:00 AM MTWTh
b[16].sect_bids.append((37, -3))  # 227 10:10 AM 11:00 AM MTWTh
b[16].sect_bids.append((38, -3))  # 227 10:30 AM 12:35 PM MW 
b[16].sect_bids.append((39, -3))  # 227 10:30 AM 12:35 PM TTh
b[16].sect_bids.append((40, -3))  # 227 11:10 AM 1:15 PM MW
b[16].sect_bids.append((41, -3))  # 227 11:10 AM 1:15 PM TTh
b[16].sect_bids.append((42, -3))  # 227 11:45 AM 12:35 PM MTWTh
b[16].sect_bids.append((43, -3))  # 227 11:45 AM 12:35 PM MTWTh
b[16].sect_bids.append((44, -3))  # 227 12:45 PM 2:50 PM MW
b[16].sect_bids.append((45, -3))  # 227 12:45 PM 2:50 PM MW
b[16].sect_bids.append((46, -3))  # 227 12:45 PM 2:50 PM TTh
b[16].sect_bids.append((47, -3)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[16].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[16].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[16].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[16].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[16].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[16].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[16].sect_bids.append((54, -3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[16].sect_bids.append((55, -3))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[16].sect_bids.append((56, -3))  # 228A 8:00 AM 9:10 AM MTWTh
b[16].sect_bids.append((57, -3))  # 228A 12:45 PM 3:15 PM MW
b[16].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[16].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[16].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[16].sect_bids.append((61, -3))  # 228B 8:00 AM 9:10 AM MTWTh
b[16].sect_bids.append((62, -5))  # 228B 12:45 PM 3:15 PM MW 
b[16].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[16].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[16].sect_bids.append((65, 3))  # 238 8:00 AM 9:10 AM MTWTh
b[16].sect_bids.append((66, 3))  # 238 9:35 AM 10:45 AM MTWTh
b[16].sect_bids.append((67, 3))  # 238 11:10 AM 12:20 PM MTWTh
b[16].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[16].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[16].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[16].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[16].sect_bids.append((72, 2))  # 240 8:00 AM 9:25 AM MW
b[16].sect_bids.append((73, 2))  # 240 8:00 AM 9:25 AM TTh
b[16].sect_bids.append((74, 2))  # 240 9:35 AM 11:00 AM MW
b[16].sect_bids.append((75, 2))  # 240 9:35 AM 11:00 AM TTh
b[16].sect_bids.append((76, 2))  # 240 11:10 AM 12:35 PM MW 
b[16].sect_bids.append((77, 2))  # 240 11:10 AM 12:35 PM TTh 
b[16].sect_bids.append((78, 2))  # 240 12:45 PM 2:10 PM MW
b[16].sect_bids.append((79, 2))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[16].sect_bids.append((80, 2))  # 240 12:45 PM 2:10 PM MW
b[16].sect_bids.append((81, -5))  # 240 3:40 PM 5:05 PM TTh
b[16].sect_bids.append((82, -5))  # 240 3:40 PM 5:05 PM MW
b[16].sect_bids.append((83, -5))  # 240 5:15 PM 6:40 PM TTh
b[16].sect_bids.append((84, -5))  # 240 5:15 PM 6:40 PM MW Harandian
b[16].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[16].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[16].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[16].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[16].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[16].sect_bids.append((90, 3))  # 260 8:00 AM 9:10 AM MTWTh
b[16].sect_bids.append((91, 3))  # 260 9:35 AM 10:45 AM MTWTh
b[16].sect_bids.append((92, 3))  # 260 11:10 AM 12:20 PM MTWTh
b[16].sect_bids.append((93, 3))  # 260 12:45 PM 1:55 PM MTWTh
b[16].sect_bids.append((94, -1))  # 260 12:45 PM 3:15 PM MW
b[16].sect_bids.append((95, -2))  # 260 2:25 PM 3:35 PM MTWTh
b[16].sect_bids.append((96, -2))  # 260 2:25 PM 3:35 PM MTWTh
b[16].sect_bids.append((97, -5))  # 260 4:10 PM 6:40 PM MW
b[16].sect_bids.append((98, -5))  # 260 4:10 PM 6:40 PM TTh
b[16].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[16].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[16].sect_bids.append((101, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[16].sect_bids.append((102, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[16].sect_bids.append((103, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[16].sect_bids.append((104, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[16].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[16].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[16].sect_bids.append((107, 0))  # 261 2:25 PM 3:35 PM MTWTh
b[16].sect_bids.append((108, -5))  # 261 4:10 PM 6:40 PM MW Martinez
b[16].sect_bids.append((109, -5))  # 261 4:10 PM 6:40 PM TTh
b[16].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[16].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[16].sect_bids.append((112, 4))  # 262 8:00 AM 9:10 AM MTWTh
b[16].sect_bids.append((113, 4))  # 262 9:35 AM 10:45 AM MTWTh
b[16].sect_bids.append((114, 4))  # 262 11:10 AM 12:20 PM MTWTh
b[16].sect_bids.append((115, 4))  # 262 11:10 AM 12:20 PM MTWTh
b[16].sect_bids.append((116, -5))  # 262 4:10 PM 6:40 PM TTh
b[16].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[16].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[16].sect_bids.append((119, 3))  # 263 8:00 AM 9:10 AM MTWTh
b[16].sect_bids.append((120, 3))  # 263 9:35 AM 10:45 AM MTWTh
b[16].sect_bids.append((121, 3))  # 263 11:10 AM 12:20 PM MTWT
b[16].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[16].sect_bids.append((123, 0))  # 270 8:00 AM 9:25 AM MW
b[16].sect_bids.append((124, 0))  # 270 12:45 PM 2:10 PM MW
b[16].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[16].sect_bids.append((126, 0))  # 275 9:35 AM 11:00 AM TTh
b[16].sect_bids.append((127, -5))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='sotode2', semester='Fa2019', timestamp=datetime.datetime.now()))
b[17].bid_1_prep = 3
b[17].bid_2_prep = 4
b[17].bid_3_prep = 1
b[17].bid_4_prep = -3
b[17].bid_5_prep = -5
b[17].min_acc_units = 15
b[17].max_acc_units = 20
b[17].min_des_units = 18
b[17].max_des_units = 19
b[17].sect_bids.append((1, 0))  # 110 8:00 am MTWTh adj
b[17].sect_bids.append((2, 0))  # 110 9:35 am MTWTh adj 
b[17].sect_bids.append((3, 0))  # 110 4:10 PM MW adj
b[17].sect_bids.append((4, -5))  # 110 7:00 PM TTh
b[17].sect_bids.append((5, 0))  # 110 8:00 AM MTWTh adj
b[17].sect_bids.append((6, 2))  # 115 8:00 AM MTWTh 
b[17].sect_bids.append((7, 2))  # 115 11:10 AM MTWTh
b[17].sect_bids.append((8, 2))  # 115 12:45 PM MW
b[17].sect_bids.append((9, 2))  # 115 12:45 PM TTh
b[17].sect_bids.append((10, 3))  # 115 4:10 PM TTh
b[17].sect_bids.append((11, 3))  # 134 8:00 AM MTWTh LEHAVI
b[17].sect_bids.append((12, 3))  # 134 8:00 AM MTWTh
b[17].sect_bids.append((13, 3))  # 134 8:00 AM MTWTh
b[17].sect_bids.append((14, 3))  # 134 9:35 AM MTWTh
b[17].sect_bids.append((15, 3))  # 134 9:35 AM MTWTh
b[17].sect_bids.append((16, 3))  # 134 11:10 AM MTWTh
b[17].sect_bids.append((17, 3)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[17].sect_bids.append((18, 3)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[17].sect_bids.append((19, 3)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[17].sect_bids.append((20, 3))  # 134 12:45 PM 3:55 PM MW 
b[17].sect_bids.append((21, 3))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[17].sect_bids.append((22, 3))  # 134 3:30 PM 6:40 PM MW Le 
b[17].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[17].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[17].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[17].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[17].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[17].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[17].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[17].sect_bids.append((30, 2))  # 227 8:00 AM 8:50 AM MTWTh
b[17].sect_bids.append((31, 2))  # 227 8:00 AM 10:05 AM MW
b[17].sect_bids.append((32, 2))  # 227 8:00 AM 10:05 AM TTh
b[17].sect_bids.append((33, 2))  # 227 9:35 AM 10:25 AM MTWTh
b[17].sect_bids.append((34, 2))  # 227 9:35 AM 11:40 AM MW 
b[17].sect_bids.append((35, 2))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[17].sect_bids.append((36, 2))  # 227 10:10 AM 11:00 AM MTWTh
b[17].sect_bids.append((37, 2))  # 227 10:10 AM 11:00 AM MTWTh
b[17].sect_bids.append((38, 2))  # 227 10:30 AM 12:35 PM MW 
b[17].sect_bids.append((39, 2))  # 227 10:30 AM 12:35 PM TTh
b[17].sect_bids.append((40, 2))  # 227 11:10 AM 1:15 PM MW
b[17].sect_bids.append((41, 2))  # 227 11:10 AM 1:15 PM TTh
b[17].sect_bids.append((42, 2))  # 227 11:45 AM 12:35 PM MTWTh
b[17].sect_bids.append((43, 2))  # 227 11:45 AM 12:35 PM MTWTh
b[17].sect_bids.append((44, 2))  # 227 12:45 PM 2:50 PM MW
b[17].sect_bids.append((45, 2))  # 227 12:45 PM 2:50 PM MW
b[17].sect_bids.append((46, 2))  # 227 12:45 PM 2:50 PM TTh
b[17].sect_bids.append((47, 2)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[17].sect_bids.append((48, 2))  # 227 4:35 PM 6:40 PM MW
b[17].sect_bids.append((49, 2))  # 227 4:35 PM 6:40 PM TTh
b[17].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[17].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[17].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[17].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[17].sect_bids.append((54, 1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[17].sect_bids.append((55, 1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[17].sect_bids.append((56, 1))  # 228A 8:00 AM 9:10 AM MTWTh
b[17].sect_bids.append((57, 1))  # 228A 12:45 PM 3:15 PM MW
b[17].sect_bids.append((58, 1))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[17].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[17].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[17].sect_bids.append((61, 1))  # 228B 8:00 AM 9:10 AM MTWTh
b[17].sect_bids.append((62, 1))  # 228B 12:45 PM 3:15 PM MW 
b[17].sect_bids.append((63, 1))  # 228B 4:10 PM 6:40 PM MW
b[17].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[17].sect_bids.append((65, -1))  # 238 8:00 AM 9:10 AM MTWTh
b[17].sect_bids.append((66, -1))  # 238 9:35 AM 10:45 AM MTWTh
b[17].sect_bids.append((67, -1))  # 238 11:10 AM 12:20 PM MTWTh
b[17].sect_bids.append((68, -1))  # 238 4:10 PM 6:40 PM MW 
b[17].sect_bids.append((69, -1))  # 238 4:10 PM 6:40 PM TTh
b[17].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[17].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[17].sect_bids.append((72, 4))  # 240 8:00 AM 9:25 AM MW
b[17].sect_bids.append((73, 4))  # 240 8:00 AM 9:25 AM TTh
b[17].sect_bids.append((74, 4))  # 240 9:35 AM 11:00 AM MW
b[17].sect_bids.append((75, 4))  # 240 9:35 AM 11:00 AM TTh
b[17].sect_bids.append((76, 4))  # 240 11:10 AM 12:35 PM MW 
b[17].sect_bids.append((77, 4))  # 240 11:10 AM 12:35 PM TTh 
b[17].sect_bids.append((78, 4))  # 240 12:45 PM 2:10 PM MW
b[17].sect_bids.append((79, 4))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[17].sect_bids.append((80, 4))  # 240 12:45 PM 2:10 PM MW
b[17].sect_bids.append((81, 4))  # 240 3:40 PM 5:05 PM TTh
b[17].sect_bids.append((82, 4))  # 240 3:40 PM 5:05 PM MW
b[17].sect_bids.append((83, 4))  # 240 5:15 PM 6:40 PM TTh
b[17].sect_bids.append((84, 4))  # 240 5:15 PM 6:40 PM MW Harandian
b[17].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[17].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[17].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[17].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[17].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[17].sect_bids.append((90, 5))  # 260 8:00 AM 9:10 AM MTWTh
b[17].sect_bids.append((91, 5))  # 260 9:35 AM 10:45 AM MTWTh
b[17].sect_bids.append((92, 5))  # 260 11:10 AM 12:20 PM MTWTh
b[17].sect_bids.append((93, 5))  # 260 12:45 PM 1:55 PM MTWTh
b[17].sect_bids.append((94, 5))  # 260 12:45 PM 3:15 PM MW
b[17].sect_bids.append((95, 5))  # 260 2:25 PM 3:35 PM MTWTh
b[17].sect_bids.append((96, 5))  # 260 2:25 PM 3:35 PM MTWTh
b[17].sect_bids.append((97, 5))  # 260 4:10 PM 6:40 PM MW
b[17].sect_bids.append((98, 5))  # 260 4:10 PM 6:40 PM TTh
b[17].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[17].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[17].sect_bids.append((101, 4))  # 261 8:00 AM 9:10 AM MTWTh
b[17].sect_bids.append((102, 4))  # 261 8:00 AM 9:10 AM MTWTh
b[17].sect_bids.append((103, 4))  # 261 9:35 AM 10:45 AM MTWTh
b[17].sect_bids.append((104, 4))  # 261 9:35 AM 10:45 AM MTWTh
b[17].sect_bids.append((105, 4))  # 261 11:10 AM 12:20 PM MTWTh
b[17].sect_bids.append((106, 4))  # 261 12:45 PM 3:15 PM MW
b[17].sect_bids.append((107, 4))  # 261 2:25 PM 3:35 PM MTWTh
b[17].sect_bids.append((108, 4))  # 261 4:10 PM 6:40 PM MW Martinez
b[17].sect_bids.append((109, 4))  # 261 4:10 PM 6:40 PM TTh
b[17].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[17].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[17].sect_bids.append((112, 5))  # 262 8:00 AM 9:10 AM MTWTh
b[17].sect_bids.append((113, 5))  # 262 9:35 AM 10:45 AM MTWTh
b[17].sect_bids.append((114, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[17].sect_bids.append((115, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[17].sect_bids.append((116, 5))  # 262 4:10 PM 6:40 PM TTh
b[17].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[17].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[17].sect_bids.append((119, 5))  # 263 8:00 AM 9:10 AM MTWTh
b[17].sect_bids.append((120, 5))  # 263 9:35 AM 10:45 AM MTWTh
b[17].sect_bids.append((121, 5))  # 263 11:10 AM 12:20 PM MTWT
b[17].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[17].sect_bids.append((123, 3))  # 270 8:00 AM 9:25 AM MW
b[17].sect_bids.append((124, 3))  # 270 12:45 PM 2:10 PM MW
b[17].sect_bids.append((125, 3))  # 270 5:15 PM 6:40 PM TTh
b[17].sect_bids.append((126, 2))  # 275 9:35 AM 11:00 AM TTh
b[17].sect_bids.append((127, 2))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='tabataz', semester='Fa2019', timestamp=datetime.datetime.now()))
b[18].bid_1_prep = 4
b[18].bid_2_prep = 5
b[18].bid_3_prep = 0
b[18].bid_4_prep = -2
b[18].bid_5_prep = -5
b[18].min_acc_units = 9
b[18].max_acc_units = 11
b[18].min_des_units = 10
b[18].max_des_units = 10
b[18].sect_bids.append((1, -2))  # 110 8:00 am MTWTh adj
b[18].sect_bids.append((2, -2))  # 110 9:35 am MTWTh adj 
b[18].sect_bids.append((3, -2))  # 110 4:10 PM MW adj
b[18].sect_bids.append((4, -2))  # 110 7:00 PM TTh
b[18].sect_bids.append((5, -2))  # 110 8:00 AM MTWTh adj
b[18].sect_bids.append((6, 5))  # 115 8:00 AM MTWTh 
b[18].sect_bids.append((7, 5))  # 115 11:10 AM MTWTh
b[18].sect_bids.append((8, 5))  # 115 12:45 PM MW
b[18].sect_bids.append((9, 5))  # 115 12:45 PM TTh
b[18].sect_bids.append((10, -5))  # 115 4:10 PM TTh
b[18].sect_bids.append((11, 5))  # 134 8:00 AM MTWTh LEHAVI
b[18].sect_bids.append((12, 5))  # 134 8:00 AM MTWTh
b[18].sect_bids.append((13, 5))  # 134 8:00 AM MTWTh
b[18].sect_bids.append((14, 5))  # 134 9:35 AM MTWTh
b[18].sect_bids.append((15, 5))  # 134 9:35 AM MTWTh
b[18].sect_bids.append((16, 5))  # 134 11:10 AM MTWTh
b[18].sect_bids.append((17, 5)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[18].sect_bids.append((18, 5)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[18].sect_bids.append((19, 5)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[18].sect_bids.append((20, 5))  # 134 12:45 PM 3:55 PM MW 
b[18].sect_bids.append((21, -5))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[18].sect_bids.append((22, -5))  # 134 3:30 PM 6:40 PM MW Le 
b[18].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[18].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[18].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[18].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[18].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[18].sect_bids.append((28, -5))  # 215 3:40 PM 5:05 PM TTh 
b[18].sect_bids.append((29, -5))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[18].sect_bids.append((30, -5))  # 227 8:00 AM 8:50 AM MTWTh
b[18].sect_bids.append((31, -5))  # 227 8:00 AM 10:05 AM MW
b[18].sect_bids.append((32, -5))  # 227 8:00 AM 10:05 AM TTh
b[18].sect_bids.append((33, -5))  # 227 9:35 AM 10:25 AM MTWTh
b[18].sect_bids.append((34, -5))  # 227 9:35 AM 11:40 AM MW 
b[18].sect_bids.append((35, -5))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[18].sect_bids.append((36, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[18].sect_bids.append((37, -5))  # 227 10:10 AM 11:00 AM MTWTh
b[18].sect_bids.append((38, -5))  # 227 10:30 AM 12:35 PM MW 
b[18].sect_bids.append((39, -5))  # 227 10:30 AM 12:35 PM TTh
b[18].sect_bids.append((40, -5))  # 227 11:10 AM 1:15 PM MW
b[18].sect_bids.append((41, -5))  # 227 11:10 AM 1:15 PM TTh
b[18].sect_bids.append((42, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[18].sect_bids.append((43, -5))  # 227 11:45 AM 12:35 PM MTWTh
b[18].sect_bids.append((44, -5))  # 227 12:45 PM 2:50 PM MW
b[18].sect_bids.append((45, -5))  # 227 12:45 PM 2:50 PM MW
b[18].sect_bids.append((46, -5))  # 227 12:45 PM 2:50 PM TTh
b[18].sect_bids.append((47, -5)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[18].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[18].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[18].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[18].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[18].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[18].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[18].sect_bids.append((54, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[18].sect_bids.append((55, -5))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[18].sect_bids.append((56, -5))  # 228A 8:00 AM 9:10 AM MTWTh
b[18].sect_bids.append((57, -5))  # 228A 12:45 PM 3:15 PM MW
b[18].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[18].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[18].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[18].sect_bids.append((61, -5))  # 228B 8:00 AM 9:10 AM MTWTh
b[18].sect_bids.append((62, -5))  # 228B 12:45 PM 3:15 PM MW 
b[18].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[18].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[18].sect_bids.append((65, -5))  # 238 8:00 AM 9:10 AM MTWTh
b[18].sect_bids.append((66, -5))  # 238 9:35 AM 10:45 AM MTWTh
b[18].sect_bids.append((67, -5))  # 238 11:10 AM 12:20 PM MTWTh
b[18].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[18].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[18].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[18].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[18].sect_bids.append((72, 3))  # 240 8:00 AM 9:25 AM MW
b[18].sect_bids.append((73, 3))  # 240 8:00 AM 9:25 AM TTh
b[18].sect_bids.append((74, 3))  # 240 9:35 AM 11:00 AM MW
b[18].sect_bids.append((75, 3))  # 240 9:35 AM 11:00 AM TTh
b[18].sect_bids.append((76, 3))  # 240 11:10 AM 12:35 PM MW 
b[18].sect_bids.append((77, 3))  # 240 11:10 AM 12:35 PM TTh 
b[18].sect_bids.append((78, 3))  # 240 12:45 PM 2:10 PM MW
b[18].sect_bids.append((79, 3))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[18].sect_bids.append((80, 3))  # 240 12:45 PM 2:10 PM MW
b[18].sect_bids.append((81, -3))  # 240 3:40 PM 5:05 PM TTh
b[18].sect_bids.append((82, -3))  # 240 3:40 PM 5:05 PM MW
b[18].sect_bids.append((83, -3))  # 240 5:15 PM 6:40 PM TTh
b[18].sect_bids.append((84, -3))  # 240 5:15 PM 6:40 PM MW Harandian
b[18].sect_bids.append((85, -3))  # 240 7:00 PM 8:25 PM MW
b[18].sect_bids.append((86, -3))  # 240 7:00 PM 8:25 PM TTh
b[18].sect_bids.append((87, -3))  # 240 7:00 PM 8:25 PM TTh
b[18].sect_bids.append((88, -3))  # 240 8:35 PM 10:00 PM MW 
b[18].sect_bids.append((89, -3))  # 240 8:35 PM 10:00 PM TTh 
b[18].sect_bids.append((90, 3))  # 260 8:00 AM 9:10 AM MTWTh
b[18].sect_bids.append((91, 3))  # 260 9:35 AM 10:45 AM MTWTh
b[18].sect_bids.append((92, 3))  # 260 11:10 AM 12:20 PM MTWTh
b[18].sect_bids.append((93, 3))  # 260 12:45 PM 1:55 PM MTWTh
b[18].sect_bids.append((94, 3))  # 260 12:45 PM 3:15 PM MW
b[18].sect_bids.append((95, -3))  # 260 2:25 PM 3:35 PM MTWTh
b[18].sect_bids.append((96, -3))  # 260 2:25 PM 3:35 PM MTWTh
b[18].sect_bids.append((97, -4))  # 260 4:10 PM 6:40 PM MW
b[18].sect_bids.append((98, -4))  # 260 4:10 PM 6:40 PM TTh
b[18].sect_bids.append((99, -4))  # 260 7:00 PM 9:30 PM MW
b[18].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[18].sect_bids.append((101, -5))  # 261 8:00 AM 9:10 AM MTWTh
b[18].sect_bids.append((102, -5))  # 261 8:00 AM 9:10 AM MTWTh
b[18].sect_bids.append((103, -5))  # 261 9:35 AM 10:45 AM MTWTh
b[18].sect_bids.append((104, -5))  # 261 9:35 AM 10:45 AM MTWTh
b[18].sect_bids.append((105, -5))  # 261 11:10 AM 12:20 PM MTWTh
b[18].sect_bids.append((106, -5))  # 261 12:45 PM 3:15 PM MW
b[18].sect_bids.append((107, -5))  # 261 2:25 PM 3:35 PM MTWTh
b[18].sect_bids.append((108, -5))  # 261 4:10 PM 6:40 PM MW Martinez
b[18].sect_bids.append((109, -5))  # 261 4:10 PM 6:40 PM TTh
b[18].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[18].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[18].sect_bids.append((112, -5))  # 262 8:00 AM 9:10 AM MTWTh
b[18].sect_bids.append((113, -5))  # 262 9:35 AM 10:45 AM MTWTh
b[18].sect_bids.append((114, -5))  # 262 11:10 AM 12:20 PM MTWTh
b[18].sect_bids.append((115, -5))  # 262 11:10 AM 12:20 PM MTWTh
b[18].sect_bids.append((116, -5))  # 262 4:10 PM 6:40 PM TTh
b[18].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[18].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[18].sect_bids.append((119, -5))  # 263 8:00 AM 9:10 AM MTWTh
b[18].sect_bids.append((120, -5))  # 263 9:35 AM 10:45 AM MTWTh
b[18].sect_bids.append((121, -5))  # 263 11:10 AM 12:20 PM MTWT
b[18].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[18].sect_bids.append((123, -5))  # 270 8:00 AM 9:25 AM MW
b[18].sect_bids.append((124, -5))  # 270 12:45 PM 2:10 PM MW
b[18].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[18].sect_bids.append((126, -5))  # 275 9:35 AM 11:00 AM TTh
b[18].sect_bids.append((127, -5))  # 275 3:40 PM 5:05 PM MW


b.append(UBids(user='veigajr', semester='Fa2019', timestamp=datetime.datetime.now()))
b[19].bid_1_prep = 4
b[19].bid_2_prep = 5
b[19].bid_3_prep = 2
b[19].bid_4_prep = -2
b[19].bid_5_prep = -5
b[19].min_acc_units = 14
b[19].max_acc_units = 20
b[19].min_des_units = 17
b[19].max_des_units = 19
b[19].sect_bids.append((1, -2))  # 110 8:00 am MTWTh adj
b[19].sect_bids.append((2, -2))  # 110 9:35 am MTWTh adj 
b[19].sect_bids.append((3, -2))  # 110 4:10 PM MW adj
b[19].sect_bids.append((4, -2))  # 110 7:00 PM TTh
b[19].sect_bids.append((5, -2))  # 110 8:00 AM MTWTh adj
b[19].sect_bids.append((6, 0))  # 115 8:00 AM MTWTh 
b[19].sect_bids.append((7, 0))  # 115 11:10 AM MTWTh
b[19].sect_bids.append((8, 0))  # 115 12:45 PM MW
b[19].sect_bids.append((9, 0))  # 115 12:45 PM TTh
b[19].sect_bids.append((10, -1))  # 115 4:10 PM TTh
b[19].sect_bids.append((11, 4))  # 134 8:00 AM MTWTh LEHAVI
b[19].sect_bids.append((12, 4))  # 134 8:00 AM MTWTh
b[19].sect_bids.append((13, 4))  # 134 8:00 AM MTWTh
b[19].sect_bids.append((14, 4))  # 134 9:35 AM MTWTh
b[19].sect_bids.append((15, 4))  # 134 9:35 AM MTWTh
b[19].sect_bids.append((16, 4))  # 134 11:10 AM MTWTh
b[19].sect_bids.append((17, 4)) # 134 11:10 AM MTWTh TCHERTCHIAN
b[19].sect_bids.append((18, 4)) # 134 12:45 PM 2:10 PM MTWTh Bennett
b[19].sect_bids.append((19, 4)) # 134 12:45 PM 2:10 PM MTWTh Bojkov
b[19].sect_bids.append((20, 4))  # 134 12:45 PM 3:55 PM MW 
b[19].sect_bids.append((21, -2))  # 134 3:30 PM 6:40 PM TTh Taub-Hoglund
b[19].sect_bids.append((22, -2))  # 134 3:30 PM 6:40 PM MW Le 
b[19].sect_bids.append((23, -5))  # 6:50 PM 10:00 PM MW Grigoryan 
b[19].sect_bids.append((24, -5))  # 134 6:50 PM 10:00 PM MW
b[19].sect_bids.append((25, -5))  # 134 6:50 PM 10:00 PM TTh 
b[19].sect_bids.append((26, -5))  # 134 6:50 PM 10:00 PM TTh
b[19].sect_bids.append((27, -5))  # 215 5:15 PM 6:40 PM MW
b[19].sect_bids.append((28, -2))  # 215 3:40 PM 5:05 PM TTh 
b[19].sect_bids.append((29, 3))  # 227 7:00 AM 7:50 AM MTWTh Paulus 
b[19].sect_bids.append((30, 3))  # 227 8:00 AM 8:50 AM MTWTh
b[19].sect_bids.append((31, 3))  # 227 8:00 AM 10:05 AM MW
b[19].sect_bids.append((32, 3))  # 227 8:00 AM 10:05 AM TTh
b[19].sect_bids.append((33, 3))  # 227 9:35 AM 10:25 AM MTWTh
b[19].sect_bids.append((34, 3))  # 227 9:35 AM 11:40 AM MW 
b[19].sect_bids.append((35, 3))  #  227 9:35 AM 11:40 AM TTh LEHAVI
b[19].sect_bids.append((36, 3))  # 227 10:10 AM 11:00 AM MTWTh
b[19].sect_bids.append((37, 3))  # 227 10:10 AM 11:00 AM MTWTh
b[19].sect_bids.append((38, 3))  # 227 10:30 AM 12:35 PM MW 
b[19].sect_bids.append((39, 3))  # 227 10:30 AM 12:35 PM TTh
b[19].sect_bids.append((40, 3))  # 227 11:10 AM 1:15 PM MW
b[19].sect_bids.append((41, 3))  # 227 11:10 AM 1:15 PM TTh
b[19].sect_bids.append((42, 3))  # 227 11:45 AM 12:35 PM MTWTh
b[19].sect_bids.append((43, 3))  # 227 11:45 AM 12:35 PM MTWTh
b[19].sect_bids.append((44, 3))  # 227 12:45 PM 2:50 PM MW
b[19].sect_bids.append((45, 3))  # 227 12:45 PM 2:50 PM MW
b[19].sect_bids.append((46, 3))  # 227 12:45 PM 2:50 PM TTh
b[19].sect_bids.append((47, 3)) # 227 12:45 PM 2:50 PM TTh Zilberbrand
b[19].sect_bids.append((48, -5))  # 227 4:35 PM 6:40 PM MW
b[19].sect_bids.append((49, -5))  # 227 4:35 PM 6:40 PM TTh
b[19].sect_bids.append((50, -5))  # 227 7:00 PM 9:05 PM MW
b[19].sect_bids.append((51, -5))  # 227 7:00 PM 9:05 PM MW
b[19].sect_bids.append((52, -5))  # 227 7:00 PM 9:05 PM TTh
b[19].sect_bids.append((53, -5))  # 227 7:00 PM 9:05 PM TTh
b[19].sect_bids.append((54, 1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[19].sect_bids.append((55, 1))  # A-228A 9:35 AM 12:05 PM MTWTh 10-unit 8-weekx2
b[19].sect_bids.append((56, 1))  # 228A 8:00 AM 9:10 AM MTWTh
b[19].sect_bids.append((57, 1))  # 228A 12:45 PM 3:15 PM MW
b[19].sect_bids.append((58, -5))  # 228A 4:10 PM 6:40 PM TTh Nikjeh
b[19].sect_bids.append((59, -5))  # 228A 7:00 PM 9:30 PM MW
b[19].sect_bids.append((60, -5))  # 228A 7:00 PM 9:30 PM TTh 
b[19].sect_bids.append((61, 1))  # 228B 8:00 AM 9:10 AM MTWTh
b[19].sect_bids.append((62, 1))  # 228B 12:45 PM 3:15 PM MW 
b[19].sect_bids.append((63, -5))  # 228B 4:10 PM 6:40 PM MW
b[19].sect_bids.append((64, -5))  # 228B 7:00 PM 9:30 PM MW Trujillo 
b[19].sect_bids.append((65, -5))  # 238 8:00 AM 9:10 AM MTWTh
b[19].sect_bids.append((66, -5))  # 238 9:35 AM 10:45 AM MTWTh
b[19].sect_bids.append((67, -5))  # 238 11:10 AM 12:20 PM MTWTh
b[19].sect_bids.append((68, -5))  # 238 4:10 PM 6:40 PM MW 
b[19].sect_bids.append((69, -5))  # 238 4:10 PM 6:40 PM TTh
b[19].sect_bids.append((70, -5))  # 238 7:00 PM 9:30 PM MW
b[19].sect_bids.append((71, -5))  # 238 7:00 PM 9:30 PM TTh New
b[19].sect_bids.append((72, 4))  # 240 8:00 AM 9:25 AM MW
b[19].sect_bids.append((73, 4))  # 240 8:00 AM 9:25 AM TTh
b[19].sect_bids.append((74, 4))  # 240 9:35 AM 11:00 AM MW
b[19].sect_bids.append((75, 4))  # 240 9:35 AM 11:00 AM TTh
b[19].sect_bids.append((76, 4))  # 240 11:10 AM 12:35 PM MW 
b[19].sect_bids.append((77, 4))  # 240 11:10 AM 12:35 PM TTh 
b[19].sect_bids.append((78, 4))  # 240 12:45 PM 2:10 PM MW
b[19].sect_bids.append((79, 4))  # 240 12:45 PM 2:10 PM TTh Vardapetyan
b[19].sect_bids.append((80, 4))  # 240 12:45 PM 2:10 PM MW
b[19].sect_bids.append((81, 4))  # 240 3:40 PM 5:05 PM TTh
b[19].sect_bids.append((82, 4))  # 240 3:40 PM 5:05 PM MW
b[19].sect_bids.append((83, -5))  # 240 5:15 PM 6:40 PM TTh
b[19].sect_bids.append((84, -5))  # 240 5:15 PM 6:40 PM MW Harandian
b[19].sect_bids.append((85, -5))  # 240 7:00 PM 8:25 PM MW
b[19].sect_bids.append((86, -5))  # 240 7:00 PM 8:25 PM TTh
b[19].sect_bids.append((87, -5))  # 240 7:00 PM 8:25 PM TTh
b[19].sect_bids.append((88, -5))  # 240 8:35 PM 10:00 PM MW 
b[19].sect_bids.append((89, -5))  # 240 8:35 PM 10:00 PM TTh 
b[19].sect_bids.append((90, 3))  # 260 8:00 AM 9:10 AM MTWTh
b[19].sect_bids.append((91, 3))  # 260 9:35 AM 10:45 AM MTWTh
b[19].sect_bids.append((92, 3))  # 260 11:10 AM 12:20 PM MTWTh
b[19].sect_bids.append((93, 3))  # 260 12:45 PM 1:55 PM MTWTh
b[19].sect_bids.append((94, 3))  # 260 12:45 PM 3:15 PM MW
b[19].sect_bids.append((95, 3))  # 260 2:25 PM 3:35 PM MTWTh
b[19].sect_bids.append((96, 3))  # 260 2:25 PM 3:35 PM MTWTh
b[19].sect_bids.append((97, -2))  # 260 4:10 PM 6:40 PM MW
b[19].sect_bids.append((98, -2))  # 260 4:10 PM 6:40 PM TTh
b[19].sect_bids.append((99, -5))  # 260 7:00 PM 9:30 PM MW
b[19].sect_bids.append((100, -5))  # 260 7:00 PM 9:30 PM TTh
b[19].sect_bids.append((101, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[19].sect_bids.append((102, 5))  # 261 8:00 AM 9:10 AM MTWTh
b[19].sect_bids.append((103, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[19].sect_bids.append((104, 5))  # 261 9:35 AM 10:45 AM MTWTh
b[19].sect_bids.append((105, 5))  # 261 11:10 AM 12:20 PM MTWTh
b[19].sect_bids.append((106, 5))  # 261 12:45 PM 3:15 PM MW
b[19].sect_bids.append((107, 5))  # 261 2:25 PM 3:35 PM MTWTh
b[19].sect_bids.append((108, -2))  # 261 4:10 PM 6:40 PM MW Martinez
b[19].sect_bids.append((109, -2))  # 261 4:10 PM 6:40 PM TTh
b[19].sect_bids.append((110, -5))  # 261 7:00 PM 9:30 PM MW Kharaghani
b[19].sect_bids.append((111, -5))  # 261 7:00 PM 9:30 PM TTh Lin
b[19].sect_bids.append((112, 5))  # 262 8:00 AM 9:10 AM MTWTh
b[19].sect_bids.append((113, 5))  # 262 9:35 AM 10:45 AM MTWTh
b[19].sect_bids.append((114, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[19].sect_bids.append((115, 5))  # 262 11:10 AM 12:20 PM MTWTh
b[19].sect_bids.append((116, -2))  # 262 4:10 PM 6:40 PM TTh
b[19].sect_bids.append((117, -5))  # 262 7:00 PM 9:30 PM MW
b[19].sect_bids.append((118, -5))  # 262 7:00 PM 9:30 PM TTh
b[19].sect_bids.append((119, 3))  # 263 8:00 AM 9:10 AM MTWTh
b[19].sect_bids.append((120, 3))  # 263 9:35 AM 10:45 AM MTWTh
b[19].sect_bids.append((121, 3))  # 263 11:10 AM 12:20 PM MTWT
b[19].sect_bids.append((122, -5))  # 263 7:00 PM 9:30 PM TTh
b[19].sect_bids.append((123, 1))  # 270 8:00 AM 9:25 AM MW
b[19].sect_bids.append((124, 1))  # 270 12:45 PM 2:10 PM MW
b[19].sect_bids.append((125, -5))  # 270 5:15 PM 6:40 PM TTh
b[19].sect_bids.append((126, 1))  # 275 9:35 AM 11:00 AM TTh
b[19].sect_bids.append((127, 1))  # 275 3:40 PM 5:05 PM MW

