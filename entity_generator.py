import random
import names
import itertools
from random_words import LoremIpsum, RandomEmails, RandomNicknames, RandomWords

from faker import Faker
fake = Faker()

rw = RandomWords()
rn = RandomNicknames()
re = RandomEmails()

bigModel = False

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def countStatisticInFrame(callTimeline, keyName, expectedValue):
    return sum(
        1 if callFrame[keyName] == expectedValue else 0 for callFrame in callTimeline
    )

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

def generateCallFrame(callFrameProfile):
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
      "gender": random.choice(callFrameProfile['genderProfile']),
      "emotion": random.choice(callFrameProfile['emotionProfile']),
      "conversationTopic_informationQuery": callFrameProfile['conversationTopic_informationQuery'] if random.choice([True, False, False]) else False,
      "conversationTopic_pickupCollection": callFrameProfile['conversationTopic_pickupCollection'] if random.choice([True, False, False]) else False,
      "conversationTopic_delivery": callFrameProfile['conversationTopic_delivery'] if random.choice([True, False, False]) else False,
      "type": callFrameProfile['typeProfile'] if random.choice([True, False, False]) else "none",
      "satisfaction": random.choice(callFrameProfile['satisfactionProfile']),
      "kindness": random.choice(callFrameProfile['kindnessProfile']),
    }

def generateCallFrameProfile():

    conversationTopic = random.randint(1, 3)
    isBusiness = random.choice([True, False])
    goodConversation = random.choice([True, False])
    if goodConversation:
        emotionProfile = random.choice([
            ["calm", "happy", "neutral"],
            ["neutral", "neutral", "neutral", "calm", "happy"],
            ["neutral", "neutral", "neutral", "calm"],
        ])
        satisfactionProfile = random.choice([
            ["satisfied", "neutral", "neutral", "neutral", "neutral"],
            ["neutral"],
            ["satisfied", "neutral"],
        ])
        kindnessProfile = random.choice([
            ["kind", "neutral", "neutral", "neutral", "neutral"],
            ["kind", "neutral"],
            ["kind"],
            ["neutral"],
        ])
    else:
        emotionProfile = random.choice([
            ["sad", "angry", "fearful", "neutral", "neutral", "neutral", "neutral", ],
            ["angry", "fearful", "neutral", "neutral", "neutral", "neutral", ],
            ["happy", "fearful", "neutral", "neutral", "neutral", "neutral", ],
            ["fearful", "neutral", "neutral", "neutral",  ],
            ["angry", "neutral", ],
        ])
        satisfactionProfile = random.choice([
            ["unsatisfied", "neutral", "neutral", "neutral", "neutral"],
            ["unsatisfied"],
            ["unsatisfied", "neutral"],
        ])
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
      "conversationTopic_informationQuery": conversationTopic == 1,
      "conversationTopic_pickupCollection": conversationTopic == 2,
      "conversationTopic_delivery": conversationTopic == 3,
      "typeProfile": "business" if isBusiness else "private",
      "satisfactionProfile": satisfactionProfile,
      "kindnessProfile": kindnessProfile
    }

def generateCall():

    callLength = random.randint(60, 600)
    callFrameProfile = generateCallFrameProfile()
    callTimeline = [
        generateCallFrame(callFrameProfile)
        for _ in range(int(callLength / 10))
    ]
    callStatistics = calculateStatistics(callTimeline)
    return {
        "datetime": fake.date_between(start_date='-1y', end_date='-1d'),
        "length": callLength,
        "timeline": callTimeline,
        "statistics": callStatistics
    }

def generateEmployee():
    if bigModel:
        callCount = random.randint(1000, 5000)
    else:
        callCount = random.randint(10, 50)
    calls = [ generateCall() for _ in range(callCount) ]
    aggregatedStatistics = aggregateStatistics([ call['statistics'] for call in calls ])
    lengthAverage = int(mean([ call['length'] for call in calls ]))

    return {
        "callIds": list(range(1, callCount+1)),
        "calls": calls,
        "name": names.get_full_name(),
        "lengthAverage": lengthAverage,
        "statistics": aggregatedStatistics,
    }

def generateCompany():
    if bigModel:
        employeeCount = random.randint(20, 60)
    else:
        employeeCount = random.randint(4, 8)

    employees = [ generateEmployee() for _ in range(employeeCount) ]
    calls = []
    for employee in employees:
        calls.extend(employee['calls'])
    aggregatedStatistics = aggregateStatistics([ call['statistics'] for call in calls ])
    lengthAverage = int(mean([ call['length'] for call in calls ]))

    return {
        'employeeIds': list(range(1, employeeCount+1)),
        'employees': employees,
        'lengthAverage': lengthAverage,
        'statistics': aggregatedStatistics
    }