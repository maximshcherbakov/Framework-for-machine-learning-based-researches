# all treats for forecast, error measurements, etc.
import pandas as pd

class forecast_machine(object):
	"""
		params - entity of 'parameters' type
		data_provider - entity, which has 'get_data' method, containing pandas dataframe of data for forecasting
		benchmark model - typle(benchmark model, dictionary of params for model, including variation range and step of change )
		forecast_models - array of objects same to benchmark model, contains of all needed to calculate and optimize
						  forecast models
		error_measurement_functions - functions, that calculate quality of forecasting  

	"""
	def __init__(self, params, data_provider, benchmark_model, forecast_models, error_measurement_functions):
		
		# check for params
		rp = ['forecast_horizon', 'training_set_size', 'columns_for_forecasting'] #'input_parameters', 'output_parameters']
		for p in rp:
			if not params.contains(p):
				raise Exception('Required parameter "' + p + '" did not provided')

		self.params = params
		self.data_provider = data_provider
		self.benchmark_model = benchmark_model[0]
		self.benchmark_model_params = benchmark_model[1]

		self.forecast_models = forecast_models

		# values may be DataFrames or Series. It depends on columns count
		#self.input_values = data_provider.get_data()[params.input_parameters] # that is for multi-dimentional forecasting
		#self.output_values = data_provider.get_data()[params.output_parameters]
		self.forecasting_values = data_provider.get_data()[params.columns_for_forecasting]

		# if training_set_size between 0 and 1 then share specified
		# otherwise number of records
		if params.training_set_size > 0 and params.training_set_size < 1:
			cnt = data_provider.get_data().shape[0]
			training_cnt = int(cnt*params.training_set_size)
			self.training_set = self.forecasting_values[:training_cnt]
			self.testing_set = self.forecasting_values[training_cnt:]

			# calculate number, according to share and divide values into training and testing dataset
		elif params.training_set_size >= 1: 
			tss = int(training_set_size) # user may specify float number or number with fraction. 
										 # it's possible, but requires rounding
			self.training_set = self.forecasting_values[:tss]
			self.testing_set = self.forecasting_values[tss:]
			# divide dataset
		else: 
			# error, value out of allowed range
			raise ValueError('"training_set_size" has wrong value: ' + str(params.training_set_size))

		print('tr s ' + str(len(self.training_set)))
		print('ts s ' + str(len(self.testing_set)))

	def benchmark(self):
		if not 'benchmark_model_result' in self.__dict__:
			self.benchmark_model_result = self.benchmark_model.forecast(self.benchmark_model_params,
																		 self.training_set['Ele Act Technobo (Wh)'].tolist(), # hardcoded. that's bad. TO DO fix it later
																		 self.params.forecast_horizon)
		return self.benchmark_model_result

	# for future
	def search(self):
		
		error_measurements_results = []
		for error_measurement in self.error_measurement_functions:
			forecast_models_results = []
			for forecast_model in self.forecast_models:
				# it's expected that model doesn't have too much parameters and theirs' variations,
				# otherwise it will hurt everybody

				# for each parameters variant (for this it's needed to create 'parameter' entity
						# which will aggregate parameter default value, variation range, step, beer, etc.)
					# calculate forecast
					# calculate error 
					# add forecast result to array 
					# add error measurement to array
		# save all data in self.search_raw
		# from self.search_raw acquire best results for each model for each error measurement
