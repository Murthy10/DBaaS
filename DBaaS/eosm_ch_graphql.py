query1 = """
{
  allDidokOsms {
    totalCount
    nodes {
      didokName
    }
  }
}
"""


query2 = """
{
  allQuery2S {
    nodes {
      uicRef
      didname
      osmname
      easting
      northing
      geomWkt
      dist 
    }
  }
}
"""

query3 = """
{
  allQuery3S {
    nodes {
      uicRef
      name
      easting
      northing
    }
  }
}
"""

query4 = """
{
  allQuery4S {
    nodes {
      name
      geom
    }
  }
}
"""

query5 = """
{
  allQuery5S {
    nodes {
      name
      geom
    }
  }
}
"""

query6 = """
{
  allQuery6S {
    nodes {
      didokName
      osmName
      geom
    }
  }
}
"""


query7 = """
{
  allQuery7S {
    nodes {
      didokName
      osmName
      geom
    }
  }
}
"""


query8a = """
{
  allQuery8As {
    nodes {
      uicRef
      name
    }
  }
}
"""

query8b = """
{
  allQuery8Bs {
    nodes {
      uicRef
      name
      easting
      easting
    }
  }
}
"""

query9 = """
{
  allQuery9S {
    nodes {
      didokName
      osmName
      geom
    }
  }
}
"""

query10 = """
{
  allQuery10S {
    nodes {
      cnt
    }
  }
}
"""

query11 = """
{
  allQuery11S {
    nodes {
      sum
    }
  }
}
"""

query12 = """
{
  allQuery12S {
    nodes {
      osmId
      name
      geom
    }
  }
}
"""

query13 = """
{
  allQuery13S {
    nodes {
      osmId
      name
      geom
    }
  }
}
"""


query14 = """
{
  allQuery14S {
    nodes {
      osmId
      name
      dist
    }
  }
}
"""
