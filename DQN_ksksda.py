import linetrace
import capture
import time
import sys

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

class QNetwork:
	def __init__(self, layer_info):
		self.model = Sequential()
		self.model.add(Dense(layer_info[1][0], activation = layer_info[1][1], input_dim = layer_info[0][0]))
		for i in range(len(layer_info) - 2):
			self.model.add(Dense(layer_info[i + 2][0], activation = layer_info[i + 1][1]))
		self.model.compile(optimizer = "sgd", loss = "mean_squared_error", metrics = ['accuracy'])
		self.input_size = layer_info[0][0]
		self.output_size = layer_info[len(layer_info) - 1][0]

layer_info = []
layer_info.append([6,'linear'])
layer_info.append([18,'sigmoid'])
layer_info.append([9,'linear'])
mainQN = QNetwork(layer_info)
mainQN.model.load_weights('weight_ksksda.h5')

def linetrace_DQN_ksksda(rc):
    print(sys._getframe().f_code.co_name)
    yield None
    while True:
        if all(rc.sensor):
            if not linetrace.off_flag:
                linetrace.line_crossed += 1
                linetrace.off_flag = True
        else:
            linetrace.off_flag = False
            if linetrace.line_crossed == 2:
                yield capture.throw
            elif linetrace.line_crossed == 4:
                yield capture.seek
            elif linetrace.line_crossed == 6:
                yield linetrace.shoot
            # elif linetrace.line_crossed >= 7:
            # yield linetrace.shoot2
        
        state = np.array(rc.motor + rc.sensor).reshape((1,-1))
        a_list = np.dot(state[0,0]!=np.array([[0],[np.nan],[10]]), state[0,1]!=np.array([[0,np.nan,10]])).reshape(9) * np.arange(1,10)
        action_list = a_list[a_list.nonzero()] - 1
        predicted_rewards = mainQN.model.predict(state)[0][action_list]
        action = action_list[np.argmax(predicted_rewards)]
        rc.motor[0] = np.clip(rc.motor[0] + 0.1*(action // 3 - 1) , 0, 1)
        rc.motor[1] = np.clip(rc.motor[1] + 0.1*(action % 3 - 1) , 0, 1)
        
        yield None

