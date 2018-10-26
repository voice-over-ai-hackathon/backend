import pprint

frames = [
  {
    "_text": " י ו פ י ע  ש ל ו ם  מ ד ב ר ת  ה ד ס  ו ו א ו  כ מ ה  ז מ ן  ה מ ת נ ה  מ ה  ז ה  צ ר י ך",
    "entities": {
      "kindness": [
        {
          "confidence": 1,
          "value": "kind",
          "type": "value"
        },
        {
          "confidence": 1,
          "value": "kind",
          "type": "value"
        }
      ],
      "satisfaction": [
        {
          "suggested": True,
          "confidence": 0.62085752895009,
          "value": "כ מ ה ז מ ן  ה מ ת נ ה  מ ה  ז ה  צ ר י ך",
          "type": "value"
        }
      ]
    },
    "msg_id": "1xyIbOIiIbc40Mdnj",
    "emotion": "male_angry"
  },
  {
    "_text": " א נ י  מ מ ש  מ ת נ צ ל ת  א י ך  א ו כ ל  ל ע ז ו ר  א י פ ה  הdelivery  ש ל נ ו  ה י י ת י",
    "entities": {
      "kindness": [
        {
          "confidence": 0.84121066738211,
          "value": "kind",
          "type": "value"
        },
        {
          "confidence": 0.79825582296268,
          "value": "kind",
          "type": "value"
        }
      ],
      "conversation_topic": [
        {
          "confidence": 1,
          "value": "delivery",
          "type": "value"
        },
        {
          "confidence": 0.8683307503783,
          "value": "delivery",
          "type": "value"
        }
      ],
      "customer_type": [
        {
          "confidence": 1,
          "value": "business",
          "type": "value"
        }
      ]
    },
    "msg_id": "1WN71vRu4MnICj6Dm",
    "emotion": "male_fearful"
  },
  {
    "_text": " צ י ו ד  א ת מ ו ל  א ת ה  מ ת ק ש ר",
    "entities": {
      "customer_type": [
        {
          "confidence": 1,
          "value": "business",
          "type": "value"
        }
      ]
    },
    "msg_id": "1kQRySu3J3Rfu0GPf",
    "emotion": "female_calm"
  },
  {
    "_text": " מ ה  ח ב ר ה  ש ל י  ל א  י ו ד ע ת  ב ע צ מ י",
    "entities": {
      "customer_type": [
        {
          "confidence": 1,
          "value": "business",
          "type": "value"
        }
      ],
      "satisfaction": [
        {
          "confidence": 1,
          "value": " ל ק ו ח  ל א  מ ר ו צ ה",
          "type": "value"
        }
      ]
    },
    "msg_id": "1gXLl3xFo9aM24DwQ",
    "emotion": "male_angry"
  },
  {
    "_text": " ת ו כ ל  ב ב ק ש ה  ל ת ת  ל י  מ ס פ ר  ט ל פ ו ן  ש ל ך  ז ה  ל א  מ ו פ י ע  ל כ ם  ע ל  ה מ ס ך  א ו  מ ש ה ו",
    "entities": {
      "kindness": [
        {
          "confidence": 0.84222354522917,
          "value": "kind",
          "type": "value"
        },
        {
          "confidence": 1,
          "value": "kind",
          "type": "value"
        },
        {
          "confidence": 1,
          "value": "kind",
          "type": "value"
        }
      ],
      "conversation_topic": [
        {
          "confidence": 1,
          "value": " ה ז מ נ ת  א י ס ו ף",
          "type": "value"
        }
      ],
      "satisfaction": [
        {
          "confidence": 0.9444316872887,
          "value": " ל ק ו ח  ל א  מ ר ו צ ה",
          "type": "value"
        }
      ]
    },
    "msg_id": "1YcC0RCYwYZXdy42z",
    "emotion": "male_fearful"
  },
  {
    "_text": " ל צ ע ר י  ל א  ט ו ב 054 888",
    "entities": {
      "kindness": [
        {
          "confidence": 0.77006926996721,
          "value": "kind",
          "type": "value"
        }
      ]
    },
    "msg_id": "1oFYZOT9ZYE2TH712"
  },
  {
    "_text": "1 2 3 4",
    "entities": {},
    "msg_id": "1cBjRN6vMDYcb03uU",
    "emotion": "male_angry"
  },
  {
    "_text": " כ ן  י ו פ י  ה פ ר ט י ם  ש ל ך  מ ו ל י  א ח ל ה  א ת ה  מ ת ק ש ר",
    "entities": {
      "kindness": [
        {
          "confidence": 1,
          "value": "kind",
          "type": "value"
        }
      ],
      "customer_type": [
        {
          "confidence": 1,
          "value": " פ ר ט י",
          "type": "value"
        }
      ],
      "satisfaction": [
        {
          "confidence": 1,
          "value": " ל ק ו ח  מ ר ו צ ה",
          "type": "value"
        }
      ]
    },
    "msg_id": "1oE3TvRKQCj9TCSS9",
    "emotion": "male_fearful"
  },
  {
    "_text": " ל ג ב י  הdelivery  ה א ח ר ו ן  נ כ ו ן  א נ י  ר ו א ה  ש ז ה  א מ ו ר  ל ה ג י ע  א ל י ך  ל מ ש ר ד",
    "entities": {
      "conversation_topic": [
        {
          "confidence": 0.89828598039533,
          "value": "delivery",
          "type": "value"
        }
      ],
      "customer_type": [
        {
          "confidence": 1,
          "value": "business",
          "type": "value"
        }
      ]
    },
    "msg_id": "1aKZc4fZjyPenOnBY",
    "emotion": "female_calm"
  },
  {
    "_text": " מ ח ר  מ ה  מ ח ר  א מ ר ו  ל י  ה י ו ם  א נ י  מ ב י נ ה",
    "entities": {},
    "msg_id": "1c280fiPe8hVdKYqy",
    "emotion": "male_angry"
  },
  {
    "_text": " ה ו א  ב ט ח  מ מ ש  נ ש ב ר  ל י  כ ב ר  מ י  כ ן  א נ י  מ מ ש  מ ת נ צ ל ת",
    "entities": {
      "satisfaction": [
        {
          "confidence": 1,
          "value": " ל ק ו ח  ל א  מ ר ו צ ה",
          "type": "value"
        }
      ],
      "kindness": [
        {
          "confidence": 0.84675173253561,
          "value": "kind",
          "type": "value"
        }
      ]
    },
    "msg_id": "1LYs7saKULvoeLWGE",
    "emotion": "male_angry"
  },
  {
    "_text": " ז ה  י ג י ע  מ ח ר  ב י ן 9  ל 12  ז ה  ב ס ד ר  ש ז ה  ל א  י ג י ע  ב ז מ ן",
    "entities": {
      "kindness": [
        {
          "confidence": 1,
          "value": "kind",
          "type": "value"
        }
      ],
      "satisfaction": [
        {
          "suggested": True,
          "confidence": 0.70422333263348,
          "value": " ל א  י ג י ע  ב ז מ ן",
          "type": "value"
        }
      ]
    },
    "msg_id": "1h4soPn0Rpy8t2Ifi",
    "emotion": "male_angry"
  }
]

