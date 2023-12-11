

from oggm_edu import MassBalance, GlacierBed, Glacier, GlacierCollection





bed = GlacierBed(top=3400, bottom=1500, width=300)

bed


bed.plot()



bed_with_slope = GlacierBed(top=3400, bottom=1500, width=300, slopes=25)
bed_with_slope.plot()


bed_with_multiple_slopes = GlacierBed(top=3400, bottom=1500, width=300,
                                      slopes=[25, 10],
                                      # Slope sections are defined by altitude
                                      # pairs. Here we have two parirs.
                                      slope_sections=[3400, 2200, 1500])
bed_with_multiple_slopes.plot()


mass_balance = MassBalance(ela=3000, gradient=4)

mass_balance


glacier = Glacier(bed=bed, mass_balance=mass_balance)


glacier



glacier.progress_to_year(1)


glacier.plot()


glacier


glacier.progress_to_year(150)

glacier.plot()


glacier


glacier.progress_to_year(150)


glacier.progress_to_year(500)

glacier.plot()

glacier


glacier.progress_to_year(450)


mass_balance_2 = MassBalance(ela=2500, gradient=4)
glacier_multiple_slopes = Glacier(bed=bed_with_multiple_slopes,
                                  mass_balance=mass_balance_2)
glacier_multiple_slopes.progress_to_year(400)

glacier_multiple_slopes.plot()


glacier.history


glacier.plot_history()





wide_narrow_bed = GlacierBed(altitudes=[3400, 2800, 1500],
                             widths=[600, 300, 300])

wide_narrow_bed


wide_narrow_bed.plot()


wide_narrow_glacier = Glacier(bed=wide_narrow_bed,
                              mass_balance=mass_balance)

wide_narrow_glacier


collection = GlacierCollection()
collection.add([glacier, wide_narrow_glacier])


collection


collection.progress_to_year(600)


collection.plot()


collection.plot_history()




