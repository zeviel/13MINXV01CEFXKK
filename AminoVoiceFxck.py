import amino
import asyncio
import pyfiglet
import rainbowtext
print(rainbowtext.text("""Script by Lil Zevi
Github : https://github.com/LilZevi"""))
print(rainbowtext.text(pyfiglet.figlet_format("Aminovoicefxck", font="small")))

async def main():
	client = amino.Client()
	emails = open("emails.txt", "r")
	chatlink = input(rainbowtext.text("Chat Link >> "))
	password = input(rainbowtext.text("Password For All Accounts >> "))
	for line in emails:
		email = line.strip()
		try:
			await client.login(email=email, password=password)
			chat_info = await client.get_from_code(chatlink)
			chat_id = chat_info.objectId
			community_id = chat_info.path[1:chat_info.path.index('/')]
			await client.join_voice_chat(comId=community_id, chatId=chat_id, joinType=2)
			print(rainbowtext.text(f"{email} Joined To Voice Chat"))
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"{email} VerificationRequired")
			link = e.args[0]['url']
			print(link)
		except amino.lib.util.exceptions.ActionNotAllowed:
			print(rainbowtext.text(f"ActionNotAllowed {email}"))
		except:
			print(rainbowtext.text(f"{email} Can't Join To Voice Chat"))
			pass
