import matplotlib.pyplot as plt

import seaborn as sns
sns.set_context('notebook')
sns.set_style('ticks')

import numpy as np
import oggm
from oggm import utils, cfg, workflow, graphics

cfg.initialize()


cfg.PATHS['working_dir'] = utils.gettempdir('ti_model')

cfg.PARAMS['border'] = 10


print('T_solid = {}°C'.format(cfg.PARAMS['temp_all_solid']))
print('T_melt = {}°C'.format(cfg.PARAMS['temp_melt']))

gdir = workflow.init_glacier_directories([utils.demo_glacier_id('hef')], from_prepro_level=3)[0]

from oggm.core import massbalance

mb_cal = massbalance.PastMassBalance(gdir)


print('the glacier selected is {},'.format(gdir.name))


print('mu_star = {:2f} mm K^-1 yr^-1.'.format(mb_cal.mu_star))


print('epsilon = {:2f} mm.'.format(mb_cal.bias))



fpath = gdir.get_filepath('climate_historical')

print(fpath)


import xarray as xr

climate = xr.open_dataset(fpath)
climate


annual_cycle = climate.groupby('time.month').mean(dim='time')


import calendar

fig, ax = plt.subplots(1, 2, figsize=(16, 9))
ax[0].plot(annual_cycle.month, annual_cycle.temp); ax[1].plot(annual_cycle.month, annual_cycle.prcp);
ax[0].set_title('Average temperature / (°C)'); ax[1].set_title('Total precipitation / (mm)');
for a in ax:
    a.set_xticks(annual_cycle.month.values)
    a.set_xticklabels([calendar.month_abbr[m] for m in annual_cycle.month.values])




ref_mb = gdir.get_ref_mb_data()

ref_mb[['ANNUAL_BALANCE']].plot(title='Annual mass balance: {}'.format(gdir.name), legend=False);



fls = gdir.read_pickle('inversion_flowlines')


print(ref_mb.index.values)


ref_mb['OGGM (calib)'] = mb_cal.get_specific_mb(fls=fls, year=ref_mb.index.values)


print('rho_ice = {} kg m^-3.'.format(cfg.PARAMS['ice_density']))


fig, ax = plt.subplots(1, 1)
ax.plot(ref_mb['ANNUAL_BALANCE'], label='Observed')
ax.plot(ref_mb['OGGM (calib)'], label='Modelled')
ax.set_ylabel('Specific mass balance / (mm w.e. y$^{-1}$)')
ax.legend(frameon=False);


fig, ax = plt.subplots(1, 1)
ax.plot(ref_mb['ANNUAL_BALANCE'], ref_mb['OGGM (calib)'], 'ok');
ax.plot(ref_mb['ANNUAL_BALANCE'], ref_mb['ANNUAL_BALANCE'], '-r');
ax.set_xlim(-3000, 2000)
ax.set_ylim(-3000, 2000)
ax.set_xlabel('Observed');
ax.set_ylabel('OGGM (calib)');



bias = ref_mb['OGGM (calib)'] - ref_mb['ANNUAL_BALANCE']

fig, ax = plt.subplots(1, 1)
ax.plot(bias);
