import pandas
import numpy

data = pandas.read_csv("data_task4_old.txt", encoding='utf-8', sep='\t+', engine='python')
data['assigned_ts'] = pandas.to_datetime(data['assigned_ts'])
data['closed_ts'] = pandas.to_datetime(data['closed_ts'])
data['work_ts'] = data['closed_ts']- data['assigned_ts']
print(data)

maxmicrotasks = pandas.DataFrame (data, columns=['login', 'Microtasks', 'work_ts']).nlargest(100, 'Microtasks')
print(maxmicrotasks)

minmircotasks = pandas.DataFrame (data, columns=['login', 'Microtasks', 'work_ts' ]).nsmallest(100, 'Microtasks')
print(minmircotasks)

maxwork_ts = pandas.DataFrame (data, columns=['login', 'Microtasks', 'work_ts']).nlargest(100, 'work_ts')
print(maxwork_ts)

minwork_ts = pandas.DataFrame (data, columns=['login', 'Microtasks', 'work_ts' ]).nsmallest(100, 'work_ts')
print(minwork_ts)

AVG_time = data[['work_ts']].mean(axis=0)
AVG_task = data[['Microtasks']].mean(axis=0)
print(AVG_time)
print(AVG_task)

dataperday = pandas.read_csv("data_task4_old.txt", encoding='utf-8', sep='\t+', engine='python')
dataperday['assigned_ts'] = pandas.to_datetime(data['assigned_ts']).dt.date
dataperday['closed_ts'] = pandas.to_datetime(data['closed_ts']).dt.date
del dataperday['tid']
microtasksperday = dataperday.groupby(by=['assigned_ts']).sum('Microtasks').groupby(level=[0]).cumsum()
AVG_taskperday = microtasksperday[['Microtasks']].mean(axis=0)
print(AVG_taskperday)

datapersingleuser = pandas.read_csv("data_task4_old.txt", encoding='utf-8', sep='\t+', engine='python')
datapersingleuser['assigned_ts'] = pandas.to_datetime(data['assigned_ts']).dt.date
datapersingleuser['closed_ts'] = pandas.to_datetime(data['closed_ts']).dt.date
del datapersingleuser['tid']
microtasksperdaysingleuser = datapersingleuser.groupby(by=['login','assigned_ts']).sum().groupby(level=[0]).cumsum()
AVG_taskperdayperuser = microtasksperdaysingleuser[['Microtasks']].mean(axis=0)
print(AVG_taskperdayperuser)


worst = pandas.read_csv("data_task3.csv", encoding='utf-8', sep='\t+', engine='python')
worst['assigned_ts'] = pandas.to_datetime(data['assigned_ts'])
worst['closed_ts'] = pandas.to_datetime(data['closed_ts'])
worst['work_ts'] = data['closed_ts']- data['assigned_ts']
print(worst)
