import mlflow

def calculate_sum(x,y):
    return x + y

def calculate_product(x,y):
    return x * y

if __name__ == "__main__":
    with mlflow.start_run():
        x , y = 75,10
        z = calculate_product(x,y)
        # tracking the experiment with the MLFlow
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_metric("z",z)