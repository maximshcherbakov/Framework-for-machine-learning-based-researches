from code.forecasting_models.base import base_model as pb
import random

class random_model(pb.base_model):
    
	def forecast(self, parameters, training_set, forecast_horizon):
		forecast_values = []

		generator = random.seed()

		max_value = max(training_set)
		min_value = min(training_set)
		
		for x in range(0, forecast_horizon):
			forecast_values.append(random.randrange(min_value, max_value))

		return forecast_values