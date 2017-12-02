import random


part1 = ["machine learning solution" , "recursive algorithm" , "e-portal" , "cross platform app" , "revolutionary supply chain management platform", "real-time code sharing tool" , "distributed solutions matrix", "backwards compatible hardware driver", "protocol suite"]
part2 = ["LGBT assylum seekers",  "obese children", "the homeless" ,"the elderly", "rural communities" ,  "young people in disadvantaged areas",  ]
part3 = ["bespoke twitter API","Big Data", "the Cloud", "open source software","obfuscated code" , "bitcoin mining",  "a deep web neural network", "social media", "distributed networks", "node.js" ,]

rand1 = random.randrange(0,len(part1))
rand2 = random.randrange(0,len(part2))
rand3 = random.randrange(0,len(part3))

print("We need a " + part1[rand1] + " to help " + part2[rand2] + " using " + part3[rand3])