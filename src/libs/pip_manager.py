# importing pip related modules
from pypi_simple import PyPISimple
from pypi_simple.errors import NoSuchProjectError

# importing requests to get description
import requests

# creating the client
client = PyPISimple()

def get_package_information(package_name):
    try:
        # getting package
        package_page = client.get_project_page(package_name)
        # Build a list of tuples for ALL versions found
        results = [
            (package_page.project, info.version) 
            for info in package_page.packages
        ]
        return results
    except NoSuchProjectError:
        return "The package, " + package_name + "could not be found!"
