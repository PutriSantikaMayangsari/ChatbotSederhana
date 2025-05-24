1. Open MongoDB and Connect it to localhost:27017
2. Start the flask server:
	- Open Command Prompt --> cmd
	- cd C:\Users\user\Desktop\ugm-chatbot
	- venv\Scripts\activate
	- python chatbotmka.py
	- Keep this command prompt open.
3. Start nGrok
	- Open a new command prompt --> cmd
	- cd C:\Users\user\Desktop\ugm-chatbot
	- ngrok.exe http 5000
	- Copy the URL link followed by forwarding
4. Go to https://console.twilio.com
	- Messaging” > “WhatsApp
	- Connect sandbox by scanning QR
	- In the “When a message comes in” field, enter the new URL with /chatbotmka
