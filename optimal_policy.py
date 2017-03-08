import helper as hlp

states = hlp.load_txt_data("logs/sim_improved-learning.txt").get_data()

print states

#Initialize the correct counter
correct = 0

#Initialize the wrong counter
wrong = 0

for key in states:

    #Check the traffic light
    if key[1] == 'red':

        #If best move == None is correct
        if hlp.is_best_move(None,states[key]):
            correct += 1

        #Else it is wrong
        else:
            wrong += 1

print "In case the fraffic light is red"
print "Correct states: " + str(correct)
print "Wrong states: " + str(wrong)