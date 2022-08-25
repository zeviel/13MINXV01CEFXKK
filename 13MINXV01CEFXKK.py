import amino
from rainbowtext import text
from pyfiglet import figlet_format
print(text("""Script by zeviel
Github : https://github.com/zeviel"""))
print(text(figlet_format("13MINXV01CEFXKK", font="small")))

client = amino.Client()
password = input(text("-- Password for all accounts::: "))
link_info = client.get_from_code(input(text("-- Chat Link::: ")))
com_id = link_info.comId
chat_id = link_info.objectId
with open ("emails.txt", "r") as file:
	for line in file:
		try:
			email = line.strip()
			client.login(email=email, password=password)
			sub_client = amino.SubClient(comId=com_id, profile=client.profile)
			sub_client.join_chat(chatId=chat_id)
			client.join_video_chat_as_viewer(comId=com_id, chatId=chat_id)
			print(text(f"-- {email} Joined to voice chat..."))
		except Exception as e:
			print(e)
