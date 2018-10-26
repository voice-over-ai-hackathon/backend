import random
import names
import uifaces
from random_words import LoremIpsum, RandomEmails, RandomNicknames, RandomWords

from faker import Faker

fake = Faker()

rw = RandomWords()
rn = RandomNicknames()
re = RandomEmails()

_employeeId = 1
_callId = 1

bigModel = False

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def countStatisticInFrame(callTimeline, keyName, expectedValue):
    return sum(
        1 if callFrame[keyName] == expectedValue else 0 for callFrame in callTimeline
    )

def generateCallId():
    global _callId
    newCallId = _callId
    _callId = _callId + 1
    return newCallId

def generateEmployeeId():
    global _employeeId
    newEmployeeId = _employeeId
    _employeeId = _employeeId + 1
    return newEmployeeId

def aggregateStatistic(statisticsArray, statistic):
    return sum(
        currentStatistics[statistic] for currentStatistics in statisticsArray
    )

def aggregateStatistics(statisticsArray):
    return {
        "genderMale": aggregateStatistic(statisticsArray, "genderMale"),
        "genderFemale": aggregateStatistic(statisticsArray, "genderFemale"),
        "emotionCalm": aggregateStatistic(statisticsArray, "emotionCalm"),
        "emotionHappy": aggregateStatistic(statisticsArray, "emotionHappy"),
        "emotionSad": aggregateStatistic(statisticsArray, "emotionSad"),
        "emotionAngry": aggregateStatistic(statisticsArray, "emotionAngry"),
        "emotionFearful": aggregateStatistic(statisticsArray, "emotionFearful"),
        "emotionNeutral": aggregateStatistic(statisticsArray, "emotionNeutral"),
        "conversationTopic_informationQuery": aggregateStatistic(statisticsArray, "conversationTopic_informationQuery"),
        "conversationTopic_pickupCollection": aggregateStatistic(statisticsArray, "conversationTopic_pickupCollection"),
        "conversationTopic_delivery": aggregateStatistic(statisticsArray, "conversationTopic_delivery"),
        "typeBusiness": aggregateStatistic(statisticsArray, "typeBusiness"),
        "typePrivate": aggregateStatistic(statisticsArray, "typePrivate"),
        "satisfactionSatisfied": aggregateStatistic(statisticsArray, "satisfactionSatisfied"),
        "satisfactionUnsatisfied": aggregateStatistic(statisticsArray, "satisfactionUnsatisfied"),
        "satisfactionNeutral": aggregateStatistic(statisticsArray, "satisfactionNeutral"),
        "kindnessKind": aggregateStatistic(statisticsArray, "kindnessKind"),
        "kindnessUnkind": aggregateStatistic(statisticsArray, "kindnessUnkind"),
        "kindnessNeutral": aggregateStatistic(statisticsArray, "kindnessNeutral"),
    }

def calculateStatistics(callTimeline):
    return {
        "totalFrames": len(callTimeline),
        "genderMale": countStatisticInFrame(callTimeline, "gender", "male"),
        "genderFemale": countStatisticInFrame(callTimeline, "gender", "female"),
        "emotionCalm": countStatisticInFrame(callTimeline, "emotion", "calm"),
        "emotionHappy": countStatisticInFrame(callTimeline, "emotion", "happy"),
        "emotionSad": countStatisticInFrame(callTimeline, "emotion", "sad"),
        "emotionAngry": countStatisticInFrame(callTimeline, "emotion", "angry"),
        "emotionFearful": countStatisticInFrame(callTimeline, "emotion", "fearful"),
        "emotionNeutral": countStatisticInFrame(callTimeline, "emotion", "neutral"),
        "conversationTopic_informationQuery": countStatisticInFrame(callTimeline, "conversationTopic_informationQuery", True),
        "conversationTopic_pickupCollection": countStatisticInFrame(callTimeline, "conversationTopic_pickupCollection", True),
        "conversationTopic_delivery": countStatisticInFrame(callTimeline, "conversationTopic_delivery", True),
        "typeBusiness": countStatisticInFrame(callTimeline, "type", "business"),
        "typePrivate": countStatisticInFrame(callTimeline, "type", "private"),
        "satisfactionSatisfied": countStatisticInFrame(callTimeline, "satisfaction", "satisfied"),
        "satisfactionUnsatisfied": countStatisticInFrame(callTimeline, "satisfaction", "unsatisfied"),
        "satisfactionNeutral": countStatisticInFrame(callTimeline, "satisfaction", "neutral"),
        "kindnessKind": countStatisticInFrame(callTimeline, "kindness", "kind"),
        "kindnessUnkind": countStatisticInFrame(callTimeline, "kindness", "unkind"),
        "kindnessNeutral": countStatisticInFrame(callTimeline, "satisfaction", "neutral"),
    }

