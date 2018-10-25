# System modules
import logging
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

from entity_generator import generateCompany

def without_keys(d, keys):
     return {x: d[x] for x in d if x not in keys}

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
COMPANY = generateCompany()
companyToReturn = without_keys(COMPANY, "employees")
employeesToReturn = [ without_keys(employee, "calls") for employee in COMPANY["employees"] ]

def analyzeCallFrame():
    return None

def findEmployee(employeeId):
    try:
        employee = employeesToReturn[int(employeeId)]
        return employee
    except Exception:
        logging.exception("Error getting employee")
        return None

def findCall(employeeId, callId):
    try:
        employee = COMPANY["employees"][int(employeeId)]
    except Exception:
        logging.exception("Error getting employee")
        employee = None

    try:
        call = employee["calls"][int(callId)]
        return call
    except Exception:
        logging.exception("Error getting call")
        return None


def getCall(employeeId, callId):
    call = findCall(employeeId, callId)

    if not call:
        return abort(
            404,
            f"Call with ID {callId} not found"
        )

    return call


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