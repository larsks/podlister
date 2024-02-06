from fastapi import FastAPI
from kubernetes import client, config

def create_app():
    config.load_config()
    v1 = client.CoreV1Api()
    app = FastAPI()

    @app.get('/pods/{namespace}')
    def list_pods(namespace: str):
        pods = v1.list_namespaced_pod(namespace)
        return [pod.metadata.name for pod in pods.items]

    return app

app = create_app()
