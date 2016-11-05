from framework.forecasting.base import base_model as pb
import random

class random_model(pb.base_model):
    
	def forecast(self, parameters, training_set, forecast_horizon):

		generator = random.seed()

		result = {}
		for x in training_set:
			forecast_values = []


			max_value = max(training_set)
			min_value = min(training_set)
			
			for y in range(0, forecast_horizon):
				forecast_values.append(random.randrange(min_value, max_value))

			result.add(x, forecast_values)

		return result

	def get_name(self):
		return 'random'