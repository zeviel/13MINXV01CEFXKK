import samino
from rainbowtext import text
from pyfiglet import figlet_format
from websocket import WebSocketConnectionClosedException
print(text("""Script by deluvsushi
Github : https://github.com/deluvsushi"""))
print(text(figlet_format("aminovoicefxck", font="small")))

def main():
	client = samino.Client()
	password = input(text("-- Password for all accounts::: "))
	link_Info = client.get_from_link(input(text("-- Chat Link::: ")))
	com_id = linkInfo.comId; chat_id = linkInfo.objectId
	with open ("emails.txt", "r") as emails:
		for line in emails:
			try:
				email = line.strip()
				client.login(email=email, password=password)
				local = samino.Local(comId=com_id)
				local.join_chat(chatId=chat_id)
				client.socketClient.joinVideoChatAsSpectator(com_id, chat_id)
				print(text(f"-- {email} Joined to voice chat..."))
			except (samino.lib.Except, WebSocketConnectionClosedException) as e:
				print(f"- Error::: {email} - {e.args[0]}\n")

main()
