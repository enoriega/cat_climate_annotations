




from oggm_edu import SurgingGlacier, Glacier, GlacierBed, MassBalance, GlacierCollection



bed = GlacierBed(altitudes=[3400, 3000, 2500, 1500],
                 widths=[500, 400, 300, 300])
mass_balance = MassBalance(ela=2900, gradient=4)

bed.plot()


surging_glacier = SurgingGlacier(bed=bed, mass_balance=mass_balance)


surging_glacier.normal_years

surging_glacier.surging_years

surging_glacier

surging_glacier.basal_sliding

surging_glacier.basal_sliding_surge


surging_glacier.progress_to_year(400)

surging_glacier.plot_history()


surging_glacier.plot()



glacier = Glacier(bed=bed, mass_balance=mass_balance)

collection = GlacierCollection()
collection.add([surging_glacier, glacier])

collection.progress_to_year(400)

collection.plot_history()

collection.plot()

collection



surging_glacier_strong = SurgingGlacier(bed=bed, mass_balance=mass_balance)

surging_glacier_strong.basal_sliding_surge = 5.7e-20 * 50

collection.add(surging_glacier_strong)

collection.progress_to_year(400)

collection

collection.plot_history()