def calculateMetricsByFilter(calls, filterFunc):
    totalCount = sum([ 1 if filterFunc(call) else 0 for call in calls ])
    totalLength = sum([ call["length"] if filterFunc(call) else 0 for call in calls ])

    return float(totalCount), float(totalLength)

def calculateMetrics(calls):
    allCallCount, allCallLength = calculateMetricsByFilter(calls, lambda call: True)
    businessCallCount, businessCallLength = calculateMetricsByFilter(calls, lambda call: call["analysis"]["type"] == "business")
    privateCallCount, privateCallLength = calculateMetricsByFilter(calls, lambda call: call["analysis"]["type"] == "private")
    informationQueryCallCount, informationQueryCallLength = \
        calculateMetricsByFilter(calls, lambda call: call["analysis"]["conversationTopic_informationQuery"])
    pickupCollectionCallCount, pickupCollectionCallLength = \
        calculateMetricsByFilter(calls, lambda call: call["analysis"]["conversationTopic_pickupCollection"])
    deliveryCallCount, deliveryCallLength = \
        calculateMetricsByFilter(calls, lambda call: call["analysis"]["conversationTopic_delivery"])

    goodCalls = sum(1 if call["analysis"]["emotion"] in ("neutral", "happy", "calm") else 0 for call in calls)
    badCalls = sum(1 if call["analysis"]["emotion"] in ("angry", "sad", "fearful") else 0 for call in calls)
    score = goodCalls - badCalls

    return {
        "score": score,
        "callPercentage": {
            "all": int(allCallCount / allCallCount * 100.0),
            "business": int(businessCallCount / allCallCount * 100.0),
            "private": int(privateCallCount / allCallCount * 100.0),
            "conversationTopic_informationQuery": int(informationQueryCallCount / allCallCount * 100.0),
            "conversationTopic_pickupCollection": int(pickupCollectionCallCount / allCallCount * 100.0),
            "conversationTopic_delivery": int(deliveryCallCount / allCallCount * 100.0),
        },
        "callAverageLength": {
            "all": int(allCallLength / allCallCount),
            "business": int(businessCallLength / businessCallCount),
            "private": int(privateCallLength / privateCallCount),
            "conversationTopic_informationQuery": int(informationQueryCallLength / informationQueryCallCount),
            "conversationTopic_pickupCollection": int(pickupCollectionCallLength / pickupCollectionCallCount),
            "conversationTopic_delivery": int(deliveryCallLength / deliveryCallCount),
        },
    }

def generateCallFrame(callProfile):
    # {
    #     "genderProfile": random.choice(
    #         ["male", "female"],
    #         ["male", "male"],
    #         ["female", "male"],
    #     ),
    #     "emotionProfile": emotionProfile,
    #     "conversationTopic_informationQuery": conversationTopic == 1,
    #     "conversationTopic_pickupCollection": conversationTopic == 2,
    #     "conversationTopic_delivery": conversationTopic == 1,
    #     "typeProfile": "business" if isBusiness else "private",
    #     "satisfactionProfile": satisfactionProfile,
    #     "kindnessProfile": kindnessProfile
    # }

    return {
      "gender": random.choice(callProfile['genderProfile']),
      "emotion": random.choice(callProfile['emotionProfile']),
      "conversationTopic_informationQuery": callProfile['conversationTopic_informationQuery'] if random.choice([True, False, False]) else False,
      "conversationTopic_pickupCollection": callProfile['conversationTopic_pickupCollection'] if random.choice([True, False, False]) else False,
      "conversationTopic_delivery": callProfile['conversationTopic_delivery'] if random.choice([True, False, False]) else False,
      "type": callProfile['typeProfile'] if random.choice([True, False, False]) else "none",
      "satisfaction": random.choice(callProfile['satisfactionProfile']),
      "kindness": random.choice(callProfile['kindnessProfile']),
    }

