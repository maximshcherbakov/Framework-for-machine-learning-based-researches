class model_parameter(object):
	
	def __init__(self, param_name, default_value, param_range, step):
		self.name = param_name
		self.default_value = default_value
		self.min_value = param_range[0]
		self.max_value = param_range[1]
		self.step = step
		self.variation_serie = None

	def variation(self):
		if self.variation_serie is None:
			self.variation_serie = xrange(self.min_value, self.max_value, self.step)
		return self.variation_serie