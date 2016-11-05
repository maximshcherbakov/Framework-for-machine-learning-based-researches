from framework.data.csv_data_provider import csv_data_provider as dp

from framework.forecasting.naive_model import naive_model
from framework.forecasting.random_model import random_model
from framework.forecasting.simple_average_model import simple_average_model

from framework.measurement.absolute.mean_absolute_error import mean_absolute_error as mae
from framework.measurement.absolute.root_mean_square_error import root_mean_square_error as rmse
from framework.measurement.absolute.mean_square_error import mean_square_error as mse
from framework.measurement.absolute.median_absolute_error import median_absolute_error as mdae

from framework.forecasting.forecast_handler import forecast_handler

# create data provider
data_provider_parameters = {
	'filepath': 'data/data1.csv',
	'testing_set_size': 96,
	'missing_values_processing_policy' : None
}
data_provider = dp(data_provider_parameters)
print(type(data_provider.get_testing_set()))

# debug output
print(data_provider.get_testing_set().keys())
print(len(data_provider.get_testing_set()['Ele Act Technobo (Wh)']))
print(len(data_provider.get_training_set()['Ele Act Technobo (Wh)']))

# estimate models
naive = {'model': naive_model(), 'parameters': None}
forecast_handler_params = {
	'forecasting_columns' : ['Ele Act Technobo (Wh)'],
	'testing_set_size' : 96
}

err_m = [
	mae(),
	rmse(),
	mse(),
	mdae()
]

fh = forecast_handler(data_provider, forecast_handler_params, naive, None, err_m)
bench_result = fh.get_benchmark_result()
print(type(bench_result))
print(len(bench_result))

# get error measurements for benchmark model
bench_measurements = fh.get_error_measurements(bench_result)
print(bench_measurements)


# perform grid search
fh.grid_search()

# grid search

print('success')