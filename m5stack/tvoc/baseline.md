Baseline Set & Get

All VOC/gas sensors use the same underlying technology: a tin oxide element that, when exposed to organic compounds, changes resistance. The 'problem' with these sensors is that the baseline changes, often with humidity, temperature, and other non-gas-related-events. To keep the values coming out reasonable, you'll need to calibrate the sensor.


If no stored baseline is available after initializing the baseline algorithm, the sensor has to run for 12 hours until the baseline can be stored. This will ensure an optimal behavior for preceding startups. Reading out the baseline prior should be avoided unless a valid baseline is restored first. Once the baseline is properly initialized or restored, the current baseline value should be stored approximately once per hour. While the sensor is off, baseline values are valid for a maximum of seven days.
Restarting the sensor without reading back a previously stored baseline will result in the sensor trying to determine a new baseline. The adjustement algorithm will be accelerated for 12hrs which is the Maximum time required to find a new baseline.
The sensor adjusts to the best value it has been exposed to. So keeping it indoors the sensor thinks this is the best value and sets it to ~0ppb tVOC and 400ppm CO2eq. As soon as you expose the sensor to outside air it can adjust to the global H2 Background Signal. For normal Operation exposing the sensor to outside air for 10min cumulative time should be sufficient.
If you're experienced with sensors that don't have a baseline, you either won't be able to measure absolute values or you'll have to implement your own baseline algorithm.
The sensor to sensor variation of SGP30 in terms of sensitivity is very good as each of them is calibrated. But the baseline has to be determined for each sensor individually during the first Operation.
To make that easy, SGP lets you query the 'baseline calibration readings' from the sensor with code like this:

co2eq_base, tvoc_base = sgp30.baseline_co2eq, sgp30.baseline_tvoc

This will grab the two 16-bit sensor calibration words and place them in the variables so-named.
You should store the

googleSearch: get_iaq_baseline()  python
