import datetime
timeStamp = 1555722339
dateArray1 = datetime.datetime.fromtimestamp(timeStamp)
timeStamp = 1555764285
dateArray2 = datetime.datetime.utcfromtimestamp(timeStamp)

t=max(dateArray1,dateArray2)
# otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")


print(dateArray1,dateArray2,(t-dateArray1).seconds)
