import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import os
import json

# Initialize the Cosmos client
COSMOS_URL = os.getenv('COSMOS_URL')
COSMOS_KEY = os.getenv('COSMOS_KEY')
COSMOS_DATABASE_NAME = os.getenv('COSMOS_DATABASE_NAME')
COSMOS_CONTAINER_NAME = os.getenv('COSMOS_CONTAINER_NAME')

client = CosmosClient(COSMOS_URL, COSMOS_KEY)
database = client.get_database_client(COSMOS_DATABASE_NAME)
container = database.get_container_client(COSMOS_CONTAINER_NAME)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    resume_id = req.params.get('id')
    if not resume_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            resume_id = req_body.get('id')

    if resume_id:
        try:
            # Query the Cosmos DB for the resume
            query = "SELECT * FROM c WHERE c.id=@id"
            parameters = [ { "name":"@id", "value": resume_id } ]
            items = list(container.query_items(
                query=query,
                parameters=parameters,
                enable_cross_partition_query=True
            ))

            if not items:
                return func.HttpResponse(
                    "Resume not found.",
                    status_code=404
                )

            resume_data = items[0]

            # Assuming the resume file content is stored in the 'fileContent' field
            file_content = resume_data.get('fileContent')

            if not file_content:
                return func.HttpResponse(
                    "Resume content not found.",
                    status_code=404
                )

            return func.HttpResponse(
                file_content,
                status_code=200,
                mimetype='application/pdf'
            )

        except exceptions.CosmosHttpResponseError as e:
            return func.HttpResponse(
                "Error retrieving the resume: {}".format(e),
                status_code=500
            )
    else:
        return func.HttpResponse(
             "Please pass an id on the query string or in the request body",
             status_code=400
        )
