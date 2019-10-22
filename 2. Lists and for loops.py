row_2=['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3=['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
ratings_1=row_1[3]
ratings_2=row_2[3]
ratings_3=row_3[3]
total=ratings_1+ratings_2+ratings_3
average=total/3

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
rating_1=row_1[-1]
rating_2=row_2[-1]
rating_3=row_3[-1]
total_rating=rating_1+rating_2+rating_3
average_rating=total_rating/3

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
insta_rating_data = [row_2[0], row_2[3], row_2[4]]
pandora_rating_data = [row_5[0], row_5[3], row_5[4]]
avg_rating = (fb_rating_data[2] + insta_rating_data[2] + pandora_rating_data[2]) / 3

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
first_4_fb=row_1[:4]
last_3_fb=row_1[-3:]
pandora_3_4=row_5[2:4]

app_data_set=list(row_1,row_2,row_3,row_4,row_5)
avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] +
              app_data_set[2][-1] + app_data_set[3][-1] +
              app_data_set[4][-1]) / 5
              
opened_file=open('AppleStore.csv')
read_file=opened_file.read()
print(read_file[:300])
opened_file.close()

new_line_split = read_file.split("\n")
header_list = new_line_split[0].split(",")
row_1_list = new_line_split[1].split(",")
row_2_list = new_line_split[2].split(",")
first_three_lists = [header_list, row_1_list, row_2_list]

header = new_line_split[0]
data_row_1 = new_line_split[1]
data_row_2 = new_line_split[2]
first_three = [header, data_row_1, data_row_2]
index=0
for each_string in first_three:
    first_three[index]=each_string.split(",")
    print(first_three[index])
    index+=1
print(first_three)