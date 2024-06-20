import win32com.client as win32
from selenium import webdriver
import time

outlook = win32.Dispatch("outlook.application")
email_out = outlook.CreateItem(0)

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/Pyautogui/formulario.html")
time.sleep(20)

nome_element = driver.find_element("id", "nome")
email_element = driver.find_element("id", "email")
mensagem_element = driver.find_element("id", "mensagem")

nome = nome_element.get_attribute("value")
email = email_element.get_attribute("value")
mensagem = mensagem_element.get_attribute("value")

email_out.To = email
email_out.Subject = 'Mandando e-mail'
email_out.HTMLBody = mensagem
anexo = fr'C:\Users\liviapisanello-ieg\Downloads\COMUNICAR-SE E ESCREVER BEM.pptx'
email_out.Attachments.Add(anexo)
email_out.Send()
driver.quit()
