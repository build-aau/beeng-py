import beeng

eng = beeng.Engine()

success, data = eng.get_summer_comfort('../test-data/Eksempel_v8_Parcelhus.xml')

if success == True:
    print(data)
