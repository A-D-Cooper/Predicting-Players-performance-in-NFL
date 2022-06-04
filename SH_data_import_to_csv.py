import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time



driver = webdriver.Chrome("C:/SeleniumDrivers/chromedriver.exe")


def login():
    username = "AD1999"
    password = "Iamdbcooper1971"
    driver.get("https://stathead.com/users/login.cgi")
    driver.implicitly_wait(30)

    usernm_txt = driver.find_element_by_id("username")
    pas_txt = driver.find_element_by_id("password")

    usernm_txt.send_keys(username)
    pas_txt.send_keys(password)

    sub_btn = driver.find_element_by_id("sh-login-button")
    sub_btn.click()


def convert_to_csv():
    #driver.get("https://stathead.com/football/pgl_finder.cgi")
    #driver.implicitly_wait(30)

    driver.implicitly_wait(30)
    try:
        menu = driver.find_element_by_xpath('//*[@id="results_sh"]/div/ul/li[1]/span')

    except NoSuchElementException:
        time.sleep(10)
        driver.refresh()
        try:
            menu = driver.find_element_by_xpath('//*[@id="results_sh"]/div/ul/li[1]/span')

        except NoSuchElementException:
            time.sleep(10)
            driver.refresh()
            menu = driver.find_element_by_xpath('//*[@id="results_sh"]/div/ul/li[1]/span')

    action = ActionChains(driver)
    action.move_to_element(menu)
    csv_btn = driver.find_element_by_xpath("//button[text()='Get table as CSV (for Excel)']")
    action.move_to_element(csv_btn)
    action.click().perform()


def url_ls():

    # 1. URL for passing 1-6, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=pass_cmp&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=pass_att&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=pass_inc&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=pass_cmp_perc&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=pass_yds&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=pass_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 2. URL for passing 7-12, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=pass_int&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=pass_rating&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=pass_sacked&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=pass_sacked_yds&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=pass_yds_per_att&ccomp%5B6%5D=gt&cstat%5B6%5D=pass_adj_yds_per_att&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 3. URL for Rushing 1-4, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=rush_att&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=rush_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=rush_yds_per_att&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=rush_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 4. URL for Receiving 1-7, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=targets&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=rec&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=rec_yds&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=rec_yds_per_rec&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=rec_td&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=catch_pct&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=rec_yds_per_tgt&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 5. URL for Scoring 1-10, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=xpm&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=xpa&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=xp_perc&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=fgm&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=fga&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=fg_perc&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=two_pt_md&ccomp%5B8%5D=gt&cval%5B8%5D=0&cstat%5B8%5D=safety_md&ccomp%5B9%5D=gt&cval%5B9%5D=0&cstat%5B9%5D=all_td&ccomp%5B10%5D=gt&cval%5B10%5D=0&cstat%5B10%5D=scoring&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 6. URL for Fantasy 1-4, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=fantasy_points&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=fantasy_points_ppr&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=draftkings_points&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=fanduel_points&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 7. URL for Kick Returns 1-4, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=kick_ret&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=kick_ret_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=kick_ret_yds_per_ret&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=kick_ret_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 8. URL for Punt Returns 1-4, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=punt_ret&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=punt_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=punt_ret_yds_per_ret&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=punt_blocked&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 9. URL for sacks and Tackles 1, 1-4, https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=sacks&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=tackles_solo&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=tackles_assists&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=tackles_combined&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=tackles_loss&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=qb_hits&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 10. URL for Def interception and Fumbles , https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=def_int&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=def_int_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=def_int_td&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=pass_defended&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=fumbles&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=fumbles_lost&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=fumbles_forced&ccomp%5B8%5D=gt&cval%5B8%5D=0&cstat%5B8%5D=fumbles_rec&ccomp%5B9%5D=gt&cval%5B9%5D=0&cstat%5B9%5D=fumbles_rec_yds&ccomp%5B10%5D=gt&cval%5B10%5D=0&cstat%5B10%5D=fumbles_rec_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99
    # 11. URL punting and Total yards , https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=punt&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=punt_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=punt_yds_per_punt&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=punt_blocked&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=touches&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=total_offense&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=yds_from_scrimmage&ccomp%5B8%5D=gt&cval%5B8%5D=0&cstat%5B8%5D=all_purpose_yds&ccomp%5B9%5D=gt&cval%5B9%5D=0&cstat%5B9%5D=ret_yds&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99


    url_lst = [
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=pass_cmp&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=pass_att&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=pass_inc&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=pass_cmp_perc&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=pass_yds&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=pass_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=pass_int&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=pass_rating&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=pass_sacked&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=pass_sacked_yds&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=pass_yds_per_att&ccomp%5B6%5D=gt&cstat%5B6%5D=pass_adj_yds_per_att&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=rush_att&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=rush_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=rush_yds_per_att&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=rush_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=targets&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=rec&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=rec_yds&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=rec_yds_per_rec&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=rec_td&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=catch_pct&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=rec_yds_per_tgt&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=xpm&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=xpa&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=xp_perc&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=fgm&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=fga&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=fg_perc&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=two_pt_md&ccomp%5B8%5D=gt&cval%5B8%5D=0&cstat%5B8%5D=safety_md&ccomp%5B9%5D=gt&cval%5B9%5D=0&cstat%5B9%5D=all_td&ccomp%5B10%5D=gt&cval%5B10%5D=0&cstat%5B10%5D=scoring&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=fantasy_points&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=fantasy_points_ppr&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=draftkings_points&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=fanduel_points&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=kick_ret&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=kick_ret_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=kick_ret_yds_per_ret&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=kick_ret_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=punt_ret&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=punt_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=punt_ret_yds_per_ret&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=punt_blocked&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=sacks&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=tackles_solo&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=tackles_assists&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=tackles_combined&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=tackles_loss&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=qb_hits&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=def_int&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=def_int_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=def_int_td&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=pass_defended&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=fumbles&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=fumbles_lost&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=fumbles_forced&ccomp%5B8%5D=gt&cval%5B8%5D=0&cstat%5B8%5D=fumbles_rec&ccomp%5B9%5D=gt&cval%5B9%5D=0&cstat%5B9%5D=fumbles_rec_yds&ccomp%5B10%5D=gt&cval%5B10%5D=0&cstat%5B10%5D=fumbles_rec_td&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=punt&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=punt_yds&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=punt_yds_per_punt&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=punt_blocked&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=touches&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=total_offense&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=yds_from_scrimmage&ccomp%5B8%5D=gt&cval%5B8%5D=0&cstat%5B8%5D=all_purpose_yds&ccomp%5B9%5D=gt&cval%5B9%5D=0&cstat%5B9%5D=ret_yds&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99',
    ]

    return url_lst


