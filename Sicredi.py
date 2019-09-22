from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver.exe")

driver.get("https://www.sicredi.com.br/html/ferramenta/simulador-investimento-poupanca")

driver.find_element_by_name("valorAplicar").send_keys("10,00")
driver.find_element_by_name("valorInvestir").send_keys("10,00")
driver.find_element_by_name("tempo").send_keys("0")
driver.find_element_by_class_name("btSelect").click()

if driver.find_element_by_name("valorAplicar").get_attribute("aria-invalid"):
    element = driver.find_element_by_id("valorAplicar-error")
    if element.is_displayed():
        print("Campo: Qual o valor que você quer aplicar? - QA ok")
    else:
        print("Campo: Qual o valor que você quer aplicar? - QA not ok")

if driver.find_element_by_name("valorInvestir").get_attribute("aria-invalid"):
    element = driver.find_element_by_id("valorInvestir-error")
    if element.is_displayed():
        print("Campo: Quanto você quer poupar todo mês? - QA ok")
    else:
        print("Campo: Quanto você quer poupar todo mês? - QA not ok")

if driver.find_element_by_name("tempo").get_attribute("aria-invalid"):
    element = driver.find_element_by_id("tempo-error")
    if element.is_displayed():
        print("Campo: Por quanto tempo você quer poupar? - QA ok")
    else:
        print("Campo: Por quanto tempo você quer poupar? - QA not ok")

if driver.find_element_by_name("valorAplicar").get_attribute("aria-invalid") and driver.find_element_by_name("valorInvestir").get_attribute("aria-invalid"):
    driver.find_element_by_class_name("btnLimpar").click()

driver.implicitly_wait(10)
driver.find_element_by_name("valorAplicar").send_keys("20,00")
driver.find_element_by_name("valorInvestir").send_keys("20,00")
driver.find_element_by_name("tempo").send_keys("2")

driver.find_element_by_class_name("btnSimular").click()