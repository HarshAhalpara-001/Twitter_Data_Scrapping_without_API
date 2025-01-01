from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
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
        email_field.send_keys("byx9umfz@4xoay.com")
        time.sleep(0)
        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(),'Next')]]"))
        )
        button.click()
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text")))
        
        username_field.send_keys("@GetDue49015")
        next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='ocfEnterTextNextButton']"))
            )
        next_button.click()
        print("Next button clicked using data-testid.")
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password")))
        username_field.send_keys("H@rsh_Sorry")
        # data-testid="LoginForm_Login_Button"
        next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='LoginForm_Login_Button']"))
        )
        next_button.click()
        print(f"Button with text Next clicked successfully.")
        time.sleep(5)
        target_url = "https://x.com/search?f=live&q=%22BMW%22%20(%22Problem%22%20OR%20%2C%20OR%20%22damaged%22)%20until%3A2020-12-31%20since%3A2020-12-01&src=typed_query"
        driver.get(target_url)
        time.sleep(5)
        
        def scroll_to_bottom(driver):
            scroll_pause_time = 2  # Adjust based on how fast the content loads
            last_height = driver.execute_script("return document.body.scrollHeight")
            
            while True:
                # Scroll to the bottom
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_pause_time)  # Wait for new content to load
                
                # Calculate new scroll height and compare with the last height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:  # Stop if no new content is loaded
                    break
                last_height = new_height

        # Scroll to the bottom to load all content
        scroll_to_bottom(driver)

        articles = driver.find_elements(By.TAG_NAME, "article")
        
        article_data = []

        # Fetch the full HTML for each article and store it as an object
        for i, article in enumerate(articles, start=1):
            # article_html = article.get_attribute("outerHTML")
            article_html = article.text
            article_data.append({
                "id": i,
                "html": article_html
            })

        # Save the article data to a file as JSON
        with open("articles.txt", "w", encoding="utf-8") as file:
            json.dump(article_data, file, indent=4)

        print("Articles saved to 'articles.txt'.")

        try:
            with open("articles.txt", "w", encoding="utf-8") as file:
                # Convert the list to a JSON string
                file.write(json.dumps(article_data, indent=4))
            print("Articles saved to 'articles.txt'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        #driver.quit()  # Uncomment to close the browser automatically
        pass

# Example usage:
click_sign_in_edge("https://x.com/home?lang=en")