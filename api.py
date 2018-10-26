# System modules
import logging
import datetime

# 3rd party modules
from flask import make_response, abort

from entity_generator import generateCompany, generateCallProfile, generateCallFrame


def without_keys(d, keys):
     return {x: d[x] for x in d if x not in keys}

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
COMPANY = generateCompany()
companyToReturn = without_keys(COMPANY, ["employees", "calls"])
employeesToReturn = [ without_keys(employee, ["calls"]) for employee in COMPANY["employees"] ]

# _callFrameProfile = generateCallProfile()
# def analyzeCallFrame():
#     return generateCallFrame(
#         _callFrameProfile
#     )
def analyzeCallFrame():
    return None

def findEmployee(employeeId):
    try:
        employee = employeesToReturn[int(employeeId) - 1]
        return employee
    except Exception:
        logging.exception("Error getting employee")
        return None

def findCall(callId):
    try:
        call = COMPANY["calls"][int(callId) - 1]
        return call
    except Exception:
        logging.exception("Error getting call")
        return None


def ping():

    return {
        'result': 'ping',
        'datetime': datetime.datetime.utcnow()
    }

def getCalls():
    return COMPANY['calls']

def getCall(callId):
    call = findCall(callId)

    if not call:
        return abort(
            404,
            f"Call with ID {callId} not found"
        )

    return call


def getEmployees():
    return employeesToReturn

def getEmployee(employeeId):
    employee = findEmployee(employeeId)

    if not employee:
        return abort(
            404,
            f"Employee with ID {employeeId} not found"
        )

    return employee

def getCompany():
    return companyToReturn