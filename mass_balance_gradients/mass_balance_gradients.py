



from oggm_edu import MassBalance, GlacierBed, Glacier, GlacierCollection


bed = GlacierBed(top=3400, bottom=1500, width=400)
mass_balance = MassBalance(ela=3000, gradient=4)
glacier = Glacier(bed=bed, mass_balance=mass_balance)


collection = GlacierCollection()
collection.fill(glacier, n=3, attributes_to_change=
                {'gradient':[0.3, 4, 15]}
               )


complex_mb = MassBalance(ela=3000, gradient=[3, 7, 10, 15],
                         breakpoints=[2700, 2250, 1800])
glacier_complex_mb = Glacier(bed=bed, mass_balance=complex_mb)

collection.add(glacier_complex_mb)

collection.progress_to_year(300)

collection.plot()

collection.plot_mass_balance()




collection = GlacierCollection()
collection.fill(glacier, n=3, attributes_to_change=
                {'gradient':[0.3, 4, 15]}
               )

collection.progress_to_equilibrium()

collection.plot()


collection



glacier


glacier.progress_to_equilibrium()

glacier.plot()


glacier.eq_states


glacier.add_temperature_bias(bias=1., duration=1)


glacier.progress_to_equilibrium()

glacier.plot()

glacier.eq_states


glacier.response_time


glacier


bed = GlacierBed(top=3400, bottom=1500, width=400)
mass_balance = MassBalance(ela=3000, gradient=4)
glacier = Glacier(bed=bed, mass_balance=mass_balance)

collection = GlacierCollection()
collection.fill(glacier, n=3, attributes_to_change=
                {'gradient':[1, 4, 15]}
               )

collection.progress_to_equilibrium()

collection


collection.glaciers[0].add_temperature_bias(bias=1., duration=1)
collection.glaciers[1].add_temperature_bias(bias=1., duration=1)
collection.glaciers[2].add_temperature_bias(bias=1., duration=1)

collection.progress_to_equilibrium()

collection

collection.plot_history()


collection.glaciers[0].plot_state_history(eq_states=True)







