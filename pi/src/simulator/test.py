from datetime import datetime

str_sim_date= "2013-04-29 15:59:02"
sim_date = datetime.strptime(str_sim_date, "%Y-%m-%d %H:%M:%S")
print(sim_date)