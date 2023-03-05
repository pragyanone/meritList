import csv

verbose = 1
if verbose == 1:
    print("Verbose Output:")

csvFile = "mscPriority2078-revised.csv"
# S.N.,Roll No,Applicant Name,Gender,District,Rank,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,Quota
priority1At = 6
noOfPriorities = 18
regularSeats = 5
fullFeeSeats = 6
noOfPrograms = 46
programNames = [
    "1-Information and Communication Engineering Regular",
    "2-Information and Communication Engineering Full Fee",
    "3-Computer System and Knowledge Engineering Regular",
    "4-Computer System and Knowledge Engineering Full Fee",
    "5-Computer Engineering Specialization in Data Science Regular",
    "6-Computer Engineering Specialization in Data Science Full Fee",
    "7-Power System Engineering Regular",
    "8-Power System Engineering Full Fee",
    "9-Structural Engineering Regular",
    "10-Structural Engineering Full Fee",
    "11-Water Resources Engineering Regular",
    "12-Water Resources Engineering Full Fee",
    "13-Environmental Engineering Regular",
    "14-Environmental Engineering Full Fee",
    "15-Geotechnical Engineering Regular",
    "16-Geotechnical Engineering Full Fee",
    "17-Transportation Engineering Regular",
    "18-Transportation Engineering Full Fee",
    "19-Disaster Risk Management Regular",
    "20-Disaster Risk Management Full Fee",
    "21-Construction Management Regular",
    "22-Construction Management Full Fee",
    "23-Hydropower Engineering Regular",
    "24-Hydropower Engineering Full Fee",
    "25-Renewable Energy Engineering Regular",
    "26-Renewable Energy Engineering Full Fee",
    "27-Technology and Innovation Management Regular",
    "28-Technology and Innovation Management Full Fee",
    "29-Energy Systems Planning and Management Regular",
    "30-Energy Systems Planning and Management Full Fee",
    "31-Mechanical Systems Design and Engineering Regular",
    "32-Mechanical Systems Design and Engineering Full Fee",
    "33-Material Science and Engineering Regular",
    "34-Material Science and Engineering Full Fee",
    "35-Climate Change and Development Regular",
    "36-Climate Change and Development Full Fee",
    "37-Applied Mathematics Regular",
    "38-Applied Mathematics Full Fee",
    "39-Urban Planning Regular",
    "40-Urban Planning Full Fee",
    "41-Energy for Sustainable Social Development Regular",
    "42-Energy for Sustainable Social Development Full Fee",
    "43-Energy Efficient Buildings Regular",
    "44-Energy Efficient Buildings Full Fee",
    "45-Architecture Regular",
    "46-Architecture Full Fee",
]


def int1(s):
    if s == "":
        return -1
    else:
        return int(s)


with open(csvFile) as f:
    reader = csv.reader(f, delimiter=",")
    applicant = []
    line = 0
    for row in reader:
        line += 1
        if line < 2:
            continue
        applicant.append(row[5])

applicants = dict.fromkeys(applicant)
with open(csvFile) as f:
    reader = csv.reader(f, delimiter=",")
    line = 0
    for row in reader:
        line += 1
        if line < 2:
            continue
        applicants[row[5]] = [row[index] for index in range(5)]
        for index in range(5, priority1At - 1 + noOfPriorities):
            applicants[row[5]].append(int1(row[index]))

programs = {k: [] for k in range(1, noOfPrograms + 1)}
i = 0
for applicant in applicants:
    if verbose == 1:
        print("\napplicant = ", applicant, f"({applicants[applicant][3]})")
    for priority in range(noOfPriorities):
        program = applicants[applicant][priority1At + priority]
        if program < 0:
            break
        if verbose == 1:
            print("\tpriority =", priority)
            print("\t\tprogram = ", program)
        if not program % 2 == 0:
            capacity = regularSeats
        else:
            capacity = fullFeeSeats
        if len(programs[program]) < capacity:
            genderList = [applicants[rank][3] for rank in programs[program]]
            genderList.append(applicants[applicant][3])
            if verbose == 1:
                print("\t\t", genderList)
            if (capacity - len(programs[program]) == 1) and (
                "Female" not in genderList
            ):
                continue
            programs[program].append(applicant)
            if verbose == 1:
                print(f"\t\t\t{program}: {programs[program]}")
            break
        if verbose == 1:
            print("\t\t\tlen programs[program] = ", len(programs[program]))

detail = 1
if detail == 1:
    print("\nDetailed Result:\n")
    for program in programs:
        print(
            f"{programNames[program-1]}: ",
            [
                f"{applicants[rank][5]}-{applicants[rank][2]} ({applicants[rank][3][0]})"
                for rank in programs[program]
            ],
        )
print("\nSummarized Result:\n")
for program in programs:
    print(f"{program}: {programs[program]}")
