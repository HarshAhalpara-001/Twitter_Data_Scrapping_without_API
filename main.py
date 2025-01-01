from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import csv
# import requests
import time
def click_sign_in_edge(url):
    """Clicks the "Sign in" button on a webpage using Microsoft Edge."""
    try:
        options = Options()
        options.add_experimental_option("detach", True)  # Keep browser open

        # Provide the correct path to your msedgedriver.exe
        driver = webdriver.Edge(options=options)

        driver.get(url)
        # Fallback to XPath if data-testid is not found
        driver.maximize_window()
        sign_in_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/login')]"))
        )
        sign_in_link.click()
        print("click on Login page")
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text")))
        time.sleep(1)
        email_field.send_keys("hersh22@cumfoto.com")             # EMAIL
        time.sleep(0)
        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(),'Next')]]"))
        )
        button.click()
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text")))
        time.sleep(1)
        username_field.send_keys("@NothingHersh22")            # username 
        next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='ocfEnterTextNextButton']"))
            )
        next_button.click()
        print("Next button clicked using data-testid.")
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password")))
        time.sleep(1)
        username_field.send_keys("H@rsh_sorry")             # password
        # data-testid="LoginForm_Login_Button"
        next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='LoginForm_Login_Button']"))
        )
        next_button.click()
        print(f"Button with text Next clicked successfully.")
        time.sleep(5)
        unit_data="2020-12-31"
        since_data="2020-12-1"
        target_url = f"https://x.com/search?f=live&q=%22BMW%22%20(%22Problem%22%20OR%20%2C%20OR%20%22damaged%22)%20until%3A{unit_data}%20since%3A{since_data}&src=typed_query"
        driver.get(target_url)
        time.sleep(5)
        
        def scroll_to_bottom(driver):
            scroll_pause_time = 3  # Adjust based on how fast the content loads
            last_height = driver.execute_script("return document.body.scrollHeight")
            article_data = []
            articles = driver.find_elements(By.TAG_NAME, "article")        
            for i, article in enumerate(articles, start=1):
                # article_html = article.get_attribute("outerHTML")
                article_html = article.text
                single_line_data = "||".join(article_html.splitlines())
                article_data.append(single_line_data)
                
            while True:
                # Scroll to the bottom
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_pause_time)  # Wait for new content to load
                articles = driver.find_elements(By.TAG_NAME, "article")

                # Fetch the full HTML for each article and store it as an object
                for i, article in enumerate(articles, start=1):
                    # article_html = article.get_attribute("outerHTML")
                    article_html = article.text
                    single_line_data = "||".join(article_html.splitlines())
                    article_data.append(single_line_data)

                # Calculate new scroll height and compare with the last height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:  # Stop if no new content is loaded
                    break
                last_height = new_height
            print("data take completed from web_page")
            # Save the article data to a file as JSON


            with open("fetched_data_of_BMW_from_tweeter.txt", "a", encoding="utf-8") as file:
                for article in article_data:
                    x = str(article)
                    file.write(f"{x} \n")  # Append with a newline
            print("data saved in file")
        
        # Scroll to the bottom to load all content
        scroll_to_bottom(driver)

        print("Articles saved to 'articles.txt'.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        #driver.quit()  # Uncomment to close the browser automatically
        pass

# Example usage:
click_sign_in_edge("https://x.com/home?lang=en")