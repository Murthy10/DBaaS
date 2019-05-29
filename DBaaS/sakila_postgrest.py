query1a = "actor?select=first_name,last_name&order=last_name.asc"

query1b = "actor?select=first_name,last_name&order=first_name.asc,last_name.asc"

query2a = "actor?select=actor_id,first_name,last_name&first_name=eq.Joe"

query2b = "actor?select=actor_id,first_name,last_name&last_name=ilike.*gen*"

query2c = "actor?select=actor_id,first_name,last_name&last_name=ilike.*LI*&order=last_name.asc,first_name.asc"

query2d = "country?select=country_id,country&country=in.(Afghanistan,Bangladesh,China)"

query4a = "query4a"

query4b = "query4b"

query6a = "staff?select=first_name,last_name,address(address)&order=last_name.asc"

query6b = "query6b"

query6c = "query6c"

query6d = "query6d"

query6e = "query6e"

query7a = "query7a"

query7b = "query7b"

# query7c = "customer?select=first_name,last_name,email,address(address,city(city,country(country)))&address.city.country.country=eq.Canada"
query7c = "country?select=country,city(address(customer(last_name,email)))&country=eq.Canada"

query7d = "query7d"

query7e = "query7e"

query7f = "query7f"

query7g = "store?select=store_id,address(address,city(city,country(country)))"

query7h = "query7h"
