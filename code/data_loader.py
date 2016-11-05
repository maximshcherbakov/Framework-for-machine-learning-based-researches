# data loader
import pandas as pd
from code.base.with_required_params import with_required_params

class data_loader(with_required_params):

	def __init__ (self, params):
		rp = ['path_to_data', 'filename']
		self.required_params = rp

		# check for params
		for p in rp:
			params.contains(p)
			if not params.contains(p):
				raise Exception('parameter with name "' + p + '" required, but not specified')

		# save parameters
		self.params = params

		self.data = None

	def load_data(self):
		print(self.filepath())

		# maybe all those parametehrs should be passed as parameters of entity 'params'
		self.data = pd.read_csv(self.filepath(), index_col = False, sep=';', header=0)

		# set up indexing by index column
		if self.params.contains('index_column'):
			self.data.set_index(self.params.index_column)

		self.fix_missing_values('delete_rows')

	# TO DO determine which policies allowed and implement them 
	# in future this function should be able to setted outside class for each column of dataset
	def fix_missing_values(self, policy):
		if policy == 'delete_rows':
			pass
		elif policy == 'zeros':
			pass
		elif policy == 'average':
			pass
		elif policy == 'custom_value':
			pass

	def filepath(self):
		# it's not so good to work with files in style like this
		# maybe it won't work on Linux machines.
		# rewrite using 'pathlib' or make constraints for input parameters
		separator = ''
		if self.params.get('path_to_data')[-1] != '/':
			separator = '/'

		return self.params.get('path_to_data') + separator + self.params.get('filename')
				
	def get_data(self):
		if self.data is not  None:
			return self.data

		self.load_data()

		return self.data