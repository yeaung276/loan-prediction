FROM python:3.8-slim
ARG port

USER root
ENV PORT=$port
WORKDIR ./usr/app/

COPY ../requirements.txt ./

RUN pip install pip --upgrade \
    && pip install -r requirements.txt

COPY ../LoanPrediction .

EXPOSE $PORT

CMD python main.py --host 0.0.0.0 --port $PORT