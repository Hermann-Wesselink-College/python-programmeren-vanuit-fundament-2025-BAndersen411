# Opdracht 1 tot en met 7 van pragraaf 2.10
from datetime import datetime
datum = datetime.now()
print(str(datum))
from datetime import datetime
datumtijd = datetime.now()
jaar = datumtijd.year
print(str(jaar))

from datetime import datetime
datum = datetime.now()
month = datum.month
print(str(month))
from datetime import datetime
datum = datetime.now()
day = datum.day
print(str(day))

from datetime import datetime
datum = datetime.now()
dag = datum.day
maand = datum.month
jaar = datum.year
print(str(dag) + "-" + str(maand) + "-" + str(jaar))

from datetime import datetime
datum = datetime.now()
print(f"{datum.day}-{datum.month}-{datum.year}")

from datetime import datetime
datumtijd = datetime.now()
minute = datumtijd.minute
hour = datumtijd.hour
print(f'{datum.hour}:{datum.minute}')



from datetime import datetime
datum = datetime.now()
from datetime import datetime
datumtijd = datetime.now()
minute = datumtijd.minute
hour = datumtijd.hour
print(f'De datum is {datum.day}-{datum.month}-{datum.year} Het is nu {datum.hour}:{datum.minute}')




#Waarom moet de datum eronder op de Amerikaanse manier zijn# 

from datetime import datetime
d0 = datetime(2025, 10, 1)
d1 = datetime(2009, 4, 6)
verschil = d0 - d1
print(verschil.days)

from datetime import datetime
d0 = datetime.now()
d1 = datetime(2009, 4, 6)
verschil = d0 - d1
print(verschil.days)

from datetime import datetime
d0 = datetime.now()
d1 = datetime(2009, 4, 6)
datumVerschil = d0 - d1
dagenVerschil = datumVerschil.days / 365.25
print(dagenVerschil)