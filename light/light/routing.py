from channels.routing import ProtocolTypeRouter,URLRouter
import lightcontrol.routing
from channels.auth import AuthMiddlewareStack
from django.urls import path
from lightcontrol import consumers
#application = ProtocolTypeRouter({
#	'websocket' : AuthMiddlewareStack(
#	URLRouter(
#	lightcontrol.routing.websocket_urlpatterns
#	)
#	),
#})

application = ProtocolTypeRouter({
	"websocket" : URLRouter([
	path('lightcontrol/',consumers.lightconsumer),
])
})
