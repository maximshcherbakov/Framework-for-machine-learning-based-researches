from framework.forecasting.base import base_model as bm

class simple_average_model(bm.base_model):

	def forecast(self, parameters, training_set, forecast_horizon):
		print(type(training_set))
		print(len(training_set))
		# acquire required parameters
		lag = parameters['lag']
		repetition_interval = parameters['repetition_interval']
		frequency = parameters['frequency']

		forecast = []
		for i in range(0,forecast_horizon):
			arr = []
			for l in range(1, lag + 1):
				arr.append(training_set[i - l * frequency])

			forecast.append(sum(arr)/float(len(arr)))

		return forecast

	def get_name(self):
		return 'simple average'