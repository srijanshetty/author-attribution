count_rnt_0 = count_rnt_1 = count_rnt_2 = count_rnt_3 = count_rnt_4 = count_rnt_5 = 0
count_prem_0 = count_prem_1 = count_prem_2 = count_prem_3 = count_prem_4 = count_prem_5 = 0
count_dharamvir_0 = count_dharamvir_1 = count_dharamvir_2 = count_dharamvir_3 = count_dharamvir_4 = count_dharamvir_5 = 0
count_vibhuti_0 = count_vibhuti_1 = count_vibhuti_2 = count_vibhuti_3 = count_vibhuti_4 = count_vibhuti_5 = 0
count_sarat_0 = count_sarat_1 = count_sarat_2 = count_sarat_3 = count_sarat_4 = count_sarat_5 = 0

for i in range(1710):
    if i < 151:
        if clusters[i] == 0:
            count_rnt_0 = count_rnt_0 + 1
        elif clusters[i] == 1:
            count_rnt_1 = count_rnt_1 + 1
        elif clusters[i] == 2:
            count_rnt_2 = count_rnt_2 + 1
        elif clusters[i] == 3:
            count_rnt_3 = count_rnt_3 + 1
        elif clusters[i] == 4:
            count_rnt_4 = count_rnt_4 + 1
        else:
            count_rnt_5 = count_rnt_5 + 1
    elif i < 693:
        if clusters[i] == 0:
            count_sarat_0 = count_sarat_0 + 1
        elif clusters[i] == 1:
            count_sarat_1 = count_sarat_1 + 1
        elif clusters[i] == 2:
            count_sarat_2 = count_sarat_2 + 1
        elif clusters[i] == 3:
            count_sarat_3 = count_sarat_3 + 1
        elif clusters[i] == 4:
            count_sarat_4 = count_sarat_4 + 1
        else:
            count_sarat_5 = count_sarat_5 + 1
    elif i < 1111:
        if clusters[i] == 0:
            count_vibhuti_0 = count_vibhuti_0 + 1
        elif clusters[i] == 1:
            count_vibhuti_1 = count_vibhuti_1 + 1
        elif clusters[i] == 2:
            count_vibhuti_2 = count_vibhuti_2 + 1
        elif clusters[i] == 3:
            count_vibhuti_3 = count_vibhuti_3 + 1
        elif clusters[i] == 4:
            count_vibhuti_4 = count_vibhuti_4 + 1
        else:
            count_vibhuti_5 = count_vibhuti_5 + 1
    elif i < 1509:
        if clusters[i] == 0:
            count_prem_0 = count_prem_0 + 1
        elif clusters[i] == 1:
            count_prem_1 = count_prem_1 + 1
        elif clusters[i] == 2:
            count_prem_2 = count_prem_2 + 1
        elif clusters[i] == 3:
            count_prem_3 = count_prem_3 + 1
        elif clusters[i] == 4:
            count_prem_4 = count_prem_4 + 1
        else:
            count_prem_5 = count_prem_5 + 1
    else:
        if clusters[i] == 0:
            count_dharamvir_0 = count_dharamvir_0 + 1
        elif clusters[i] == 1:
            count_dharamvir_1 = count_dharamvir_1 + 1
        elif clusters[i] == 2:
            count_dharamvir_2 = count_dharamvir_2 + 1
        elif clusters[i] == 3:
            count_dharamvir_3 = count_dharamvir_3 + 1
        elif clusters[i] == 4:
            count_dharamvir_4 = count_dharamvir_4 + 1
        else:
            count_dharamvir_5 = count_dharamvir_5 + 1

