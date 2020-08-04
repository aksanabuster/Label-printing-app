from graphql_client import GraphQLClient
from conf import badgeTemplateUri, serverUrl
from printerStatus import getPrinters
import gqlWs


# start up sequence (APP starter)
print(f'ws://{serverUrl}/graphql-ws')
ws = GraphQLClient(f'ws://{serverUrl}/graphql')

query = """
  subscription {
    printRequested{
        id
        success
    }
  }
"""



availablePrinters = getPrinters()

def newData(ws,messege):
    availablePrinters[0].print("file:///home/boris/Documents/PrinterHub/test.html","badge-test","png")
    print(messege)

# callback function
gqlWs.start(newData)



# later stop the subscription
# ws.stop_subscribe(sub_id)
# ws.close()