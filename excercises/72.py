import webbrowser

search_term = input("Please input what you want to search: ")

# response = requests.get("https://www.google.com/search?hl=pl&source=hp&ei=RPy-W4z6PIyrsgHM1YTwBw&q=%s&oq=%s&gs_l=psy-ab.3..35i39k1j0i131k1j0l8.5127.5921.0.6099.10.8.0.0.0.0.232.331.1j0j1.3.0....0...1c.1.64.psy-ab..7.3.409.6..0i67k1.78.HOZGnhSbbro" % (search_term, search_term))
# print(response.text)
url = "https://www.google.com/search?hl=pl&source=hp&ei=RPy-W4z6PIyrsgHM1YTwBw&q=%s&oq=%s&gs_l=psy-ab.3..35i39k1j0i131k1j0l8.5127.5921.0.6099.10.8.0.0.0.0.232.331.1j0j1.3.0....0...1c.1.64.psy-ab..7.3.409.6..0i67k1.78.HOZGnhSbbro" % (search_term, search_term)
webbrowser.open_new(url)