from countryinfo import CountryInfo
count=input("Enter your Country : ")
country = CountryInfo(count)
print("Capital is : ", country.capital())
print("Currency is : ", country.currencies())
print("Languages are : ", country.languages())
print("Borders are : ", country.borders())
print("Other names : ", country.alt_spellings())
print('Have a nice day :)')
