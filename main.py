from code.parameters import parameters
from code.data_loader import data_loader
from code.measurement.absolute.mean_square_error import mean_square_error
from code.measurement.absolute.mean_absolute_error import mean_absolute_error
from code.forecasting_models.naive_model import naive_model
from code.forecasting_models.random_model import random_model
from code.forecasting_models.simple_average_model import simple_average_model
from code.forecast_machine import forecast_machine
from code.utils.forecast_model_parameter import forecast_model_parameter

#define params
params = parameters()
params.path_to_data = 'D:/Framework/data/'
params.filename = 'data1.csv'
params.index_column = 'ExpectedDateTime'
params.daily_pattern = 96
params.frequency = params.daily_pattern
params.forecast_horizon = params.daily_pattern
params.planning_horizon_interval = 2
params.training_set_size = 0.95

#params.input_parameters = ['Electricity Meter reading (Wh)', 'Gas Consumption BEMT (m³)']
#params.output_parameters = 'Solar local consumption (Wh)'
params.columns_for_forecasting = ['Ele Act Technobo (Wh)'] # obligatory an array, not a single value

#print(params.get_all())
#print(params.contains('filename'))

# load data
dl = data_loader(params)
data = dl.get_data()

# separate module for visualization.
# TO DO: create that module

# prepare error measurements
em = [ mean_absolute_error(), mean_square_error() ]
#for m in em:
#	print(m.get_name())

# benchmark model
bench_model = (random_model(), None)

# all forecast models models
forecast_models = [(random_model(), None), 
					(naive_model(), None), 
					(simple_average_model(), {'repetition_interval' : 7, 'lag' : 4, 'frequency' : 96})]

# create forecast machine
machine = forecast_machine(params, dl, bench_model, forecast_models, em)

#print(type(machine.training_set))
#f = simple_average_model().forecast({'repetition_interval' : 7, 'lag' : 4, 'frequency' : 96}, machine.training_set['Ele Act Technobo (Wh)'].tolist(), 96)
#print(f)
res = machine.benchmark()
print(res)