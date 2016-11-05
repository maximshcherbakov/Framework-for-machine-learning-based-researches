from framework.common.parameterizable import parameterizable

# class for models benchmarking and estimation
class forecast_handler(parameterizable):

	addidional_parameters = ['forecasting_columns']
	parameters = {}
	def __init__(self, 
					data_provider, 
					parameters, 
					benchmark_model, 
					forecasting_models, 
					error_measurements):
		self.data_provider = data_provider
		self.parameters = parameters
		self.benchmark_model = benchmark_model
		self.forecasting_models = forecasting_models
		self.error_measurements = error_measurements


	def get_benchmark_result(self):
		columns = None
		if 'forecasting_columns' in self.parameters:
			columns = self.parameters['forecasting_columns']

		model = self.benchmark_model['model']
		params = self.benchmark_model['parameters']

		benchmark_result = model.forecast(params, 
											self.data_provider.get_training_set(columns), 
											self.parameters['testing_set_size'])
		return benchmark_result


	def get_error_measurements(self, forecasted_set):
		print('err_m')
		result = {}
		for column in forecasted_set.keys():
			col_result = {}
			for model in self.error_measurements:
				#print(column)
				#print(model.get_name())
				#print(self.data_provider.get_testing_set([column])[column])
				#print(forecasted_set[column])
				col_result[model.get_name()] = model.calculate(self.data_provider.get_testing_set([column])[column],
																	forecasted_set[column])

			result[column] = col_result
		return result


	def grid_search(self):
		columns = None
		if 'forecasting_columns' in self.parameters:
			columns = self.parameters['forecasting_columns']
		else:
			columns = list(self.data_provider.get_training_set().keys())

		result = {}

		for column in columns:
			col_result = {}
				for model in self.forecasting_models:
					model_result = {}

					# for each param set
						# learn model
						# get test values

						# for each error measurement
							#calculate and add to param_set_result = {}

					col_result[model.get_name()] = model_result

			result[column] = col_result

		return result