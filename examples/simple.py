import beeng

eng = beeng.Engine()

model = eng.load_model('../test-data/Eksempel_v8_Administration.xml')

res_success, res_xml = eng.get_res_xml(model)
key_success, key_xml = eng.get_key_xml(model)

assert res_success == True
assert key_success == True

with open('res.xml', 'w') as res_file:
    res_file.write(res_xml)

with open('key.xml', 'w') as key_file:
    key_file.write(key_xml)