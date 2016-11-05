# base class for all data providers
class data_provider(object):

	# parameters, e.g. data location, missing values policy, etc.
	parameters = {}

	required_parameters = []

	additional_parameters = []

	# returns training dataset
	def get_training_set(self, columns = None):
		pass

	# returns testing dataset
	def get_testing_set(self, columns = None):
		pass