def generateCallProfile(callAnalysis):

    isBusiness = callAnalysis["type"] == "business"
    goodEmotion = callAnalysis["emotion"] in ("neutral", "happy", "calm")
    if goodEmotion:
        emotionProfile = random.choice([
            ["calm", "happy", "neutral"],
            ["neutral", "neutral", "neutral", "calm", "happy"],
            ["neutral", "neutral", "neutral", "calm"],
        ])
    else:
        emotionProfile = random.choice([
            ["sad", "angry", "fearful", "neutral", "neutral", "neutral", "neutral", ],
            ["angry", "fearful", "neutral", "neutral", "neutral", "neutral", ],
            ["happy", "fearful", "neutral", "neutral", "neutral", "neutral", ],
            ["fearful", "neutral", "neutral", "neutral",  ],
            ["angry", "neutral", ],
        ])

    goodSatisfaction = callAnalysis["satisfaction"] in ("neutral", "satisfied")
    if goodSatisfaction:
        satisfactionProfile = random.choice([
            ["satisfied", "neutral", "neutral", "neutral", "neutral"],
            ["neutral"],
            ["satisfied", "neutral"],
        ])
    else:
        satisfactionProfile = random.choice([
            ["unsatisfied", "neutral", "neutral", "neutral", "neutral"],
            ["unsatisfied"],
            ["unsatisfied", "neutral"],
        ])

    goodKindness = callAnalysis["kindness"] in ("neutral", "kind")
    if goodKindness:
        kindnessProfile = random.choice([
            ["kind", "neutral", "neutral", "neutral", "neutral"],
            ["kind", "neutral"],
            ["kind"],
            ["neutral"],
        ])
    else:
        kindnessProfile = random.choice([
            ["unkind", "neutral", "neutral", "neutral", "neutral"],
            ["unkind", "neutral"],
            ["unkind"],
        ])

    return {
      "genderProfile": random.choice([
          ["male", "female"],
          ["male", "male"],
          ["female", "male"],
      ]),
      "emotionProfile": emotionProfile,
      "conversationTopic_informationQuery": callAnalysis["conversationTopic_informationQuery"],
      "conversationTopic_pickupCollection": callAnalysis["conversationTopic_pickupCollection"],
      "conversationTopic_delivery": callAnalysis["conversationTopic_delivery"],
      "typeProfile": "business" if isBusiness else "private",
      "satisfactionProfile": satisfactionProfile,
      "kindnessProfile": kindnessProfile
    }

def generateCall():

    callLength = random.randint(60, 600)
    callTopic = random.choice([1, 2, 3])
    callAnalysis = {
      "gender": random.choice(["male", "female"]),
      "emotion": random.choice(["calm", "happy", "sad", "angry", "fearful", "neutral"]),
      "conversationTopic_informationQuery": callTopic == 1,
      "conversationTopic_pickupCollection": callTopic == 2,
      "conversationTopic_delivery": callTopic == 3,
      "type": random.choice(["business", "private"]),
      "satisfaction": random.choice(["satisfied", "unsatisfied", "neutral"]),
      "kindness": random.choice(["kind", "unkind", "neutral"]),
    }
    callProfile = generateCallProfile(callAnalysis)

    callTimeline = [
        generateCallFrame(callProfile)
        for _ in range(int(callLength / 10))
    ]
    callStatistics = calculateStatistics(callTimeline)
    return {
        "id": generateCallId(),
        "datetime": fake.date_time_between(start_date='-1y', end_date='-1d'),
        "length": callLength,
        "timeline": callTimeline,
        "analysis": callAnalysis,
        "statistics": callStatistics
    }

def generateEmployee():

    isMale = random.choice([True, False])
    if bigModel:
        callCount = random.randint(1000, 5000)
    else:
        callCount = random.randint(10, 50)
    calls = [ generateCall() for _ in range(callCount) ]
    aggregatedStatistics = aggregateStatistics([ call['statistics'] for call in calls ])
    lengthAverage = int(mean([ call['length'] for call in calls ]))
    pic = random.choice(uifaces.male)['photo'] if isMale else random.choice(uifaces.female)['photo']

    return {
        "id": generateEmployeeId(),
        "callIds": [ call['id'] for call in calls ],
        "calls": calls,
        "name": uifaces.randomManName() if isMale else uifaces.randomWomanName(),
        "picture": pic,
        "lengthAverage": lengthAverage,
        "metrics": calculateMetrics(calls),
        "statistics": aggregatedStatistics,
    }

def generateCompany():
    if bigModel:
        employeeCount = random.randint(20, 60)
    else:
        employeeCount = random.randint(10, 20)

    employees = [ generateEmployee() for _ in range(employeeCount) ]
    calls = []
    for employee in employees:
        calls.extend(employee['calls'])
    aggregatedStatistics = aggregateStatistics([ call['statistics'] for call in calls ])
    lengthAverage = int(mean([ call['length'] for call in calls ]))

    employeesByScore = sorted(employees, key=lambda employee: employee['metrics']["score"])
    topFiveEmployees = employeesByScore[0:5]
    bottomFiveEmployees = employeesByScore[-5:]

    return {
        'topFiveEmployeeIds': [ employee['id'] for employee in topFiveEmployees ],
        'bottomFiveEmployeeIds': [employee['id'] for employee in bottomFiveEmployees],
        'employeeIds': [ employee['id'] for employee in employees ],
        'employees': employees,
        'calls': calls,
        'lengthAverage': lengthAverage,
        "metrics": calculateMetrics(calls),
        'statistics': aggregatedStatistics
    }