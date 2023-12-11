


from oggm_edu import MassBalance, GlacierBed, Glacier, GlacierCollection




top_elev = 3400 # m, the peak elevation
bottom_elev = 1500 # m, the elevation at the bottom of the glacier



bed_width = 300  # m, the constant width of the rectangular valley
bed_slope = 10  # degrees, the slope of the bed
bed = GlacierBed(top=top_elev, bottom=bottom_elev, width=bed_width, slopes=bed_slope)


bed.plot()



bed




ELA = 3000 # equilibrium line altitude in meters above sea level
altgrad = 4 # altitude gradient in mm/m
mb_model = MassBalance(ELA, gradient=altgrad)

mb_model



glacier = Glacier(bed=bed, mass_balance=mb_model)


glacier


glacier.plot_mass_balance()





runtime = 1
glacier.progress_to_year(runtime)


glacier.plot()


glacier



runtime = 150
glacier.progress_to_year(150)


glacier.plot()


glacier



runtime = 150
glacier.progress_to_year(runtime)

glacier.plot()

glacier



glacier.progress_to_year(450)
glacier



glacier.history


glacier.plot_history()







new_slope = 20

new_bed = GlacierBed(top=top_elev, bottom=bottom_elev, width=bed_width, slopes=new_slope)

new_glacier = Glacier(bed=new_bed, mass_balance=mb_model)



collection = GlacierCollection()
collection.add([glacier, new_glacier])


collection


collection.progress_to_year(600)


collection.plot_side_by_side(figsize=(10, 5))


collection.plot_history()

collection




