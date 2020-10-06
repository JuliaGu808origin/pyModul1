# Find all occurrences of “USA” in given string ignoring the case
# ?怎麽顯示結果
import re
text = """
Send free text to USA using SENDaTEXT. 
Using internet, you can send free text messages to usa. 
Simply enter the phone number on the dialpad and click on "usA". 
You can now send free texts to UsA mobile and landline phones from uSA your computer or smartphone. 
Send a message to your loved ones in USa today!
"""
founds = re.findall(r'(USA|usa|USa|Usa|uSA|uSa)', text)
print(founds)
