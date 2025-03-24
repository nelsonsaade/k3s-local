from fastapi import FastAPI
from python_terraform import Terraform
import os

app = FastAPI()
TF_DIR = "/app/terraform"

@app.post("/create_namespace/")
def create_namespace(namespace: str):
    tf = Terraform(working_dir=TF_DIR)
    return_code, stdout, stderr = tf.apply(vars={"namespace_name": namespace}, skip_plan=True)

    if return_code == 0:
        return {"message": f"Namespace '{namespace}' creado correctamente"}
    else:
        return {"error": stderr}
