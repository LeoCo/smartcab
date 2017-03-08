import re

class load_txt_data(object):

    def __init__(self,filename):
        self.filename = filename

    def clean_string(self,x):
        if x == 'None':
            return None
        else:
            return x[1:-1]

    def get_data(self):

        with open(self.filename) as f:
            content = f.readlines()
        content = [x.strip() for x in content]

        #Clean firsts rows and last one
        del content[0:4]
        content.pop()

        #Recreate the states variable
        states = {}

        for i in xrange(0, len(content),6):

            regular_exp = re.match(r'\((.*),\s(.*),\s(.*),\s(.*),\s(.*)\)', content[i])

            key = (self.clean_string(regular_exp.group(1)),
                   self.clean_string(regular_exp.group(2)),
                   self.clean_string(regular_exp.group(3)),
                   self.clean_string(regular_exp.group(4)),
                   self.clean_string(regular_exp.group(5)))

            value = { None : float(re.match(r'--.*: (.*)', content[i + 1]).group(1)),
                      'forward' : float(re.match(r'--.*: (.*)', content[i + 2]).group(1)),
                      'right' : float(re.match(r'--.*: (.*)', content[i + 3]).group(1)),
                      'left' : float(re.match(r'--.*: (.*)', content[i + 4]).group(1))}

            states[key] = value

        return states

def is_best_move(best, moves):

    #Check if there is a best move
    for m in moves:
        if moves[m] > moves[best]:
            return False

    #If not return true
    return True

if __name__ == '__main__':

    print load_txt_data("logs/sim_improved-learning.txt").get_data()