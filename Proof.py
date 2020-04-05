import math

Flex_Positions = [["ICU Physician",["Stepdown Physician", "Floor Physician", "Respiratory Therapist", "Medical Assistant", "Nonmedical Staff"]],
            ["Stepdown Physician",["Floor Physician", "Respiratory Therapist", "Medical Assistant", "Nonmedical Staff"]],
            ["Floor Physician", ["Respiratory Therapist", "Medical Assistant","Nonmedical Staff"]],
            ["Medical Assistant", ["Nonmedical Staff"]],
            ["Nonmedical Staff",[]],
            ["ICU Nurse", ["Stepdown Nurse", "Floor Nurse", "Medical Assistant", "Nonmedical Staff"]],
            ["Stepdown Nurse",["Floor Nurse", "Medical Assistant", "Nonmedical Staff"]],
            ["Floor Nurse", ["Medical Assistant", "Nonmedical Staff"]],
            ["Respiratory Therapist", ["Medical Assistant","Nonmedical Staff"]]
                ]

Target_Ratios = [["ICU Physician",50],["Stepdown Physician",50], ["Floor Physician", 25], ["Respiratory Therapist", 5], ["Medical Assistant", 50], ["Nonmedical Staff", 100],
                 ["ICU Nurse",5],["Stepdown Nurse",5], ["Floor Nurse", 5], ]

Flex_Ratios = [["ICU Physician",[["Stepdown Physician", 3], ["Floor Physician", 3]]],
            ["Stepdown Physician",[["Floor Physician", 3], ["ICU Physician", 1]]],
            ["Floor Physician",[["Stepdown Physician", 1], ["ICU Physician", 1]]],
            ["ICU Nurse", [["Stepdown Nurse", 3], ["Floor Nurse", 3]]],
            ["Stepdown Nurse", [["Floor Nurse", 3], ["ICU Nurse", 1]]],
            ["Floor Nurse", [["Stepdown Nurse", 1], ["ICU Nurse", 1]]]]

Flex_Possibilities = [["ICU Physician",["Stepdown Physician", "Floor Physician"]],
            ["Stepdown Physician",["Floor Physician", "ICU Physician"]],
            ["Floor Physician",["Stepdown Physician", "ICU Physician"]],
            ["ICU Nurse", ["Stepdown Nurse", "Floor Nurse"]],
            ["Stepdown Nurse",["Floor Nurse", "ICU Nurse"]],
            ["Floor Nurse", ["Stepdown Nurse", "ICU Nurse"]]]

Staff_Input = [["ICU Physician", 5],["Stepdown Physician", 5], ["Floor Physician", 0], ["Respiratory Therapist", 5], ["Medical Assistant", 5], ["Nonmedical Staff", 5], ["ICU Nurse", 5], ["Stepdown Nurse", 5], ["Floor Nurse", 4]]

Patient_Input= [["ICU Patients", 25],["Stepdown Patients", 25], ["Floor Patients", 25], []]

P_Sum = Patient_Input[0][1] + Patient_Input[1][1] + Patient_Input[2][1]

Patient_Input[3] = ["Sum", P_Sum]

Extra_List = [["ICU Physician", 0], ["Stepdown Physician", 0], ["Floor Physician", 0],  ["Respiratory Therapist", 0], ["Medical Assistant", 0], ["Nonmedical Staff", 0], ["ICU Nurse", 0], ["Stepdown Nurse", 0], ["Floor Nurse", 0]]

for index in range(0, 9):
    if index == 0 or index == 6 or index == 3:
        P_Index = 0
    elif index == 1 or index == 7:
        P_Index = 1
    elif index == 2 or index == 8:
        P_Index = 2
    else:
        P_Index = 3

    if (Target_Ratios[index][1]*Staff_Input[index][1])/Patient_Input[P_Index][1] >= 1:

        Extra_List[index][1] = math.floor((Target_Ratios[index][1]*Staff_Input[index][1] - Patient_Input[P_Index][1])/Target_Ratios[index][1])

