from environment import TrafficLight

tl = TrafficLight()

for x in range(0,50):
    tl.update(x)
    print str(x) + " " + str(tl.state)