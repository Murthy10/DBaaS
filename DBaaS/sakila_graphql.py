query1a = """
{
  allActors(orderBy: LAST_NAME_ASC) {
    nodes {
      firstName
      lastName
    }
  }
}
"""

query1b = """
{
  allActors(orderBy: FIRST_NAME_ASC) {
    nodes {
      firstName
      lastName
    }
  }
}
"""

query2a = """
{
  allActors(condition: {firstName: "Joe"}) {
    nodes {
      firstName
      lastName
      actorId
    }
  }
}
"""

query2b = """
{
  allActors(filter: {lastName: {includesInsensitive: "gen"}}) {
    nodes {
      firstName
      lastName
      actorId
    }
  }
}
"""

query2c = """
{
  allActors(filter: {lastName: {includesInsensitive: "LI"}}, orderBy: [LAST_NAME_ASC, FIRST_NAME_ASC]) {
    nodes {
      firstName
      lastName
      actorId
    }
  }
}   
"""

query2d = """
{
  allCountries(filter: {or: [
    {country: {equalTo: "Afghanistan"}},
    {country: {equalTo: "Bangladesh"}},
        {country: {equalTo: "China"}},
  ]}) {
    nodes {
      countryId
      country
    }
  }
}
"""

query4a = """
{
  allQuery4As {
    nodes {
      lastName
      lastNameCount
    }
  }
}
"""

query4b = """
{
  allQuery4Bs {
    nodes {
      lastName
      lastNameCount
    }
  }
}
"""

query6a = """
{
  allStaff {
    nodes {
      addressByAddressId {
        address
      }
      firstName
      lastName
    }
  }
}
"""

query6b = """
{
  allQuery6Bs {
    nodes {
      firstName
      lastName
      totalAmount
    }
  }
}
"""

query6c = """
{
  allQuery6Cs {
    nodes {
      title
      actorCount
    }
  }
}
"""

query6e = """
{
  allQuery6Es {
    nodes {
      firstName
      lastName
      totalPaidByEachCustomer
    }
  }
}
"""

query7a = """
{
  allQuery7As {
    nodes {
      title
    }
  }
}
"""

query7b = """
{
  allQuery7Bs {
    nodes {
      firstName
      lastName
    }
  }
}
"""

query7ca = """
{
  allCountries(filter: {country: {equalTo: "Canada"}}) {
    nodes {
      citiesByCountryId {
        nodes {
          addressesByCityId {
            nodes {
              customersByAddressId {
                nodes {
                  firstName
                  lastName
                }
              }
            }
          }
        }
      }
    }
  }
}
"""

query7cb = """
{
  allQuery7Cs {
    nodes {
      firstName
      lastName
    }
  }
}
"""

query7e = """
{
  allQuery7Es {
    nodes {
      title
      rentalCount
    }
  }
}
"""

query7f = """
{
  allQuery7Fs {
    nodes {
      storeId
      sum
    }
  }
}
"""

query7g = """
{
  allStores {
    nodes {
      addressByAddressId {
        cityByCityId {
          countryByCountryId {
            country
          }
          city
        }
      }
      storeId
    }
  }
}
"""

query7h = """
{
  allQuery7Hs {
    nodes {
      name
      sum
    }
  }
}
"""
