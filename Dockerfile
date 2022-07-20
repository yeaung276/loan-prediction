FROM python:3.8-slim
ARG port

USER root
ENV PORT=$port
WORKDIR ./usr/app/

COPY ./requirements.txt ./

RUN pip install pip --upgrade \
    && pip install -r requirements.txt

COPY LoanPrediction .

# RUN chgrp -R 0 LoanPrediction \
#     && chmod -R g=u LoanPrediction

# RUN cd LoanPrediction

# EXPOSE $PORT

# CMD python main.py 0.0.0.0 $PORT