# global parameters
# all entities that use global parameters, contain reference to entity of type 'parameters'
# so this entity should have single instance and this instance should be treated carefully
# to avoid big problems
#
# TO DO: maybe it's not a good way to store parameters in such way and each
# class which uses params should have a copy of them?
class parameters:
	
	def get(self, param_name):
		return self.__dict__[param_name]

	def get_all(self):
		return self.__dict__

	def contains(self, param_name):
		return param_name in self.__dict__