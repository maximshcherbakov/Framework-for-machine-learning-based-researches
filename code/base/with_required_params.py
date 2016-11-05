# base class for all classes, required parameters
class with_required_params:

	required_params = []

	def add_required_param(self, param_name):
		required_params.append(param_name)

	def delete_required_param(self, param_name):
		required_params.remove(param_name)