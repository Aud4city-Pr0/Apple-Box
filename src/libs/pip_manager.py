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
        for info in package_page.packages:
            return (package_page.project, info.version)
    except NoSuchProjectError:
        return "The package, " + package_page + "could not be found!"
