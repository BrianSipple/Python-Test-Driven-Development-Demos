from selenium import webdriver

browser = webdriver.Firefox()

# Helga has heard about a cool new online to-do app. She goes
# to check out its homepage
browser.get("http://localhost:8000")

# She notices the page title and header mention to-do lists
assert "To-Do" in browser.title

# She is invited to enter a to-do item straight away

# She types "Buy orange spools" into a text box (Helga's hobby
# is 3D-Printing)

# When she hits enter, the page updates, and now the page lists
# "1: Buy orange spools" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Buy orange spools to make a coffee mug (Helga is also a coffee connoisseur)
#
#
# The page updates again, and now shows both items on her list

