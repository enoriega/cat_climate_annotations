



from oggm_edu import GlacierBed, MassBalance, Glacier, GlacierCollection


bed = GlacierBed(top=3400, bottom=1500, width=300)
mass_balance = MassBalance(ela=3000, gradient=4)
glacier = Glacier(bed=bed, mass_balance=mass_balance)



glacier.creep


collection = GlacierCollection()

collection.fill(glacier, n=3)
collection


collection.change_attributes({"creep": ["* 10", "", "/ 10"]})


collection.progress_to_year(800)


collection.plot()

collection.plot_history()



glacier.basal_sliding

collection = GlacierCollection()
collection.fill(glacier, n=2)


collection.change_attributes({'basal_sliding':[0, 5.7e-20]})

collection.progress_to_year(800)


collection.plot()

collection.plot_history()






