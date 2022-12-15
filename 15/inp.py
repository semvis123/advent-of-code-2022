inputData = """Sensor at x=407069, y=1770807: closest beacon is at x=105942, y=2000000
Sensor at x=2968955, y=2961853: closest beacon is at x=2700669, y=3091664
Sensor at x=3069788, y=2289672: closest beacon is at x=3072064, y=2287523
Sensor at x=2206, y=1896380: closest beacon is at x=105942, y=2000000
Sensor at x=3010408, y=2580417: closest beacon is at x=2966207, y=2275132
Sensor at x=2511130, y=2230361: closest beacon is at x=2966207, y=2275132
Sensor at x=65435, y=2285654: closest beacon is at x=105942, y=2000000
Sensor at x=2811709, y=3379959: closest beacon is at x=2801189, y=3200444
Sensor at x=168413, y=3989039: closest beacon is at x=-631655, y=3592291
Sensor at x=165506, y=2154294: closest beacon is at x=105942, y=2000000
Sensor at x=2720578, y=3116882: closest beacon is at x=2700669, y=3091664
Sensor at x=786521, y=1485720: closest beacon is at x=105942, y=2000000
Sensor at x=82364, y=2011850: closest beacon is at x=105942, y=2000000
Sensor at x=2764729, y=3156203: closest beacon is at x=2801189, y=3200444
Sensor at x=1795379, y=1766882: closest beacon is at x=1616322, y=907350
Sensor at x=2708986, y=3105910: closest beacon is at x=2700669, y=3091664
Sensor at x=579597, y=439: closest beacon is at x=1616322, y=907350
Sensor at x=2671201, y=2736834: closest beacon is at x=2700669, y=3091664
Sensor at x=3901, y=2089464: closest beacon is at x=105942, y=2000000
Sensor at x=144449, y=813212: closest beacon is at x=105942, y=2000000
Sensor at x=3619265, y=3169784: closest beacon is at x=2801189, y=3200444
Sensor at x=2239333, y=3878605: closest beacon is at x=2801189, y=3200444
Sensor at x=2220630, y=2493371: closest beacon is at x=2966207, y=2275132
Sensor at x=1148022, y=403837: closest beacon is at x=1616322, y=907350
Sensor at x=996105, y=3077490: closest beacon is at x=2700669, y=3091664
Sensor at x=3763069, y=3875159: closest beacon is at x=2801189, y=3200444
Sensor at x=3994575, y=2268273: closest beacon is at x=3072064, y=2287523
Sensor at x=3025257, y=2244500: closest beacon is at x=2966207, y=2275132
Sensor at x=2721366, y=1657084: closest beacon is at x=2966207, y=2275132
Sensor at x=3783491, y=1332930: closest beacon is at x=3072064, y=2287523
Sensor at x=52706, y=2020407: closest beacon is at x=105942, y=2000000
Sensor at x=2543090, y=47584: closest beacon is at x=3450858, y=-772833
Sensor at x=3499766, y=2477193: closest beacon is at x=3072064, y=2287523"""

testData = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


import re
inputData = [[[int(coord) for coord in re.split('[=,]', y) if re.match('-?\d+', coord)]
              for y in x.split(':')] for x in inputData.splitlines()]
testData = [[[int(coord) for coord in re.split('[=,]', y) if re.match('-?\d+', coord)]
              for y in x.split(':')] for x in testData.splitlines()]