# {
#     "_text": " י ו פ י ע  ש ל ו ם  מ ד ב ר ת  ה ד ס  ו ו א ו  כ מ ה  ז מ ן  ה מ ת נ ה  מ ה  ז ה  צ ר י ך",
#     "entities": {
#         "kindness": [
#             {
#                 "confidence": 1,
#                 "value": "kind",
#                 "type": "value"
#             },
#             {
#                 "confidence": 1,
#                 "value": "kind",
#                 "type": "value"
#             }
#         ],
#         "satisfaction": [
#             {
#                 "suggested": True,
#                 "confidence": 0.62085752895009,
#                 "value": "כ מ ה ז מ ן  ה מ ת נ ה  מ ה  ז ה  צ ר י ך",
#                 "type": "value"
#             }
#         ]
#     },
#     "msg_id": "1xyIbOIiIbc40Mdnj",
#     "emotion": "male_angry"
# },

newFrames = []
for idx, frame in enumerate(frames):

    newFrame = {}

    if 'emotion' in frame:
        emotion = frame['emotion'].split("_")[1]
        newFrame['emotion'] = emotion
    if 'entities' in frame:
        entities = frame['entities'].keys()
        newFrame['entities'] = list(entities)
    newFrames.append(newFrame)

pprint.pprint(newFrames)