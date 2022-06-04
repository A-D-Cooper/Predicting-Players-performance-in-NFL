import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:/SeleniumDrivers/chromedriver.exe")



def cat_sec_1():

    #URL for this, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=pass_cmp&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=pass_att&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=pass_inc&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=pass_cmp_perc&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=pass_yds&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=pass_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99


    driver.get("https://stathead.com/football/pgl_finder.cgi")
    driver.implicitly_wait(30)

    # 1. Select Passes completed and fill value of 0
    drop_menu = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/select')
    select = Select(drop_menu)
    select.select_by_value('pass_cmp')
    pas_input = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/div[2]/input[1]')
    pas_input.send_keys('0')

    # 2. Select Passes Attempts from the list and put 0
    drop_menu = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/select')
    select = Select(drop_menu)
    select.select_by_value('pass_att')
    pas_input = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/div[3]/input[1]')
    pas_input.send_keys('0')

    # 3. Select Passes incomplete from the list and put 0
    drop_menu = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/select')
    select = Select(drop_menu)
    select.select_by_value('pass_inc')
    pas_input = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/div[4]/input[1]')
    pas_input.send_keys('0')

    # 4. Select Pass complete perc from the list and put 0
    drop_menu = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/select')
    select = Select(drop_menu)
    select.select_by_value('pass_cmp_perc')
    pas_input = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/div[5]/input[1]')
    pas_input.send_keys('0')

    # 5. Select Passes incomplete from the list and put 0
    drop_menu = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/select')
    select = Select(drop_menu)
    select.select_by_value('pass_yds')
    pas_input = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/div[6]/input[1]')
    pas_input.send_keys('0')

    # 6. Select Passing TD and put 0
    drop_menu = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/select')
    select = Select(drop_menu)
    select.select_by_value('pass_td')
    pas_input = driver.find_element_by_xpath('//*[@id="content_grid"]/div[1]/div[3]/div[1]/div[7]/input[1]')
    pas_input.send_keys('0')

    submit_btn = driver.find_element_by_xpath('//*[@id="stathead_results"]/div[2]/p[2]/input')
    submit_btn.click()