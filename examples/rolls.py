import sys
import os

import collections

# Complete the function below.


def differentTeams(skills):
    x = {"p": 0, "c": 0, "m": 0, "b": 0, "z": 0}
    for skill in skills:
        x[skill] += 1
    print(x.get(min(x, key=x.get)))


if __name__ == "__main__":
    f = open("/Users/balassit/workspace/interview/examples/output", "w")

    try:
        skills = str(input())
    except:
        skills = None

    res = differentTeams(skills)
    f.write(str(res) + "\n")
    f.close()