def str_concat(strng, f_line):

    driver.implicitly_wait(30)
    try:
        data_in_str = driver.find_element_by_xpath('//*[@id="csv_results"]').text

    except NoSuchElementException:
        driver.refresh()
        try:
            data_in_str = driver.find_element_by_xpath('//*[@id="csv_results"]').text

        except NoSuchElementException:
            driver.refresh()
            data_in_str = driver.find_element_by_xpath('//*[@id="csv_results"]').text

    if f_line:
        first_line = data_in_str.find('\n') + 1
        second_line = data_in_str.find('\n', first_line) + 1
        third_line = data_in_str.find('\n', second_line) + 1
        fourth_line = data_in_str.find('\n', third_line) + 1
        fifth_line = data_in_str.find('\n', fourth_line) + 1

        concat_str = strng + data_in_str[fifth_line:] + '\n'

    else:
        first_line = data_in_str.find('\n') + 1
        second_line = data_in_str.find('\n', first_line) + 1
        third_line = data_in_str.find('\n', second_line) + 1
        fourth_line = data_in_str.find('\n', third_line) + 1
        fifth_line = data_in_str.find('\n', fourth_line) + 1
        sixth_line = data_in_str.find('\n', fifth_line) + 1

        concat_str = strng + data_in_str[sixth_line:] + '\n'

    return concat_str


def next_btn(link_url):

    strng = ''
    last_page = False
    f_line = True

    while not last_page:
        driver.get(link_url)
        driver.implicitly_wait(30)

        html_source = driver.page_source
        convert_to_csv()
        strng = str_concat(strng, f_line)
        f_line = False

        soup = BeautifulSoup(html_source, 'lxml')
        links = soup.find_all('div', class_='prevnext')

        for link in links:
            l = link.find_all('a', class_='button2 next')
            if len(l) == 0:
                last_page = True
            else:
                link_url = "https://stathead.com" + l[0]['href']

    return strng


def write_to_csv():
    url_lst = url_ls()

    url_lst = [
        'https://stathead.com/football/pgl_finder.cgi?request=1&match=game&order_by_asc=0&order_by=all_td&year_min=1990&year_max=2021&game_type=R&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=pass_cmp&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=rush_att&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=targets&ccomp%5B12%5D=gt&cval%5B12%5D=0&cstat%5B12%5D=fantasy_points&ccomp%5B13%5D=gt&cval%5B13%5D=0&cstat%5B13%5D=kick_ret&ccomp%5B14%5D=gt&cval%5B14%5D=0&cstat%5B14%5D=punt_ret&ccomp%5B15%5D=gt&cval%5B15%5D=0&cstat%5B15%5D=sacks&ccomp%5B16%5D=gt&cval%5B16%5D=0&cstat%5B16%5D=tackles_solo&ccomp%5B17%5D=gt&cval%5B17%5D=0&cstat%5B17%5D=def_int&ccomp%5B19%5D=gt&cval%5B19%5D=0&cstat%5B19%5D=fumbles&age_min=0&age_max=99&season_start=1&season_end=-1&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99'

    ]

    file_n = 'SH Football data link'
    counter = 11
    for u in url_lst[5:6]:
        strng = next_btn(u)
        file_name = file_n + ' ' + str(counter) + '.csv'
        file = open(file_name, 'w+')
        file.write(strng)
        file.close()
        counter += 1


if __name__ == "__main__":
    login()
    write_to_csv()

