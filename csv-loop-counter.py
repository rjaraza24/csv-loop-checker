

import csv

### CSV for SANROTSC
loop = 0
sj = "SANRO Terminal A San Juan "
sm = "SANRO Terminal B SM East"

nv = "Novaliches-Malinta Terminal General Luis "
#nv = "Novaliches-Malinta Terminal General Luis A"
ml = "Novaliches-Malinta Terminal Maysan Road"

row_elm = list()

#with open(r"C:\Users\63956\Desktop\Report\may16\Sanro-Unit-26-4-24-csv-out.csv", 'rt') as inp:
with open(r"C:\Users\63956\Desktop\Report\june8\u35-10-24-24H.csv", 'rt') as inp:

    for row in csv.reader(inp):
     row_elm.append(str(row[3]))


    print(len(row_elm))

    # print(row_elm)

    for index,elem in enumerate(row_elm):
        if (index + 3 < len(row_elm) ):
         # prev_el = str(row_elm[index - 1])
         curr_el = (row_elm[index])
         next_el = (row_elm[index + 1])
         next_next_el = (row_elm[index + 2])
         next_next_next_el = (row_elm[index + 3])
         print(curr_el, next_el, next_next_el, next_next_next_el)
         if (curr_el == sj and next_el == sm  and next_next_el == sm and next_next_next_el == sj):
             loop+=1
             continue
         elif (curr_el == nv and next_el == ml and next_next_el == ml and next_next_next_el == nv):
             loop+=1
             continue
         # elif (curr_el == sj and next_el == sm and next_next_el == sm and next_next_next_el == sj):
         #     loop+=1
         #     continue
         # elif (curr_el == sm and next_el == sm and next_next_el == sj and next_next_next_el == sj):
         #     loop+=1
         #     continue
         # elif (curr_el == sm and next_el == sj and next_next_el == sj and next_next_next_el == sm):
         #     loop+=1
         #     continue

        # if row_elm == sj:
        #  print("san juan")
        # elif row_elm == sm:
        #  print("sm")
        #if row[3] == "SANRO Terminal A San Juan " and (row[3] + 1) == "SANRO Terminal A San Juan " and (row[3] + 2) == "SANRO Terminal B SM East" and (row[3] + 3) == "SANRO Terminal B SM East":
            #loop+=1



print(loop)