Extra_ICU_Physicians = Extra_List[0]
Extra_Stepdown_Physicians = Extra_List[1]
Extra_Floor_Physicians  = Extra_List[2]
Extra_Respiratory_Therapists  = Extra_List[3]
Extra_Medical_Assistants = Extra_List[4]
Extra_Nonmedical_Staff = Extra_List[5]
Extra_ICU_Nurses = Extra_List[6]
Extra_Stepdown_Nurses = Extra_List[7]
Extra_Floor_Nurses = Extra_List[8]


Needed_List = [["ICU Physician", 0], ["Stepdown Physician", 0], ["Floor Physician", 0],  ["Respiratory Therapist", 0], ["Medical Assistant", 0], ["Nonmedical Staff", 0], ["ICU Nurse", 0], ["Stepdown Nurse", 0], ["Floor Nurse", 0]]

for index in range(0, 9):
    if index == 0 or index == 6 or index == 3:
        P_Index = 0
    elif index == 1 or index == 7:
        P_Index = 1
    elif index == 2 or index == 8:
        P_Index = 2
    else:
        P_Index = 3

    if (Target_Ratios[index][1]*Staff_Input[index][1])/Patient_Input[P_Index][1] <= 1:

        Needed_List[index][1] = math.ceil((Patient_Input[P_Index][1]-Target_Ratios[index][1]*Staff_Input[index][1])/Target_Ratios[index][1])

Needed_ICU_Physicians = Needed_List[0]
Needed_Stepdown_Physicians = Needed_List[1]
Needed_Floor_Physicians = Needed_List[2]
Needed_Respiratory_Therapists = Needed_List[3]
Needed_Medical_Assistants = Needed_List[4]
Needed_Nonmedical_Staff = Needed_List[5]
Needed_ICU_Nurses = Needed_List[6]
Needed_Stepdown_Nurses = Needed_List[7]
Needed_Floor_Nurses = Needed_List[8]

index = 0
unmet_need = False

Needed_Staff = []

run = True

for index in range(0, 9):
    if Needed_List[index][1] != 0:
        unmet_need = True
        Needed_Staff.append(Needed_List[index][0])

if unmet_need == False:
    print("Surge is within capacity")

else:

    staff_type = 0

    for staff_type in range(0, len(Needed_Staff)):
        index = 0
        Flex_Index = -1

        for index in range(0,4):

            if run == True and Flex_Ratios[index][0] == Needed_Staff[staff_type]:
                Flex_Index = index

        potential_pull = []
        Potential_Positions = []

        for i in range(0, 9):

            if Extra_List[i][0] in Flex_Possibilities[Flex_Index][1] and Extra_List[i][1] > 0:
                potential_pull.append(Extra_List[i])

                for search in range(0,9):

                    if Extra_List[search] == potential_pull[len(potential_pull)-1]:
                        Potential_Positions.append(search)

        #Reassigning
        Position_Index = len(Potential_Positions) - 1
        index = 0
        row_index = len(Potential_Positions) - 1

        while len(Needed_Staff) > 0 and run == True:

            if Needed_List[Flex_Index][1] <= potential_pull[index][1] and run == True:
                #print("Staff Type---", staff_type)

                if Extra_List[Potential_Positions[Position_Index]][0][-5:] != Needed_Staff[index][-5:]:
                    run = False
                    break

                print("Reassign ", Extra_List[Potential_Positions[Position_Index]][0], " to ", Needed_Staff[index])
                Extra_List[Potential_Positions[Position_Index]][1] = Extra_List[Potential_Positions[Position_Index]][1] - Needed_List[Flex_Index][1]
                Needed_List[Flex_Index][1] = Needed_List[Flex_Index][1] - Flex_Ratios[Flex_Index][Potential_Positions[1]][Potential_Positions[Position_Index]][1]
                Position_Index -= 1

                if Needed_List[row_index][1] != 0:
                    print('need still present')

                elif len(Needed_Staff) > 0:
                    #print("Required Staff", Needed_List)
                    Needed_Staff.remove(Needed_Staff[index])
                    row_index -= 1

        staff_type += 1

    if (len(potential_pull) > 0) == False:
        print("not possible")
        print("Required Staff-----", Needed_List)
        print("Extra Staff------", Extra_List)
    else:
        a = 1
        print("Required Staff-----", Needed_List)
        print("Extra Staff------", Extra_List)