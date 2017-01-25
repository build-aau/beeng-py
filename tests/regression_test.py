import logging
import hashlib
import beeng


logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


def process_model(eng, path):
    # type: (beeng.Engine, str) -> None
    model = eng.load_model(path)
    res_success, res_xml = eng.get_res_xml(model)
    key_success, key_xml = eng.get_key_xml(model)
    assert res_success == True
    assert key_success == True


def test_1():
    """
    Tests that the engine can be found automatically and results can be produced
    """
    eng = beeng.Engine()
    process_model(eng, 'test-data/Eksempel_v8_Administration.xml')
    process_model(eng, 'test-data/Eksempel_v8_Etagehus.xml')
    process_model(eng, 'test-data/Eksempel_v8_Parcelhus.xml')


def test_2():
    """
    Tests legacy support (Be10)
    """
    eng = beeng.Engine(r'C:\Program Files (x86)\SBi\Be10 v7\Be10Eng.dll')
    process_model(eng, 'test-data/Eksempel_v8_Administration.xml')
    process_model(eng, 'test-data/Eksempel_v8_Etagehus.xml')
    process_model(eng, 'test-data/Eksempel_v8_Parcelhus.xml')
