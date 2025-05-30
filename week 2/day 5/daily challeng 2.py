# -*- coding: utf-8 -*-
"""daily challenge

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zeM_lKwd1xxYBDLqzZqvYqQwpdrZjKS-

Instructions :
Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
Test your code with multiple sites such as google, ynet, imdb, etc.
"""

import requests
import time

def webpage_load_time(url):
  """
  Measures the time it takes for a webpage to load.

  Args:
    url: The URL of the webpage to test.

  Returns:
    The load time in seconds, or None if an error occurs.
  """
  try:
    start_time = time.time()
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    end_time = time.time()
    return end_time - start_time
  except requests.exceptions.RequestException as e:
    print(f"Error fetching URL {url}: {e}")
    return None

# Test with multiple websites
websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for website in websites:
  load_time = webpage_load_time(website)
  if load_time is not None:
    print(f"Load time for {website}: {load_time:.4f} seconds")