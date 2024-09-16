def normalize_data(n_cases, n_people, scale):
    norm_cases = []
    for idx, n in enumerate(n_cases):
        norm_cases.append(n/n_people[idx]*scale)
    return norm_cases

regions = ['Seoul', 'Geongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people= [9550227, 13530519, 3359527, 3322373, 2938429, 2630254, 2393626, 2118183, 1838353, 1792476, 1597179, 1536270, 1454679, 1441970, 1124459, 675883, 365309] # 2021-08
n_covid = [644, 529, 38,29,148,28,41,62,23,27,27,33,16,40,20,5,4] # 2021-09-21

sum_people= sum(n_people) # TODO) The total number of people
sum_covid= sum(n_covid) # TODO) The total number of new cases
norm_covid= normalize_data(n_covid, n_people, 1000000) # The new cases per 1 million people

# Print population by region
print('### Korean Population by Region')
print('* Total population:', sum_people)
print()
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')

for idx, pop in enumerate(n_people):
    # 각 지역 인구 비율 계산
    ratio = (pop / sum_people) * 100
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))
print('')

print('### COVID-19 New Cases by Region')
print('* Total New Cases:', sum_covid)
print()
print('| Region   | New Cases | Ratio (%) | Cases per Million |')
print('| -------- | --------- | --------- | ----------------- |')

for idx, cases in enumerate(n_covid):
    case_ratio = (cases / sum_covid) * 100
    print('| %s | %d | %.1f | %.2f |' % (regions[idx], cases, case_ratio, norm_covid[idx]))
