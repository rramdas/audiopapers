# How it works

- Customer uploads a pdf file.
  - This is the job of the Django pdfparser app
- pdf files is analyzed and made text-to-speech friendly
  - This is the job of the Airflow DAG using scipdf
- text-to-speech is run
  - This is also done by the Airflow DAG using gTTS
- Customer can listen to his pdf file
  - This is the job of the Dango Audiopp app

# Set up dev env

Architecture consist of:

- Django 
- Airflow
- GROBID

## Django and Python dependencies

Django and all required Python packages will be installed by running

pip install -r requirements.txt

## Grobid

Grobid is the AI analyzing the pdfs.

Run a Grobid server:

```
docker run --rm --gpus --init all -p 8070:8070 grobid/grobid:0.7.3
```

On MacosX you need to increase the memory available to Docker otherwise Grobid will not run.


If you use Colima:

```
colima start --cpu 4 --memory 8
```

## Airflow

```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.3/docker-compose.yaml'

mkdir -p ./dags ./logs ./plugins ./config

echo -e "AIRFLOW_UID=$(id -u)" > .env

```

You can remove the examples Airflow loads by setting the variable for that in docker-compose.yaml file to false

```
AIRFLOW__CORE__LOAD__EXAMPLES: 'false' 
````