import pandas as pd
from framework.data.data_provider import data_provider
from framework.common.parameterizable import parameterizable

# data provider for single csv file
class csv_data_provider(data_provider, parameterizable):

	# data loaded on demand.
	# indicates, whether data loaded, or not
	data_loaded = False

	parameters = {}
	required_parameters = ['filepath', 
							'testing_set_size', 
							'missing_values_processing_policy']

	additional_parameters = ['index_column']


	def __init__(self, params):
		self.check_parameters(params, self.required_parameters)

		self.data_loaded = False
		self.parameters = params


	def get_training_set(self, columns = None):
		if not self.data_loaded:
			self.load_data()

		iterable = columns
		if iterable is None:
			iterable = self.training_set
		
		result = {}
		for col in iterable:
			result[col] = list(self.training_set[col])
		print(type(result))
		return result

	def get_testing_set(self, columns = None):
		if not self.data_loaded:
			self.load_data()
		
		iterable = columns
		if iterable is None:
			iterable = self.testing_set
		
		result = {}
		for col in iterable:
			result[col] = list(self.testing_set[col])
		
		return result

	def load_data(self):
		# load data using pandas
		data = pd.read_csv(self.parameters['filepath'], index_col = False, sep=';', header=0)

		# fix missing values (TO DO)
		#self.fix_missing_values(data, self.parameters['missing_values_processinng_policy'])

		# set index
		if 'index_column' in self.parameters.keys():
			data.set_index(self.parameters['index_column'])

		# divide into training and testing

		# if training_set_size between 0 and 1 then share specified
		# otherwise number of records
		if self.parameters['testing_set_size'] > 0 and self.parameters['testing_set_size'] < 1:
			cnt = data.shape[0]
			testing_set_size = int(cnt*self.parameters['testing_set_size'])
			training_set_size = cnt - testing_set_size
			self.training_set = data[:training_cnt]
			self.testing_set = data[training_cnt:]

			# calculate number, according to share and divide values into training and testing dataset
		elif self.parameters['testing_set_size'] >= 1: 
			tss = data.shape[0] - int(self.parameters['testing_set_size']) # user may specify float number or number with fraction. 
										 									# it's possible, but requires rounding
			self.training_set = data[:tss]
			self.testing_set = data[tss:]
			# divide dataset
		else: 
			# error, value out of allowed range
			raise ValueError('"training_set_size" has wrong value: ' + str(params.training_set_size))

		# switch flag of load completion into true to avoid redundand data loads
		self.data_loaded = True






