import logging
import hashlib
import beeng


logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


def load_engine():
    return beeng.Engine()


def process_model(eng, path):
    # type: (beeng.Engine, str) -> None
    model = eng.load_model(path)
    res_success, res_xml = eng.get_res_xml(model)
    key_success, key_xml = eng.get_key_xml(model)
    assert res_success == True
    assert key_success == True


def test_1():
    eng = load_engine()
    process_model(eng, 'test-data/Eksempel_v8_Administration.xml')
    process_model(eng, 'test-data/Eksempel_v8_Etagehus.xml')
    process_model(eng, 'test-data/Eksempel_v8_Parcelhus.xml')
