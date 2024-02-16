# from common_util.firstname_generator import firstname as fname

from common_util import firstname_generator as fname
from common_util import lastname_generator as lname
from postgres import db_connection as conn
from common_util import uuid_generator as uid
from postgres import insert_records as insert
from common_util import period_generator as period
from common_util import ssn_generator as ssn
from common_util import dob_generator as dob
from common_util import start_by_generator as start_by
from common_util import end_by_generator as end_by
from common_util import startdate_generator as start_date
from common_util import enddate_generator as end_date
from my import my_insert_records as my_insert

from mongo import mongo_db_connection as mongo_conn

from aws import read_secreat_manager as sec
# command + option+L to indentation
import json

# lneed to provide for execution variable like local or aws
execution_mode = "aws"


def pii_generator():
    pii = []
    pii_my = []
    pii_json_string = []
    for i in range(10000):
        uuid = uid.uuid_gen()
        first_name = fname.firstname()
        last_name = lname.lastname()
        # ssn
        ssn_gen = ssn.ssn()
        # dob
        # dob_gen = dob.dob()
        # period
        period_gen = period.period()
        # started_by
        start_by_gen = start_by.start_by()
        # startdate
        # start_date_gen = start_date.start_date()
        # ended_by
        end_by_gen = end_by.end_by()
        # enddate
        # end_date_gen = end_date.end_date()

        # for postgresql
        pii.append((uuid, first_name, last_name, ssn_gen, period_gen, start_by_gen, end_by_gen))
        # for mysql
        pii_my.append((first_name, last_name, ssn_gen, period_gen, start_by_gen, end_by_gen))
        # for mongodb
        dict_pii = {}
        dict_pii["first_name"] = first_name
        dict_pii["last_name"] = last_name
        dict_pii["ssn"] = ssn_gen
        # dict_pii["dob"] = dob_gen
        dict_pii["period"] = period_gen
        dict_pii["started_by"] = start_by_gen
        # dict_pii["start_date"] = start_date_gen
        dict_pii["ended_by"] = end_by_gen
        # dict_pii["end_date"] = end_date_gen

        json_string = json.dumps(dict_pii)
        dict_pii.clear()
        pii_json_string.append(json_string)

    return pii, pii_json_string, pii_my


if __name__ == "__main__":
    sec_data = sec.get_secret()

    pii, pii_json_string, pii_my = pii_generator()

    # postgres
    connection = conn.postgre_conn(sec_data, execution_mode)
    insert.insert(pii, connection)

    # mysql
    my_insert.insert(pii_my, sec_data, execution_mode)

    # mongo
    # mongo_conn.mongo_conn(pii_json_string)
