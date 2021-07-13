import amino
import re
import pyfiglet
import rainbowtext
print(rainbowtext.text("""Script by Lil Zevi
Github : https://github.com/LilZevi"""))
print(rainbowtext.text(pyfiglet.figlet_format("Aminovoicefxck", font="small")))
client = amino.Client()
emails = open("emails.txt", "r")
chatlink = input(rainbowtext.text("Chat Link >> "))
password = input(rainbowtext.text("Password For All Accounts >> "))
for line in emails:
	email = line.strip()
	try:
		client.login(email=email, password=password)
		chat_info = client.get_from_code(chatlink)
		chat_id = chat_info.objectId
		community_id = chat_info.path[1:chat_info.path.index('/')]
		client.join_voice_chat(comId=community_id, chatId=chat_id, joinType=2)
		print(rainbowtext.text(f"{email} Joined To Voice Chat"))
	except amino.lib.util.exceptions.VerificationRequired as e:
		print(rainbowtext.text(f"VerificationRequired for {email}"))
		url = re.search("(?P<url>https?://[^\s'\"]+)", str(e)).group("url")
		print(f"Verification Link = {url}")
	except amino.lib.util.exceptions.ActionNotAllowed:
		print(rainbowtext.text(f"ActionNotAllowed {email}"))
	except:
		print(rainbowtext.text(f"{email} Can't Join To Voice Chat"))
		pass
