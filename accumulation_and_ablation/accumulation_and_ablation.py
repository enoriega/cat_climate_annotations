from oggm_edu import Glacier, MassBalance, GlacierBed

top = 3400
bottom = 0
wide_narrow_bed = GlacierBed(altitudes=[top, (top-bottom) * 2/3, bottom],
                             widths=[1500, 500, 500])

wide_narrow_bed.plot()
mass_balance = MassBalance(ela=(top-bottom)*2/3, gradient=3)
glacier = Glacier(bed=wide_narrow_bed, mass_balance=mass_balance)
glacier.plot()

glacier.progress_to_equilibrium()
glacier.plot()

glacier.specific_mass_balance

from matplotlib import pyplot as plt
import numpy as np

mb = glacier.mass_balance.get_annual_mb(glacier.current_state.surface_h)
mb = mb * glacier.bed.widths * glacier.bed.map_dx *\
        glacier.current_state.dx_meter
q = (mb).cumsum()

fig, ax = plt.subplots()
ax.plot(glacier.bed.distance_along_glacier[q>0], q[q>0])
idx = np.argmin(np.abs(mb))
ax.axvline(glacier.bed.distance_along_glacier[idx], c='k')
ax.text(glacier.bed.distance_along_glacier[idx]-0.1, 0, 'ELA',
            ha='right')
ax.set_xlabel('Distance along glacier [km]')
ax.set_ylabel('Ice flux $q$ (m$^3$ s$^{-1}$)')