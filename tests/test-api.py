# Una vez hemos hecho el deploy en Hugging Face, podemos probar la API de Gradio
# usando el cliente de Gradio (https://github.com/gradio-app/gradio-client)

from gradio_client import Client

client = Client("Patriciagsbcn/practica-chat")
result = client.predict(
	"Where is the hospital located!!",
	5,
	0.55,
	api_name="/ask"
)
print(result)