# basic class for entities with parameters
class parameterizable(object):

	def check_parameters(self, parameters, required_parameters):
		for param in required_parameters:
			if param not in parameters.keys():
				raise TypeError('Required parameter "' + param + '" did not provided')